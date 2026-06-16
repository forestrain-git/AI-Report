---
description: "从大纲MD生成HTML幻灯片，支持迭代编辑、部署到Cloudflare、发送飞书。完整的PPT制作流水线。"
agent: main
---

# PPT 制作流水线

从大纲 markdown 到可演示的 HTML 幻灯片，一站式完成。

## 输入

`$ARGUMENTS` — 大纲文件路径（如 `ppt/outlines/PPT结构讨论-v2.1.md`），或直接描述需求。

## 流水线步骤

### Phase 1：大纲确认

1. 读取大纲文件，理解结构（Part 1-N、每页标题、内容类型）
2. 如果用户未指定风格，询问：
   - 风格选择：`guizang-whiteboard`（白底楷体蓝，国企宣讲）还是 `frontend-slides`（创意动画风）
   - 是否需要部署到 Cloudflare
   - 是否需要发送飞书
3. 确认大纲无误后进入生成

### Phase 2：HTML 生成

根据选定风格调用对应技能：

- **白板蓝风格** → 调用 `guizang-whiteboard` 技能，基于 `ppt/outlines/` 大纲生成
- **创意动画风格** → 调用 `frontend-slides` 技能

生成规则：
- 输出到 `ppt/html-deck/` 目录
- 单文件 HTML，内联所有 CSS/JS
- 保持 16:9 固定舞台
- 每页 `<section class="slide">` 带唯一 ID

### Phase 3：迭代编辑

用户可能对生成结果提出修改：
- 单页内容调整 → 直接 Edit 对应 section
- 整体结构调整 → 回到 Phase 1 修改大纲后重新生成
- 风格微调 → 修改 CSS 变量或布局参数

### Phase 4：部署（可选）

如果用户要求部署：
1. 确认 Cloudflare token 可用（检查环境变量或 `.env` 文件）
2. 调用 `cloudflare-deploy` 技能
3. 返回公网链接

### Phase 5：分发（可选）

如果用户要求发飞书：
1. 使用飞书 API 上传文件或发送链接
2. 确认发送成功

## 常用文件路径

| 内容 | 路径 |
|:---|:---|
| 大纲文件 | `ppt/outlines/*.md` |
| 逐页提示词 | `ppt/outlines/国企AI宣讲-逐页提示词-PPT生成用.md` |
| HTML 输出 | `ppt/html-deck/` |
| 演讲支持 | `ppt/演讲支持/` |
| 会后资源 | `ppt/assets/` |

## 注意事项

- 大纲是核心：先确保大纲内容准确、逻辑通顺，再生成 HTML
- 每次修改后重新检查 16:9 舞台是否溢出
- 知识库引用在脚注中标注"小组调研"
- 保持承上启下的叙事逻辑，每页标题要能独立概括本页内容
