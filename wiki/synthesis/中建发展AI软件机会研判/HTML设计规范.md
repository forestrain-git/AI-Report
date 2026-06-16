# 子报告HTML设计规范

> 参考模板：`五步法分析/SC-03-供应链金融AI.html`
> 用于生成28个五步法分析子报告的统一HTML页面

---

## 一、设计原则

- **移动端优先**：max-width 480px，字号≥13px，触摸友好的间距
- **暗色header + 白色内容区**：渐变色header承载核心评分，白色卡片承载详细内容
- **高对比度**：评分区域必须白底+深色文字，不在暗色背景上放小字
- **视觉层级清晰**：总分大圆 > 七维评分条 > 卡片内容 > 表格细节

---

## 二、CSS变量体系

```css
:root {
  --blue: #1d4ed8;
  --blue-light: #dbeafe;
  --blue-50: #eff6ff;
  --green: #16a34a;
  --green-bg: #dcfce7;
  --amber: #d97706;
  --amber-bg: #fef3c7;
  --red: #dc2626;
  --red-bg: #fee2e2;
  --slate-50: #f8fafc;
  --slate-100: #f1f5f9;
  --slate-200: #e2e8f0;
  --slate-300: #cbd5e1;
  --slate-400: #94a3b8;
  --slate-500: #64748b;
  --slate-600: #475569;
  --slate-700: #334155;
  --slate-800: #1e293b;
  --slate-900: #0f172a;
  --radius: 12px;
  --radius-sm: 8px;
  --grad-header: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  --grad-green: linear-gradient(135deg, #43a047, #66bb6a);
  --grad-yellow: linear-gradient(135deg, #ef6c00, #ffa726);
  --grad-red: linear-gradient(135deg, #e53935, #ef5350);
}
```

---

## 三、页面结构（必须按此顺序）

```
1. Hero Header（暗色渐变背景）
   ├── hero-code：编码标签（如"五步法深度分析 · SC-03"）
   ├── hero-badge：88px圆形评分徽章（绿色渐变，数字36px）
   ├── hero-title：业务名称（20px）
   ├── hero-sub：副标题/关联方（13px）
   └── hero-judgment：判定胶囊（✅/⚠️/🔴）

2. Dimension Score Strip（白色卡片，浮在header下方）
   ├── dim-strip-title："七维评分 · 各维度表现"
   └── 7行 dim-item：
       ├── dim-label（76px宽，13px）
       ├── dim-bar（8px高进度条）
       └── dim-score（48px宽，13px，格式"17/18"）

3. Content Area（padding: 16px）
   ├── Card 1: 预判摘要（summary-box）
   ├── Card 2: 行业预判六模块（M1-M6）
   ├── Card 3: 五步法逐层分析（Step 1-5）
   ├── Card 4: 20张硬伤卡牌诊断
   ├── Card 5: 关键假设清单
   ├── Card 6: 敏感性分析 + 备选路径
   └── Card 7: 下一步行动

4. Back Link（← 返回全景报告，href="../report"）

5. Footer
```

---

## 四、评分颜色规则

| 分值范围 | 颜色 | CSS类 | 渐变 |
|:---|:---|:---|:---|
| 绿色（优秀） | fill-green | `linear-gradient(90deg, #22c55e, #16a34a)` | 进度条≥80% |
| 黄色（中等） | fill-yellow | `linear-gradient(90deg, #d97706, #ca8a04)` | 进度条60-79% |
| 红色（风险） | fill-red | `linear-gradient(90deg, #ef4444, #dc2626)` | 进度条<60% |

**总分徽章颜色**：
- ✅ ≥75：绿色渐变 `var(--grad-green)`
- ⚠️ 50-74：黄色渐变 `var(--grad-yellow)`
- 🔴 <50：红色渐变 `var(--grad-red)`

**进度条宽度**：`得分/满分 * 100%`

---

## 五、七维评分条格式

```html
<div class="dim-strip">
  <div class="dim-strip-title">七维评分 · 各维度表现</div>
  <!-- 7行，每行格式： -->
  <div class="dim-item">
    <span class="dim-label">变化天花板</span>
    <div class="dim-bar-wrap">
      <div class="dim-bar"><div class="fill fill-{color}" style="width:{pct}%"></div></div>
      <span class="dim-score">{得分}/{满分}</span>
    </div>
  </div>
  <!-- ⑦ 风险扣分用负数格式：-3/10 -->
</div>
```

七维维度名称和满分：
| 维度 | 名称 | 满分 |
|:---|:---|:---|
| ① | 变化天花板 | 18 |
| ② | 终局时机 | 17 |
| ③ | 需求真伪 | 17 |
| ④ | 方案优劣 | 17 |
| ⑤ | 商业模型 | 16 |
| ⑥ | 增长壁垒 | 15 |
| ⑦ | 风险扣分 | -10（负向） |

---

## 六、组件清单

| 组件 | CSS类 | 用途 |
|:---|:---|:---|
| 白色卡片 | `.card` | 所有内容区块 |
| 药丸标签 | `.tag .tag-green/yellow/red/blue` | 状态标记 |
| 判定胶囊 | `.verdict-badge .vg/va/vr` | 整体判定 |
| 摘要框 | `.summary-box .green-border` | 预判摘要数据行 |
| 进度条 | `.summary-strip` | 毛利率/硬伤总分等指标 |
| 表格 | `.tbl-wrap > table` | 数据对比 |
| LTV网格 | `.ltv-grid > .ltv-card` | 商业模型关键指标 |
| 阶段条 | `.phase-bar > .phase` | 增长三阶段 |
| 假设卡片 | `.assumption-item` | P0/P1/P2假设 |
| 敏感网格 | `.sens-grid > .sens-item` | 备选路径 |
| 行动卡片 | `.action-card` | 下一步行动 |
| 协同框 | `.synergy-box` | 协同关系图 |
| 调用框 | `.callout` | 关键判断/洞察 |
| 代码块 | `.synergy-box`（pre格式） | 产业链图 |
| 圆点标记 | `.dir-dot .green/yellow/red/blue` | 列表项标记 |

---

## 七、内容模板

每个子报告必须包含以下卡片（按顺序）：

1. **预判摘要**：硬伤卡牌总分 + P0致命伤 + 整体判定
2. **行业预判六模块**：M1拆解行业 → M2洞察变化 → M3稳态B → M4 Timing → M5天花板 → M6集中度
3. **五步法**：Step1需求 → Step2解决方案 → Step3商业模式 → Step4增长 → Step5壁垒
4. **20张硬伤卡牌**：汇总表（可压缩为8行，每行2-3张卡牌）
5. **关键假设清单**：P0/P1/P2分组
6. **敏感性分析 + 备选路径**
7. **下一步行动**
8. **协同关系**（如适用）

---

## 八、评分数据来源

所有评分必须与 `README.md` 中的七维总表一致。七维明细评分来自各五步法分析MD文件的评分输出。

**评分核实清单**（生成前必须检查）：
- [ ] 总分与README一致
- [ ] 七维明细加总 = 总分（允许±1分误差）
- [ ] 判定标识正确（≥75=✅，50-74=⚠️，<50=🔴）
- [ ] 硬伤卡牌总分与MD文件一致
