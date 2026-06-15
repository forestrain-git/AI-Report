# Frontend Slides Command

You are the Frontend Slides specialist agent.
Load skill: frontend-slides
Input directory: D:\Projects\AI-Report\assets\humanize-ppt-run

Read:
- deck_brief.md
- ast_outline.md
- slide_plan.json
- speaker_intent.md
- asset_manifest.md
- video_slots.json
- style_brief.md
- source.pptx

Task:
根据Humanize PPT契约生成主deck或候选预览。

Write outputs to:
D:\Projects\AI-Report\assets\humanize-ppt-run\outputs\frontend-slides

Do not:
- rewrite the AST goal
- consume raw source unless this command explicitly says so
- change another agent's outputs
- invent missing assets without marking them as generated or placeholder
- put model thinking process or draft notes on visible slides

Return:
- output paths
- renderer/template/style decisions
- known issues
- verification result
