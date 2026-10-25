// Rend un ou plusieurs HTML paged.js en PDF. Usage : node render.cjs a.html [b.html …] (écrit a.pdf, b.pdf…)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  await Promise.all(process.argv.slice(2).map(async (src) => {
    const p = await b.newPage();
    const t0 = Date.now();
    await p.goto('file://' + path.resolve(src), { waitUntil: 'networkidle', timeout: 120000 });
    let last = -1;
    for (;;) {
      const done = await p.evaluate(() => window.__paged === true);
      const n = await p.evaluate(() => document.querySelectorAll('.pagedjs_page').length);
      if (done) break;
      if (Date.now() - t0 > (+process.env.LIMITE || 900000)) {
        const fin = await p.evaluate(() => {
          const pages = document.querySelectorAll('.pagedjs_page');
          const last = pages[pages.length - 1].querySelector('.pagedjs_page_content');
          return last ? last.innerText.slice(-300) : '';
        });
        console.log(src, 'BLOQUÉ à la page', n, '| fin de la dernière page :', JSON.stringify(fin));
        await p.close(); return;
      }
      if (n !== last) { last = n; }
      await new Promise(r => setTimeout(r, 3000));
    }
    const n = await p.evaluate(() => document.querySelectorAll('.pagedjs_page').length);
    const titres = await p.evaluate(() => [...document.querySelectorAll('h1[id], h2[id], h3[id]')].map(h => {
      const pg = h.closest('.pagedjs_page');
      return { id: h.id, niveau: +h.tagName[1], titre: h.textContent.trim().replace(/\s+/g, ' '), page: pg ? +pg.dataset.pageNumber : 0 };
    }).filter(t => t.page));
    require('fs').writeFileSync(src.replace(/\.html$/, '.json'), JSON.stringify({ pages: n, titres }, null, 1));
    await p.pdf({ path: src.replace(/\.html$/, '.pdf'), preferCSSPageSize: true, printBackground: true, timeout: 600000 });
    console.log(src, n, 'pages en', Math.round((Date.now() - t0) / 1000), 's');
    await p.close();
  }));
  await b.close();
})();
