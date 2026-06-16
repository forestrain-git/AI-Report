const fs = require('fs');
const path = require('path');

const DECK_DIR = __dirname;

/**
 * 给 CSS 文本中的每条规则加 slide 作用域前缀
 * @param {string} css - 原始 CSS（已移除 body 规则）
 * @param {string} slideId - 如 "slide-0"
 * @returns {string} 作用域后的 CSS
 */
function scopeCss(css, slideId) {
  if (!css || !css.trim()) return css;

  // 第一步：移除 CSS 注释（避免注释中的 { } 干扰深度计数）
  const noComments = css.replace(/\/\*[\s\S]*?\*\//g, '');

  // 第二步：按 brace 深度切分 CSS 语句
  const statements = [];
  let depth = 0;
  let current = '';
  let i = 0;

  while (i < noComments.length) {
    const ch = noComments[i];

    if (ch === '{') {
      depth++;
      current += ch;
    } else if (ch === '}') {
      depth--;
      current += ch;
      if (depth === 0) {
        const stmt = current.trim();
        if (stmt) statements.push(stmt);
        current = '';
      }
    } else {
      current += ch;
    }
    i++;
  }
  // 残留内容（格式空白等）
  if (current.trim()) statements.push(current.trim());

  // 第三步：给每条规则的选择器加 #slideId 前缀
  const scoped = statements.map(stmt => {
    const braceIdx = stmt.indexOf('{');
    if (braceIdx === -1) return stmt; // 不是规则

    const pre = stmt.substring(0, braceIdx).trim();
    const rest = stmt.substring(braceIdx);

    // 不处理 at-rules（@keyframes, @media, @import, @font-face 等）
    if (pre.startsWith('@')) return stmt;

    // 处理逗号分隔的选择器列表
    const selectors = pre.split(',').map(s => {
      s = s.trim();
      if (!s) return s;
      // :root / html 是全局选择器，不做作用域
      if (s === ':root' || s === 'html') return s;
      // 已经包含 slide ID 则不重复
      if (s.includes('#' + slideId)) return s;
      return '#' + slideId + ' ' + s;
    });

    return selectors.join(', ') + ' ' + rest;
  });

  return scoped.filter(Boolean).join('\n');
}

// 读取 index.html 提取 DECK_MANIFEST
const indexHtml = fs.readFileSync(path.join(DECK_DIR, 'index.html'), 'utf8');
const manifestMatch = indexHtml.match(/window\.DECK_MANIFEST = (\[[\s\S]*?\]);/);
if (!manifestMatch) {
  console.error('Cannot find DECK_MANIFEST in index.html');
  process.exit(1);
}
const manifest = eval(manifestMatch[1]);

// 读取共享 CSS，预处理掉 @import
const tokensCss = fs.readFileSync(path.join(DECK_DIR, 'shared', 'tokens.css'), 'utf8');
const slideSystemCss = fs.readFileSync(path.join(DECK_DIR, 'shared', 'slide-system.css'), 'utf8')
  .replace(/@import\s+url\(["']?tokens\.css["']?\);?\s*\n?/g, '');
const sharedCss = tokensCss + '\n' + slideSystemCss;

// 处理每个 slide
const slides = manifest.map((item, idx) => {
  const slidePath = path.join(DECK_DIR, item.file);
  const html = fs.readFileSync(slidePath, 'utf8');

  // 1. 提取 body 标签属性（如 style、class）
  const bodyTagMatch = html.match(/<body([^>]*)>/i);
  const bodyAttrs = bodyTagMatch ? bodyTagMatch[1] : '';
  const bodyInlineStyleMatch = bodyAttrs.match(/style="([^"]*)"/i);
  let bodyInlineStyle = bodyInlineStyleMatch ? bodyInlineStyleMatch[1].trim() : '';

  // 2. 提取 body 内容
  const bodyContentMatch = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
  let bodyContent = bodyContentMatch ? bodyContentMatch[1].trim() : '';

  // 3. 提取所有 <style> 标签内容
  const styles = [];
  const styleRegex = /<style>([\s\S]*?)<\/style>/g;
  let styleMatch;
  while ((styleMatch = styleRegex.exec(html)) !== null) {
    styles.push(styleMatch[1]);
  }
  let privateCss = styles.join('\n');

  // 4. 从 privateCss 中提取多行 body { ... } 规则
  const bodyRuleMatch = privateCss.match(/^[\s]*body\s*\{([\s\S]*?)\n\s*\}/m);
  let bodyStyle = bodyRuleMatch ? bodyRuleMatch[1].trim() : '';

  // 合并 body 内联 style 和 CSS 中的 body 样式
  if (bodyInlineStyle) {
    bodyStyle = bodyStyle ? bodyInlineStyle + '; ' + bodyStyle : bodyInlineStyle;
  }

  // 5. 从 privateCss 中移除 body 规则
  privateCss = privateCss.replace(/^[\s]*body\s*\{[\s\S]*?\n\s*\}\s*\n?/gm, '');

  // 6. 清理空白行
  privateCss = privateCss.replace(/\n{3,}/g, '\n\n').trim();

  // 7. 修正路径
  bodyContent = bodyContent.replaceAll('../shared/', './shared/');
  bodyContent = bodyContent.replaceAll('../demos/', './demos/');
  bodyContent = bodyContent.replaceAll('../../assets/', '../assets/');
  bodyContent = bodyContent.replaceAll('../../archive/', '../archive/');
  privateCss = privateCss.replaceAll('../shared/', './shared/');

  // 8. CSS 作用域隔离：给每条规则加 #slide-N 前缀
  const slideId = 'slide-' + idx;
  privateCss = scopeCss(privateCss, slideId);

  // 提取原始 display 值（默认 flex，来自共享 CSS 的 body { display: flex; }）
  const displayMatch = bodyStyle.match(/display:\s*([^;]+)/);
  const originalDisplay = displayMatch ? displayMatch[1].trim() : 'flex';
  // 从 bodyStyle 中移除 display 声明，避免重复
  bodyStyle = bodyStyle.replace(/display:\s*[^;]+;?\s*/g, '');

  return {
    label: item.label,
    bodyStyle,
    originalDisplay,
    privateCss,
    bodyContent
  };
});

const parts = [];

// HTML 头部 + 共享 CSS + 主框架样式
parts.push(`<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>AI时代：我们的选择与行动 · 宣讲PPT</title>
<style>
${sharedCss}

/* 覆盖共享CSS中的 body 属性，匹配原始 index.html 的画布效果 */
html, body {
  width: 100%;
  height: 100%;
  background: #e2e8f0;
}

/* 主框架 */
#stage {
  position: fixed;
  top: 50%; left: 50%;
  transform-origin: top left;
  will-change: transform;
  background: #fff;
  box-shadow: 0 10px 60px rgba(0,0,0,0.4);
  width: 1920px;
  height: 1080px;
}

.slide {
  display: none;
  width: 1920px;
  height: 1080px;
  position: relative;
  overflow: hidden;
}

/* 导航 UI */
.counter {
  position: fixed;
  bottom: 20px; right: 20px;
  background: rgba(0,0,0,0.65);
  color: #fff;
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 13px;
  letter-spacing: 0.05em;
  font-variant-numeric: tabular-nums;
  z-index: 100;
  user-select: none;
  opacity: 0.7;
  transition: opacity 0.2s;
}
.counter:hover { opacity: 1; }
.counter .label { color: rgba(255,255,255,0.7); margin-left: 8px; }

.nav-zone {
  position: fixed;
  top: 0; bottom: 0;
  width: 15%;
  cursor: pointer;
  z-index: 50;
}
.nav-zone.left  { left: 0; }
.nav-zone.right { right: 0; }
.nav-hint {
  position: absolute;
  top: 50%; transform: translateY(-50%);
  width: 44px; height: 44px;
  border-radius: 999px;
  background: rgba(255,255,255,0.08);
  color: rgba(255,255,255,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  opacity: 0;
  transition: opacity 0.2s;
}
.nav-zone.left  .nav-hint { left: 20px; }
.nav-zone.right .nav-hint { right: 20px; }
.nav-zone:hover .nav-hint { opacity: 1; }

@media print {
  @page { size: 1920px 1080px; margin: 0; }
  html, body { background: #fff; overflow: visible; height: auto; }
  #stage { position: static; transform: none !important; box-shadow: none; }
  .counter, .nav-zone { display: none !important; }
  .slide { display: block !important; position: static; page-break-after: always; }
}
</style>
</head>
<body>`);

// 生成 slide divs
parts.push('<div id="stage">');
slides.forEach((slide, idx) => {
  const bodyStyle = slide.bodyStyle ? slide.bodyStyle + '; ' : '';
  const disp = idx === 0 ? slide.originalDisplay : 'none';
  parts.push(`  <div class="slide${idx === 0 ? ' active' : ''}" id="slide-${idx}" data-display="${slide.originalDisplay}" style="${bodyStyle}display: ${disp};">`);
  if (slide.privateCss) {
    parts.push(`    <style>${slide.privateCss}</style>`);
  }
  parts.push(`    ${slide.bodyContent}`);
  parts.push(`  </div>`);
});
parts.push('</div>');

// 导航 UI + JS
parts.push(`
<div class="nav-zone left" id="navL"><div class="nav-hint">&#8249;</div></div>
<div class="nav-zone right" id="navR"><div class="nav-hint">&#8250;</div></div>
<div class="counter" id="counter">1 / ${slides.length}</div>

<script>
const deck = ${JSON.stringify(manifest)};
const slideEls = document.querySelectorAll('.slide');
const counter = document.getElementById('counter');
const storageKey = 'deck-index-' + location.pathname;
let current = 0;

function fit() {
  const W = 1920, H = 1080;
  const s = Math.min(window.innerWidth / W, window.innerHeight / H);
  const x = (window.innerWidth - W * s) / 2;
  const y = (window.innerHeight - H * s) / 2;
  const stage = document.getElementById('stage');
  stage.style.transform = 'translate(' + x + 'px, ' + y + 'px) scale(' + s + ')';
  stage.style.top = '0';
  stage.style.left = '0';
}

function show(idx) {
  if (idx < 0 || idx >= slideEls.length) return;
  slideEls[current].classList.remove('active');
  slideEls[current].style.display = 'none';
  slideEls[idx].classList.add('active');
  slideEls[idx].style.display = slideEls[idx].getAttribute('data-display') || 'flex';
  current = idx;
  counter.innerHTML = (idx + 1) + ' / ' + slideEls.length + ' <span class="label">' + (deck[idx].label || '') + '</span>';
  try { localStorage.setItem(storageKey, String(idx)); } catch (_) {}
  if (location.hash !== '#' + (idx + 1)) {
    history.replaceState(null, '', '#' + (idx + 1));
  }
}

function next() { show(Math.min(current + 1, slideEls.length - 1)); }
function prev() { show(Math.max(current - 1, 0)); }

function onKey(e) {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  switch (e.key) {
    case 'ArrowRight': case ' ': case 'PageDown': e.preventDefault(); next(); break;
    case 'ArrowLeft': case 'PageUp': e.preventDefault(); prev(); break;
    case 'Home': e.preventDefault(); show(0); break;
    case 'End': e.preventDefault(); show(slideEls.length - 1); break;
    case 'p': case 'P': window.print(); break;
    default:
      if (e.key >= '1' && e.key <= '9') {
        const i = parseInt(e.key, 10) - 1;
        if (i < slideEls.length) { e.preventDefault(); show(i); }
      }
  }
}

document.addEventListener('keydown', onKey);
document.getElementById('navL').addEventListener('click', prev);
document.getElementById('navR').addEventListener('click', next);
window.addEventListener('resize', fit);
window.addEventListener('hashchange', function() {
  const m = location.hash.match(/^#(\\d+)$/);
  if (m) show(parseInt(m[1], 10) - 1);
});

const hashMatch = location.hash.match(/^#(\\d+)$/);
if (hashMatch) current = Math.min(parseInt(hashMatch[1], 10) - 1, slideEls.length - 1);
else try {
  const v = parseInt(localStorage.getItem(storageKey), 10);
  if (!isNaN(v) && v >= 0 && v < slideEls.length) current = v;
} catch (_) {}

fit();
show(current);
</script>
</body>
</html>`);

const output = parts.join('\n');
const outPath = path.join(DECK_DIR, 'single-file.html');
fs.writeFileSync(outPath, output, 'utf8');

const stats = fs.statSync(outPath);
console.log('Generated: ' + outPath);
console.log('Slides:    ' + slides.length);
console.log('Size:      ' + (stats.size / 1024).toFixed(1) + ' KB');
console.log('Size:      ' + (stats.size / 1024 / 1024).toFixed(2) + ' MB');
