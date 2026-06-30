import re

with open('D:/Projects/AI-Report/260627-AI宣讲-v4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: Replace missing construction-ai-global.jpg with bim-digital-twin.jpg
html = html.replace('assets/construction-ai-global.jpg', 'assets/bim-digital-twin.jpg', 1)

# Fix 2: Enlarge logo containers from 70px to 100px
html = html.replace('width:70px;height:70px;', 'width:100px;height:100px;')
html = html.replace('max-width:56px;max-height:56px;', 'max-width:80px;max-height:80px;')

# Fix 3: Enrich Balfour Beatty card
html = html.replace(
    '<p style="font-size:var(--text-h3);font-weight:700;margin:0 0 4px;">\U0001f1ec\U0001f1e7 Balfour Beatty <span class="tag tag-red" style="font-size:10px;">LLM · 2025</span></p>\n          <p style="font-size:var(--text-body);color:var(--ink-dim);margin:0;line-height:1.5;">StoaOne + Copilot：自研LLM助手+全员部署，投资<b>720万英镑</b>，生产率<b>↑14-15%</b>',
    '<p style="font-size:var(--text-body);font-weight:700;margin:0 0 2px;">\U0001f1ec\U0001f1e7 英国 · Balfour Beatty</p>\n          <p style="font-size:var(--text-h3);font-weight:700;color:var(--accent-dark);margin:0 0 4px;">StoaOne + Copilot 全员部署</p>\n          <p style="font-size:var(--text-body);color:var(--ink-dim);margin:0;line-height:1.5;"><span class="tag tag-red" style="font-size:10px;">LLM · 2025</span> 英国最大建筑商（伦敦），2025.7完成AI全员上线——自研LLM助手+Microsoft Copilot。<strong>投资720万镑，试点生产率↑14-15%</strong>',
    1
)

print("Fix applied: Balfour Beatty")

# Fix 4: Enrich Strabag card
html = html.replace(
    '<p style="font-size:var(--text-h3);font-weight:700;margin:0 0 4px;">\U0001f1e6\U0001f1f9 Strabag <span class="tag tag-blue" style="font-size:10px;">ML · 2024</span></p>\n          <p style="font-size:var(--text-body);color:var(--ink-dim);margin:0;line-height:1.5;">DARIA财务风险AI：传统指标正常时也能预警，准确率<b>80%</b>，集团交通基建<b>全面推广</b>',
    '<p style="font-size:var(--text-body);font-weight:700;margin:0 0 2px;">\U0001f1e6\U0001f1f9 奥地利 · Strabag</p>\n          <p style="font-size:var(--text-h3);font-weight:700;color:var(--accent-dark);margin:0 0 4px;">DARIA 财务风险预警系统</p>\n          <p style="font-size:var(--text-body);color:var(--ink-dim);margin:0;line-height:1.5;"><span class="tag tag-blue" style="font-size:10px;">ML · 2024</span> 欧洲最大建筑集团之一（维也纳），DARIA用机器学习预测项目财务风险。<strong>传统指标正常时也能提前预警，准确率80%</strong>，交通基建全面推广',
    1
)
print("Fix applied: Strabag")

# Fix 5: Enrich Kajima card
html = html.replace(
    '<p style="font-size:var(--text-h3);font-weight:700;margin:0 0 4px;">\U0001f1ef\U0001f1f5 鹿岛建设 <span class="tag tag-green" style="font-size:10px;">AI自律 · 2020-2025</span></p>\n          <p style="font-size:var(--text-body);color:var(--ink-dim);margin:0;line-height:1.5;">A4CSEL：AI学习熟练工操作数据，<b>14台无人重机</b>24h协调，创国产水库<b>月施工量最高纪录</b>',
    '<p style="font-size:var(--text-body);font-weight:700;margin:0 0 2px;">\U0001f1ef\U0001f1f5 日本 · 鹿岛建设</p>\n          <p style="font-size:var(--text-h3);font-weight:700;color:var(--accent-dark);margin:0 0 4px;">A4CSEL 无人化施工系统</p>\n          <p style="font-size:var(--text-body);color:var(--ink-dim);margin:0;line-height:1.5;"><span class="tag tag-green" style="font-size:10px;">AI自律 · 2020-2025</span> 日本五大综合建设业（1840年创业），A4CSEL让AI学习熟练工操作数据，驱动<strong>14台无人重型机械24h协同</strong>，创国产水库月施工量最高纪录',
    1
)
print("Fix applied: Kajima")

# Fix 6: Enrich Skanska card
html = html.replace(
    '<p style="font-size:var(--text-h3);font-weight:700;margin:0 0 4px;">\U0001f1f8\U0001f1ea Skanska <span class="tag tag-gray" style="font-size:10px;">LLM+机器人 · 2024-2025</span></p>\n          <p style="font-size:var(--text-body);color:var(--ink-dim);margin:0;line-height:1.5;">Safety Sidekick（图像安全AI）+ Dusty放线机器人，已评估<b>70+AI工具</b>',
    '<p style="font-size:var(--text-body);font-weight:700;margin:0 0 2px;">\U0001f1f8\U0001f1ea 瑞典 · Skanska</p>\n          <p style="font-size:var(--text-h3);font-weight:700;color:var(--accent-dark);margin:0 0 4px;">Safety Sidekick + Dusty机器人</p>\n          <p style="font-size:var(--text-body);color:var(--ink-dim);margin:0;line-height:1.5;"><span class="tag tag-gray" style="font-size:10px;">LLM+机器人 · 2024-2025</span> 全球前五大建筑商（斯德哥尔摩），AI图像识别实时检测安全隐患（3000+员工），同时部署Dusty放线机器人。<strong>已评估70+AI工具，Dusty单项目节省100万美元返工</strong>',
    1
)
print("Fix applied: Skanska")

with open('D:/Projects/AI-Report/260627-AI宣讲-v4.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("All done!")
