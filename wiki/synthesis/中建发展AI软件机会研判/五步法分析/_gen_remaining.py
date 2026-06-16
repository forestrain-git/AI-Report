#!/usr/bin/env python3
"""Generate LW-03, LW-04, LW-05, SAFE-01 HTML reports."""
import os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from _gen_templates import CSS

def ds(dims):
    lines = []
    for n, s, m in dims:
        p = int(s/m*100)
        c = "fill-green" if p>=80 else ("fill-yellow" if p>=60 else "fill-red")
        lines.append(f'  <div class="dim-item">\n    <span class="dim-label">{n}</span>\n    <div class="dim-bar-wrap">\n      <div class="dim-bar"><div class="fill {c}" style="width:{p}%"></div></div>\n      <span class="dim-score">{s}/{m}</span>\n    </div>\n  </div>')
    return "\n".join(lines)

def hs(s):
    return {0:'<span class="hs hs-0">0</span>',1:'<span class="hs hs-1">1</span>',2:'<span class="hs hs-2">2</span>'}.get(s, f'<span class="hs hs-3">{s}</span>')

def mkpage(code, title, sub, total, judgment, dims, hard_score, body):
    if total>=75: bg,sh,vc,vi="var(--grad-green)","rgba(67,160,71,0.45)","vg","&#x2705;"
    elif total>=50: bg,sh,vc,vi="var(--grad-yellow)","rgba(217,119,6,0.45)","va","&#x26A0;&#xFE0F;"
    else: bg,sh,vc,vi="var(--grad-red)","rgba(229,57,53,0.45)","vr","&#x1F534;"
    sbc="green-border" if total>=75 else "yellow-border"
    bb="var(--green-bg);color:var(--green)" if total>=75 else "var(--amber-bg);color:var(--amber)"
    hc="green" if hard_score<=5 else ("yellow" if hard_score<=10 else "red")
    hp=hard_score*5
    hg="var(--grad-green)" if hard_score<=5 else ("var(--grad-yellow)" if hard_score<=10 else "var(--grad-red)")
    hcl="var(--green)" if hard_score<=5 else ("var(--amber)" if hard_score<=10 else "var(--red)")
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>{code} {title} - 五步法深度分析</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="container">
<div class="hero">
  <div class="hero-code">五步法深度分析 &middot; {code}</div>
  <div class="hero-badge-wrap">
    <div class="hero-badge" style="background:{bg};box-shadow:0 4px 24px {sh};">
      <span class="num">{total}</span>
      <span class="unit">总分</span>
    </div>
  </div>
  <div class="hero-title">{title}</div>
  <div class="hero-sub">{sub}</div>
  <div class="hero-judgment"><span style="font-size:16px;">{vi}</span> {judgment}</div>
</div>
<div class="dim-strip">
  <div class="dim-strip-title">七维评分 &middot; 各维度表现</div>
{ds(dims)}
</div>
<div class="content">
{body}
  <a class="back-link" href="../report.html">&#x2190; 返回全景报告</a>
</div>
<div class="footer">
  <p>基于一堂五步法 + 业务预判 + 行业预判方法论</p>
  <p>{code} {title} &middot; 深度分析报告</p>
  <p class="brand">中建发展AI软件方向 &middot; 2026-06-15</p>
</div>
</div>
</body>
</html>'''

# Read body content from separate files
for fname in ["_body_lw03.py","_body_lw04.py","_body_lw05.py","_body_safe01.py"]:
    p = os.path.join(BASE, fname)
    if os.path.exists(p):
        exec(open(p, encoding="utf-8").read())
