# Accessibility Statement

*CompTIA SecurityX (CAS-005) Textbook*

We want this textbook to work for everyone preparing for the SecurityX exam, including learners who use screen readers, keyboard navigation, screen magnifiers, or other assistive technology. This page summarizes the accessibility features in place, the standard we aim for, the known gaps we are still working on, and how to report problems.

## Conformance Target

The site targets **WCAG 2.1 Level AA**. It has not been independently audited; the statement below reflects internal review of the published HTML and source markdown as of May 2026.

## What Is in Place

- **Semantic structure.** Each chapter uses a single `<h1>`, properly nested `<h2>`/`<h3>` headings, ordered/unordered lists, and a single `<main id="main">` landmark, so screen readers and reader-mode tools can navigate the document outline.
- **Skip link.** Every page begins with a "Skip to content" link that becomes visible on first Tab. Keyboard users can jump past the header on every page.
- **Visible focus indicator.** A high-contrast yellow focus ring (~12:1 against the page background) appears on every keyboard-focused link, button, and form control. Browser default outlines are not suppressed.
- **Table column and row headers.** Every `<th>` in a table header row carries `scope="col"`, and on tables whose left column names the subject of each row (e.g., "Document Type," "Threat Actor," "Certificate Type") the first cell of every body row is `<th scope="row">`. Screen readers in table-navigation mode therefore re-announce both the column header and the row label as the user moves between cells.
- **Table captions.** Every table carries a `<caption>` element naming the table and summarizing what it compares ("Table 5.2: Common IAM-centric TTPs ..."). Screen readers announce the caption on table entry, so users know what the table is about before navigating into the cells.
- **Descriptive alt text.** Every figure in chapters 1–12 has an alt attribute that describes what the diagram shows — not just its title — so the educational content is available to screen-reader users. Figures with on-page captions (`*Figure X.Y: ...*`) duplicate the caption text into the alt attribute on purpose.
- **Text-first content.** All concepts, case studies, key points, and warnings are presented as text. Figures reinforce the prose but no exam-relevant content is image-only.
- **Keyboard navigation.** Every link, button, and form control is reachable and operable from the keyboard. There are no custom interactive controls that bypass the browser's focus model.
- **Practice-problem feedback.** When you check answers on a cloze exercise, the score is announced through an `aria-live` status region, incorrect answers are marked with `aria-invalid="true"`, and each blank carries an `aria-label` identifying its position ("Answer 3 of 7"). Color is paired with text labels in the explanation panel so the green ✓ / red ✗ is not the only signal.
- **Reduced motion.** The site honors `prefers-reduced-motion`. Hover transforms, transitions, and animations collapse to near-zero duration for users who request that preference.
- **Color is not the only signal.** Callout boxes (Case Study, Warning, Key Point, Thought Question, Example) all carry a visible text label in addition to their color treatment.
- **Resizable text.** The stylesheet uses relative units, so browser zoom and OS-level text-size settings scale the content without breaking layout up to 200%.
- **Language declared.** Every page declares `lang="en"` so assistive tech selects the correct pronunciation.

## Known Limitations

- **Generated diagrams.** Figures are rendered as PNG. The alt text conveys the concept, but the underlying matplotlib source (in `src/scripts/generate_figures_chXX.py`) is not yet exposed as SVG with `<title>`/`<desc>` elements. SVG with structured descriptions is on the roadmap.
- **Color contrast in dark theme.** The site uses a dark-mode-first palette. Body text, accent links, and primary buttons all pass AA against their backgrounds, but the palette has not been independently re-measured against WCAG 2.1 since the last theme adjustment. If you encounter a specific combination that is hard to read, please report it.
- **No transcripts for figures.** A small number of complex figures (e.g., the Cyber Kill Chain, the AI/ML pipeline) would benefit from a long-description `<details>` block in addition to the alt text. This is on the roadmap.

## Reporting an Issue

If you hit something that does not work with your assistive technology — or you have a suggestion for how to make a section clearer — please open an issue at <https://github.com/brendanpshea/securityx/issues> or email <brendanpshea@gmail.com>. Include the page URL, the assistive tech you are using, and what you expected to happen. Accessibility bug reports are treated as priority issues.

## Last Reviewed

2026-05-14
