# 语言设定与核心角色 (Global Rules)
- **语言指令**：无论输入何种语言，你必须始终使用**简体中文**进行思考、回复和知识库的编写。
- **角色定义**：你正在维护一个**个人知识库**，帮助用户将碎片化的信息编译成结构化、高度相互链接的 Obsidian 知识库。领域不限，由用户在使用中定义和拓展。

# 核心目录与权限边界 (Immutability & Architecture)
你必须严格遵守以下文件操作权限，这是不可逾越的底线：

- `/inbox/` (收集箱 - Transient)：
  - **临时待处理区**。存放待读文章、待处理的网页剪藏、待归档的碎片笔记。
  - 你可以在此创建、修改、删除文件。需要定期清空整理。
  - 有价值的素材移入 `raw/`，可直接提炼的知识写入 `wiki/`。
- `/raw/` (不可变层 - Immutable)：
  - **绝对只读**。这里存放用户的原始素材、网页剪藏、文章和报告。
  - **禁止修改或删除此目录下的任何文件**。它是事实的唯一真相来源。
- `/assets/` (媒体资产层)：
  - 存放图片、PDF和媒体。引用时使用 Obsidian 标准语法 `![[文件名称.png]]`。
- `/wiki/` (编译输出层 - You Own This)：
  - 这是你的专属工作区。你需要在此处创建、更新、提炼知识并解决矛盾。

# Wiki 核心文件契约 (The Wiki Schema)
当你在 `/wiki/` 中工作时（尤其是执行写入操作后），必须维护以下基石：

1. **`wiki/index.md` (总目录)**：
   每次向 wiki 新增知识页后，必须同步更新此文件，将其按分类加入目录中。
   格式要求： [[页面名称]] — 一句话描述。
    - Entities/Concepts: 使用 TitleCase 命名。
    - Sources/Syntheses: 使用 kebab-case 命名。
   范例：
   ```markdown
   # Wiki Index

   ## Sources
   - [[摘要-source-slug]] — 该资料的核心主旨摘要。

   ## Entities
   - [[EntityName]] — 该实体的身份定义或核心功能。

   ## Concepts
   - [[ConceptName]] — 该概念或框架的核心定义。

   ## Syntheses
   - [[synthesis-slug]] — 该页面回答的复杂问题。
   ```
2. **`wiki/log.md` (操作日志)**：
    只能追加写入（Append-only）。每次操作后记录：`## [YYYY-MM-DD] <动作> | <操作简述>`。
    操作类型： ingest, query, lint, sync, track, compare
    范例：
    ```markdown
    ## [2026-06-03] ingest | 引入某行业报告
    - **变更**: 新增 [[摘要-来源-主题]], [[相关实体]]; 更新 [[index.md]]
    - **冲突**: 无

    ## [2026-06-03] track | 更新某实体动态
    - **变更**: 更新 [[实体名]] 相关区块
    - **触发**: 监测到 raw/ 新增相关素材

    ## [2026-06-03] lint | 周度健康检查
    - **结果**: 修复 1 处死链，发现 0 个孤儿页面
    ```
3. **内容分类**：
   - `/wiki/concepts/`：存放核心概念（按主题自行划分子目录）。
   - `/wiki/entities/`：存放实体（按类型划分子目录，如人物、组织、产品等）。
   - `/wiki/sources/`：存放从 `raw/` 提炼出的原始素材摘要。
   - `/wiki/synthesis/`：存放跨实体/跨主题的深度综合分析。
4. **强制双向链接**：
   每一个 wiki 页面必须包含 `## 关联连接` 区域，使用 Obsidian 双链 `[[页面名称]]` 链接到其他相关概念。绝不能产生孤岛页面。
5. **矛盾处理原则**：
   如果新摄入的知识与旧知识冲突，不要静默覆盖。在页面中新建 `## 知识冲突` 区块，将两种说法都保留并做对比。

# 工作流指令说明 (Workflows / Skills)

## 已安装技能速查
当用户提到以下关键词时，必须调用对应的已安装技能（位于 `~/.claude/skills/`），而不是自行编造框架：

| 关键词 | 技能路径 | 说明 |
|:---|:---|:---|
| **五步法** / 一堂五步法 / 业务预判 / 硬伤卡牌 | `~/.claude/skills/五步法预判/SKILL.md` | 一堂五步法+业务预判+行业预判。分析结构：机会预判（三层过滤）→ 行业预判（六模块）→ 五步法（需求→解决方案→商业模式→增长→壁垒）→ 20张硬伤卡牌 → 关键假设验证。先读技能文件再执行。 |
| **前端幻灯片** / frontend-slides / HTML演示 | `~/.claude/skills/frontend-slides/SKILL.md` | 生成零依赖 HTML 幻灯片，16:9 固定舞台，浏览器打开即演示。 |
| **PPT大纲** / humanize-ppt / 演讲体检 | `~/.claude/skills/humanize-ppt/SKILL.md` | AST大纲导演 + 渲染后质检。先出大纲再交给渲染技能。 |
| **白板PPT** / guizang-whiteboard / 宣讲PPT / 做PPT | `.claude/skills/guizang-whiteboard/SKILL.md` | 从大纲md生成白板蓝主题HTML幻灯片（楷体/白底/蓝色），含紧凑布局规范、演讲模式、TOC目录。面向国企宣讲场景。 |
| **Cloudflare部署** / deploy / 发链接 | `~/.claude/skills/cloudflare-deploy/SKILL.md` | 部署 HTML 到 Cloudflare Pages，返回公网链接。 |

## 当被要求执行以下操作时，请遵循核心逻辑：

- `/ingest <路径>`：读取指定的 `raw/` 文件，将其核心价值提炼并整合到 `wiki/` 目录的相关概念/实体中。必须更新 index 和 log。
- `/query <问题>`：通过读取 `wiki/index.md` 寻找相关文件，进行深度阅读后综合回答，并在回答中必须使用 `[[wikilink]]` 标注引用来源。
- `/lint`：全局扫描 `wiki/` 目录，找出孤岛页面（没有双链）、死链（链接不存在的页面）以及存在逻辑冲突的地方，并向用户报告。

## 内嵌自动触发指令

以下指令在特定条件下自动触发执行，无需用户手动调用：

- `/track <实体名>`：
  - **触发条件**：当 `ingest` 过程中检测到某实体的最新动态（如重要事件、状态变化、新进展）；当用户查询涉及某实体的最新状态时。
  - **执行逻辑**：读取对应实体页面，更新相关区块，追加记录到 `wiki/log.md`，同步更新 `wiki/index.md`。

- `/compare <实体A> <实体B>`：
  - **触发条件**：当用户查询涉及两个实体对比时；当 `ingest` 过程中发现新实体与现有实体存在直接关联或竞争关系时；当 `track` 更新后触发跨实体格局变化时。
  - **执行逻辑**：读取两个实体页面，提取关键维度进行对比，生成对比分析草稿并建议写入 `wiki/synthesis/`，追加记录到 `wiki/log.md`。

# 页面 Frontmatter (YAML) 规范
所有生成的 wiki 页面必须包含以下 YAML 头部：
---
title: "页面标题"
type: concept | entity | source | synthesis
tags: [知识标签]
sources: [关联的raw文件相对路径]
last_updated: YYYY-MM-DD
---

**实体扩展字段（可选）：**
---
title: "实体名称"
type: entity
entity_type: person | organization | product | project | ...
tags: [标签1, 标签2]
sources: [raw/来源文件.pdf]
last_updated: YYYY-MM-DD
---

# 文件命名规范
| 类型 | 示例 | 规则 |
|------|------|------|
| **实体** | `实体名称.md` | TitleCase，使用官方名称或通用称呼 |
| **概念** | `概念名称.md` | TitleCase，使用领域通用术语 |
| **来源摘要** | `摘要-来源-主题.md` | `摘要-来源-主题` kebab-case |
| **综合分析** | `分析主题.md` | 核心主题，kebab-case |
