#!/usr/bin/env python3
"""Validate rule files: syntax, duplicates, empty payload, overlay presence."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import (  # noqa: E402
    INVALID_TYPE_RE,
    ROOT,
    TYPE_RE,
    is_clash,
    load_manifest,
    parse_rule_line,
    parse_rules,
    split_header_body,
)

KNOWN_TYPES = {
    "DOMAIN",
    "DOMAIN-SUFFIX",
    "DOMAIN-KEYWORD",
    "IP-CIDR",
    "IP-CIDR6",
    "IP-ASN",
    "PROCESS-NAME",
    "USER-AGENT",
    "URL-REGEX",
    "GEOIP",
    "SRC-IP-CIDR",
    "DEST-PORT",
    "SRC-PORT",
}


def check_file(path: Path, clash: bool) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        errors.append("missing trailing newline")
    if "\r" in text:
        errors.append("CRLF / CR line endings")
    if INVALID_TYPE_RE.search(text):
        errors.append("invalid token 'DOMAIN,SUFFIX' (should be DOMAIN-SUFFIX)")

    header, body = split_header_body(text)
    if clash:
        if "payload:" not in text:
            errors.append("Clash file missing 'payload:'")
        payload_seen = any(l.strip() == "payload:" for l in body) or any(
            l.strip() == "payload:" for l in header
        )
        # payload is usually first body-ish line; tolerate it in body
        if not payload_seen and not any(l.strip() == "payload:" for l in text.splitlines()):
            errors.append("payload: marker not found")

    rules = []
    unknown = 0
    for i, raw in enumerate(text.splitlines(), 1):
        s = raw.strip()
        if not s or s.startswith("#") or s == "payload:":
            continue
        line = s[2:].strip() if clash and s.startswith("- ") else s
        if clash and s.startswith("-") and not s.startswith("- "):
            line = s[1:].strip()
        if INVALID_TYPE_RE.match(line):
            errors.append(f"L{i}: DOMAIN,SUFFIX is invalid")
            continue
        parsed = parse_rule_line(s, clash=clash)
        if not parsed:
            # allow comment-like leftover
            if s.startswith("-") or TYPE_RE.match(line) is None:
                # maybe unknown type
                if "," in line:
                    typ = line.split(",", 1)[0].strip().upper()
                    if typ not in KNOWN_TYPES:
                        unknown += 1
                        errors.append(f"L{i}: unknown / unparsable rule: {s[:80]}")
            continue
        rules.append(parsed)

    if len(rules) == 0:
        errors.append("no parsable rules")

    seen = {}
    dups = 0
    for t, v in rules:
        key = (t.upper(), v.lower())
        if key in seen:
            dups += 1
        else:
            seen[key] = True
    if dups:
        errors.append(f"{dups} duplicate rule(s)")

    # TOTAL header consistency (warning-as-error for small files only)
    total_line = next((h for h in header if h.startswith("# TOTAL:")), None)
    if total_line:
        try:
            declared = int(total_line.split(":", 1)[1].strip())
            if declared != len(rules) and len(rules) < 500:
                errors.append(f"TOTAL header {declared} != parsed {len(rules)}")
        except ValueError:
            errors.append("invalid TOTAL header")
    return errors


def main() -> int:
    man = load_manifest()
    files = []
    for item in man["rules"]:
        files.append(ROOT / item["local"])
    for rel in man.get("custom", []):
        files.append(ROOT / rel)

    missing = [p for p in files if not p.exists()]
    failed = 0
    ok = 0
    if missing:
        for p in missing:
            print(f"[MISSING] {p.relative_to(ROOT)}")
            failed += 1

    for p in files:
        if not p.exists():
            continue
        errs = check_file(p, clash=is_clash(p))
        rel = p.relative_to(ROOT)
        if errs:
            failed += 1
            print(f"[FAIL] {rel}")
            for e in errs:
                print(f"       - {e}")
        else:
            ok += 1
            print(f"[OK]   {rel}")

    print(f"---\nok={ok} failed={failed} total={len(files)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
