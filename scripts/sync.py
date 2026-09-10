#!/usr/bin/env python3
"""Fetch upstream blackmatrix7 rules, merge overlays, write local copies."""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import (  # noqa: E402
    ROOT,
    extract_name,
    extract_updated,
    format_header,
    is_clash,
    load_manifest,
    load_overlay,
    merge_rules,
    parse_rules,
    render_clash,
    render_surge,
    split_header_body,
)

UA = {"User-Agent": "Config_Self-sync/1.0 (+https://github.com/chentanwan/Config_Self)"}
UPSTREAM_REPO = "https://github.com/blackmatrix7/ios_rule_script"
MIRROR_REPO = "https://github.com/chentanwan/Config_Self"


def fetch(url: str, timeout: int = 180) -> str:
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        raise SystemExit(f"HTTP {e.code} fetching {url}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"network error fetching {url}: {e.reason}") from e
    return data.decode("utf-8")


def write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def remotes_of(item: dict) -> list[str]:
    if item.get("remotes"):
        return list(item["remotes"])
    if item.get("remote"):
        return [item["remote"]]
    return []


def sync_one(item: dict, base: str, dry_run: bool) -> tuple[str, str]:
    local = ROOT / item["local"]
    remotes = remotes_of(item)
    clash = is_clash(item["local"])
    rules: list[tuple[str, str]] = []
    extra_notes: list[str] = []
    updated: str | None = None
    name = item.get("name") or Path(item["local"]).stem
    first_name: str | None = None

    if item.get("note"):
        extra_notes.append(f"# NOTE: {item['note']}")
    if len(remotes) > 1:
        extra_notes.append("# UPSTREAM: " + ", ".join(remotes))

    for remote in remotes:
        url = base.rstrip("/") + "/" + remote
        text = fetch(url)
        header, body = split_header_body(text)
        part = parse_rules(body, clash=is_clash(remote))
        if not part:
            raise SystemExit(f"no rules parsed from {url}")
        rules = merge_rules(rules, part)
        u = extract_updated(header)
        if u and (updated is None or u > updated):
            updated = u
        if first_name is None:
            first_name = extract_name(header, name)

    if remotes and not item.get("name") and first_name:
        name = first_name

    overlay_rel = item.get("overlay")
    if overlay_rel:
        extra = load_overlay(ROOT / overlay_rel)
        before = len(rules)
        rules = merge_rules(rules, extra)
        extra_notes.append(
            f"# OVERLAY-ADDED: {len(rules) - before} rule(s) from {overlay_rel}"
        )

    if not rules:
        raise SystemExit(f"no rules produced for {item['local']}")

    author = "blackmatrix7" if remotes else "Config_Self"
    repo = UPSTREAM_REPO if remotes else MIRROR_REPO
    hdr = format_header(
        name,
        updated,
        overlay_rel,
        rules,
        extra_notes,
        author=author,
        repo=repo,
    )
    content = render_clash(hdr, rules) if clash else render_surge(hdr, rules)

    if dry_run:
        return item["local"], "dry-run"
    changed = write_if_changed(local, content)
    return item["local"], "updated" if changed else "unchanged"


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync rules from blackmatrix7")
    parser.add_argument("--only", help="substring filter on local path")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    man = load_manifest()
    base = man["upstream_base"]
    items = man["rules"]
    if args.only:
        items = [i for i in items if args.only.lower() in i["local"].lower()]
        if not items:
            print("no matching rules", file=sys.stderr)
            return 1

    stats = {"updated": 0, "unchanged": 0, "dry-run": 0}
    for item in items:
        local, status = sync_one(item, base, args.dry_run)
        stats[status] = stats.get(status, 0) + 1
        print(f"[{status:9s}] {local}")

    print(
        "---\n"
        f"updated={stats['updated']} unchanged={stats['unchanged']} "
        f"dry-run={stats['dry-run']} total={len(items)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
