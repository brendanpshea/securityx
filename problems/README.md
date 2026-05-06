# Interactive Problems

One JSON file per problem. The build script (`src/scripts/build_problems.py`)
renders these into static HTML pages under `docs/problems/`.

## Schema

```json
{
  "id": "ch01-snow-white-awareness",
  "chapter": 1,
  "title": "Snow White Builds an Awareness Program",
  "context_md": "Markdown setup, 100-300 words. May reference textbook characters.",
  "prompt_md": "Optional short instruction shown above the cloze body.",
  "body_md": "Markdown with {{token}} placeholders for each blank.",
  "blanks": {
    "token_name": {
      "answer": "Correct option text",
      "distractors": ["wrong 1", "wrong 2", "wrong 3", "wrong 4"],
      "explanation": "Why the answer is correct (revealed after Submit)."
    }
  }
}
```

### Authoring rules
- Each blank's `distractors` must be coherent with the answer (same category:
  all IPs, all tools, all frameworks, etc.) — per-blank pools are intentional.
- Aim for 5-15 blanks per problem.
- `id` becomes the page filename (`docs/problems/<id>.html`) and the
  `localStorage` key.
- `body_md` may use any markdown; tokens are replaced at build time with
  span placeholders the renderer fills with `<select>` elements.

## Build

```
python src/scripts/build_problems.py
```
