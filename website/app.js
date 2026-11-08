/* Progressive enhancements. Navigation, downloads and FAQs also work without JS. */
(() => {
  const root = document.documentElement;
  const labels = root.lang === 'om' ? {
    light: 'Gara bifa ifaatti jijjiiri', dark: 'Gara bifa dukkanaatti jijjiiri',
    openMenu: 'Tarree filannoowwanii bani', closeMenu: 'Tarree filannoowwanii cufi'
  } : {
    light: 'Switch to light appearance', dark: 'Switch to dark appearance',
    openMenu: 'Open navigation', closeMenu: 'Close navigation'
  };
  const themeButton = document.querySelector('.theme-toggle');
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  let explicitTheme = null;
  try { explicitTheme = localStorage.getItem('aob-site-appearance'); } catch { /* Session-only preference. */ }

  function setTheme(theme) {
    root.dataset.theme = theme;
    const label = theme === 'dark' ? labels.light : labels.dark;
    themeButton.setAttribute('aria-label', label);
    themeButton.title = label;
    document.querySelector('meta[name="theme-color"]').content = theme === 'dark' ? '#211b17' : '#fbf5e9';
  }
  setTheme(root.dataset.theme || (systemTheme.matches ? 'dark' : 'light'));
  themeButton.hidden = false;
  themeButton.addEventListener('click', () => {
    explicitTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(explicitTheme);
    try { localStorage.setItem('aob-site-appearance', explicitTheme); } catch { /* Keep it for this visit. */ }
  });
  systemTheme.addEventListener('change', event => {
    if (explicitTheme !== 'light' && explicitTheme !== 'dark') setTheme(event.matches ? 'dark' : 'light');
  });

  const nav = document.querySelector('.site-nav');
  const menuButton = document.querySelector('.menu-toggle');
  const mobile = window.matchMedia('(max-width: 1279px)');
  let menuOpen = false;
  function setMenu(open, restoreFocus = false) {
    menuOpen = open;
    nav.hidden = mobile.matches && !open;
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? labels.closeMenu : labels.openMenu);
    if (restoreFocus) menuButton.focus();
  }
  function layoutMenu() {
    menuButton.hidden = !mobile.matches;
    setMenu(false);
  }
  layoutMenu();
  mobile.addEventListener('change', layoutMenu);
  menuButton.addEventListener('click', () => {
    const opening = !menuOpen;
    setMenu(opening);
    // The expanded navigation is visually below the button, but precedes it in
    // source order. Start keyboard users on its first link rather than skipping it.
    if (opening) nav.querySelector('a').focus();
  });
  nav.addEventListener('click', event => {
    const link = event.target.closest('a');
    if (!link || link.hasAttribute('data-feedback') || !mobile.matches) return;
    setMenu(false);
    // Move keyboard focus with the navigation, rather than leaving it hidden.
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    }
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menuOpen) setMenu(false, true);
  });
  document.addEventListener('click', event => {
    if (menuOpen && !event.target.closest('.header-inner')) setMenu(false);
  });

  const dialog = document.querySelector('.image-dialog');
  if (typeof dialog.showModal === 'function') {
    const image = dialog.querySelector('.dialog-image');
    const caption = dialog.querySelector('.dialog-caption');
    let trigger;
    document.querySelectorAll('[data-lightbox]').forEach(link => {
      link.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        trigger = link;
        image.src = link.href;
        image.alt = link.querySelector('img').alt;
        caption.textContent = link.dataset.caption;
        dialog.showModal();
        document.body.classList.add('dialog-open');
      });
    });
    dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => {
      const bounds = dialog.getBoundingClientRect();
      if (event.target === dialog && (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom)) dialog.close();
    });
    dialog.addEventListener('close', () => {
      document.body.classList.remove('dialog-open');
      if (trigger) trigger.focus({ preventScroll: true });
    });
  }
})();
