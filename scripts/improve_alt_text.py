"""Promote each figure's existing Figure X.Y caption into its image alt
attribute, in both src/*.md and docs/*.html. Run once after authoring new
figures whose captions are richer than their alt text."""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "chapters"
DOCS = ROOT / "docs" / "chapters"

FIG_PREFIX = re.compile(r"^Figure\s+\d+\.\d+:\s*")


def caption_to_alt(caption: str) -> str:
    """Strip the 'Figure X.Y:' lead-in so the alt reads as a description."""
    return FIG_PREFIX.sub("", caption.strip()).strip()


def process_md(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=False)
    img_re = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")
    cap_re = re.compile(r"^\*(Figure\s+\d+\.\d+:.*)\*\s*$")
    changes = 0
    for i, line in enumerate(lines):
        m = img_re.match(line)
        if not m:
            continue
        # Find the next non-blank line and check for caption.
        j = i + 1
        while j < len(lines) and lines[j].strip() == "":
            j += 1
        if j >= len(lines):
            continue
        cm = cap_re.match(lines[j])
        if not cm:
            continue
        new_alt = caption_to_alt(cm.group(1))
        if new_alt and new_alt != m.group(1):
            # Escape ']' inside markdown alt to be safe.
            safe_alt = new_alt.replace("]", "\\]")
            lines[i] = f"![{safe_alt}]({m.group(2)})"
            changes += 1
    if changes:
        path.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")
    return changes


def process_html(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    # Match an <img ...> followed (within a small window) by <em>Figure X.Y: ...</em>.
    img_re = re.compile(
        r'(<img\s+)alt="([^"]*)"(\s+src="[^"]+"\s*/?>)',
    )
    cap_re = re.compile(r"<em>(Figure\s+\d+\.\d+:[^<]+)</em>")
    new_parts = []
    last = 0
    changes = 0
    for m in img_re.finditer(text):
        # Captions can run 500+ chars; give the lookahead room for the longest.
        window = text[m.end(): m.end() + 2000]
        cm = cap_re.search(window)
        new_parts.append(text[last:m.start()])
        if cm:
            new_alt = caption_to_alt(cm.group(1))
            if new_alt and new_alt != m.group(2):
                safe_alt = html.escape(new_alt, quote=True)
                new_parts.append(f'{m.group(1)}alt="{safe_alt}"{m.group(3)}')
                changes += 1
                last = m.end()
                continue
        new_parts.append(m.group(0))
        last = m.end()
    new_parts.append(text[last:])
    if changes:
        path.write_text("".join(new_parts), encoding="utf-8")
    return changes


def main() -> None:
    total_md = total_html = 0
    for path in sorted(SRC.glob("ch*.md")):
        n = process_md(path)
        total_md += n
        print(f"{path.name}: {n} alt(s) rewritten")
    for path in sorted(DOCS.glob("ch*.html")):
        n = process_html(path)
        total_html += n
        print(f"{path.name}: {n} alt(s) rewritten")
    print(f"\nTotal: {total_md} markdown, {total_html} html")


if __name__ == "__main__":
    main()
