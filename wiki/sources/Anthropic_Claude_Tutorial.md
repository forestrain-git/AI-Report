---
type: source
source_file: "raw/articles/Anthropic_Claude_Tutorial.md"
ingest_date: "2026-06-09"
summary: "Anthropic 官方提供的 Claude 提示工程交互式教程（9章Jupyter Notebook），配套5大课程模块、67个Cookbook实战案例及13门免费Academy课程，覆盖从初学者到生产级开发者的完整学习路径。"
tags: ["教程", "Claude", "Anthropic", "提示工程", "Jupyter Notebook", "交互式学习", "API", "工具使用", "Agent"]
---

# Anthropic Claude Tutorial — 源文件摘要

## 文档基本信息

| 属性 | 内容 |
|------|------|
| **来源** | Anthropic 官方 GitHub 仓库 + platform.claude.com |
| **形式** | Jupyter Notebook 交互式教程 + 在线文档 + Cookbook 代码示例 |
| **章节数** | 核心教程 9 章 + 附录 3 节；综合课程 5 大模块；Cookbook 67 个案例 |
| **核心主题** | 提示工程（Prompt Engineering）、Claude API 使用、工具调用（Tool Use）、Agent 构建、生产级部署 |
| **目标受众** | 初学者 → 进阶开发者 → 生产级工程师 |
| **费用** | 全部免费，自定进度 |
| **成本优化** | 教程默认使用 Claude 3 Haiku（最低成本模型） |

---

## 核心要点

1. **9章交互式提示工程教程**：从基础提示结构到行业复杂用例（聊天机器人、法律、金融、编程），采用 Jupyter Notebook 格式，每章含"Example Playground"实验区和答案密钥，支持 Google Sheets 替代格式。

2. **5大课程模块体系化学习**：API 基础 → 提示工程 → 真实世界提示 → 提示评估 → 工具使用，形成从入门到生产的完整路径，配套 AWS Workshop 和 Google Vertex 版本。

3. **67个 Cookbook 实战案例**：覆盖 14 个类别（工具、Agent 模式、RAG、集成、多模态等），时间跨度 2023-2026，最新重点为 Claude Managed Agents 和 Agent SDK。

4. **13门免费 Academy 课程**：通过 Skilljar 平台提供，覆盖 Claude 101、API 开发、Claude Code 实战、MCP 协议、AI 教育应用等方向。

5. **多格式与生态支持**：除 GitHub 外，提供 Google Sheets + Claude for Sheets 扩展、AWS Bedrock 实现、社区补充练习（Panaversity）等替代学习路径。

---

## 章节概览

### 核心教程：Prompt Engineering Interactive Tutorial（9章 + 附录）

| 级别 | 章节 | 标题 | 核心内容 |
|------|------|------|----------|
| 初级 | 1 | Basic Prompt Structure | 提示词构建基础 |
| 初级 | 2 | Being Clear and Direct | 沟通清晰度技巧 |
| 初级 | 3 | Assigning Roles | 基于角色的提示策略 |
| 中级 | 4 | Separating Data from Instructions | 数据与指令分离 |
| 中级 | 5 | Formatting Output & Speaking for Claude | 输出结构化和预填充 |
| 中级 | 6 | Precognition (Thinking Step by Step) | 思维链推理 |
| 中级 | 7 | Using Examples | 少样本和多样本提示 |
| 高级 | 8 | Avoiding Hallucinations | 减少虚假信息的技巧 |
| 高级 | 9 | Building Complex Prompts | 行业复杂用例（聊天机器人、法律、金融、编程） |
| 附录 | — | Chaining / Tool Use / Search & Retrieval | 高级技术 |

### 综合课程：Anthropic Courses（5大模块）

| 序号 | 课程 | 核心内容 |
|------|------|----------|
| 1 | Anthropic API Fundamentals | API 密钥、模型参数、多模态提示、流式响应 |
| 2 | Prompt Engineering Interactive Tutorial | 关键提示技术分步指南 |
| 3 | Real World Prompting | 复杂真实场景的提示设计 |
| 4 | Prompt Evaluations | 生产级提示质量评估 |
| 5 | Tool Use | 工具调用完整实现 |

### Cookbook 重点类别（67个案例）

| 类别 | 数量 | 代表案例 |
|------|------|----------|
| Tools | ~14 | 程序化工具调用、工具搜索、上下文压缩 |
| Agent Patterns | ~13 | 多代理协调、工作流、记忆管理 |
| RAG & Retrieval | ~12 | 知识图谱、上下文检索、Text-to-SQL |
| Integrations | ~11 | LlamaIndex、Pinecone、MongoDB、ElevenLabs |
| Multimodal | ~7 | 视觉分析、文档转录、图像裁剪工具 |
| Claude Managed Agents | ~6 | 生产部署、多代理协调、结果验证 |

---

## 与知识库关联

### 关联工具页面

- [[wiki/tools/Claude-Code]] —— 教程中的"Claude Code in Action"课程和 Panaversity 的 Claude Code 练习直接关联，提供从基础到高级的 Claude Code 使用技能训练。

### 关联模型页面

- [[wiki/models/Claude]] —— 所有教程均基于 Claude 模型家族（Claude 3 Haiku/Sonnet/Opus、Claude 3.5/3.7 Sonnet 等），涵盖模型选择、参数调优、能力边界（上下文长度、多模态、工具使用、扩展思考等）。

### 可延伸创建的概念页面

- [[wiki/concepts/提示工程]] —— 9章教程的核心主题
- [[wiki/concepts/思维链推理]] —— 第6章 Precognition 内容
- [[wiki/concepts/少样本学习]] —— 第7章 Using Examples 内容
- [[wiki/concepts/工具使用]] —— 附录和 Tool Use 课程
- [[wiki/concepts/RAG]] —— Cookbook 中 RAG & Retrieval 类别
- [[wiki/concepts/Agent]] —— Cookbook 中 Agent Patterns 和 Managed Agents
- [[wiki/concepts/多模态]] —— Cookbook 中 Multimodal 类别

---

## 适用性评估（针对中建发展集团受众）

| 维度 | 评估 |
|------|------|
| **零基础友好度** | 高 —— 初级3章专为初学者设计，使用类比和清晰解释 |
| **非技术管理者适用性** | 中高 —— 概念和策略层面可直接应用；API/代码部分需要技术同事协助 |
| **实战价值** | 高 —— 行业用例（法律、金融、编程）可直接映射到企业场景 |
| **培训建议** | 建议管理层学习第1-3章（基础概念）+ 第9章行业案例；技术团队学习全系列 |
| **成本** | 低 —— 全部免费，且使用最低成本模型 |

---

## 获取限制说明

- 官方文档站点（docs.anthropic.com）已迁移至 platform.claude.com，部分页面需要身份验证
- 本摘要基于成功访问的 GitHub 公开仓库、Cookbook 公开页面和 WebSearch 结果综合整理
- 原始完整内容建议直接从 GitHub 仓库（anthropics/prompt-eng-interactive-tutorial、anthropics/courses）克隆获取
