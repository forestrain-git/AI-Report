---
name: guizang-whiteboard
description: "从大纲md生成白板蓝主题HTML幻灯片。适用场景：国企宣讲、中高层分享、需要楷体白底风格的演讲PPT。含紧凑布局规范、组件系统、演讲模式、TOC目录。当用户提到'做PPT'、'生成幻灯片'、'宣讲PPT'、'白板风格'、'guizang白板'时使用。"
version: "1.0.0"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, Agent
---

# Guizang Whiteboard PPT 技能

> 从大纲 markdown 生成单文件 HTML 幻灯片，白底楷体蓝色主题，面向国企中高层宣讲场景。

## 适用场景

- 国企/央企中高层 AI 宣讲、战略分享、业务汇报
- 需要楷体（KaiTi）白底蓝色主题的正式演讲
- 内容密度高、需要数据表格和卡片布局的演示
- 需要演讲模式（Presenter Mode）和 TOC 目录导航

## 与 guizang-ppt-skill 的区别

| 维度 | guizang-ppt-skill（归藏原版） | 本技能（白板蓝） |
|:---|:---|:---|
| 视觉风格 | 杂志风/瑞士风，WebGL 背景 | 白底楷体，纯色背景 |
| 字体 | Noto Serif SC / Inter | KaiTi 楷体 |
| 适用场景 | 创意分享、产品发布 | 国企宣讲、正式汇报 |
| 内容密度 | 中低密度，注重视觉冲击 | 高密度，注重信息完整 |

## 工作流

### Step 1：读取大纲

从 `ppt/outlines/` 目录读取结构大纲文件（如 `PPT结构讨论-v2.1.md`）。大纲定义了：
- 分部分结构（Part 1-N）
- 每页标题、内容类型、数据点
- 叙事曲线（承上启下关系）
- 知识库引用

### Step 2：生成 HTML

基于 [skeleton.html](assets/skeleton.html) 模板，按大纲结构逐页生成 `<section class="slide">` 元素。

**slide 类型**：
- `data-type="cover"` — 封面页（居中大标题）
- `data-type="content"` — 内容页（header + body + footnote）
- `data-type="pivot"` — 定调/金句页（大留白居中）
- `data-type="toc"` — 全局目录页（当前部分高亮）
- `data-type="part"` — 分部过渡页

**详细组件参考**：[references/design-system.md](references/design-system.md)

### Step 3：应用紧凑布局规范

内容页（content）必须使用紧凑布局，确保内容铺满页面不出现滚动条：

```html
<section class="slide" data-type="content" style="padding-top:16px;padding-bottom:56px;">
  <div class="slide-header" style="margin-bottom:4px;">
    <span class="kicker" style="margin-bottom:6px;">第一部分 · 主题</span>
    <h2 class="slide-title" style="margin-bottom:14px;font-size:clamp(24px,2vw,30px);">
      叙述型标题——用一句话覆盖页面全部内容，同时承上启下
    </h2>
  </div>
  <div class="slide-body">
    <!-- 内容区域 -->
  </div>
  <div class="footnote">来源：xxx</div>
  <div class="speaker-notes">演讲备注</div>
</section>
```

**关键数值**：
| 元素 | 默认值 | 紧凑值 |
|:---|:---|:---|
| slide padding-top | 60px | 16px |
| slide padding-bottom | 112px | 56px |
| slide-header margin-bottom | 8px | 4px |
| kicker margin-bottom | 12px | 6px |
| slide-title margin-bottom | 28px | 14px |
| slide-title font-size | clamp(28px,2.4vw,36px) | clamp(24px,2vw,30px) |

**注意**：padding-bottom 56px 必须 ≥ 导航栏高度（48px）+ 安全间距。

### Step 4：标题规范——叙述型标题

每页标题不是"概述型"，而是"叙述型"——用一句话覆盖页面全部内容，串起来可直接朗读全篇：

```
✅ 国务院定了硬指标——2027年智能终端普及率超70%，建筑业被直接点名"全要素智能化"
❌ 国发〔2025〕11号：量化目标
```

标题之间要有承上启下的逻辑关系，使听众只读标题就能理解完整叙事线。

### Step 5：添加 TOC 目录页

每个 Part 开头插入一张全局目录页，展示全部 5 个部分，当前部分高亮，已完成部分绿色标记：

```html
<section class="slide" data-type="toc">
  <div class="kicker">主题 · AI 分享</div>
  <div class="toc-wrap">
    <div class="toc-row done"><div class="toc-dot">1</div><div class="toc-name">第一部分</div><div class="toc-tag">为什么要做</div></div>
    <div class="toc-connector done"></div>
    <div class="toc-row current"><div class="toc-dot">2</div><div class="toc-name">第二部分</div><div class="toc-tag">别人在做什么</div></div>
    <div class="toc-connector"></div>
    <div class="toc-row"><div class="toc-dot">3</div><div class="toc-name">第三部分</div><div class="toc-tag">是什么</div></div>
    <!-- ... -->
  </div>
</section>
```

### Step 6：本地预览

生成的 HTML 文件直接双击在浏览器中打开即可预览。键盘操作：
- ← → / Space：翻页
- P：演讲模式
- G：跳转到指定页
- Home / End：首页 / 末页

## 知识库联动

生成 PPT 内容时，优先从 `wiki/` 知识库提取数据：
- 政策类 → `wiki/synthesis/AI政策与国资导向.md`、`wiki/synthesis/国企AI宣讲-政策锚定.md`
- 案例类 → `wiki/industry/国有企业AI应用案例.md`、`wiki/synthesis/全球建筑企业AI应用案例.md`
- 集团类 → `wiki/synthesis/中建发展AI战略定位分析.md`、`wiki/entities/中建发展.md`
- 技术类 → `wiki/concepts/Agent.md`、`wiki/concepts/大语言模型.md`

每个数据点必须有来源标注（页脚 footnote）。

## 参考文件

- [设计系统完整参考](references/design-system.md) — 颜色、字体、组件、布局、JS 引擎
- [HTML 骨架模板](assets/skeleton.html) — 可直接运行的起手模板
