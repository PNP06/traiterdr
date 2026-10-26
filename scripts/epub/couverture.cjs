// Couverture de la version liseuse : la couverture du PDF (scripts/pdf/cover.html) en JPEG 1588 × 2246.
// Usage : node couverture.cjs couverture.jpg
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.resolve(__dirname, '../pdf/cover.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: process.argv[2], type: 'jpeg', quality: 90 });
  await b.close();
})();
