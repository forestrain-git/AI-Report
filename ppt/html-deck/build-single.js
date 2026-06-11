const fs = require('fs');
const path = require('path');

const DECK_DIR = __dirname;

// 读取 index.html 提取 DECK_MANIFEST
const indexHtml = fs.readFileSync(path.join(DECK_DIR, 'index.html'), 'utf8');
const manifestMatch = indexHtml.match(/window\.DECK_MANIFEST = (\[[\s\S]*?\]);/);
if (!manifestMatch) {
  console.error('Cannot find DECK_MANIFEST in index.html');
  process.exit(1);
}
const manifest = eval(manifestMatch[1]);

// 读取共享 CSS
const sharedCss = [
  fs.readFileSync(path.join(DECK_DIR, 'shared', 'tokens.css'), 'utf8'),
  fs.readFileSync(path.join(DECK_DIR, 'shared', 'slide-system.css'), 'utf8')
].join('\n');

// 读取每个 slide 的完整 HTML，用 JSON.stringify 安全编码
const slides = manifest.map(item => {
  const slidePath = path.join(DECK_DIR, item.file);
  const content = fs.readFileSync(slidePath, 'utf8');
  return JSON.stringify(content);
});

const parts = [];

// HTML 头部
parts.push(`<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>AI时代：我们的选择与行动 · 宣讲PPT</title>
<style>
${sharedCss}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; background: #e2e8f0; overflow: hidden; font-family: -apple-system, "PingFang SC", sans-serif; }
#stage { position: fixed; top: 50%; left: 50%; transform-origin: top left; will-change: transform; background: #fff; box-shadow: 0 10px 60px rgba(0,0,0,0.4); }
iframe { width: 100%; height: 100%; border: 0; display: block; background: #0a1628; }
.counter { position: fixed; bottom: 20px; right: 20px; background: rgba(0,0,0,0.65); color: #fff; padding: 6px 14px; border-radius: 999px; font-size: 13px; letter-spacing: 0.05em; font-variant-numeric: tabular-nums; z-index: 100; user-select: none; opacity: 0.7; transition: opacity 0.2s; }
.counter:hover { opacity: 1; }
.counter .label { color: rgba(255,255,255,0.7); margin-left: 8px; }
.nav-zone { position: fixed; top: 0; bottom: 0; width: 15%; cursor: pointer; z-index: 50; }
.nav-zone.left  { left: 0; }
.nav-zone.right { right: 0; }
.nav-hint { position: absolute; top: 50%; transform: translateY(-50%); width: 44px; height: 44px; border-radius: 999px; background: rgba(255,255,255,0.08); color: rgba(255,255,255,0.6); display: flex; align-items: center; justify-content: center; font-size: 22px; opacity: 0; transition: opacity 0.2s; }
.nav-zone.left  .nav-hint { left: 20px; }
.nav-zone.right .nav-hint { right: 20px; }
.nav-zone:hover .nav-hint { opacity: 1; }
@media print {
  @page { size: 1920px 1080px; margin: 0; }
  html, body { background: #fff; overflow: visible; height: auto; }
  #stage { position: static; transform: none !important; box-shadow: none; }
  .counter, .nav-zone { display: none !important; }
  .print-stack { display: block; }
  .print-stack iframe { width: 1920px; height: 1080px; page-break-after: always; display: block; }
}
</style>
</head>
<body>
<div id="stage"><iframe id="frame" src="about:blank"></iframe></div>
<div class="nav-zone left" id="navL"><div class="nav-hint">&#8249;</div></div>
<div class="nav-zone right" id="navR"><div class="nav-hint">&#8250;</div></div>
<div class="counter" id="counter">1 / 1</div>
<div class="print-stack" id="printStack" style="display:none;"></div>
<script>`);

// JS 数据
parts.push('window.DECK_MANIFEST = ' + JSON.stringify(manifest, null, 2) + ';');
parts.push('window.DECK_WIDTH = 1920;');
parts.push('window.DECK_HEIGHT = 1080;');
parts.push('window.SLIDE_HTML = [');
for (let i = 0; i < slides.length; i++) {
  parts.push('  // ' + manifest[i].label);
  parts.push('  ' + slides[i] + (i < slides.length - 1 ? ',' : ''));
}
parts.push('];');

// JS 逻辑
parts.push(`
const storageKey = 'deck-index-' + location.pathname;
let current = 0;

const W = window.DECK_WIDTH || 1920;
const H = window.DECK_HEIGHT || 1080;
const stage = document.getElementById('stage');
const frame = document.getElementById('frame');
const counter = document.getElementById('counter');
const printStack = document.getElementById('printStack');

stage.style.width = W + 'px';
stage.style.height = H + 'px';

function fit() {
  const s = Math.min(window.innerWidth / W, window.innerHeight / H);
  const x = (window.innerWidth - W * s) / 2;
  const y = (window.innerHeight - H * s) / 2;
  stage.style.transform = 'translate(' + x + 'px, ' + y + 'px) scale(' + s + ')';
  stage.style.top = '0';
  stage.style.left = '0';
}

function show(idx) {
  if (idx < 0 || idx >= window.SLIDE_HTML.length) return;
  current = idx;
  frame.srcdoc = window.SLIDE_HTML[idx];
  counter.innerHTML = (idx + 1) + ' / ' + window.SLIDE_HTML.length + ' <span class="label">' + (window.DECK_MANIFEST[idx].label || '') + '</span>';
  try { localStorage.setItem(storageKey, String(idx)); } catch (_) {}
  if (location.hash !== '#' + (idx + 1)) {
    history.replaceState(null, '', '#' + (idx + 1));
  }
}

function next() { show(Math.min(current + 1, window.SLIDE_HTML.length - 1)); }
function prev() { show(Math.max(current - 1, 0)); }

function onKey(e) {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  switch (e.key) {
    case 'ArrowRight': case ' ': case 'PageDown': e.preventDefault(); next(); break;
    case 'ArrowLeft': case 'PageUp': e.preventDefault(); prev(); break;
    case 'Home': e.preventDefault(); show(0); break;
    case 'End': e.preventDefault(); show(window.SLIDE_HTML.length - 1); break;
    case 'p': case 'P': window.print(); break;
    default:
      if (e.key >= '1' && e.key <= '9') {
        const i = parseInt(e.key, 10) - 1;
        if (i < window.SLIDE_HTML.length) { e.preventDefault(); show(i); }
      }
  }
}

document.addEventListener('keydown', onKey);

// 只绑 window，避免重复触发
function bindIframeKeys() {
  try {
    const iw = frame.contentWindow;
    if (!iw) return;
    iw.addEventListener('keydown', onKey);
  } catch (_) {}
}
frame.addEventListener('load', bindIframeKeys);

document.getElementById('navL').addEventListener('click', prev);
document.getElementById('navR').addEventListener('click', next);
window.addEventListener('resize', fit);
window.addEventListener('hashchange', function() {
  const m = location.hash.match(/^#(\\d+)$/);
  if (m) show(parseInt(m[1], 10) - 1);
});

const hashMatch = location.hash.match(/^#(\\d+)$/);
if (hashMatch) current = Math.min(parseInt(hashMatch[1], 10) - 1, window.SLIDE_HTML.length - 1);
else try {
  const v = parseInt(localStorage.getItem(storageKey), 10);
  if (!isNaN(v) && v >= 0 && v < window.SLIDE_HTML.length) current = v;
} catch (_) {}
fit();
show(current);

window.addEventListener('beforeprint', function() {
  printStack.innerHTML = '';
  window.SLIDE_HTML.forEach(function(html) {
    const f = document.createElement('iframe');
    f.srcdoc = html;
    printStack.appendChild(f);
  });
  printStack.style.display = 'block';
  document.getElementById('stage').style.display = 'none';
});
window.addEventListener('afterprint', function() {
  printStack.innerHTML = '';
  printStack.style.display = 'none';
  document.getElementById('stage').style.display = '';
});
</script>
</body>
</html>`);

const output = parts.join('\n');
const outPath = path.join(DECK_DIR, 'single-file.html');
fs.writeFileSync(outPath, output, 'utf8');

const stats = fs.statSync(outPath);
console.log('Generated: ' + outPath);
console.log('Slides:    ' + manifest.length);
console.log('Size:      ' + (stats.size / 1024).toFixed(1) + ' KB');
console.log('Size:      ' + (stats.size / 1024 / 1024).toFixed(2) + ' MB');
