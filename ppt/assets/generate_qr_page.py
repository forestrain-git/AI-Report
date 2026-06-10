#!/usr/bin/env python3
"""Generate the 会后学习资源包 HTML page with embedded QR codes."""

import qrcode, io, base64, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# === QR Code URLs (placeholder - replace with real URLs before distribution) ===
resources = {
    'quickstart': {
        'url': 'https://example.com/ai-quickstart',
        'title': 'AI 快速入门指南',
        'subtitle': '2小时 · 按角色定制'
    },
    'course': {
        'url': 'https://www.coursera.org/learn/ai-for-everyone',
        'title': '吴恩达 AI 通识课',
        'subtitle': '6小时 · 全球最佳入门'
    },
    'challenge': {
        'url': 'https://example.com/ai-30day',
        'title': '30天 AI 实战挑战',
        'subtitle': '每天15分钟'
    },
    'tools': {
        'url': 'https://example.com/ai-tools',
        'title': '工具速查卡',
        'subtitle': '5个工具 · 3分钟上手'
    },
    'community': {
        'url': 'https://example.com/ai-community',
        'title': 'AI 学习社群',
        'subtitle': '持续更新 · 互相学习'
    }
}

# Generate QR codes as base64 data URIs
qr_data = {}
for key, res in resources.items():
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=8, border=2)
    qr.add_data(res['url'])
    qr.make(fit=True)
    img = qr.make_image(fill_color='#16213e', back_color='white')
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    b64 = base64.b64encode(buf.getvalue()).decode()
    qr_data[key] = f'data:image/png;base64,{b64}'

# Build HTML
html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 学习资源包 - 中建发展</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    background: #f5f7fa;
    color: #1a1a2e;
    min-height: 100vh;
  }}
  .header {{
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: white;
    padding: 48px 24px 40px;
    text-align: center;
  }}
  .header h1 {{ font-size: 28px; font-weight: 700; margin-bottom: 8px; letter-spacing: 1px; }}
  .header .subtitle {{ font-size: 15px; opacity: 0.85; line-height: 1.6; }}
  .header .badge {{
    display: inline-block;
    background: rgba(255,255,255,0.15);
    padding: 4px 16px;
    border-radius: 20px;
    font-size: 13px;
    margin-top: 12px;
  }}
  .section-label {{
    font-size: 13px;
    font-weight: 600;
    color: #0f3460;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin: 32px 0 8px;
    padding: 0 24px;
  }}
  .container {{ max-width: 480px; margin: 0 auto; padding: 0 24px; }}

  .qr-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 24px;
  }}
  .qr-card {{
    background: white;
    border-radius: 16px;
    padding: 20px 16px;
    text-align: center;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    transition: transform 0.2s;
  }}
  .qr-card:hover {{ transform: translateY(-2px); box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
  .qr-card.wide {{ grid-column: 1 / -1; }}
  .qr-card img {{ width: 140px; height: 140px; border-radius: 8px; }}
  .qr-card.wide img {{ width: 160px; height: 160px; }}
  .qr-card h3 {{ font-size: 15px; font-weight: 600; margin: 12px 0 4px; color: #1a1a2e; }}
  .qr-card p {{ font-size: 12px; color: #666; line-height: 1.4; }}
  .qr-card .tag {{
    display: inline-block;
    background: #e8f4f8;
    color: #0f3460;
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 10px;
    margin-top: 6px;
  }}

  .role-section {{
    background: white;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 16px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  }}
  .role-section h3 {{
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .role-desc {{ font-size: 13px; color: #666; margin-bottom: 12px; }}
  .timeline {{ padding-left: 20px; border-left: 2px solid #e8f4f8; }}
  .timeline-item {{
    position: relative;
    padding: 8px 0 8px 16px;
    font-size: 14px;
    color: #444;
    line-height: 1.5;
  }}
  .timeline-item::before {{
    content: '';
    position: absolute;
    left: -25px;
    top: 14px;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #0f3460;
    border: 2px solid white;
    box-shadow: 0 0 0 2px #e8f4f8;
  }}
  .timeline-item strong {{ color: #1a1a2e; }}
  .tool-tag {{
    background: #fff3e0;
    color: #e65100;
    font-size: 11px;
    padding: 1px 6px;
    border-radius: 4px;
    margin-left: 4px;
  }}

  .tools-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
  }}
  .tool-chip {{
    background: #f8f9fa;
    border-radius: 10px;
    padding: 12px;
    text-align: center;
    font-size: 13px;
  }}
  .tool-chip .tool-name {{ font-weight: 600; color: #1a1a2e; }}
  .tool-chip .tool-desc {{ font-size: 11px; color: #888; margin-top: 2px; }}

  .footer {{
    text-align: center;
    padding: 32px 24px 48px;
    color: #999;
    font-size: 12px;
    line-height: 1.8;
  }}
  .footer strong {{ color: #666; }}

  @media print {{
    body {{ background: white; }}
    .header {{ padding: 24px; }}
    .qr-card, .role-section {{ box-shadow: none; border: 1px solid #eee; break-inside: avoid; }}
  }}
</style>
</head>
<body>

<div class="header">
  <h1>🚀 AI 学习资源包</h1>
  <p class="subtitle">扫一个码，从今天开始行动</p>
  <div class="badge">中建发展 · AI 转型工作组</div>
</div>

<div class="container">
  <div class="section-label">用微信扫一个就够</div>
  <div class="qr-grid">
    <div class="qr-card wide">
      <img src="{qr_data['quickstart']}" alt="快速入门">
      <h3>📋 AI 快速入门指南</h3>
      <p>按你的角色，给你最短路径</p>
      <div class="tag">⏱ 2 小时 · 推荐首选</div>
    </div>
    <div class="qr-card">
      <img src="{qr_data['course']}" alt="通识课程">
      <h3>🎓 吴恩达通识课</h3>
      <p>全球最佳<br>AI 入门课</p>
      <div class="tag">⏱ 6 小时</div>
    </div>
    <div class="qr-card">
      <img src="{qr_data['challenge']}" alt="30天挑战">
      <h3>🔥 30天实战挑战</h3>
      <p>每天 15 分钟<br>从会用到用好</p>
      <div class="tag">⏱ 每天 15 分钟</div>
    </div>
    <div class="qr-card">
      <img src="{qr_data['tools']}" alt="工具速查">
      <h3>🧰 工具速查卡</h3>
      <p>5 个工具<br>3 分钟上手</p>
      <div class="tag">⚡ 即用</div>
    </div>
    <div class="qr-card">
      <img src="{qr_data['community']}" alt="学习社群">
      <h3>👥 AI 学习社群</h3>
      <p>持续更新<br>互相学习</p>
      <div class="tag">💬 长期</div>
    </div>
  </div>

  <div class="section-label">按你的角色 · 推荐路径</div>

  <div class="role-section">
    <h3>👔 班子成员 / 决策层</h3>
    <p class="role-desc">核心问题：AI 对我的业务意味着什么？怎么决策？</p>
    <div class="timeline">
      <div class="timeline-item"><strong>第 1 周</strong>：完成吴恩达《AI For Everyone》<span class="tool-tag">Coursera</span><br><small style="color:#888">收获：理解 AI 能做什么、不能做什么、怎么定战略</small></div>
      <div class="timeline-item"><strong>第 2 周</strong>：用豆包帮你处理 3 件日常事务（邮件/报告/摘要）<span class="tool-tag">豆包</span></div>
      <div class="timeline-item"><strong>第 3 周</strong>：让秘书/助理用 Kimi 整理一份 50 页行业报告<span class="tool-tag">Kimi</span></div>
      <div class="timeline-item"><strong>第 4 周</strong>：在部门会上分享你的 AI 体验——这就是最好的推动</div>
    </div>
  </div>

  <div class="role-section">
    <h3>🏢 本部职能岗</h3>
    <p class="role-desc">核心问题：AI 能帮我提高哪些工作效率？</p>
    <div class="timeline">
      <div class="timeline-item"><strong>第 1 天</strong>：用豆包写一封你一直在拖的邮件 <span class="tool-tag">豆包</span></div>
      <div class="timeline-item"><strong>第 3 天</strong>：用 Kimi 读一份 20 页 PDF，10 分钟提取要点 <span class="tool-tag">Kimi</span></div>
      <div class="timeline-item"><strong>第 5 天</strong>：用通义听悟整理一次会议录音，30 分钟纪要变 5 分钟 <span class="tool-tag">通义听悟</span></div>
      <div class="timeline-item"><strong>第 7 天</strong>：用 AI 生成一份周报初稿——从"写"变成"改"</div>
      <div class="timeline-item"><strong>第 14 天</strong>：扫 30 天挑战码，系统提升</div>
    </div>
  </div>

  <div class="role-section">
    <h3>💻 信息化系统条线</h3>
    <p class="role-desc">核心问题：怎么把 AI 集成到系统和工作流中？</p>
    <div class="timeline">
      <div class="timeline-item"><strong>第 1 周</strong>：完成 Elements of AI（含中文版）<span class="tool-tag">免费</span></div>
      <div class="timeline-item"><strong>第 2 周</strong>：学习 Claude Code 基础操作，尝试用 AI 写一个数据处理脚本 <span class="tool-tag">Claude Code</span></div>
      <div class="timeline-item"><strong>第 3 周</strong>：用 Cursor 搭建一个简单的数据看板 <span class="tool-tag">Cursor</span></div>
      <div class="timeline-item"><strong>第 4 周</strong>：把经验分享给一个本部同事——传播 AI 文化</div>
      <div class="timeline-item"><strong>持续</strong>：加入社群，参与技术交流</div>
    </div>
  </div>

  <div class="section-label">5 个工具 · 3 分钟上手</div>
  <div class="role-section" style="padding:16px;">
    <div class="tools-grid">
      <div class="tool-chip"><div class="tool-name">🫘 豆包</div><div class="tool-desc">写邮件/报告/文案</div></div>
      <div class="tool-chip"><div class="tool-name">🌙 Kimi</div><div class="tool-desc">读长文档/提取要点</div></div>
      <div class="tool-chip"><div class="tool-name">🎙 通义听悟</div><div class="tool-desc">会议录音→纪要</div></div>
      <div class="tool-chip"><div class="tool-name">🤖 WorkBuddy</div><div class="tool-desc">无代码建系统</div></div>
      <div class="tool-chip" style="grid-column:1/-1;"><div class="tool-name">🧠 Claude</div><div class="tool-desc">深度对话/分析/编程——AI 中的"最强大脑"</div></div>
    </div>
  </div>

</div>

<div class="footer">
  <strong>扫码即学 · 学了就用 · 用了再学</strong><br>
  有问题？扫码加入学习社群，我们持续更新<br><br>
  <span style="font-size:11px;">中建发展 AI 转型工作组 · 2026年6月</span>
</div>

</body>
</html>'''

out_path = os.path.join(SCRIPT_DIR, '会后学习资源包.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Generated: {out_path} ({len(html)} bytes)')
