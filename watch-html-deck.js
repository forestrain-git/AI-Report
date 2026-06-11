const fs = require('fs');
const { execSync } = require('child_process');

const WATCH_DIR = 'ppt/html-deck';
const DEBOUNCE_MS = 3000;

let timer = null;
let isCommitting = false;

function getTimestamp() {
  const d = new Date();
  return d.toISOString().replace('T', ' ').slice(0, 19);
}

function commit() {
  if (isCommitting) {
    timer = setTimeout(commit, DEBOUNCE_MS);
    return;
  }

  try {
    const status = execSync('git status --porcelain ppt/html-deck/', { encoding: 'utf8' });
    if (!status.trim()) return;

    isCommitting = true;
    execSync('git add ppt/html-deck/');
    const ts = getTimestamp();
    execSync(`git commit -m "auto(html-deck): ${ts}"`);
    console.log(`[${ts}] Auto-committed html-deck changes`);
  } catch (e) {
    console.error('Commit failed:', e.message);
  } finally {
    isCommitting = false;
  }
}

function onChange(eventType, filename) {
  if (!filename) return;
  // 忽略截图目录、隐藏文件、日志文件
  if (filename.includes('screenshots')) return;
  if (filename.startsWith('.')) return;
  if (filename.endsWith('.log')) return;

  const relPath = `${WATCH_DIR}/${filename}`;
  console.log(`[change] ${eventType}: ${relPath}`);
  clearTimeout(timer);
  timer = setTimeout(commit, DEBOUNCE_MS);
}

// 递归监视
fs.watch(WATCH_DIR, { recursive: true }, onChange);

// 也直接监视 slides/ 和 shared/ 子目录（Windows fs.watch 有时递归不可靠）
['slides', 'shared'].forEach(sub => {
  const subDir = `${WATCH_DIR}/${sub}`;
  if (fs.existsSync(subDir)) {
    fs.watch(subDir, { recursive: true }, onChange);
  }
});

console.log(`[${getTimestamp()}] Watching ${WATCH_DIR}/ for changes...`);
console.log(`Press Ctrl+C to stop.`);
