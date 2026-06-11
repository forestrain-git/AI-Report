const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  const base = path.resolve(__dirname);

  const slides = [
    'slides/01-cover.html','slides/02-why-me.html','slides/03-agenda.html',
    'slides/04-part1-cover.html','slides/05-window-usage.html','slides/06-team-sync.html',
    'slides/07-stage2-cover.html','slides/08-windsurf-shock.html','slides/09-overconfidence.html',
    'slides/10-garbage-station.html','slides/11-two-reports.html','slides/12-trust.html',
    'slides/13-team-meeting.html','slides/14-stage3-cover.html','slides/15-strange-business.html',
    'slides/16-lobster-duality.html','slides/17-sanxing-liubu.html','slides/18-reversal.html',
    'slides/19-product-manager.html','slides/20-formula-quality.html','slides/21-team-other-side.html',
    'slides/22-learning-method.html','slides/23-stage4-cover.html','slides/24-zero-to-solution.html',
    'slides/25-zero-to-cc.html','slides/25-llm-wiki.html','slides/26-cc-ob.html',
    'slides/28-cc-ob-project.html','slides/27-team-transform.html','slides/28-three-leaps.html',
    'slides/29-stage4-reflection.html','slides/30-part2-cover.html','slides/31-window-tools.html',
    'slides/32-kimi.html','slides/33-lobster-tool.html','slides/34-cc-tool.html',
    'slides/35-yitang-case.html','slides/36-summary.html','slides/37-closing.html'
  ];

  const overflows = [];
  for (const f of slides) {
    const filePath = path.join(base, f);
    await page.goto('file:///' + filePath.replace(/\\/g, '/'));
    await page.waitForTimeout(600);
    const scrollH = await page.evaluate(() => document.documentElement.scrollHeight);
    const scrollW = await page.evaluate(() => document.documentElement.scrollWidth);
    const name = path.basename(f);
    if (scrollH > 1080 || scrollW > 1920) {
      overflows.push({ name, w: scrollW, h: scrollH });
      await page.screenshot({ path: `overflow_${name.replace('.html','')}.png`, fullPage: false });
    }
  }
  console.log('=== OVERFLOW REPORT ===');
  if (overflows.length === 0) {
    console.log('All 39 slides fit within 1920x1080.');
  } else {
    for (const o of overflows) {
      console.log(`${o.name}: ${o.w}x${o.h} OVERFLOW`);
    }
  }
  await browser.close();
})().catch(e => console.error(e.message));
