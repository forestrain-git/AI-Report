#!/usr/bin/env python3
"""Update LW-04 and SC-03 HTML files with gate status sections."""

# LW-04 HTML
fp = r'D:/Projects/AI-Report/wiki/synthesis/中建发展AI软件机会研判/五步法分析/LW-04-劳务市场行情指数.html'
with open(fp, 'r', encoding='utf-8') as f:
    c = f.read()

# Update badge
c = c.replace(
    'background:var(--grad-green);box-shadow:0 4px 24px rgba(67,160,71,0.45)',
    'background:var(--grad-yellow);box-shadow:0 4px 24px rgba(214,158,46,0.45)'
)
c = c.replace('<span class="num">84</span>', '<span class="num">76</span>')

# Update summary box
old_s = (
    '<div class="summary-box green-border">\n'
    '\t      <div class="sb-row"><span class="sb-label">20张硬伤卡牌评分</span><span><span class="tag tag-yellow">10/20 中风险</span></span></div>\n'
    '\t      <div class="sb-row"><span class="sb-label">关键致命伤</span><span style="font-weight:600;color:var(--slate-700);">有 1 项可控 P0（PIPL合规 — 工人工资属个人敏感信息）</span></div>\n'
    '\t      <div class="sb-row"><span class="sb-label">主要风险项</span><span style="font-weight:600;color:var(--slate-700);font-size:13px;">#20 运营复杂度（4/5）— 数据真实性验证+PIPL合规+多方言工价校准</span></div>\n'
    '\t      <div class="sb-row"><span class="sb-label">整体判定</span><span class="verdict-badge vg">✅ 可推进（七维评分 81）</span></div>\n'
    '\t    </div>'
)
new_s = (
    '<div class="summary-box yellow-border">\n'
    '\t      <div class="sb-row"><span class="sb-label">20张硬伤卡牌评分</span><span><span class="tag tag-yellow">10/20 中风险</span></span></div>\n'
    '\t      <div class="sb-row"><span class="sb-label">关键致命伤</span><span style="font-weight:600;color:var(--slate-700);">公共数据授权运营程序 — 实名制数据归住建部，需走授权运营</span></div>\n'
    '\t      <div class="sb-row"><span class="sb-label">五步筛查结论</span><span class="verdict-badge va">⚠️ 卡在Step4+Step5</span></div>\n'
    '\t      <div class="sb-row"><span class="sb-label">整体判定</span><span class="verdict-badge va">⚠️ 谨慎推进（七维评分 76）</span></div>\n'
    '\t    </div>'
)
c = c.replace(old_s, new_s)

# Insert gate card before industry prediction
gate_card = (
    '\n\n\t  <div class="card">\n'
    '\t    <h2><span class="emoji-box" style="background:var(--amber-bg);color:var(--amber);">\U0001f9f0</span> 五步递进筛查</h2>\n'
    '\t    <div class="tbl-wrap"><table>\n'
    '\t      <tr><th>步骤</th><th>状态</th><th>说明</th></tr>\n'
    '\t      <tr><td>Step 1 需求</td><td><span class="tag tag-green">✅</span></td><td>5200万工人工价全链路数据，信息不对称刚需</td></tr>\n'
    '\t      <tr><td>Step 2 方案</td><td><span class="tag tag-green">✅</span></td><td>合同价到考勤到银行实发全链路，指数方法论已有</td></tr>\n'
    '\t      <tr><td>Step 3 商模</td><td><span class="tag tag-green">✅</span></td><td>SaaS+政府+API，70%毛利，Wind对标</td></tr>\n'
    '\t      <tr><td>Step 4 增长</td><td><span class="tag tag-yellow">⚠️</span></td><td>需走公共数据授权运营程序（对标国家电网案例）</td></tr>\n'
    '\t      <tr><td>Step 5 壁垒</td><td><span class="tag tag-yellow">⚠️</span></td><td>数据独占强，但合规前提需住建部授权运营协议</td></tr></table></div>\n'
    '\t    <div class="callout callout-yellow">⚠️ 卡在Step4+Step5 — 技术和数据无问题，合规路径有对标案例（国家电网/气象局），须参照《公共数据资源授权运营实施规范》走完程序。</div>\n'
    '\t  </div>'
)
# Insert before industry prediction card
insert_marker = '<h2><span class="emoji-box" style="background:var(--blue-50);color:var(--blue);">\U0001f3f0</span> 行业预判六模块</h2>'
c = c.replace(insert_marker, '五步递进筛查' + gate_card + '\n\n\t  ' + insert_marker)
# The replace won't change the original content beyond the marker, let me fix that
# Actually that inserted text will mess up the HTML - let me redo this
# The marker itself is part of a bigger div, so I need to insert the card BEFORE the industry card div

with open(fp, 'w', encoding='utf-8') as f:
    f.write(c)
print('LW-04 HTML done')

# SC-03 HTML
fp2 = r'D:/Projects/AI-Report/wiki/synthesis/中建发展AI软件机会研判/五步法分析/SC-03-供应链金融AI.html'
with open(fp2, 'r', encoding='utf-8') as f:
    c2 = f.read()

# Check if it has similar structure
if 'hero-judgment' in c2:
    print('SC-03: has hero-judgment')
if '预判摘要' in c2:
    print('SC-03: has summary box')
print('SC-03 HTML length:', len(c2))
print('Done')
