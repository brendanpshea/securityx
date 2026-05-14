"""Inject a 'Skip to content' link and id='main' into every generated HTML
page under docs/. Idempotent — re-running on already-updated files is a no-op."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

SKIP_LINK = '<a class="skip-link" href="#main">Skip to content</a>'

BODY_RE = re.compile(r"(<body[^>]*>)", re.IGNORECASE)
MAIN_RE = re.compile(r"<main\b([^>]*)>", re.IGNORECASE)


def patch(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    if SKIP_LINK not in text:
        m = BODY_RE.search(text)
        if m:
            insert_at = m.end()
            text = text[:insert_at] + "\n    " + SKIP_LINK + text[insert_at:]

    def add_id(match: re.Match) -> str:
        attrs = match.group(1)
        if re.search(r"\bid\s*=", attrs):
            return match.group(0)
        return f'<main id="main"{attrs}>'

    text = MAIN_RE.sub(add_id, text, count=1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in DOCS.rglob("*.html"):
        if patch(path):
            changed += 1
            print(f"updated {path.relative_to(ROOT)}")
    print(f"\n{changed} file(s) updated")


if __name__ == "__main__":
    main()
