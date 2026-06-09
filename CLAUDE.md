# AI 知识库与科普 PPT 制作 - Schema 规范

这是 AI 知识库与科普 PPT 制作项目的 LLM Wiki Schema。所有与此项目相关的 AI 助手操作都应遵循此规范。

---

## 项目背景

**项目名称**: AI 知识库与科普 PPT 制作
**核心目标**:
1. 汇总全网最先进的 AI 知识，构建结构化知识库
2. 制作 AI 科普系列 PPT，覆盖不同受众（小白/进阶/专业）
3. 追踪 AI 行业动态，保持知识库时效性
4. 沉淀 AI 学习路径和最佳实践

**资料类型**:
- 学术论文与技术报告（arXiv、Google Research、OpenAI 等）
- 官方文档与博客（模型发布、技术解读、API 文档）
- 行业文章与解读（技术博客、媒体分析、播客转录）
- 新闻动态（产品发布、融资、政策、争议事件）
- 开源项目与工具（GitHub、HuggingFace 等）
- PPT 素材（图表、示意图、图标、配色方案）

---

## 目录结构

```
AI-Teaching/
├── CLAUDE.md              # 本文件：Schema规范
├── index.md               # 知识库总索引（由LLM维护）
├── log.md                 # 操作日志（由LLM维护）
├── raw/                   # 原始资料（只读，人放入，LLM读取）
│   ├── inbox/            # 【暂存区】丢入文件和文件夹，我来处理
│   ├── papers/           # 论文/技术报告（从inbox自动归类）
│   ├── articles/         # 行业文章/博客（从inbox自动归类）
│   ├── news/             # 新闻动态（从inbox自动归类）
│   └── assets/           # 图片、图表、PPT素材（从inbox自动归类）
├── wiki/                  # LLM生成的知识库
│   ├── sources/          # 源文件摘要（按原始资料生成）
│   ├── concepts/         # 概念页面（AI术语、技术原理）
│   ├── models/           # 模型页面（各LLM、AI模型介绍）
│   ├── tools/            # 工具页面（AI工具、平台）
│   ├── industry/         # 行业应用页面
│   └── synthesis/        # 综合页面（科普文章、学习路径）
├── ppt/                   # PPT制作工作区
│   ├── outlines/         # PPT大纲（按系列/主题存放）
│   ├── scripts/          # 演讲稿/逐字稿
│   └── assets/           # PPT专用素材（从wiki/assets复制或生成）
└── scripts/               # 辅助脚本
```

**文件存放说明**：
1. **推荐方式**：把所有文件和文件夹丢进 `raw/inbox/` 暂存区
2. 告诉我"处理inbox"，我会：
   - 扫描 inbox 中的所有文件（包括子文件夹里的）
   - **处理重复文件**（见下方重复文件规则）
   - **自动分类**到 papers/articles/news/assets
   - **生成摘要**并更新wiki
3. **重复文件处理规则**：
   - 如果文件名相同 → 保留修改时间较新的文件
   - 如果内容相似（如同一模型的不同版本报告）→ 保留新版本，旧版标记为archived
   - 在日志中记录重复文件处理情况

---

## 页面类型定义

### 1. wiki/sources/ - 源文件摘要

每导入一个原始文档，创建一个对应的摘要页面。

**命名规范**: `源文件名称.md`（保持与原始文件同名，去除扩展名，英文优先）

**必须包含的Frontmatter**:
```yaml
---
type: source
source_file: "raw/papers/XXX.pdf"  # 原始文件路径
ingest_date: "2026-04-27"
summary: "一句话总结"
tags: ["LLM", "Transformer", "OpenAI"]
---
```

**内容结构**:
- 文档基本信息（名称、作者、发布时间、来源）
- 核心要点（3-5条）
- 关键数据/结论
- 涉及的相关概念和模型（双向链接）
- 与其他源文件的关系（更新、反驳、补充）

### 2. wiki/concepts/ - 概念页面

对 AI 领域核心概念建立独立页面。

**概念分类**:
- **基础概念**: 机器学习、深度学习、神经网络、梯度下降、损失函数
- **架构概念**: Transformer、CNN、RNN、GAN、Diffusion
- **训练概念**: 预训练、微调、RLHF、提示工程、RAG、Agent
- **应用概念**: 多模态、代码生成、图像生成、语音识别
- **前沿概念**: MoE、推理模型、世界模型、具身智能

**命名规范**: 概念名称.md，如 `Transformer.md`、`提示工程.md`、`RAG.md`

**必须包含的Frontmatter**:
```yaml
---
type: concept
concept_type: "architecture"  # architecture/training/application/frontier
related_models: ["models/GPT-4.md"]
related_sources: ["sources/Attention_Is_All_You_Need.md"]
difficulty: "intermediate"  # beginner/intermediate/advanced
last_updated: "2026-04-27 14:30"
tags: []
---
```

**内容结构**:
- 概念定义（一句话 + 详细解释）
- 直观理解/类比（帮助科普 PPT 表达）
- 技术原理（公式、图示描述）
- 典型应用
- 常见误区
- 演进历史
- 相关概念链接
- PPT 表达建议（哪些点适合用图、哪些适合举例）

### 3. wiki/models/ - 模型页面

对主流 AI 模型建立独立页面。

**模型类型**:
- **大语言模型**: GPT 系列、Claude、Gemini、Llama、DeepSeek 等
- **图像生成模型**: DALL-E、Midjourney、Stable Diffusion、Flux 等
- **多模态模型**: GPT-4V、Claude 3、Gemini Pro 等
- **语音模型**: Whisper、ElevenLabs 等
- **代码模型**: Codex、CodeT5、StarCoder 等
- **推理模型**: o1、o3、DeepSeek-R1 等

**命名规范**: `模型名称.md`，如 `GPT-4.md`、`Claude-3.7-Sonnet.md`、`DeepSeek-V3.md`

**必须包含的Frontmatter**:
```yaml
---
type: model
model_type: "LLM"  # LLM/image/multimodal/voice/code/reasoning
organization: "OpenAI"
release_date: "2024-05-13"
status: "active"  # active/deprecated/preview
related_sources: ["sources/GPT-4_Technical_Report.md"]
last_updated: "2026-04-27 14:30"
tags: []
---
```

**内容结构**:
- 模型概览（定位、核心特点、适用场景）
- 技术规格（参数量、上下文长度、训练数据规模等）
- 版本演进（各版本差异、升级点）
- 性能表现（基准测试、横向对比）
- 使用方式（API、定价、免费额度）
- 典型应用案例
- 局限性与注意事项
- 竞品对比

### 4. wiki/tools/ - 工具页面

对 AI 工具、平台和框架建立独立页面。

**工具类型**:
- **对话工具**: ChatGPT、Claude、Kimi、文心一言、通义千问
- **图像工具**: Midjourney、Stable Diffusion WebUI、ComfyUI
- **开发工具**: Cursor、GitHub Copilot、V0、Claude Code
- **视频工具**: Sora、Runway、Pika、可灵
- **音频工具**: Suno、Udio、ElevenLabs
- **框架平台**: HuggingFace、LangChain、LlamaIndex、Ollama
- **Agent 框架**: AutoGPT、CrewAI、Dify、Coze

**命名规范**: `工具名称.md`，如 `ChatGPT.md`、`Cursor.md`、`ComfyUI.md`

**必须包含的Frontmatter**:
```yaml
---
type: tool
tool_type: "chat"  # chat/image/dev/video/audio/framework/agent
organization: "OpenAI"
pricing: "free/freemium/paid/opensource"
related_models: ["models/GPT-4.md"]
last_updated: "2026-04-27 14:30"
tags: []
---
```

**内容结构**:
- 工具简介（定位、核心功能）
- 上手指南（注册、基础使用）
- 高级技巧（提示词模板、工作流）
- 适用人群与场景
- 定价与限制
- 竞品对比
- 更新动态

### 5. wiki/industry/ - 行业应用页面

记录 AI 在各行业的应用实践。

**行业分类**:
- 教育、医疗、金融、法律、设计、编程、内容创作、游戏

**命名规范**: `行业名称.md`，如 `教育.md`、`医疗.md`、`内容创作.md`

**必须包含的Frontmatter**:
```yaml
---
type: industry
related_tools: ["tools/ChatGPT.md"]
related_models: []
last_updated: "2026-04-27 14:30"
tags: []
---
```

**内容结构**:
- 行业 AI 应用概览
- 典型应用场景与案例
- 常用工具组合
- 效果与局限
- 发展趋势

### 6. wiki/synthesis/ - 综合页面

高层次的整合内容，直接服务于科普 PPT 制作。

**核心页面**:
- `AI发展时间线.md` - 关键里程碑事件
- `AI学习路径.md` - 从入门到精通的学习路线
- `模型对比表.md` - 主流模型横向对比
- `工具选型指南.md` - 不同场景用什么工具
- `AI术语速查.md` - 快速查阅术语含义
- `AI安全与伦理.md` - AI 安全、对齐、伦理问题
- `AI行业趋势.md` - 当前热点与未来预测

**PPT 系列专题**（每个专题独立文件）:
- `PPT-什么是AI.md` - AI 小白入门
- `PPT-大语言模型原理.md` - LLM 原理科普
- `PPT-AI工具实战.md` - 工具使用指南
- `PPT-AI与未来.md` - AI 发展趋势与影响
- `PPT-AI安全.md` - AI 安全与伦理

**必须包含的Frontmatter**:
```yaml
---
type: synthesis
last_updated: "2026-04-27 14:30"
tags: []
---
```

### synthesis/ PPT 专题管理规则

- **每个 PPT 专题对应一个独立文件**：命名格式为 `synthesis/PPT-{专题名称}.md`
- **内容结构**：必须包含 PPT 大纲（每页标题 + 要点 + 配图建议）、演讲备注、参考资料
- **专题归档**：过时专题移动至 `synthesis/archived/`，并在索引中标记

---

## PPT 制作规范

### 1. PPT 大纲文件 (ppt/outlines/)

每个 PPT 大纲独立文件，命名格式：`{系列}-{序号}-{主题}.md`

**内容结构**:
```markdown
# PPT主题

## 基本信息
- 目标受众：初学者/进阶用户/专业人士
- 预计页数：20-30页
- 演讲时长：15-30分钟

## 大纲

### 第1页：封面
- 标题：XXX
- 副标题：XXX
- 配图建议：XXX

### 第2页：目录
- 要点1
- 要点2
- 要点3

### 第3页：什么是XXX
- 核心定义
- 类比解释
- 配图建议：XXX

...

## 演讲备注
- 开场白：XXX
- 过渡语：XXX
- 结尾总结：XXX

## 参考资料
- [[wiki/concepts/XXX]]
- [[wiki/models/XXX]]
```

### 2. PPT 素材管理 (ppt/assets/)

- 按专题分类存放素材
- 命名规范：`{专题}-{类型}-{描述}.{扩展名}`
- 类型：chart（图表）、diagram（示意图）、icon（图标）、photo（照片）

### 3. 受众分级

| 级别 | 特点 | PPT风格 |
|------|------|---------|
| 小白 | 非技术背景，第一次接触AI | 多用类比、少讲公式、图文并茂 |
| 进阶 | 用过AI工具，想了解原理 | 适度技术细节、原理图解 |
| 专业 | 开发者/研究者 | 深入技术、论文引用、代码示例 |

---

## 工作流程

### 流程0：处理 inbox 暂存区 (Process Inbox)

当用户将文件放入 `raw/inbox/`（包括子文件夹）并要求处理时：

1. **扫描 inbox**
   - 递归扫描 inbox/ 及其所有子文件夹
   - 列出所有待处理文件

2. **处理重复文件**（去重规则）
   - **文件名相同**：
     - 比较修改时间，保留较新的文件
     - 删除（或移动至 inbox/archived/）旧文件
     - 在日志中记录
   - **内容相似**（如同一模型的不同版本报告）：
     - 保留最新版本
     - 旧版本移动至 `raw/archived/`
     - 在日志中标记版本替换关系

3. **自动分类**
   - 读取每个文件内容，判断类型：
     - `raw/papers/` - 论文、技术报告、arXiv 预印本
     - `raw/articles/` - 行业文章、博客、解读
     - `raw/news/` - 新闻、动态、公告
     - `raw/assets/` - 图片、图表、示意图、PPT素材
   - 移动文件到对应文件夹
   - 如果目标位置已有同名文件，执行去重规则

4. **清理 inbox**
   - 处理完成后，清空 inbox/（删除空文件夹）

5. **继续流程1**（导入新资料）

### 流程1：导入新资料 (Ingest)

当用户将新文件放入 raw/ 目录并要求处理时：

1. **自动归类**（如果文件在 raw/ 根目录）
   - 读取文件内容，判断文件类型
   - 移动到对应子文件夹
   - 在日志中记录移动操作

2. **读取源文件**
   - **首选工具**：使用 `markitdown` Python API 将文档转换为结构化 Markdown
     - 支持格式：PDF、Word、Excel、PowerPoint、HTML、Markdown
     - **Windows 环境**：通过 Python 脚本调用，写入 UTF-8 编码文件
   - **markitdown 失败处理**：
     1. 检查依赖缺失 → 提示安装
     2. 检查扫描版 PDF → fallback 到 OCR 或视觉 LLM
   - **纯图片**：归档到 `raw/assets/`

3. **创建源摘要** (wiki/sources/)
   - 根据模板创建源文件摘要页
   - 提取核心要点和关键数据

4. **更新概念页** (wiki/concepts/)
   - 识别文档中涉及的概念
   - 更新现有概念页，或创建新概念页

5. **更新模型页** (wiki/models/)
   - 识别文档中提及的模型
   - 更新现有模型页，或创建新模型页

6. **更新工具页** (wiki/tools/)
   - 识别文档中提及的工具
   - 更新或创建工具页

7. **更新索引** (index.md)

8. **记录日志** (log.md)

### 流程2：回答问题 (Query)

当用户提出关于 AI 的问题时：

1. **读取 index.md** - 了解知识库整体结构
2. **定位相关页面** - 根据问题找到相关概念/模型/工具页
3. **读取详细内容** - 深入阅读相关页面
4. **综合分析** - 结合多个来源给出答案
5. **生成引用** - 答案中标注信息来源

**可选：生成科普内容**
- 如果用户需要，可将分析结果保存为 synthesis/ 下的新页面

### 流程3：制作 PPT (Create PPT)

当用户要求制作 AI 科普 PPT 时：

1. **明确 PPT 主题和受众**
   - 主题：AI 入门、LLM 原理、工具使用等
   - 受众：小白/进阶/专业
   - 页数：预计多少页

2. **检索相关资料**
   - 查阅相关概念页、模型页、工具页
   - 查阅 synthesis/ 下是否有类似专题

3. **设计大纲**
   - 构建 PPT 结构（封面→目录→正文→总结→Q&A）
   - 每页规划：标题、核心要点、配图建议
   - 考虑叙事逻辑（由浅入深、问题驱动、案例驱动）

4. **生成大纲文件**
   - 保存至 `ppt/outlines/`
   - 包含演讲备注和参考资料

5. **收集/建议素材**
   - 列出需要的图表、示意图
   - 建议从 wiki 中提取的内容

6. **审核与输出**
   - 提示用户大纲可进一步调整
   - 如需实际 PPT 文件，建议使用 PowerPoint/Keynote/Gamma 等工具

### 流程4：更新动态 (Update)

当用户要求更新 AI 行业动态时：

1. **明确更新范围**
   - 时间范围：本周/本月/本季度
   - 主题范围：全领域/特定方向（如模型发布、工具更新）

2. **检索新资料**
   - 检查 raw/news/ 和 raw/articles/ 中的新文件
   - 如无新文件，提示用户先放入资料

3. **整理动态**
   - 按类别汇总（模型发布、工具更新、政策、融资等）
   - 标注重要程度（🔥重磅 / ⭐重要 / 📌参考）

4. **更新页面**
   - 更新相关模型页、工具页
   - 更新 `synthesis/AI行业趋势.md`

5. **生成动态简报**
   - 可选保存为 `synthesis/AI动态-{日期}.md`

### 流程5：健康检查 (Lint)

定期（或用户要求时）执行：

1. 扫描 orphan 页面（无入链的孤立页面）
2. 检查过时信息（模型版本、工具定价、API 变动）
3. 识别缺失的概念页（被提及但未创建的页面）
4. 检查重复或矛盾信息
5. 更新模型状态（标记已淘汰模型）
6. 建议新的内容方向

---

## 链接规范

- **双向链接**: 使用 Obsidian 格式 `[[页面名称]]`
- **带别名链接**: `[[页面名称|显示文本]]`
- **外部链接**: 使用标准markdown `[文本](URL)`
- **源文件引用**: `[[wiki/sources/文档名|显示名]]`
- **概念引用**: 在正文中引用概念时，链接到对应概念页

---

## 日志格式

**log.md** 使用统一格式：

```markdown
## [2026-04-27] ingest | 《GPT-4 Technical Report》
- 摘要页: [[wiki/sources/GPT-4_Technical_Report]]
- 更新模型: [[wiki/models/GPT-4]]
- 关键发现: 上下文长度扩展到 128K

## [2026-04-27] query | Transformer 原理
- 查询范围: Transformer、注意力机制相关页面
- 生成内容: 科普解释 + 图示建议

## [2026-04-27] ppt | AI入门科普
- 受众: 初学者
- 页数: 25页
- 输出: [[ppt/outlines/AI-01-什么是AI]]

## [2026-04-27] update | 行业动态
- 时间范围: 2026-04-20 至 2026-04-27
- 新增模型: XXX
- 更新页面: [[wiki/models/XXX]]

## [2026-04-27] lint | 健康检查
- 发现2个orphan页面
- 标记1个已过时模型
```

---

## 时间戳规范

所有 Wiki 页面的 Frontmatter 中，`last_updated` 字段必须**精确到小时和分钟**：

```yaml
last_updated: "2026-04-27 14:30"
```

- 格式：`YYYY-MM-DD HH:MM`
- 采用 24 小时制
- 每次更新页面内容时，必须同步更新该字段

---

## 命名约定速查

| 类型 | 示例 |
|------|------|
| 源文件摘要 | `wiki/sources/Attention_Is_All_You_Need.md` |
| 概念页 | `wiki/concepts/Transformer.md` |
| 模型页 | `wiki/models/GPT-4.md` |
| 工具页 | `wiki/tools/ChatGPT.md` |
| 行业页 | `wiki/industry/教育.md` |
| 综合页 | `wiki/synthesis/AI发展时间线.md` |
| PPT专题 | `wiki/synthesis/PPT-什么是AI.md` |
| PPT大纲 | `ppt/outlines/AI-01-什么是AI.md` |

---

## 提示词模板

### 导入资料时
```
请按照CLAUDE.md中的"流程1：导入新资料"处理 raw/papers/XXX.pdf：
1. 创建wiki/sources/XXX.md摘要
2. 更新或创建相关概念页、模型页、工具页
3. 更新index.md
4. 在log.md记录操作
```

### 回答问题时
```
请基于wiki回答："Transformer的工作原理是什么？"
1. 先读取index.md了解结构
2. 查阅相关概念页和模型页
3. 给出带引用的综合分析，适合小白理解
```

### 制作PPT时
```
请帮我制作一份AI入门科普PPT：
1. 明确受众为初学者，预计20页
2. 检索相关概念页和综合页
3. 设计PPT大纲，每页包含标题、要点、配图建议
4. 保存到ppt/outlines/AI-01-什么是AI.md
5. 在log.md记录操作
```

### 更新动态时
```
请帮我整理本周AI行业动态：
1. 扫描raw/news/和raw/articles/中的新文件
2. 按类别汇总（模型、工具、政策）
3. 更新相关模型页和工具页
4. 生成动态简报
5. 在log.md记录操作
```
