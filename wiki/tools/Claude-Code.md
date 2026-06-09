---
type: tool
tool_type: "dev"
organization: "Anthropic"
pricing: "paid"
related_models: ["models/Claude.md"]
last_updated: "2026-04-27 16:00"
tags: ["Claude Code", "AI编程", "终端", "MCP", "Agent"]
---

# Claude Code

## 工具简介

Claude Code 是 Anthropic 推出的**终端原生 AI 编程助手**。它不是普通的聊天机器人，而是一个能**真正操作你电脑文件和代码**的 AI Agent（智能代理）。

### 一句话定位

把 Claude Code 想象成一位**24小时待命的超级程序员实习生**，它能读懂你的整个项目、修改代码、运行命令、管理 Git——你只需要用自然语言告诉它要做什么。

## 核心能力

```
┌─────────────────────────────────────────────────────────────┐
│                     Claude Code 能做什么                      │
├─────────────────────────────────────────────────────────────┤
│  📁 文件操作    │ 读取、创建、修改、删除文件和文件夹            │
│  🔍 代码分析    │ 理解整个代码库，回答架构问题                  │
│  ✏️ 代码编辑    │ 跨文件修改、重构、批量替换                    │
│  🐛 调试修复    │ 分析报错、定位bug、自动修复                   │
│  🧪 测试运行    │ 执行测试、分析失败原因                        │
│  📊 Git 管理   │ 提交、分支、合并冲突解决                      │
│  🌐 MCP 扩展   │ 连接数据库、浏览器、API 等外部服务             │
│  🤖 子代理     │ 复杂任务拆给多个并行 AI 处理                  │
└─────────────────────────────────────────────────────────────┘
```

## 安装与配置

### 系统要求
- Node.js 18+
- macOS / Linux / Windows（需 Git for Windows）

### 安装

```bash
# 方式一：npm（通用）
npm install -g @anthropic-ai/claude-code

# 方式二：Homebrew（macOS）
brew install claude-code

# 方式三：WinGet（Windows）
winget install Anthropic.ClaudeCode
```

### 登录

```bash
claude auth login      # 浏览器 OAuth 登录
claude auth status     # 查看登录状态
```

### 启动

```bash
cd /your/project       # 进入你的项目目录
claude                 # 启动交互式会话
```

## 交互模式

### 1. REPL 交互模式（最常用）

```bash
$ claude
> 请分析一下这个项目的结构
> 帮我在 src/utils/ 下创建一个日期格式化工具
> 运行测试并修复失败的用例
```

### 2. 一次性模式（适合脚本）

```bash
claude -p "列出所有 TODO 注释"
claude -p "检查代码质量" --output-format json
```

### 3. 计划模式（Plan Mode）

复杂任务先制定计划，不立即执行：
```
> /plan
Claude: "我将按以下步骤进行：
  1. 先读取现有配置文件
  2. 分析需要修改的地方
  3. 创建备份
  4. 执行修改
  5. 验证结果
请确认后我再开始执行。"
```

## 核心命令（斜杠命令）

| 命令 | 作用 |
|------|------|
| `/help` | 显示所有命令 |
| `/plan` | 切换到计划模式 |
| `/compact` | 压缩对话历史，释放上下文空间 |
| `/clear` | 清空对话 |
| `/rewind` | 撤销到上一步（代码"时光机"） |
| `/cost` | 查看本次会话花费 |
| `/status` | 查看会话状态 |
| `/model` | 切换模型（Opus/Sonnet/Haiku） |

## 实用技巧

### 1. 用 `@` 引用文件

```
> @src/config.js 这个文件的作用是什么？
> 请修改 @README.md，添加安装说明
```

### 2. 用 `!` 执行 Shell 命令

```
> !git status          # 查看 git 状态（节省 token）
> !npm test            # 运行测试
> !ls -la              # 列出文件
```

### 3. 图片调试（macOS）

截图后按 `Ctrl+V` 粘贴图片，Claude 可以看懂报错截图：
```
> [粘贴报错截图]
> 这个报错怎么解决？
```

### 4. 继续上次会话

```bash
claude --continue      # 继续上次对话
```

## Claude Code + Obsidian 知识库构建

对于**非技术人员**，Claude Code 最有价值的用法是**管理和维护 Obsidian 知识库**：

### 场景 1：批量整理笔记

```
> 请扫描 00-Inbox/ 目录，把所有未分类的笔记按主题移动到 02-Notes/ 下
> 为所有没有 Frontmatter 的笔记添加基本的 YAML 头信息
```

### 场景 2：生成知识地图

```
> 请分析 02-Notes/concepts/ 下的所有笔记，生成一份知识地图
> 找出哪些笔记之间应该建立双向链接
```

### 场景 3：基于知识库回答问题

```
> 请读取我的整个知识库，回答：过去一年我关于项目管理记了哪些要点？
> 基于 wiki/industry/ 下的笔记，写一份建筑行业 AI 应用现状总结
```

### 场景 4：自动化维护

```
> 请检查所有笔记中的失效链接，列出需要修复的清单
> 为知识库运行一次"健康检查"，找出孤立的页面
```

## 权限与安全

Claude Code 执行任何操作前都会**请求你的确认**：
- 读取文件：自动允许
- 修改文件：需确认
- 执行命令：需确认
- 访问网络：需确认

```
⚠️  Claude Code wants to edit src/main.js:
    - 删除第15行
    + 添加新函数 calculateTotal()
    
    Allow? (Y/n/a/r/d): 
    Y = 允许这一次
    n = 拒绝
    a = 始终允许这个文件
    r = 只看不动
```

## 定价

- 需要 Anthropic 订阅（Claude Pro $20/月、Max、Team）或 API Key
- 使用 `/cost` 命令可实时查看花费
- Sonnet 性价比最高，日常任务推荐；复杂任务用 Opus

## 局限性与注意事项

- **非技术人员门槛**：虽然是自然语言交互，但需要在终端操作，有一定学习曲线
- **订阅成本**：需要付费订阅
- **网络要求**：需要访问 Anthropic 服务
- **不适合**：纯图形界面操作（如 Photoshop、Excel 复杂操作）

## PPT 表达建议

- **适合用图**：Claude Code 工作流程图（"你说需求 → AI 分析 → AI 执行 → 你确认"）
- **适合演示**：现场打开终端，用 Claude Code 分析一个实际项目
- **适合强调**：Claude Code 是"AI Agent"的代表——不只是聊天，而是真正帮你干活
