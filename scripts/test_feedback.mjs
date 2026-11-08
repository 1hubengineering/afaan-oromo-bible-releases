/* Optional browser QA; no runtime dependency. See website-docs/VALIDATION.md.
 * Test-only Tally transport fixtures never reach published website assets.
 */
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire(process.env.AOB_QA_DIR ? path.resolve(process.env.AOB_QA_DIR, 'package.json') : import.meta.url);
const { chromium, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const origin = process.env.AOB_SITE_URL || 'http://127.0.0.1:8770/';
const output = path.resolve(process.env.AOB_QA_OUTPUT || '_preview/feedback-qa');
fs.mkdirSync(output, { recursive: true });
const browser = await chromium.launch({ headless: true });
const results = [];
const widths = process.argv.includes('--transport-only') ? [] : process.argv.includes('--subpath-smoke') ? [375, 1440] : [320, 375, 768, 844, 1280, 1440];
const tags = ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa', 'best-practice'];
const delay = '<!doctype html><html lang="en"><head><title>Test-only transport</title></head><body><p>Test-only Tally transport, no form or submission.</p><button type="button">Keyboard test control</button></body></html>';
async function noOverflow(page) {
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
  assert.equal(await page.locator('.feedback-dialog').evaluate(el => el.scrollWidth <= el.clientWidth), true);
}
async function audit(page) {
  const result = await new AxeBuilder({ page }).withTags(tags).analyze();
  assert.deepEqual(result.violations.map(v => ({ id: v.id, nodes: v.nodes.map(n => n.target) })), []);
}
async function emit(frame, name, id) {
  await frame.evaluate(({ name, id }) => parent.postMessage(JSON.stringify({ event: name, payload: { formId: id, id: 'test-transport-only' } }), '*'), { name, id });
}
try {
  for (const locale of ['en', 'om']) for (const theme of ['light', 'dark']) for (const width of widths) {
    const context = await browser.newContext({ viewport: { width, height: width === 844 ? 390 : 900 }, colorScheme: theme, reducedMotion: 'reduce' });
    // Keep unavailable-state QA independent of the real account configuration.
    await context.route('**/feedback-config.js', route => route.fulfill({ contentType: 'text/javascript', body: "window.AOB_FEEDBACK={en:{formId:'',copyReviewed:true},om:{formId:'',copyReviewed:false}};" }));
    const page = await context.newPage();
    const errors = [];
    const tallyRequests = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('request', request => { if (request.url().startsWith('https://tally.so/')) tallyRequests.push(request.url()); });
    await page.goto(origin + (locale === 'om' ? 'om/' : ''));
    assert.deepEqual(tallyRequests, []);
    assert.equal(await page.locator('html').getAttribute('data-theme'), theme);
    const links = page.locator('[data-feedback]');
    assert.equal(await links.count(), 6);
    // Every CTA opens the same dialog, including the mobile menu's hidden link.
    for (let i = 0; i < await links.count(); i++) {
      if (i === 0 && width <= 1279) await page.locator('.menu-toggle').click();
      if (i === 3) await page.locator('.faq-list details').last().locator('summary').click();
      await links.nth(i).click();
      assert.equal(await page.locator('.feedback-dialog').isVisible(), true);
      assert.equal(await page.locator('.feedback-unavailable').isVisible(), true);
      assert.equal(await page.locator('.feedback-embed iframe').count(), 0);
      assert.equal(await page.locator('.feedback-close').evaluate(el => el === document.activeElement), true);
      await page.keyboard.press('Shift+Tab');
      // Native dialogs may let focus visit browser chrome at the boundary.
      // No background page control may receive focus while the modal is open.
      assert.equal(await page.evaluate(() => document.activeElement === document.body || Boolean(document.activeElement.closest('.feedback-dialog'))), true);
      await page.locator('.brand').first().evaluate(el => el.focus());
      assert.equal(await page.locator('.brand').first().evaluate(el => el === document.activeElement), false);
      await page.keyboard.press('Tab');
      assert.equal(await page.locator('.feedback-close').evaluate(el => el === document.activeElement), true);
      await noOverflow(page);
      if (i === 2) await audit(page);
      await page.keyboard.press('Escape');
      assert.equal(await page.locator('.feedback-dialog').isVisible(), false);
      await expect(page.locator('body')).not.toHaveClass(/dialog-open/);
      const returnTarget = i === 0 && width <= 1279 ? page.locator('.menu-toggle') : links.nth(i);
      await expect(returnTarget).toBeFocused();
    }
    assert.deepEqual(tallyRequests, []);
    if (width <= 1279) {
      await page.locator('.menu-toggle').click();
      await page.locator('.site-nav a[href="#downloads"]').click();
      assert.equal(await page.locator('.site-nav').isVisible(), false);
      assert.equal(await page.evaluate(() => document.activeElement.id), 'downloads');
    }
    const tabs = page.getByRole('tab');
    await tabs.first().focus();
    await expect(tabs.first()).toBeFocused();
    for (let i = 0; i < 4; i++) {
      if (i) await page.keyboard.press('ArrowRight');
      await expect(tabs.nth(i)).toHaveAttribute('aria-selected', 'true');
    }
    await page.locator('#panel-bookmarks [data-lightbox]').click();
    await page.keyboard.press('Escape');
    assert.equal(await page.locator('#panel-bookmarks [data-lightbox]').evaluate(el => el === document.activeElement), true);
    await page.locator('.faq-list details').evaluateAll(items => items.forEach(el => { el.open = true; }));
    await audit(page);
    await page.locator('.theme-toggle').click();
    await page.reload();
    assert.equal(await page.locator('html').getAttribute('data-theme'), theme === 'light' ? 'dark' : 'light');
    await noOverflow(page);
    if ([375,1440].includes(width)) {
      await page.locator('.theme-toggle').click();
      await page.evaluate(() => { document.activeElement.blur(); window.scrollTo({ top: 0, behavior: 'instant' }); });
      await page.screenshot({ path: path.join(output, `${locale}-${theme}-${width}.png`), fullPage: true });
      await links.nth(2).click();
      await page.locator('.feedback-dialog').screenshot({ path: path.join(output, `${locale}-${theme}-${width}-dialog.png`) });
    }
    assert.deepEqual(errors, []);
    results.push({ locale, theme, width, ctas: 6, unconfigured: true, focusReturn: true, axeViolations: 0 });
    console.log(JSON.stringify(results.at(-1)));
    await context.close();
  }

  // Configured-state mechanics only. These fixtures do not prove a real Tally
  // form, submission, localization or Sheets connection works.
  for (const locale of ['en', 'om']) {
    const context = await browser.newContext({ viewport: { width: 375, height: 820 }, colorScheme: 'dark', reducedMotion: 'reduce' });
    await context.route('**/feedback-config.js', route => route.fulfill({ contentType: 'text/javascript', body: "window.AOB_FEEDBACK={en:{formId:'TESTEN',copyReviewed:true},om:{formId:'TESTOM',copyReviewed:true}};" }));
    await context.route('https://tally.so/embed/**', route => route.fulfill({ contentType: 'text/html', body: delay }));
    const page = await context.newPage();
    await page.clock.install();
    await page.goto(origin + (locale === 'om' ? 'om/' : '') + '?email=must-not-forward@example.invalid');
    assert.equal(page.frames().length, 1);
    const id = locale === 'om' ? 'TESTOM' : 'TESTEN';
    await page.locator('#feedback [data-feedback]').click();
    const iframe = page.locator('.feedback-embed iframe');
    await iframe.waitFor();
    assert.equal(await page.locator('.feedback-embed').getAttribute('aria-busy'), 'true');
    const embed = new URL(await iframe.getAttribute('src'));
    assert.equal(embed.pathname, '/embed/' + id);
    assert.equal(embed.searchParams.has('email'), false);
    assert.equal(await iframe.getAttribute('referrerpolicy'), 'no-referrer');
    assert.equal(await page.locator('.feedback-direct').getAttribute('href'), 'https://tally.so/r/' + id);
    assert.equal(await page.locator('.feedback-language-note').isVisible(), locale === 'om');
    await page.clock.fastForward(15001);
    assert.equal(await page.locator('.feedback-retry').isVisible(), true);
    const initial = page.frames().find(f => f.url().startsWith('https://tally.so/'));
    await emit(initial, 'Tally.FormLoaded', id);
    await page.waitForFunction(() => document.querySelector('.feedback-embed').getAttribute('aria-busy') === 'false');
    assert.equal(await page.locator('.feedback-retry').isVisible(), false);
    await noOverflow(page);
    await audit(page);
    await page.locator('.feedback-dialog').screenshot({ path: path.join(output, `${locale}-configured-transport.png`) });
    // Messages from the host window or with a mismatched form must not succeed.
    await page.evaluate(id => window.dispatchEvent(new MessageEvent('message', { origin: 'https://tally.so', source: window, data: JSON.stringify({ event: 'Tally.FormSubmitted', payload: { formId: id, id: 'spoof' } }) })), id);
    await page.evaluate(id => window.dispatchEvent(new MessageEvent('message', { origin: 'https://example.invalid', source: document.querySelector('.feedback-embed iframe').contentWindow, data: JSON.stringify({ event: 'Tally.FormSubmitted', payload: { formId: id, id: 'spoof-origin' } }) })), id);
    await emit(initial, 'Tally.FormSubmitted', 'WRONGFORM');
    await initial.evaluate(() => parent.postMessage('not-json', '*'));
    assert.equal(await page.locator('.feedback-success').isVisible(), false);
    await emit(initial, 'Tally.FormSubmitted', id);
    await page.locator('.feedback-success').waitFor();
    assert.equal(await page.locator('.feedback-success h3').evaluate(el => el === document.activeElement), true);
    assert.equal(await iframe.count(), 0);
    await audit(page);
    await page.locator('.feedback-done').click();
    assert.equal(await page.locator('#feedback [data-feedback]').evaluate(el => el === document.activeElement), true);
    // Closing a pending load cancels the old frame; retry makes a fresh one.
    await page.locator('#feedback [data-feedback]').click();
    await page.clock.fastForward(15001);
    await page.locator('.feedback-retry').click();
    assert.equal(await page.locator('.feedback-embed').getAttribute('aria-busy'), 'true');
    assert.equal(await iframe.count(), 1);
    await iframe.contentFrame().getByRole('button').focus();
    await page.keyboard.press('Escape');
    // Escape is not forwarded out of a cross-origin iframe by Chromium.
    // A keyboard user can leave it backwards and close from the site shell.
    assert.equal(await page.locator('.feedback-dialog').isVisible(), true);
    for (let step = 0; step < 4 && !await page.locator('.feedback-close').evaluate(el => el === document.activeElement); step++) await page.keyboard.press('Shift+Tab');
    await expect(page.locator('.feedback-close')).toBeFocused();
    await page.keyboard.press('Escape');
    await expect(iframe).toHaveCount(0);
    await page.clock.fastForward(20000);
    assert.equal(await page.locator('.feedback-dialog').isVisible(), false);
    await context.route('https://tally.so/embed/**', route => route.abort('blockedbyclient'));
    await page.locator('#feedback [data-feedback]').click();
    await page.clock.fastForward(15001);
    await expect(page.locator('.feedback-retry')).toBeVisible();
    assert.equal(await page.locator('.feedback-success').isVisible(), false);
    await page.locator('.feedback-close').click();
    await expect(iframe).toHaveCount(0);
    results.push({ locale, configuredTransportFixture: true, loading: true, timeout: true, lateReady: true, retry: true, blockedRequest: true, iframeKeyboardExit: true, iframeEscape: 'not propagated; Shift+Tab to Close then Escape works', trustedMessages: true, confirmationFocus: true, noQueryForwarding: true, realSubmission: 'NOT TESTED' });
    console.log(JSON.stringify(results.at(-1)));
    await context.close();
  }
  for (const locale of ['en', 'om']) {
    const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 375, height: 900 }, colorScheme: 'dark' });
    const page = await context.newPage();
    await page.goto(origin + (locale === 'om' ? 'om/' : ''));
    await page.locator('#feedback [data-feedback]').click();
    assert.equal(new URL(page.url()).hash, '#feedback');
    assert.equal(await page.locator('.feedback-email a[href^="mailto:"]').isVisible(), true);
    assert.equal(await page.locator('.gallery-panel:visible').count(), 4);
    await page.locator('.language-switch').click();
    assert.equal(await page.locator('html').getAttribute('lang'), locale === 'en' ? 'om' : 'en');
    results.push({ locale, noJavaScript: true, emailFallback: true, languageNavigation: true });
    await context.close();
  }
} finally {
  fs.writeFileSync(path.join(output, 'results.json'), JSON.stringify(results, null, 2) + '\n');
  await browser.close();
}
