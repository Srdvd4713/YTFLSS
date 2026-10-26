// Playwright frame capture -> ffmpeg (Wall at Ashford engine, Kestrel Lake adaptation)
//   node render.js --part 1                 full render -> output/part1.mp4
//   node render.js --part 1 --still 3,42.5  QA stills  -> build/part1/stills/*.png
//   node render.js --part 1 --workers 6 --from 30 --to 45   (partial preview -> output/part1_preview.mp4)
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const args = Object.fromEntries(process.argv.slice(2).reduce((a, v, i, all) => (v.startsWith('--') ? a.concat([[v.slice(2), all[i + 1] && !all[i + 1].startsWith('--') ? all[i + 1] : true]]) : a), []));
const part = args.part || 1;
const ROOT = __dirname;
const BUILD = path.join(ROOT, 'build', `part${part}`);
const tl = JSON.parse(fs.readFileSync(path.join(BUILD, 'timeline.json'), 'utf8'));
const FPS = tl.fps;
const PAGE = require('url').pathToFileURL(path.join(ROOT, 'render', 'index.html')).href;

async function openPage(browser) {
  const page = await browser.newPage({ viewport: { width: tl.width, height: tl.height } });
  page.on('pageerror', e => console.error('PAGE ERROR:', e.message));
  await page.goto(PAGE);
  await page.evaluate(t => window.init(t), tl);
  return page;
}

async function stills(times) {
  const browser = await chromium.launch({ args: ['--disable-dev-shm-usage'] });
  const page = await openPage(browser);
  fs.mkdirSync(path.join(BUILD, 'stills'), { recursive: true });
  for (const t of times) {
    await page.evaluate(t => window.renderAt(t), t);
    const f = path.join(BUILD, 'stills', `t${String(t).replace('.', '_')}.png`);
    await page.screenshot({ path: f });
    console.log(f);
  }
  await browser.close();
}

async function renderChunk(browser, idx, f0, f1) {
  const page = await openPage(browser);
  const out = path.join(BUILD, `chunk_${idx}.mp4`);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-framerate', String(FPS), '-i', '-',
    // mjpeg frames are full-range: convert to limited-range yuv420p so players don't crush/wash colours
    '-vf', 'scale=in_range=pc:out_range=tv,format=yuv420p', '-color_range', 'tv',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-r', String(FPS), out]);
  const done = new Promise((res, rej) => ff.on('close', c => (c ? rej(new Error('ffmpeg ' + c)) : res())));
  for (let f = f0; f < f1; f++) {
    await page.evaluate(t => window.renderAt(t), f / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 93 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (idx === 0 && (f - f0) % 150 === 0) console.log(`  worker0 ${Math.round(100 * (f - f0) / (f1 - f0))}%`);
  }
  ff.stdin.end();
  await done;
  await page.close();
  return out;
}

async function full() {
  const t0 = Date.now();
  const from = Math.round((+args.from || 0) * FPS), to = Math.round((+args.to || tl.duration) * FPS);
  const workers = +args.workers || 4;
  const per = Math.ceil((to - from) / workers);
  const browser = await chromium.launch({ args: ['--disable-dev-shm-usage', '--no-sandbox'] });
  console.log(`part ${part}: frames ${from}-${to} (${((to - from) / FPS).toFixed(1)}s) on ${workers} workers`);
  const chunks = await Promise.all([...Array(workers).keys()].map(i => renderChunk(browser, i, from + i * per, Math.min(to, from + (i + 1) * per))));
  await browser.close();
  const list = path.join(BUILD, 'chunks.txt');
  fs.writeFileSync(list, chunks.map(c => `file '${c.replace(/\\/g, '/')}'`).join('\n'));
  const preview = args.from || args.to;
  const out = path.join(ROOT, 'output', preview ? `part${part}_preview.mp4` : `part${part}.mp4`);
  // audio is already loudness-normalised to -14 LUFS by voice.py — mux without re-normalising
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list,
    '-ss', String(from / FPS), '-t', String((to - from) / FPS), '-i', path.join(BUILD, 'mix.wav'),
    '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-shortest', out]);
  console.log(`wrote ${out} in ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}

if (args.still) stills(String(args.still).split(',').map(Number));
else full();
