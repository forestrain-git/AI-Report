# Frontend Slides Production Prompt

> Humanize PPT stops here. The next agent must follow
> `~/.agents/skills/frontend-slides/SKILL.md` end to end.
> Do not reimplement the renderer inside Humanize.

## Deck

- Title: AI 安全帽：中建发展 AI 硬件战略的第一步
- Source: D:\Projects\AI-Report\assets\ai-safety-helmet-brief-source.md
- Language: zh
- Slides: 8

## Hard rules

- Read `frontend-slides/SKILL.md` first. Use its native PPTX→HTML
  conversion, viewport-safe deck, and Vercel deploy path.
- Use the registered layouts / templates that skill ships with. Do not
  invent layout classes.
- Do not post-process the rendered HTML in Humanize. Frontend-slides
  owns its own navigation, presenter shell, and deploy step.

## Inputs already produced by Humanize

- `deck_brief.md`
- `ast_outline.md`
- `slide_plan.json`
- `speaker_intent.md`
- `asset_manifest.md`
- `video_slots.json`
- `style_brief.md`

## Hand-off

The next agent writes its output to its own convention
(e.g. `outputs/frontend-slides-rendered/index.html`).
