/* Apply only the appearance preference before the page paints. No network calls. */
(() => {
  let saved;
  try { saved = localStorage.getItem('aob-site-appearance'); } catch { /* Storage can be unavailable. */ }
  const dark = saved === 'dark' || (saved !== 'light' && window.matchMedia('(prefers-color-scheme: dark)').matches);
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
  document.querySelector('meta[name="theme-color"]').content = dark ? '#121e19' : '#f8f6ef';
})();
