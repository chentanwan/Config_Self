#!/usr/bin/env python3
"""Fetch upstream blackmatrix7 rules, merge overlays, write local copies."""
from __future__ import annotations

import argparse
import os
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


def sync_one(item: dict, base: str, dry_run: bool) -> tuple[str, str]:
    local = ROOT / item["local"]
    url = base.rstrip("/") + "/" + item["remote"]
    text = fetch(url)
    header, body = split_header_body(text)
    clash = is_clash(item["local"])
    rules = parse_rules(body, clash=clash)
    if not rules:
        # some files (e.g. custom Disney) aren't fetched this way
        raise SystemExit(f"no rules parsed from {url}")

    overlay_rel = item.get("overlay")
    extra_notes = []
    if item.get("note"):
        extra_notes.append(f"# NOTE: {item['note']}")
    if overlay_rel:
        extra = load_overlay(ROOT / overlay_rel)
        before = len(rules)
        rules = merge_rules(rules, extra)
        extra_notes.append(
            f"# OVERLAY-ADDED: {len(rules) - before} rule(s) from {overlay_rel}"
        )

    name = extract_name(header, Path(item["local"]).stem)
    updated = extract_updated(header)
    hdr = format_header(name, updated, overlay_rel, rules, extra_notes)
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
