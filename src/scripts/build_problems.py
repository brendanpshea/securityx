"""Build interactive problem pages from problems/*.json into docs/problems/."""

import json
import re
import html
from pathlib import Path

import markdown

ROOT = Path(__file__).parent.parent.parent
SRC = ROOT / "problems"
OUT = ROOT / "docs" / "problems"
OUT.mkdir(parents=True, exist_ok=True)

TOKEN_RE = re.compile(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}")

PAGE_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - SecurityX PBQ</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="stylesheet" href="../assets/css/problem.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <a class="skip-link" href="#main">Skip to content</a>
    <div class="container">
        <header>
            <a href="./index.html" class="back-link">&larr; All PBQs</a>
        </header>
        <main id="main">
            <p class="problem-chapter">Chapter {chapter}</p>
            <h1>{title}</h1>

            <section class="problem-context">{context_html}</section>
            {artifact_block}
            <section class="problem-prompt">{prompt_html}</section>

            <form id="cloze-form" class="problem-body" data-problem-id="{pid}">
                {body_html}
                <div class="problem-actions">
                    <button type="submit" class="btn btn-primary" id="btn-submit">Check answers</button>
                    <button type="button" class="btn btn-ghost" id="btn-reset">Reset</button>
                    <span id="score-readout" class="score-readout" role="status" aria-live="polite" aria-atomic="true"></span>
                </div>
            </form>
        </main>
    </div>

    <script id="problem-data" type="application/json">{data_json}</script>
    <script src="../assets/js/problem.js"></script>
</body>
</html>
"""

INDEX_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practice-Based Questions - SecurityX</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="stylesheet" href="../assets/css/problem.css">
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <a class="skip-link" href="#main">Skip to content</a>
    <div class="container">
        <header>
            <a href="../index.html" class="back-link">&larr; Table of Contents</a>
        </header>
        <main id="main">
            <h1>Practice-Based Questions</h1>
            <p>One PBQ per chapter. Read the setup, fill in the blanks, then click <strong>Check answers</strong>. You can retry until everything is green.</p>
            <ul class="problem-list">
                {items}
            </ul>
        </main>
    </div>
</body>
</html>
"""


def render_md(text: str) -> str:
    return markdown.markdown(text or "", extensions=["extra", "sane_lists"])


def replace_tokens(html_text: str, blanks: dict) -> str:
    def sub(match):
        name = match.group(1)
        if name not in blanks:
            return match.group(0)
        return f'<span class="cloze-blank" data-blank="{html.escape(name)}"></span>'
    return TOKEN_RE.sub(sub, html_text)


def build_problem(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))

    context_html = render_md(data.get("context_md", ""))
    prompt_html = render_md(data.get("prompt_md", ""))
    body_html = replace_tokens(render_md(data["body_md"]), data["blanks"])

    artifact_md = data.get("artifact_md", "")
    artifact_title = data.get("artifact_title", "")
    artifact_kind = data.get("artifact_kind", "")
    if artifact_md:
        kind_class = f" artifact-{artifact_kind}" if artifact_kind else ""
        label = artifact_title or "Supporting artifact"
        title_html = (
            f'<h2 class="problem-artifact-title">{html.escape(artifact_title)}</h2>'
            if artifact_title else ""
        )
        artifact_block = (
            f'<section class="problem-artifact{kind_class}" aria-label="{html.escape(label)}">'
            f'{title_html}'
            f'{render_md(artifact_md)}'
            f'</section>'
        )
    else:
        artifact_block = ""

    runtime = {
        "id": data["id"],
        "blanks": {
            name: {
                "answer": b["answer"],
                "distractors": b["distractors"],
                "explanation": b.get("explanation", ""),
            }
            for name, b in data["blanks"].items()
        },
    }

    page = PAGE_TMPL.format(
        title=html.escape(data["title"]),
        chapter=data["chapter"],
        pid=html.escape(data["id"]),
        context_html=context_html,
        artifact_block=artifact_block,
        prompt_html=prompt_html,
        body_html=body_html,
        data_json=json.dumps(runtime).replace("</", "<\\/"),
    )

    out_path = OUT / f"{data['id']}.html"
    out_path.write_text(page, encoding="utf-8")
    return data


def build_index(problems: list[dict]):
    problems = sorted(problems, key=lambda p: (p["chapter"], p["id"]))
    items = "\n".join(
        f'<li><a href="{html.escape(p["id"])}.html">'
        f'<span class="ch-tag">Ch {p["chapter"]}</span> {html.escape(p["title"])}'
        f"</a></li>"
        for p in problems
    )
    (OUT / "index.html").write_text(INDEX_TMPL.format(items=items), encoding="utf-8")


def main():
    problems = []
    for path in sorted(SRC.glob("*.json")):
        print(f"Building {path.name}")
        problems.append(build_problem(path))
    build_index(problems)
    print(f"Built {len(problems)} problem(s) -> {OUT}")


if __name__ == "__main__":
    main()
