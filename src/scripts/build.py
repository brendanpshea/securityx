import os
import re
import markdown
from pathlib import Path

# Setup directories
ROOT_DIR = Path(__file__).parent.parent.parent
SRC_DIR = ROOT_DIR / "src" / "chapters"
DOCS_DIR = ROOT_DIR / "docs" / "chapters"

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
    <div class="container">
        <header>
            <a href="../index.html" class="back-link">Table of Contents</a>
        </header>
        <main>
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
        html_content = pattern.sub(rf'<blockquote class="{css_class}">\n<p><strong>{title}</strong>', html_content)
        
    return html_content

def build():
    print(f"Building chapters from {SRC_DIR} to {DOCS_DIR}...")
    
    # Optional: support for tables and fenced code blocks
    md = markdown.Markdown(extensions=['tables', 'fenced_code'])
    
    if not SRC_DIR.exists():
        print("No source chapters found. Exiting.")
        return

    for md_file in SRC_DIR.glob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # Extract title from the first line if it's an H1
        title = "Chapter"
        first_line = text.split('\n')[0]
        if first_line.startswith('# '):
            title = first_line[2:].strip()
            
        # Convert to HTML
        raw_html = md.convert(text)
        
        # Inject our premium callout classes
        processed_html = inject_callout_classes(raw_html)
        
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
