# Accessibility Statement

*CompTIA SecurityX (CAS-005) Textbook*

We want this textbook to work for everyone preparing for the SecurityX exam, including learners who use screen readers, keyboard navigation, screen magnifiers, or other assistive technology. This page summarizes the accessibility features in place, the standard we aim for, the known gaps we are still working on, and how to report problems.

## Conformance Target

The site targets **WCAG 2.1 Level AA**. It has not been independently audited; the statement below reflects internal review of the published HTML and source markdown as of May 2026.

## What Is in Place

- **Semantic structure.** Each chapter uses a single `<h1>`, properly nested `<h2>`/`<h3>` headings, and ordered/unordered lists, so screen readers and reader-mode tools can navigate the document outline.
- **Descriptive alt text.** Every figure in chapters 1–12 has an alt attribute that describes what the diagram shows — not just its title — so the educational content is available to screen-reader users. Figures with on-page captions (`*Figure X.Y: ...*`) duplicate the caption text into the alt attribute on purpose.
- **Text-first content.** All concepts, case studies, key points, and warnings are presented as text. Figures reinforce the prose but no exam-relevant content is image-only.
- **Keyboard navigation.** Every link, including the practice-problem inputs, is reachable and operable from the keyboard. There are no custom interactive controls that bypass the browser's focus model.
- **Color is not the only signal.** Callout boxes (Case Study, Warning, Key Point, Thought Question, Example) all carry a visible text label in addition to their color treatment.
- **Resizable text.** The stylesheet uses relative units, so browser zoom and OS-level text-size settings scale the content without breaking layout up to 200%.
- **Language declared.** Every page declares `lang="en"` so assistive tech selects the correct pronunciation.

## Known Limitations

- **Generated diagrams.** Figures are rendered as PNG. The alt text conveys the concept, but the underlying matplotlib source (in `src/scripts/generate_figures_chXX.py`) is not yet exposed as SVG with `<title>`/`<desc>` elements. SVG with structured descriptions is on the roadmap.
- **Color contrast in dark theme.** The site uses a dark-mode-first palette. Most text/background pairs meet AA, but a small number of accent colors used inside callout titles approach the 4.5:1 floor. If you encounter a specific combination that is hard to read, please report it — it is faster for us to fix a real example than to re-audit the whole palette.
- **Practice-problem feedback.** The cloze-style problems give visual cues (green/red borders) when an answer is checked. A screen-reader-friendly status announcement (via `aria-live`) is planned but not yet implemented.
- **No transcripts for figures.** A small number of complex figures (e.g., the Cyber Kill Chain, the AI/ML pipeline) would benefit from a long-description `<details>` block in addition to the alt text. This will roll out as the figures are migrated to SVG.

## Reporting an Issue

If you hit something that does not work with your assistive technology — or you have a suggestion for how to make a section clearer — please open an issue at <https://github.com/brendanpshea/securityx/issues> or email <brendanpshea@gmail.com>. Include the page URL, the assistive tech you are using, and what you expected to happen. Accessibility bug reports are treated as priority issues.

## Last Reviewed

2026-05-14
