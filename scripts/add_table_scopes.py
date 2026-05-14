"""Add scope='col' to every <th> inside a <thead> in generated HTML pages.

Screen readers in table-navigation mode use scope to re-announce the column
header as a user arrows down a column. Without it, every data cell is read
without context. This is the single biggest table-accessibility win available
without changes to the markdown source (WCAG 1.3.1).

Idempotent: existing scope attributes are left alone.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

THEAD_RE = re.compile(r"<thead\b[^>]*>(.*?)</thead>", re.IGNORECASE | re.DOTALL)
TH_RE = re.compile(r"<th\b([^>]*)>", re.IGNORECASE)


def add_scope_to_th(th_attrs: str) -> str:
    if re.search(r"\bscope\s*=", th_attrs, re.IGNORECASE):
        return f"<th{th_attrs}>"
    return f'<th scope="col"{th_attrs}>'


def patch_thead(match: re.Match) -> str:
    inner = match.group(1)
    new_inner = TH_RE.sub(lambda m: add_scope_to_th(m.group(1)), inner)
    return f"<thead>{new_inner}</thead>"


def patch(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    new_text, count = THEAD_RE.subn(patch_thead, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    # Count how many <th>s actually gained a scope.
    return new_text.count('scope="col"') - text.count('scope="col"')


def main() -> None:
    total = 0
    for path in sorted(DOCS.rglob("*.html")):
        n = patch(path)
        if n:
            print(f"{path.relative_to(ROOT)}: +{n} scope attribute(s)")
            total += n
    print(f"\nAdded scope='col' to {total} header cell(s).")


if __name__ == "__main__":
    main()
