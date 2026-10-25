// Imprime les pages HTML (couverture, page de version) en PDF A4 avec Chromium.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  for (const name of process.argv.slice(2)) {
    await p.goto('file://' + require('path').resolve(name + '.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: name + '.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
    await p.setViewportSize({ width: 794, height: 1123 });
    await p.screenshot({ path: name + '.png' });
  }
  await b.close();
})();
