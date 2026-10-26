// Composite brand text over FLUX.2 art -> output/thumbs/thumb_<n>.html + .jpg (1280x720)
//   node thumbs.js            (run impeccable on output/thumbs/*.html afterwards — see SOP step 6)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'output', 'thumbs');
fs.mkdirSync(OUT, { recursive: true });
fs.copyFileSync(path.join(ROOT, 'render', 'fonts', 'Oswald.ttf'), path.join(OUT, 'Oswald.ttf'));

// Text formula: 1–2 imperative words ending in a period. Line 1 snow, line 2 amber.
const TEXT = [['DON\'T', 'ANSWER.'], ['NEVER', 'OPEN IT.'], ['THEY\'RE', 'WATCHING.'], ['DON\'T', 'ANSWER.'], ['KEEP IT', 'SHUT.']];

const page = (n, art, [a, b]) => `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>S01P1 thumbnail ${n}</title>
<style>
  @font-face { font-family: Oswald; src: url(Oswald.ttf); font-weight: 200 700; }
  :root { --navy: #0b1426; --snow: #eef3fa; --amber: #ffc23d; }
  body { margin: 0; }
  .thumb { position: relative; width: 1280px; height: 720px; overflow: hidden; background: var(--navy) url(${art}) center / cover; font-family: Oswald, Impact, sans-serif; }
  .shade { position: absolute; inset: 0; background: linear-gradient(100deg, rgba(11,20,38,.82) 0%, rgba(11,20,38,.35) 42%, rgba(11,20,38,0) 62%); }
  h1 { position: absolute; left: 48px; top: 36px; margin: 0; font-weight: 700; font-size: 150px; line-height: .92; letter-spacing: 1px; text-transform: uppercase;
       color: var(--snow); paint-order: stroke fill; -webkit-text-stroke: 10px var(--navy); }
  h1 span { display: block; color: var(--amber); }
  .chip { position: absolute; right: 40px; bottom: 36px; padding: 8px 20px; border: 3px solid var(--snow); border-radius: 8px;
          background: rgba(11,20,38,.8); color: var(--snow); font-weight: 600; font-size: 44px; letter-spacing: 4px; }
</style></head>
<body><div class="thumb"><div class="shade"></div><h1>${a}<span>${b}</span></h1><div class="chip">DAY 1</div></div></body></html>`;

(async () => {
  const browser = await chromium.launch();
  const p = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  for (let n = 1; n <= 5; n++) {
    const art = path.join(ROOT, 'build', 'thumbs', `art_${n}.png`);
    if (!fs.existsSync(art)) { console.log('missing', art); continue; }
    fs.copyFileSync(art, path.join(OUT, `art_${n}.png`));
    const html = path.join(OUT, `thumb_${n}.html`);
    fs.writeFileSync(html, page(n, `art_${n}.png`, TEXT[n - 1]));
    await p.goto(pathToFileURL(html).href);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(OUT, `thumb_${n}.jpg`), type: 'jpeg', quality: 92 });
    console.log('thumb', n);
  }
  await browser.close();
})();
