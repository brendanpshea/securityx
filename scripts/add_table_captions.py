"""Resync table captions between src/chapters/*.md and docs/chapters/*.html.

For each chapter:
  1. Walk the markdown in source order, harvesting tables and any
     `*Table X.Y: ...*` caption line immediately after each table.
  2. Fill missing captions from FALLBACK_CAPTIONS (keyed by chapter + the
     zero-based source-order table index).
  3. Renumber every caption sequentially (1.1, 1.2, ...) to fix any
     out-of-order legacy numbering. Write the markdown back.
  4. Inject the (renumbered) caption into the matching <table> in the
     rendered HTML as <caption>Table X.Y: ...</caption>. Any pre-existing
     <caption> on a table is replaced so the markdown stays canonical.

Idempotent: running again with no source changes produces no output.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "chapters"
SRC = ROOT / "src" / "chapters"

# Filled in only where the markdown is missing a caption for a given
# zero-indexed source-order table. Source-order means: scanning the markdown
# top-to-bottom (including tables inside callout blockquotes).
FALLBACK_CAPTIONS = {
    "ch10": {
        2: "Compensating control stack for the unpatched Allen-Bradley PLC at Yellow Brick Manufacturing — control, implementation, and owner.",
    },
}

SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}")
CAPTION_RE = re.compile(r"^\*Table\s+[\d.]+:\s*(.+?)\*\s*$")
TABLE_FULL_RE = re.compile(r"<table\b[^>]*>(.*?)</table>", re.IGNORECASE | re.DOTALL)
TABLE_OPEN_RE = re.compile(r"<table\b[^>]*>", re.IGNORECASE)
CAPTION_TAG_RE = re.compile(r"<caption\b[^>]*>.*?</caption>\s*", re.IGNORECASE | re.DOTALL)
# Matches the redundant paragraph the markdown renderer leaves after a table
# (e.g. "<p><em>Table 1.1: ...</em></p>"). Allowed across one newline inside
# the em — Pandoc wraps long captions.
TRAILING_PARA_RE = re.compile(
    r"\s*<p>\s*<em>\s*Table\s+[\d.]+:.*?</em>\s*</p>\s*",
    re.IGNORECASE | re.DOTALL,
)


def is_table_row(line: str) -> bool:
    return line.lstrip().lstrip(">").lstrip().startswith("|")


def chapter_num(name: str) -> int:
    return int(name[2:])


def harvest_md(chapter: str):
    """Walk markdown, return (new_lines, captions[]) where captions[i] is the
    caption text (no 'Table X.Y:' prefix) for the i-th source-order table,
    and new_lines is the rewritten markdown with renumbered captions filled."""
    path = SRC / f"{chapter}.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    fallback = FALLBACK_CAPTIONS.get(chapter, {})
    ch_num = chapter_num(chapter)

    out = []
    captions = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if (
            is_table_row(line)
            and i + 1 < len(lines)
            and SEP_RE.match(lines[i + 1].lstrip().lstrip(">").lstrip())
        ):
            # Consume the whole table block (preserving any leading "> " on
            # callout-embedded tables).
            out.append(line)
            j = i + 1
            while j < len(lines) and is_table_row(lines[j]):
                out.append(lines[j])
                j += 1
            table_idx = len(captions)

            # Look at the next non-blank line for an existing caption. Allow
            # for a "> " quote prefix on callout-embedded tables.
            k = j
            while k < len(lines) and lines[k].strip() in ("", ">"):
                k += 1
            existing_caption_line = (
                lines[k].lstrip().lstrip(">").lstrip()
                if k < len(lines)
                else ""
            )
            cm = CAPTION_RE.match(existing_caption_line)

            if cm:
                caption_text = cm.group(1).strip()
                # Skip past the consumed caption line and its trailing blank.
                # Preserve any blank lines between the table and the caption.
                for blank_idx in range(j, k):
                    out.append(lines[blank_idx])
                # Replace the existing caption line with a renumbered one,
                # preserving the original line's quote prefix if any.
                prefix_match = re.match(r"^(\s*>?\s*)", lines[k])
                prefix = prefix_match.group(1) if prefix_match else ""
                out.append(f"{prefix}*Table {ch_num}.{table_idx + 1}: {caption_text}*")
                captions.append(caption_text)
                i = k + 1
                continue

            # No existing caption — check fallback.
            if table_idx in fallback:
                caption_text = fallback[table_idx]
                # Determine quote-prefix from the table itself so a
                # callout-embedded table gets a callout-embedded caption.
                prefix_match = re.match(r"^(\s*>?\s*)", line)
                prefix = prefix_match.group(1) if prefix_match else ""
                # Emit a blank line then the caption line.
                out.append(prefix.rstrip() if prefix.strip() else "")
                out.append(f"{prefix}*Table {ch_num}.{table_idx + 1}: {caption_text}*")
                captions.append(caption_text)
                i = j
                continue

            # No caption available — leave the table as-is and warn.
            print(f"  WARN: {chapter}.md table#{table_idx} has no caption")
            captions.append(None)
            i = j
            continue

        out.append(line)
        i += 1

    new_text = "\n".join(out) + ("\n" if text.endswith("\n") else "")
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return captions


def patch_html(chapter: str, captions: list) -> int:
    path = DOCS / f"{chapter}.html"
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8")
    ch_num = chapter_num(chapter)

    tables = list(TABLE_FULL_RE.finditer(text))
    if len(tables) != len(captions):
        print(f"  WARN: {chapter}.html has {len(tables)} tables, harvested {len(captions)} captions")

    pieces = []
    last = 0
    changed = 0
    for idx, m in enumerate(tables):
        pieces.append(text[last:m.start()])
        table_html = m.group(0)
        caption_text = captions[idx] if idx < len(captions) else None
        if caption_text is None:
            pieces.append(table_html)
            last = m.end()
            continue

        # Strip any existing <caption> and reinsert the canonical one.
        stripped = CAPTION_TAG_RE.sub("", table_html, count=1)
        open_m = TABLE_OPEN_RE.match(stripped)
        new_caption = f"\n<caption>Table {ch_num}.{idx + 1}: {caption_text}</caption>"
        new_table = stripped[: open_m.end()] + new_caption + stripped[open_m.end():]

        if new_table != table_html:
            changed += 1
        pieces.append(new_table)
        last = m.end()

        # Consume any redundant "<p><em>Table X.Y: ...</em></p>" that the
        # markdown renderer left immediately after the table.
        trailing = TRAILING_PARA_RE.match(text, last)
        if trailing:
            last = trailing.end()
            # Keep a single newline between the table and the next block.
            pieces.append("\n")
    pieces.append(text[last:])

    new_text = "".join(pieces)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> None:
    total = 0
    for path in sorted(SRC.glob("ch*.md")):
        chapter = path.stem
        if chapter == "ch00_sample":
            continue
        print(f"{chapter}:")
        captions = harvest_md(chapter)
        non_null = sum(1 for c in captions if c is not None)
        n = patch_html(chapter, captions)
        print(f"  {non_null}/{len(captions)} captions, html updated: {n}")
        total += n
    print(f"\nTotal HTML tables touched: {total}")


if __name__ == "__main__":
    main()
