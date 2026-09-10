#!/usr/bin/env python3
"""Shared helpers for Config_Self rule sync / validation."""
from __future__ import annotations

import json
import os
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "source" / "manifest.json"

RULE_TYPES = (
    "DOMAIN-KEYWORD",
    "DOMAIN-SUFFIX",
    "DOMAIN",
    "IP-CIDR6",
    "IP-CIDR",
    "IP-ASN",
    "PROCESS-NAME",
    "USER-AGENT",
    "URL-REGEX",
    "GEOIP",
    "SRC-IP-CIDR",
    "DEST-PORT",
    "SRC-PORT",
)
TYPE_RE = re.compile(
    r"^(?P<type>" + "|".join(re.escape(t) for t in RULE_TYPES) + r")\s*,\s*(?P<value>.+?)\s*$"
)
INVALID_TYPE_RE = re.compile(r"^DOMAIN\s*,\s*SUFFIX\s*,", re.I)


def load_manifest() -> dict:
    with MANIFEST_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def split_header_body(text: str) -> tuple[list[str], list[str]]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    header: list[str] = []
    body: list[str] = []
    in_header = True
    for line in lines:
        if in_header and (line.startswith("#") or line.strip() == ""):
            header.append(line)
            continue
        in_header = False
        body.append(line)
    # drop trailing empty from split
    while body and body[-1] == "":
        body.pop()
    return header, body


def parse_rule_line(raw: str, clash: bool) -> tuple[str, str] | None:
    line = raw.strip()
    if not line or line.startswith("#"):
        return None
    if clash:
        if line == "payload:":
            return None
        if line.startswith("- "):
            line = line[2:].strip()
        elif line.startswith("-"):
            line = line[1:].strip()
    m = TYPE_RE.match(line)
    if not m:
        return None
    typ = m.group("type")
    value = m.group("value").strip()
    # drop trailing no-resolve / policy leftovers for identity
    value = re.sub(r",\s*no-resolve\s*$", "", value, flags=re.I)
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    return typ, value


def parse_rules(body: Iterable[str], clash: bool) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    seen = set()
    for raw in body:
        parsed = parse_rule_line(raw, clash)
        if not parsed:
            continue
        key = (parsed[0].upper(), parsed[1].lower())
        if key in seen:
            continue
        seen.add(key)
        out.append(parsed)
    return out


def load_overlay(path: Path) -> list[tuple[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    return parse_rules(text.splitlines(), clash=False)


def merge_rules(
    base: list[tuple[str, str]], extra: list[tuple[str, str]]
) -> list[tuple[str, str]]:
    seen = {(t.upper(), v.lower()) for t, v in base}
    out = list(base)
    for t, v in extra:
        key = (t.upper(), v.lower())
        if key in seen:
            continue
        seen.add(key)
        out.append((t, v))
    return out


def counts(rules: list[tuple[str, str]]) -> Counter:
    c: Counter = Counter()
    for t, _ in rules:
        c[t] += 1
    return c


def format_header(name: str, updated: str | None, overlay: str | None, rules: list[tuple[str, str]], extra_notes: list[str] | None = None) -> str:
    c = counts(rules)
    lines = [
        f"# NAME: {name}",
        "# AUTHOR: blackmatrix7",
        "# REPO: https://github.com/blackmatrix7/ios_rule_script",
        f"# MIRROR: https://github.com/chentanwan/Config_Self",
    ]
    if updated:
        lines.append(f"# UPDATED: {updated}")
    if overlay:
        lines.append(f"# OVERLAY: {overlay}")
    if extra_notes:
        lines.extend(extra_notes)
    for t in RULE_TYPES:
        if c[t]:
            lines.append(f"# {t}: {c[t]}")
    lines.append(f"# TOTAL: {len(rules)}")
    return "\n".join(lines) + "\n"


def extract_updated(header: list[str]) -> str | None:
    for line in header:
        if line.startswith("# UPDATED:"):
            return line.split(":", 1)[1].strip()
    return None


def extract_name(header: list[str], fallback: str) -> str:
    for line in header:
        if line.startswith("# NAME:"):
            return line.split(":", 1)[1].strip() or fallback
    return fallback


def render_clash(header: str, rules: list[tuple[str, str]]) -> str:
    lines = [header.rstrip("\n"), "payload:"]
    for t, v in rules:
        if t in ("IP-CIDR", "IP-CIDR6"):
            lines.append(f"  - {t},{v}")
        else:
            lines.append(f"  - {t},{v}")
    return "\n".join(lines) + "\n"


def render_surge(header: str, rules: list[tuple[str, str]]) -> str:
    lines = [header.rstrip("\n")]
    for t, v in rules:
        if t in ("IP-CIDR", "IP-CIDR6"):
            lines.append(f"{t},{v},no-resolve")
        elif t == "URL-REGEX":
            lines.append(f'{t},"{v}"')
        else:
            lines.append(f"{t},{v}")
    return "\n".join(lines) + "\n"


def is_clash(path: str | os.PathLike) -> bool:
    return str(path).endswith(".yaml") or str(path).endswith(".yml")


def rule_stem(local: str) -> str:
    return Path(local).stem
