"""Promote the first <td> in every <tbody> row to <th scope='row'> on tables
whose left column is a row label (term, type, framework, etc.).

This was triaged by hand: of the 26 tables in docs/chapters/*.html, 25 fit
the "left column names the subject of the row" pattern. The lone exception
is ch04.html's Traditional-vs-Zero-Trust table, where both columns are data
columns being compared side-by-side. That table is listed in EXCLUDE.

Idempotent: rows where the first cell is already a <th> are skipped.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "chapters"

# (filename, zero-based table index) pairs to skip. Add new entries as the
# author introduces tables whose first column is not a row label.
EXCLUDE = {
    ("ch04.html", 1),  # Traditional Perimeter vs Zero Trust — side-by-side comparison
}

TABLE_RE = re.compile(r"<table\b[^>]*>.*?</table>", re.IGNORECASE | re.DOTALL)
TBODY_RE = re.compile(r"(<tbody\b[^>]*>)(.*?)(</tbody>)", re.IGNORECASE | re.DOTALL)
TR_RE = re.compile(r"(<tr\b[^>]*>)(.*?)(</tr>)", re.IGNORECASE | re.DOTALL)
FIRST_TD_RE = re.compile(r"<td\b([^>]*)>(.*?)</td>", re.IGNORECASE | re.DOTALL)


def promote_row(tr_match: re.Match) -> str:
    open_tag, inner, close_tag = tr_match.group(1), tr_match.group(2), tr_match.group(3)
    new_inner, n = FIRST_TD_RE.subn(
        lambda m: f'<th scope="row"{m.group(1)}>{m.group(2)}</th>',
        inner,
        count=1,
    )
    return f"{open_tag}{new_inner}{close_tag}"


def promote_tbody(tbody_match: re.Match) -> str:
    open_tag, inner, close_tag = tbody_match.group(1), tbody_match.group(2), tbody_match.group(3)
    return f"{open_tag}{TR_RE.sub(promote_row, inner)}{close_tag}"


def patch(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    tables = list(TABLE_RE.finditer(text))
    if not tables:
        return 0

    pieces = []
    last = 0
    promoted = 0
    for idx, m in enumerate(tables):
        pieces.append(text[last:m.start()])
        original_table = m.group(0)
        if (path.name, idx) in EXCLUDE:
            pieces.append(original_table)
        else:
            new_table = TBODY_RE.sub(promote_tbody, original_table)
            promoted += new_table.count('<th scope="row"') - original_table.count('<th scope="row"')
            pieces.append(new_table)
        last = m.end()
    pieces.append(text[last:])

    new_text = "".join(pieces)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return promoted


def main() -> None:
    total = 0
    for path in sorted(DOCS.glob("ch*.html")):
        n = patch(path)
        if n:
            print(f"{path.name}: +{n} row header(s)")
            total += n
    print(f"\nPromoted {total} cell(s) to <th scope='row'>.")


if __name__ == "__main__":
    main()
