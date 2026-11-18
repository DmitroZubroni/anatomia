// Presentation-only select adapter. Existing quiz change handler and data stay intact.
document.addEventListener('DOMContentLoaded', () => {
  const tabs = [...document.querySelectorAll('.nav-tab')];
  function syncNavigation() {
    tabs.forEach(tab => {
      const selected = tab.classList.contains('active');
      tab.setAttribute('aria-selected', String(selected));
      tab.tabIndex = selected ? 0 : -1;
    });
    document.getElementById('burgerBtn').setAttribute('aria-expanded', String(document.getElementById('sidebar').classList.contains('open')));
    document.querySelectorAll('.layer-btn').forEach(button => button.setAttribute('aria-pressed', String(button.classList.contains('active'))));
  }
  tabs.forEach((tab, index) => tab.addEventListener('keydown', event => {
    if (!['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(event.key)) return;
    event.preventDefault();
    event.stopPropagation();
    const next = event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length - 1 : (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
    tabs[next].click();
    tabs[next].focus();
  }));
  const observer = new MutationObserver(syncNavigation);
  document.querySelectorAll('.nav-tab, .layer-btn, #sidebar').forEach(element => observer.observe(element, { attributes: true, attributeFilter: ['class'] }));
  syncNavigation();
  const source = document.getElementById('quizSectionSelect');
  const trigger = document.getElementById('quizSectionTrigger');
  const list = document.getElementById('quizSectionOptions');
  let active = 0;
  function close() {
    list.hidden = true;
    trigger.setAttribute('aria-expanded', 'false');
    trigger.removeAttribute('aria-activedescendant');
  }
  function highlight(index) {
    const options = [...list.children];
    active = Math.max(0, Math.min(options.length - 1, index));
    options.forEach((option, i) => option.classList.toggle('highlighted', i === active));
    if (options[active]) {
      trigger.setAttribute('aria-activedescendant', options[active].id);
      options[active].scrollIntoView({ block: 'nearest' });
    }
  }
  function choose(index) {
    source.selectedIndex = index;
    trigger.querySelector('span').textContent = source.options[index].textContent;
    close();
    trigger.focus();
    source.dispatchEvent(new Event('change', { bubbles: true }));
  }
  function open() {
    list.replaceChildren();
    [...source.options].forEach((option, index) => {
      const item = document.createElement('div');
      item.id = `quizSectionOption-${index}`;
      item.setAttribute('role', 'option');
      item.setAttribute('aria-selected', String(index === source.selectedIndex));
      item.textContent = option.textContent;
      item.addEventListener('click', () => choose(index));
      list.append(item);
    });
    const rect = trigger.getBoundingClientRect();
    const nav = document.querySelector('.header-nav');
    const bottomLimit = matchMedia('(max-width: 900px)').matches
      ? innerHeight - nav.getBoundingClientRect().top + 8
      : 16;
    const below = innerHeight - rect.bottom - bottomLimit;
    const above = rect.top - 16;
    const upwards = below < 220 && above > below;
    list.style.left = `${Math.max(8, Math.min(rect.left, innerWidth - rect.width - 8))}px`;
    list.style.width = `${Math.min(rect.width, innerWidth - 16)}px`;
    list.style.maxHeight = `${Math.min(320, upwards ? above : below)}px`;
    list.style.top = upwards ? 'auto' : `${rect.bottom + 4}px`;
    list.style.bottom = upwards ? `${innerHeight - rect.top + 4}px` : 'auto';
    list.hidden = false;
    trigger.setAttribute('aria-expanded', 'true');
    highlight(source.selectedIndex);
  }
  trigger.addEventListener('click', () => list.hidden ? open() : close());
  trigger.addEventListener('keydown', event => {
    if (event.key === 'Escape' || event.key === 'Tab') { close(); return; }
    if (!['ArrowDown', 'ArrowUp', 'Home', 'End', 'Enter', ' '].includes(event.key)) return;
    event.preventDefault();
    event.stopPropagation();
    if (list.hidden) { open(); return; }
    if (event.key === 'Enter' || event.key === ' ') choose(active);
    else highlight(event.key === 'Home' ? 0 : event.key === 'End' ? source.options.length - 1 : active + (event.key === 'ArrowDown' ? 1 : -1));
  });
  document.addEventListener('pointerdown', event => {
    if (!list.contains(event.target) && !trigger.contains(event.target)) close();
  });
  window.addEventListener('resize', close);
  document.getElementById('mainStage').addEventListener('scroll', close);
  source.hidden = true;
  trigger.hidden = false;
});
