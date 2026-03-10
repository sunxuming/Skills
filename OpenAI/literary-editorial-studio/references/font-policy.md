# Font Policy

Use this reference when the user asks for typography planning, font recommendations, or release packaging that mentions fonts.

## Core policy

- Do not bundle font binaries in this skill or in any public repo unless redistribution rights are explicitly verified.
- Prefer open fonts with a current, permissive license published by the official project source.
- Treat all font guidance as `low-risk` rather than guaranteed safe. Re-check the current license text before commercial release, redistribution, embedding, or sublicensing.
- Keep a written font manifest for each deliverable: font name, source URL, intended use, and the date of the last license check.

## Low-risk examples

These are useful starting points when their current license text still matches the official source:

- `Noto Sans CJK SC` / `Noto Serif CJK SC`
- `Source Han Sans SC` / `Source Han Serif SC`
- `LXGW WenKai`

## Red flags

- Fonts downloaded from mirror sites or unclear reposts.
- Fonts with unknown authorship or missing license text.
- Proprietary fonts copied from another computer or software bundle.
- Modified font files whose naming and reserved-font-name terms were not reviewed.
- Public repos that include third-party font binaries without a clear redistribution basis.

## Font manifest shape

```json
{
  "fonts": [
    {
      "name": "Noto Serif CJK SC",
      "use": "body",
      "source": "official",
      "last_checked": "2026-03-10"
    }
  ]
}
```

## Practical rules

- Keep font plans small. One body family and one display family are usually enough.
- Prefer fonts with broad language coverage when the manuscript contains mixed Chinese and Latin text.
- If the license status is unclear, mark the font `manual-review-required` and recommend an open alternative.
