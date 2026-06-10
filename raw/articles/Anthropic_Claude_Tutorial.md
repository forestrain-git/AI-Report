# Anthropic Claude 官方教程资源汇总

> 原始来源：Anthropic 官方文档与 GitHub 仓库
> 拉取日期：2026-06-09
> 用途：中建发展集团总部员工 AI 培训知识库

---

## 一、核心教程：Prompt Engineering Interactive Tutorial（提示工程交互式教程）

**仓库地址**：https://github.com/anthropics/prompt-eng-interactive-tutorial
**星标数**：36.2k | **分支数**：3.9k
**格式**：Jupyter Notebook（98.1%）+ Python（1.9%）
**配套资源**：
- Google Sheets 版本（含 Claude for Sheets 扩展）
- AWS Bedrock 实现版本
- 答案密钥（Google Sheets）

**设计目标**：
- 掌握优秀提示词的基本结构
- 识别常见失败模式并学习"80/20"技巧解决
- 理解 Claude 的优势与局限
- 从零开始构建常见用例的强提示词

### 章节结构（9章 + 附录）

#### 初级（Beginner）

| 章节 | 标题 | 内容描述 |
|------|------|----------|
| 第1章 | Basic Prompt Structure（基础提示词结构） | 提示词构建基础 |
| 第2章 | Being Clear and Direct（清晰直接） | 沟通清晰度技巧 |
| 第3章 | Assigning Roles（分配角色） | 基于角色的提示策略 |

#### 中级（Intermediate）

| 章节 | 标题 | 内容描述 |
|------|------|----------|
| 第4章 | Separating Data from Instructions（数据与指令分离） | 隔离上下文与命令 |
| 第5章 | Formatting Output & Speaking for Claude（格式化输出与预填充） | 输出结构化和预填充技术 |
| 第6章 | Precognition (Thinking Step by Step)（预认知：逐步思考） | 思维链推理 |
| 第7章 | Using Examples（使用示例） | 少样本和多样本提示 |

#### 高级（Advanced）

| 章节 | 标题 | 内容描述 |
|------|------|----------|
| 第8章 | Avoiding Hallucinations（避免幻觉） | 减少虚假信息的技巧 |
| 第9章 | Building Complex Prompts (Industry Use Cases)（构建复杂提示词：行业用例） | 从零构建复杂提示词——聊天机器人、法律服务、金融服务、编程 |

#### 附录：超越标准提示（Beyond Standard Prompting）

- **Chaining Prompts**（链接提示词）
- **Tool Use**（工具使用）
- **Search & Retrieval**（搜索与检索）

### 教学特色

- **交互式实验**：每课包含"Example Playground"实验区域
- **成本优化**：使用 Claude 3 Haiku（最小、最快、最便宜的模型）
- **答案密钥**：提供 Google Sheets 格式的参考答案
- **替代格式**：支持 Google Sheets + Claude for Sheets 扩展（更用户友好）
- **行业覆盖**：聊天机器人、法律、金融服务、编程等用例

---

## 二、Anthropic Courses 综合课程仓库

**仓库地址**：https://github.com/anthropics/courses
**星标数**：21.8k | **分支数**：2.3k
**格式**：Jupyter Notebook（99.9%）+ Python（0.1%）

### 五大课程模块

| 序号 | 课程名称 | 描述 | 文件路径 |
|------|----------|------|----------|
| 1 | **Anthropic API Fundamentals**（API基础） | 使用 Claude SDK 的 essentials：获取 API 密钥、模型参数、多模态提示、流式响应等 | `/anthropic_api_fundamentals/` |
| 2 | **Prompt Engineering Interactive Tutorial**（提示工程交互教程） | 关键提示技术的综合分步指南 | `/prompt_engineering_interactive_tutorial/` |
| 3 | **Real World Prompting**（真实世界提示） | 学习如何将提示技术融入复杂、真实的提示词中 | `/real_world_prompting/` |
| 4 | **Prompt Evaluations**（提示评估） | 学习如何编写生产级提示评估，衡量提示词质量 | `/prompt_evaluations/` |
| 5 | **Tool Use**（工具使用） | 在 Claude 工作流中成功实现工具使用所需的一切 | `/tool_use/` |

### 配套资源

- **AWS Workshop**（提示工程教程）：https://catalog.us-east-1.prod.workshops.aws/workshops/0644c9e9-5b82-45f2-8835-3b5aa30b1848/en-US
- **Google Vertex 版本**（真实世界提示）：https://github.com/anthropics/courses/tree/vertex/real_world_prompting

---

## 三、Claude Cookbook（实践指南与示例）

**地址**：https://platform.claude.com/cookbook/

**简介**：使用 Claude 的实用指南和示例代码集合

### 精选 Cookbook

| 标题 | 描述 |
|------|------|
| Programmatic tool calling (PTC) | 通过让 Claude 编写程序化调用工具的代码来减少延迟和 token 消耗 |
| Tool search with embeddings | 使用语义嵌入动态发现工具，将 Claude 应用扩展到数千个工具 |
| Automatic context compaction | 在长时运行的代理工作流中通过自动压缩对话历史来管理上下文限制 |
| Giving Claude a crop tool for better image analysis | 为 Claude 提供裁剪工具以放大图像区域进行详细分析 |
| Prompting for frontend aesthetics | 引导 Claude 生成独特、精致的前端设计，避免通用美学 |
| Introduction to Claude Skills | 使用 Claude 的 Excel、PowerPoint、PDF 技能创建文档、分析数据、自动化工作流 |

### 全部 Cookbook 分类统计（67个食谱，14个类别）

| 类别 | 数量 | 描述 |
|------|------|------|
| **Tools**（工具） | ~14 | 工具使用、PTC、工具选择、评估、搜索 |
| **Agent Patterns**（代理模式） | ~13 | 多代理系统、工作流、记忆、上下文管理 |
| **RAG & Retrieval**（检索增强） | ~12 | 知识图谱、嵌入、向量搜索、SQL生成 |
| **Integrations**（集成） | ~11 | 第三方服务（LlamaIndex、Pinecone、MongoDB、ElevenLabs等） |
| **Responses**（响应） | ~10 | 提示技术、JSON模式、缓存、摘要 |
| **Claude Agent SDK** | ~8 | 使用官方 SDK 构建代理 |
| **Multimodal**（多模态） | ~7 | 视觉、图像分析、文档转录 |
| **Claude Managed Agents** | ~6 | 生产级代理部署和管理 |
| **Evals**（评估） | ~5 | 评估框架、测试、提示版本控制 |
| **Skills**（技能） | ~4 | Excel、PowerPoint、PDF 自动化 |
| **Cybersecurity**（网络安全） | ~2 | 漏洞检测、威胁情报 |
| **Observability**（可观测性） | ~2 | 监控、事件响应、使用分析 |
| **Thinking**（思考） | ~2 | 扩展推理能力 |
| **Fine-Tuning**（微调） | ~1 | Bedrock 上的模型定制 |

**时间跨度**：2023年8月 至 2026年5月
**最新重点**：Claude Managed Agents（生产部署、多代理协调、结果验证）、Claude Agent SDK（托管、漏洞检测、会话管理）

---

## 四、Anthropic Academy（官方学习平台）

**平台**：Skilljar 托管的 Anthropic 学习平台

### 13门免费课程

| 课程方向 | 目标受众 | 内容 |
|----------|----------|------|
| **Claude 101** → AI Fluency: Framework & Foundations | 完全零基础者 | AI 基础框架 |
| **Building with the Claude API** | 开发者 | 将 Claude 构建到产品中 |
| **Claude Code in Action** → Agent Skills | 现有 Claude Code 用户 | Claude Code 实战 |
| **Introduction to MCP** → Advanced MCP | 工具集成开发者 | 模型上下文协议 |
| **AI Fluency for Educators** | 教师 | 课堂中使用 AI |

---

## 五、社区补充资源

### Panaversity 的 Claude Code 练习

**仓库**：https://github.com/panaversity/claude-code-exercises

| 模块 | 内容 | 练习数 | 重点 |
|------|------|--------|------|
| **basics/** M1-M4 | 4个模块 | 12个练习 | 自然语言一次性问题解决 |
| **basics/** M5-M8 | 4个模块 | 9个练习 + 3个综合项目 | 使用 CLAUDE.md 系统解决问题 |
| **skills/** M1-M8 | 8个模块 | 21个练习 + 3个综合项目 | 可复用技能和模式 |

**推荐最低路径（9个练习）**：
1. 模块1 — 文件组织（3个练习）
2. 模块2 — 研究与综合（3个练习）
3. 模块3 — 数据处理（3个练习）

### Panaversity 的 Claude Code Skills Exercises

**仓库**：https://github.com/panaversity/claude-code-skills-exercises

| 周次 | 模块 | 重点 |
|------|------|------|
| 1 | Understanding Skills | 阅读和分析现有技能 |
| 2 | First Skills | 构建简单、单用途技能 |
| 3 | Skills with Examples | 从示例输出中学习 |
| 4 | Skills with References | 添加参考材料 |
| 5 | Testing & Iteration | 寻找边界情况，衡量改进 |
| 6 | Composing Skills | 将技能链接成工作流 |
| 7 | Real-World Skills | 生产级技能 |
| 8 | Capstone | 选择：业务运营、教育套件或个人 AI |

---

## 六、资源对比与推荐

| 学习目标 | 最佳资源 | 时间投入 |
|----------|----------|----------|
| 从零学习提示工程 | **官方9章交互式教程** | 2-4小时 |
| 使用 Claude API 构建产品 | **Anthropic Academy API课程** + GitHub notebooks | 4-8小时 |
| 精通 Claude Code | **Panaversity 练习**（基础 → 技能） | 1-2周 |
| 快速动手实践 | **basics/ 模块1-3**（9个练习） | 2-3小时 |
| 生产级实现 | **Anthropic Cookbook** | 按需参考 |

---

## 七、关键特点总结

1. **全部免费** — 所有官方 Anthropic 课程均免费，无时间限制，自定进度
2. **交互式格式** — Jupyter notebooks 支持实时实验
3. **成本意识设计** — 教程使用 Claude 3 Haiku 最小化 API 成本
4. **多格式可用** — GitHub、Google Sheets、Skilljar 视频课程
5. **生态快速增长** — 社区资源如 Panaversity 迅速扩展
6. **生产导向** — Cookbook 和 Managed Agents 聚焦实际部署
7. **多层级覆盖** — 从初学者到专业开发者全覆盖

---

## 八、获取限制说明

**2026-06-09 拉取情况**：

- [x] 主文档页面（docs.anthropic.com）—— 301 重定向至 platform.claude.com，返回 404
- [x] 教程页面（docs.anthropic.com/en/docs/tutorial）—— 301 重定向，返回 404
- [x] GitHub 仓库（prompt-eng-interactive-tutorial）—— 成功获取 README 和章节结构
- [x] GitHub 仓库（courses）—— 成功获取课程结构和描述
- [x] Claude Cookbook（platform.claude.com/cookbook）—— 成功获取全部 67 个食谱
- [x] WebSearch 补充搜索 —— 成功获取 Anthropic Academy 和社区资源信息

**注**：官方文档站点（docs.anthropic.com）已迁移至 platform.claude.com，且可能需要身份验证。本文件内容基于成功访问的 GitHub 仓库、Cookbook 页面和 WebSearch 结果综合整理。
