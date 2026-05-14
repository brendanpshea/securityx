import os
import re
import shutil
import subprocess
from pathlib import Path

# Setup directories
ROOT_DIR = Path(__file__).parent.parent.parent
SRC_DIR = ROOT_DIR / "src" / "chapters"
DOCS_DIR = ROOT_DIR / "docs" / "chapters"
BIBLIOGRAPHY_FILE = ROOT_DIR / "refs.bib"

# Ensure output directory exists
DOCS_DIR.mkdir(parents=True, exist_ok=True)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - CompTIA SecurityX</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <a class="skip-link" href="#main">Skip to content</a>
    <div class="container">
        <header>
            <a href="../index.html" class="back-link">Table of Contents</a>
        </header>
        <main id="main">
            {content}
        </main>
    </div>
</body>
</html>
"""

def inject_callout_classes(html_content):
    """
    Parses HTML blockquotes and injects specific CSS classes
    based on the bolded tag (e.g., [Case Study], [Warning]).
    It also removes the brackets from the final output.
    """
    callouts = [
        ("[Case Study]", "callout-case-study", "Case Study"),
        ("[Warning]", "callout-warning", "Warning"),
        ("[Key Point]", "callout-key-point", "Key Point"),
        ("[Thought Question]", "callout-thought", "Thought Question"),
        ("[Example]", "callout-example", "Example")
    ]
    
    for tag, css_class, title in callouts:
        escaped_tag = re.escape(tag)
        # Look for <blockquote><p><strong>[Tag]</strong>
        pattern = re.compile(rf'(<blockquote>\s*<p>\s*<strong>{escaped_tag}</strong>)', re.IGNORECASE)
        # Replace the <blockquote> and remove the brackets from the tag
        html_content = pattern.sub(rf'<blockquote class="{css_class}">\n<p><strong class="callout-title">{title}</strong>', html_content)

    for tag, css_class, title in callouts:
        escaped_tag = re.escape(tag)
        nested_pattern = re.compile(rf'</p>\s*<p>\s*<strong>{escaped_tag}</strong>', re.IGNORECASE)
        html_content = nested_pattern.sub(
            rf'</p>\n</blockquote>\n<blockquote class="{css_class}">\n<p><strong class="callout-title">{title}</strong>',
            html_content,
        )
        
    return html_content

def relax_list_formatting(text):
    """
    Automatically inserts a blank line before markdown lists if the user forgot one.
    This makes the markdown parser less sensitive and prevents lists from being
    smashed into the previous paragraph.
    """
    lines = text.split('\n')
    new_lines = []
    
    list_marker_pattern = re.compile(r'^(?:\s*>\s*)?(?:[-*+]|\d+\.)\s+')
    
    for i, line in enumerate(lines):
        if list_marker_pattern.match(line):
            if i > 0:
                prev_line = lines[i-1].strip()
                if prev_line and prev_line != '>':
                    if not list_marker_pattern.match(lines[i-1]):
                        if line.lstrip().startswith('>'):
                            new_lines.append('>')
                        else:
                            new_lines.append('')
        new_lines.append(line)
        
    return '\n'.join(new_lines)

_THEAD_RE = re.compile(r"<thead\b[^>]*>(.*?)</thead>", re.IGNORECASE | re.DOTALL)
_TH_RE = re.compile(r"<th\b([^>]*)>", re.IGNORECASE)


def add_table_header_scopes(html_content):
    """Add scope='col' to every <th> inside a <thead> so screen readers
    re-announce the column header as the user navigates down a column
    (WCAG 1.3.1). Idempotent."""
    def patch_th(match):
        attrs = match.group(1)
        if re.search(r"\bscope\s*=", attrs, re.IGNORECASE):
            return match.group(0)
        return f'<th scope="col"{attrs}>'

    def patch_thead(match):
        return f"<thead>{_TH_RE.sub(patch_th, match.group(1))}</thead>"

    return _THEAD_RE.sub(patch_thead, html_content)


def separate_adjacent_callouts(text):
    """
    Inserts a blank line before a new markdown callout blockquote tag when it
    immediately follows another blockquote. Without this, Markdown treats the
    second callout as part of the first blockquote, which causes styling bleed.
    """
    lines = text.split('\n')
    new_lines = []
    callout_pattern = re.compile(r'^>\s+\*\*\[(Case Study|Warning|Key Point|Thought Question|Example)\]\*\*\s*$')

    for i, line in enumerate(lines):
        if callout_pattern.match(line) and i > 0:
            prev_line = lines[i - 1]
            if prev_line.strip().startswith('>') and prev_line.strip() != '>':
                new_lines.append('')
        new_lines.append(line)

    return '\n'.join(new_lines)

def compile_markdown_to_html(text):
    """
    Render Markdown to HTML with Pandoc citeproc so citations and the
    bibliography are resolved at build time with no client-side JavaScript.
    """
    pandoc_path = shutil.which('pandoc')
    if pandoc_path is None:
        raise RuntimeError(
            'Pandoc is required to build chapter HTML because citations are rendered '
            'statically at build time. Install Pandoc and ensure it is on PATH.'
        )

    if not BIBLIOGRAPHY_FILE.exists():
        raise RuntimeError(f'Missing bibliography file: {BIBLIOGRAPHY_FILE}')

    result = subprocess.run(
        [
            pandoc_path,
            '--from=markdown+smart+citations+pipe_tables+fenced_code_blocks',
            '--to=html5',
            '--citeproc',
            f'--bibliography={BIBLIOGRAPHY_FILE}',
            '-M',
            'link-citations=true',
            '-M',
            'reference-section-title=References',
        ],
        input=text,
        text=True,
        encoding='utf-8',
        capture_output=True,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or 'Pandoc failed without stderr output.')

    return result.stdout

def build():
    print(f"Building chapters from {SRC_DIR} to {DOCS_DIR}...")
    
    if not SRC_DIR.exists():
        print("No source chapters found. Exiting.")
        return

    for md_file in sorted(SRC_DIR.glob('*.md')):
        with open(md_file, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # Extract title from the first line if it's an H1
        title = "Chapter"
        first_line = text.split('\n')[0]
        if first_line.startswith('# '):
            title = first_line[2:].strip()
            
        # Relax list formatting
        text = relax_list_formatting(text)
        text = separate_adjacent_callouts(text)
            
        # Convert to HTML with static citation support.
        raw_html = compile_markdown_to_html(text)
        
        # Inject our premium callout classes
        processed_html = inject_callout_classes(raw_html)
        processed_html = add_table_header_scopes(processed_html)
        
        # Wrap in template
        final_html = HTML_TEMPLATE.format(title=title, content=processed_html)
        
        # Write to docs/chapters/
        out_name = md_file.stem + '.html'
        out_path = DOCS_DIR / out_name
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
            
        print(f"Compiled: {md_file.name} -> {out_name}")

if __name__ == "__main__":
    build()
