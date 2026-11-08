/* A real Tally embed, loaded only when requested. No answers are stored here. */
(() => {
  const dialog = document.querySelector('.feedback-dialog');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const locale = document.documentElement.lang === 'om' ? 'om' : 'en';
  const config = window.AOB_FEEDBACK?.[locale];
  const configured = Boolean(config?.enabled === true && typeof config.formId === 'string' && /^[a-zA-Z0-9]+$/.test(config.formId));
  const host = dialog.querySelector('.feedback-embed');
  const status = dialog.querySelector('.feedback-status');
  const unavailable = dialog.querySelector('.feedback-unavailable');
  const fallback = dialog.querySelector('.feedback-fallback');
  const retry = dialog.querySelector('.feedback-retry');
  const success = dialog.querySelector('.feedback-success');
  const languageNote = dialog.querySelector('.feedback-language-note');
  const closeButton = dialog.querySelector('.feedback-close');
  let frame;
  let timeout;
  let trigger;
  let submitted = false;

  function setStatus(key) {
    status.textContent = dialog.querySelector(`[data-feedback-message="${key}"]`).textContent;
  }

  function clearFrame() {
    window.clearTimeout(timeout);
    frame?.remove();
    frame = undefined;
    host.setAttribute('aria-busy', 'false');
  }

  function loadForm() {
    clearFrame();
    host.hidden = false;
    host.setAttribute('aria-busy', 'true');
    retry.hidden = true;
    setStatus('loading');
    const embedURL = new URL(`https://tally.so/embed/${config.formId}`);
    embedURL.search = new URLSearchParams({ alignLeft: '1', hideTitle: '1' }).toString();
    frame = document.createElement('iframe');
    frame.title = dialog.querySelector('[data-feedback-message="frameTitle"]').textContent;
    frame.referrerPolicy = 'no-referrer';
    // Direct iframe embedding deliberately avoids the widget's forwarding of
    // host-page query parameters. A neutral Tally surface preserves legibility.
    frame.src = embedURL.href;
    frame.addEventListener('error', () => {
      window.clearTimeout(timeout);
      host.setAttribute('aria-busy', 'false');
      setStatus('failed');
      retry.hidden = false;
    });
    host.append(frame);
    timeout = window.setTimeout(() => {
      host.setAttribute('aria-busy', 'false');
      setStatus('slow');
      retry.hidden = false;
    }, 15000);
  }

  document.querySelectorAll('[data-feedback]').forEach(link => {
    link.setAttribute('aria-haspopup', 'dialog');
    link.setAttribute('aria-controls', 'feedback-dialog');
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      if (dialog.open) return;
      // Collapse mobile navigation before recording/restoring a visible trigger.
      const menu = document.querySelector('.menu-toggle');
      if (menu.getAttribute('aria-expanded') === 'true') menu.click();
      trigger = link.closest('.site-nav') && menu.offsetParent !== null ? menu : link;
      submitted = false;
      success.hidden = true;
      unavailable.hidden = configured;
      fallback.hidden = !configured;
      languageNote.hidden = !configured || locale !== 'om';
      host.hidden = !configured;
      retry.hidden = true;
      status.textContent = '';
      dialog.showModal();
      dialog.scrollTop = 0;
      document.body.classList.add('dialog-open');
      closeButton.focus();
      if (configured) {
        dialog.querySelector('.feedback-direct').href = `https://tally.so/r/${config.formId}`;
        loadForm();
      }
    });
  });

  retry.addEventListener('click', loadForm);
  closeButton.addEventListener('click', () => dialog.close());
  dialog.querySelector('.feedback-done').addEventListener('click', () => dialog.close());
  // Native modal semantics keep background controls inert and handle Escape.
  // Deliberately do not dismiss on backdrop clicks: they can lose an unfinished report.
  dialog.addEventListener('close', () => {
    clearFrame();
    document.body.classList.remove('dialog-open');
    trigger?.focus({ preventScroll: true });
  });

  window.addEventListener('message', event => {
    if (!dialog.open || !frame || submitted || event.origin !== 'https://tally.so' || event.source !== frame.contentWindow) return;
    let message;
    try { message = typeof event.data === 'string' ? JSON.parse(event.data) : event.data; }
    catch { return; } // Unrelated or malformed cross-window messages are not form events.
    if (!message || message.payload?.formId !== config.formId) return;
    if (message.event === 'Tally.FormLoaded') {
      window.clearTimeout(timeout);
      host.setAttribute('aria-busy', 'false');
      setStatus('ready');
      retry.hidden = true;
    }
    if (message.event === 'Tally.FormSubmitted' && typeof message.payload.id === 'string' && message.payload.id.length > 0) {
      submitted = true;
      clearFrame();
      host.hidden = true;
      fallback.hidden = true;
      languageNote.hidden = true;
      retry.hidden = true;
      status.textContent = '';
      success.hidden = false;
      success.querySelector('h3').focus();
    }
  });
})();
