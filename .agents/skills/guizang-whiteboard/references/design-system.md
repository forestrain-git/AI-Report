# Guizang Whiteboard 设计系统参考

> 白底楷体蓝色主题，面向国企中高层宣讲场景。1920×1080 视口，单文件 HTML。

---

## 1. 颜色系统

```css
--ink:           #111827;   /* 主文字 */
--ink-dim:       #4B5563;   /* 次要文字 */
--ink-muted:     #9CA3AF;   /* 弱化文字 */
--accent:        #1A56DB;   /* 主强调色（蓝） */
--accent-light:  #E8EFFC;   /* 浅蓝背景 */
--accent-dark:   #1E40AF;   /* 深蓝（标题） */
--danger:        #CC0000;   /* 警告红 */
--danger-bg:     #FEF2F2;   /* 浅红背景 */
--success:       #059669;   /* 成功绿 */
--warning:       #D97706;   /* 警告橙 */
--surface:       #FFFFFF;   /* 卡片/页面背景 */
--surface-alt:   #F9FAFB;   /* 斑马条纹背景 */
--border:        #E5E7EB;   /* 默认边框 */
```

## 2. 字体系统

```css
--font-display: 'KaiTi','楷体','STKaiti','华文楷体',serif;           /* 标题 */
--font-body:    'KaiTi','楷体','STKaiti','华文楷体',Arial,'Noto Sans SC',sans-serif; /* 正文 */
--font-mono:    'Consolas','Courier New',monospace;                    /* 数据 */
```

### 字号阶梯

| 变量 | 值 | 用途 |
|:---|:---|:---|
| `--text-hero` | `clamp(36px, 3vw, 48px)` | 大数字/stat |
| `--text-h1` | `clamp(28px, 2.4vw, 36px)` | slide 标题（默认） |
| `--text-h2` | `clamp(24px, 2vw, 32px)` | 区块标题 |
| `--text-h3` | `clamp(20px, 1.6vw, 26px)` | 子标题 |
| `--text-body` | `clamp(18px, 1.4vw, 22px)` | 正文 |
| `--text-small` | `clamp(16px, 1.2vw, 18px)` | 辅助文字 |
| `--text-footnote` | `clamp(14px, 1vw, 16px)` | 脚注/标签 |

**紧凑模式标题**：`font-size: clamp(24px, 2vw, 30px)` — 内容页使用，比默认 h1 小两号。

## 3. 布局系统

### Slide 容器

```css
.slide {
  position: absolute; inset: 0;
  display: flex; flex-direction: column;
  padding: 60px;
  padding-bottom: 112px;  /* 60 + 52（导航栏） */
  overflow-y: auto;
}
```

### 紧凑模式（内容页必须使用）

```html
<section class="slide" data-type="content" 
  style="padding-top:16px;padding-bottom:56px;">
```

| 属性 | 默认 | 紧凑 |
|:---|:---|:---|
| padding-top | 60px | 16px |
| padding-bottom | 112px | 56px |

### 内部结构

```
.slide
  ├── .slide-header  (flex-shrink:0)
  │   ├── .kicker    (部分标签)
  │   └── .slide-title (h2)
  ├── .slide-body    (flex:1, overflow-y:hidden)
  │   └── 内容组件
  └── .footnote      (margin-top:auto, 推到底部)
```

## 4. 组件模式

### 4.1 双栏布局 .split

```html
<div class="split">
  <div class="split-left">左栏内容</div>
  <div class="split-right">右栏内容</div>
</div>
```
`grid-template-columns: 1fr 1fr; gap: 48px;`

### 4.2 卡片网格 .cards

```html
<div class="cards cards-3">
  <div class="card card-accent">
    <div class="card-title">标题</div>
    <p>内容</p>
  </div>
  <!-- ... -->
</div>
```

变体：`.cards-2` / `.cards-3` / `.cards-4` / `.card-accent`（左蓝线）/ `.card-danger`（左红线）

紧凑卡片：`style="padding:10px 14px;"` 或 `style="padding:8px 12px;font-size:var(--text-small);"`

### 4.3 数据统计 .stats

```html
<div class="stats" style="gap:16px;">
  <div class="stat" style="background:var(--accent-light);border-radius:var(--radius);padding:12px;flex:1;text-align:center;">
    <div class="stat-value">285</div>
    <div class="stat-label">接口数</div>
  </div>
</div>
```

### 4.4 时间线 .timeline

```html
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-year">2025.8</div>
    <div class="timeline-text">事件描述</div>
  </div>
</div>
```

### 4.5 引用 .quote

```html
<div class="quote">"引用文字"</div>
```
楷体斜体，左侧蓝色竖线。

### 4.6 标签 .tag

```html
<span class="tag tag-blue">蓝色标签</span>
<span class="tag tag-red">红色标签</span>
<span class="tag tag-green">绿色标签</span>
<span class="tag tag-gray">灰色标签</span>
```

### 4.7 表格

```html
<table>
  <tr><th>列1</th><th>列2</th></tr>
  <tr><td>数据</td><td>数据</td></tr>
</table>
```

紧凑表格：`<table class="compact">`

### 4.8 提示框

```html
<!-- 警告框 -->
<div style="padding:14px 20px;background:var(--danger-bg);border-radius:var(--radius);border-left:4px solid var(--danger);">
  <p style="margin:0;"><strong class="danger">⚠ 警告：</strong>内容</p>
</div>

<!-- 信息框 -->
<div style="padding:10px 14px;background:var(--surface-alt);border-radius:var(--radius);font-size:var(--text-small);">
  <strong>信息：</strong>内容
</div>

<!-- 强调框 -->
<div style="padding:10px 14px;background:var(--accent-light);border-radius:var(--radius);">
  <p style="margin:0;font-size:var(--text-small);"><strong class="accent">承上启下提示</strong></p>
</div>
```

## 5. Slide 类型模板

### 5.1 封面 cover

```html
<section class="slide active" data-type="cover">
  <div style="margin-bottom:40px;"><span class="kicker">主题标签</span></div>
  <h1 class="slide-title" style="font-size:clamp(44px,3.8vw,60px);margin-bottom:32px;">主标题</h1>
  <p class="lead">副标题描述</p>
  <div class="divider" style="margin:24px auto;"></div>
  <div style="display:flex;gap:32px;justify-content:center;margin-top:16px;">
    <span class="tag tag-blue">要点1</span>
    <span class="tag tag-blue">要点2</span>
  </div>
</section>
```

### 5.2 内容页 content（紧凑）

```html
<section class="slide" data-type="content" style="padding-top:16px;padding-bottom:56px;">
  <div class="slide-header" style="margin-bottom:4px;">
    <span class="kicker" style="margin-bottom:6px;">第一部分 · 主题</span>
    <h2 class="slide-title" style="margin-bottom:14px;font-size:clamp(24px,2vw,30px);">
      叙述型标题
    </h2>
  </div>
  <div class="slide-body">
    <!-- split / cards / stats / table 等组件 -->
  </div>
  <div class="footnote">来源：xxx</div>
  <div class="speaker-notes">演讲备注（观众看不到）</div>
</section>
```

### 5.3 定调页 pivot

```html
<section class="slide" data-type="pivot">
  <div><span class="quote-mark">"</span></div>
  <h2 class="slide-title" style="text-align:center;font-size:var(--text-hero);max-width:1100px;">
    金句或核心判断
  </h2>
  <p class="lead">补充说明</p>
  <div class="divider" style="margin:20px auto;"></div>
  <p style="color:var(--ink-dim);">过渡语：接下来进入第X部分</p>
</section>
```

### 5.4 TOC 目录页

```html
<section class="slide" data-type="toc">
  <div class="kicker">主题 · AI 分享</div>
  <div class="toc-wrap">
    <div class="toc-row done"><div class="toc-dot">1</div><div class="toc-name">已完成部分</div><div class="toc-tag">关键词</div></div>
    <div class="toc-connector done"></div>
    <div class="toc-row current"><div class="toc-dot">2</div><div class="toc-name">当前部分</div><div class="toc-tag">关键词</div></div>
    <div class="toc-connector"></div>
    <div class="toc-row"><div class="toc-dot">3</div><div class="toc-name">未到部分</div><div class="toc-tag">关键词</div></div>
  </div>
</section>
```

## 6. 导航栏

固定在页面底部，48px 高，包含：
- ◀ ▶ 翻页按钮
- 进度条（200px 宽）
- 页码显示（`1 / 33`）
- 快捷键提示

键盘操作：←→翻页 / Space下一页 / Home首页 / End末页 / P演讲模式 / G跳转

## 7. 演讲模式

按 P 键进入全屏演讲模式：
- 左半屏：当前页演讲备注（`.speaker-notes` 内容）
- 右半屏：计时器 + 页码 + 下一页标题预览
- 每页 `<div class="speaker-notes">` 中写入演讲提示

## 8. 打印

`@media print` 下所有 slide 纵向排列，每页一个 `page-break-after: always`，导航栏隐藏。

## 9. 部署

```bash
cp slide.html /tmp/project-site/index.html
source 'D:/Projects/.env'
npx wrangler pages deploy /tmp/project-site --project-name xxx --commit-dirty=true
# → https://xxx.pages.dev
```
