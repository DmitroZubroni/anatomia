# -*- coding: utf-8 -*-
"""
Studio «Калибр» — Redesign Generator for Anatomical Atlas
Style: Editorial Academic Atlas (Crimson & Bone)
Strict compliance: Rules Ц1-Ц8, У1, Т10, Д1, Д2, WCAG 2.2 AA
"""

import sys

with open('/Users/atlant/Projects/myProjects/anatomia/index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

pos_qd = orig.find('const QD = ')
pos_func = orig.find('// ── ПРАВИЛО Т10')
if pos_func == -1:
    pos_func = orig.find('function initAnatTheme()')

if pos_qd == -1 or pos_func == -1:
    print("Error: Could not locate data block in index.html")
    sys.exit(1)

data_block = orig[pos_qd:pos_func].strip()

html_content = """<!DOCTYPE html>
<html lang="ru" class="light-theme">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<meta name="theme-color" content="#991b1b">
<meta name="description" content="Интерактивный анатомический атлас и экзаменационная система по анатомии и физиологии человека. Студия «Калибр».">
<title>Анатомический Атлас — Экзамен и Интерактивные Системы</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=JetBrains+Mono:wght@400;600&family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&display=swap" rel="stylesheet">

<style>
/* ── СТУДИЯ «КАЛИБР»: ДИЗАЙН-ТОКЕНЫ EDITORIAL ACADEMIC ATLAS ── */
:root {
  /* Светлая тема по умолчанию (Bone & Crimson / Слоновая кость и кармин) */
  --bg: #fdfbf7;
  --surface: #ffffff;
  --surface-2: #f7f2ea;
  --surface-3: #efe8dc;
  --surface-glass: rgba(255, 255, 255, 0.88);
  --border: #e6ded1;
  --border-subtle: #f0e9dd;
  --border-focus: #991b1b;
  --field-border: #8c827a;

  /* Бренд: Академический багровый / Кармин */
  --primary: #991b1b;
  --primary-hover: #7f1d1d;
  --primary-soft: #fef2f2;
  --primary-border: #fca5a5;
  --on-primary: #ffffff;

  /* Акценты по правилу Ц8 */
  --accent: #991b1b;
  --accent-text: #991b1b;
  --accent-soft: #fee2e2;
  --on-accent: #ffffff;

  /* Статусы уверенности (WCAG 2.2 AA) */
  --know: #15803d;
  --know-bg: #f0fdf4;
  --know-border: #bbf7d0;
  --know-text: #166534;
  --unsure: #b45309;
  --unsure-bg: #fffbeb;
  --unsure-border: #fde68a;
  --unsure-text: #92400e;
  --noknow: #991b1b;
  --noknow-bg: #fef2f2;
  --noknow-border: #fecaca;
  --noknow-text: #7f1d1d;

  /* Ошибки и предупреждения */
  --danger: #991b1b;
  --danger-soft: #fef2f2;
  --danger-border: #fca5a5;
  --danger-text: #991b1b;

  /* Типографика (Контраст к фону > 16:1) */
  --text: #1c1917;
  --text-muted: #57534e;
  --text-dim: #78716c;

  --font-serif: 'Playfair Display', 'Cormorant Garamond', Georgia, serif;
  --font-sans: 'Manrope', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;

  --radius-xs: 4px;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-pill: 9999px;

  --shadow-sm: 0 1px 3px rgba(28,25,23,0.06);
  --shadow-md: 0 4px 14px rgba(28,25,23,0.08);
  --shadow-lg: 0 14px 32px rgba(28,25,23,0.12);

  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --header-height: 58px;
  --sidebar-width: 310px;
}

/* ── ТЁМНАЯ ТЕМА: CHARCOAL NOCTURNE (Правило Ц7, Ц8) ── */
.dark-theme {
  --bg: #141212;
  --surface: #1c1917;
  --surface-2: #262220;
  --surface-3: #332d2a;
  --surface-glass: rgba(28, 25, 23, 0.9);
  --border: #38312d;
  --border-subtle: #2b2522;
  --border-focus: #f87171;
  --field-border: #6e645c;

  --primary: #dc2626;
  --primary-hover: #ef4444;
  --primary-soft: rgba(220, 38, 38, 0.16);
  --primary-border: rgba(220, 38, 38, 0.4);
  --on-primary: #ffffff;

  --accent: #f87171;
  --accent-text: #fca5a5;
  --accent-soft: rgba(248, 113, 113, 0.14);
  --on-accent: #1c1917;

  --know: #34d399;
  --know-bg: rgba(52, 211, 153, 0.14);
  --know-border: rgba(52, 211, 153, 0.4);
  --know-text: #6ee7b7;
  --unsure: #fbbf24;
  --unsure-bg: rgba(251, 191, 36, 0.14);
  --unsure-border: rgba(251, 191, 36, 0.4);
  --unsure-text: #fde68a;
  --noknow: #f87171;
  --noknow-bg: rgba(248, 113, 113, 0.14);
  --noknow-border: rgba(248, 113, 113, 0.4);
  --noknow-text: #fca5a5;

  --danger: #f87171;
  --danger-soft: rgba(248, 113, 113, 0.16);
  --danger-border: rgba(248, 113, 113, 0.4);
  --danger-text: #fca5a5;

  --text: #f5f0ea;
  --text-muted: #b8b0a2;
  --text-dim: #877f72;

  --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 14px rgba(0,0,0,0.4);
  --shadow-lg: 0 14px 32px rgba(0,0,0,0.5);
}

/* ── БАЗОВАЯ РАЗМЕТКА И ТИПОГРАФИКА (Т10, С5) ── */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  -webkit-tap-highlight-color: transparent;
}

html, body {
  height: 100%;
  overflow: hidden;
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-sans);
  font-size: 15px;
  line-height: 1.6;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  transition: background-color 0.25s ease, color 0.25s ease;
}

:where(p, li, dd, td, th, blockquote, figcaption) {
  overflow-wrap: break-word;
  hyphens: auto;
}

:where(h1, h2, h3, h4, h5, h6) {
  overflow-wrap: break-word;
  font-family: var(--font-serif);
  font-weight: 700;
  line-height: 1.25;
}

/* Доступность: WCAG 2.2 AA (Д2, Д8) */
:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: 2px;
  border-radius: var(--radius-xs);
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* ── ШАПКА (HEADER) — ОПТИМИЗИРОВАННЫЙ БАДЖЕТ ПРОСТРАНСТВА ── */
.header {
  position: fixed;
  top: 0; left: 0; right: 0;
  height: var(--header-height);
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 200;
  box-shadow: var(--shadow-sm);
  gap: 6px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.hamburger-btn {
  display: flex;
  width: 38px;
  height: 38px;
  background: none;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  cursor: pointer;
  padding: 8px;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  transition: background-color 0.15s ease, border-color 0.15s ease;
  flex-shrink: 0;
}
.hamburger-btn:hover {
  background: var(--surface-2);
}
.hamburger-btn span {
  display: block;
  width: 18px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.2s ease, opacity 0.2s ease;
}
.hamburger-btn.active span:nth-child(1) { transform: translateY(5px) rotate(45deg); }
.hamburger-btn.active span:nth-child(2) { opacity: 0; }
.hamburger-btn.active span:nth-child(3) { transform: translateY(-5px) rotate(-45deg); }

.brand-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  text-decoration: none;
  color: inherit;
  flex-shrink: 0;
}
.brand-crest {
  width: 28px;
  height: 28px;
  border-radius: var(--radius-sm);
  background: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--on-primary);
  font-family: var(--font-serif);
  font-size: 15px;
  font-weight: 800;
  box-shadow: 0 2px 5px rgba(153, 27, 27, 0.25);
  flex-shrink: 0;
}
.brand-title {
  display: flex;
  flex-direction: column;
}
.brand-name {
  font-family: var(--font-serif);
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--text);
  white-space: nowrap;
}
.brand-name span {
  color: var(--primary);
}
.brand-sub {
  font-size: 9px;
  font-family: var(--font-mono);
  color: var(--text-dim);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Навигация вкладками (Tabs) */
.header-nav {
  display: flex;
  align-items: center;
  gap: 2px;
  flex-shrink: 1;
}
.nav-tab {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  height: 36px;
  padding: 0 8px;
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 13px;
  font-weight: 600;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 0.15s ease;
  white-space: nowrap;
  font-family: inherit;
}
.nav-tab:hover {
  background: var(--surface-2);
  color: var(--text);
}
.nav-tab.active {
  background: var(--primary-soft);
  color: var(--primary);
  font-weight: 700;
  box-shadow: inset 0 0 0 1px var(--primary-border);
}
.nav-tab svg {
  width: 15px;
  height: 15px;
  fill: currentColor;
}

/* Правый блок шапки: Прогресс, Тема, Демо-состояния */
.header-right {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-shrink: 0;
}

.study-progress-card {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 3px 7px;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--radius-pill);
}
.study-progress-bar {
  width: 40px;
  height: 5px;
  background: var(--border);
  border-radius: 3px;
  overflow: hidden;
}
.study-progress-fill {
  height: 100%;
  background: var(--primary);
  border-radius: 3px;
  transition: width 0.3s ease;
}
.study-progress-text {
  font-size: 11px;
  font-family: var(--font-mono);
  font-weight: 600;
  color: var(--text);
}

.state-switcher {
  display: flex;
  align-items: center;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 2px;
  gap: 1px;
}
.state-pill {
  height: 26px;
  padding: 0 5px;
  font-size: 11px;
  font-weight: 600;
  border: none;
  background: transparent;
  color: var(--text-muted);
  border-radius: var(--radius-xs);
  cursor: pointer;
  transition: all 0.15s ease;
  white-space: nowrap;
}
.state-pill:hover {
  color: var(--text);
}
.state-pill.active {
  background: var(--surface);
  color: var(--text);
  box-shadow: var(--shadow-sm);
}

.icon-btn {
  width: 36px;
  height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--surface);
  color: var(--text);
  cursor: pointer;
  transition: all 0.15s ease;
  flex-shrink: 0;
}
.icon-btn:hover {
  background: var(--surface-2);
  border-color: var(--border-focus);
}
.icon-btn svg {
  width: 16px;
  height: 16px;
  fill: currentColor;
}

/* ── БОКОВАЯ ПАНЕЛЬ (SIDEBAR): РЕЖИМНО-ЗАВИСИМАЯ ── */
.sidebar {
  position: fixed;
  top: var(--header-height);
  bottom: 0;
  left: 0;
  width: var(--sidebar-width);
  background: var(--surface);
  border-right: 1px solid var(--border);
  overflow-y: auto;
  z-index: 150;
  transform: translateX(-100%);
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}
.sidebar.open {
  transform: translateX(0);
  box-shadow: var(--shadow-lg);
}

.sidebar-search-wrap {
  padding: 10px 12px;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 10;
}
.sidebar-search-box {
  position: relative;
  display: flex;
  align-items: center;
}
.sidebar-search-icon {
  position: absolute;
  left: 10px;
  width: 15px;
  height: 15px;
  fill: var(--text-dim);
  pointer-events: none;
}
.sidebar-search-input {
  width: 100%;
  height: 40px;
  padding: 0 32px 0 34px;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  color: var(--text);
  font-size: 13px;
  font-family: inherit;
  outline: none;
  transition: border-color 0.15s ease, background 0.15s ease;
}
.sidebar-search-input:focus {
  border-color: var(--border-focus);
  background: var(--surface);
}
.sidebar-search-clear {
  position: absolute;
  right: 8px;
  width: 22px;
  height: 22px;
  display: none;
  align-items: center;
  justify-content: center;
  border: none;
  background: none;
  color: var(--text-dim);
  cursor: pointer;
  border-radius: 50%;
}
.sidebar-search-clear:hover {
  background: var(--border);
  color: var(--text);
}

.sidebar-content {
  flex: 1;
  padding: 8px 6px calc(24px + var(--safe-bottom));
  overflow-y: auto;
}

/* Разделы и элементы в сайдбаре */
.sec-group {
  margin-bottom: 10px;
}
.sec-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 7px 9px;
  background: var(--surface-2);
  border-radius: var(--radius-sm);
  cursor: pointer;
  user-select: none;
  transition: background-color 0.15s ease;
}
.sec-header:hover {
  background: var(--surface-3);
}
.sec-header-title {
  font-size: 12px;
  font-weight: 700;
  color: var(--text);
  line-height: 1.3;
  flex: 1;
}
.sec-header-stat {
  font-size: 11px;
  font-family: var(--font-mono);
  font-weight: 600;
  color: var(--text-dim);
  margin-left: 6px;
  white-space: nowrap;
}
.sec-progress-bar {
  height: 3px;
  background: var(--border);
  border-radius: 2px;
  margin: 3px 8px 6px;
  overflow: hidden;
}
.sec-progress-fill {
  height: 100%;
  background: var(--primary);
  border-radius: 2px;
  transition: width 0.3s ease;
}

.q-list-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 10px;
  min-height: 42px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-size: 13px;
  line-height: 1.4;
  color: var(--text-muted);
  transition: all 0.15s ease;
  margin-bottom: 2px;
}
.q-list-item:hover {
  background: var(--surface-2);
  color: var(--text);
}
.q-list-item.active {
  background: var(--primary-soft);
  color: var(--primary);
  font-weight: 600;
  box-shadow: inset 0 0 0 1px var(--primary-border);
}

.status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--border);
  flex-shrink: 0;
  transition: background-color 0.2s ease;
}
.q-list-item.know .status-dot { background: var(--know); box-shadow: 0 0 6px var(--know); }
.q-list-item.unsure .status-dot { background: var(--unsure); }
.q-list-item.noknow .status-dot { background: var(--noknow); }

.q-number-badge {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-dim);
  min-width: 18px;
  text-align: right;
  flex-shrink: 0;
}
.q-list-item.active .q-number-badge {
  color: var(--primary);
  font-weight: 700;
}

/* ── ОСНОВНАЯ ОБЛАСТЬ (MAIN STAGE) ── */
.main-stage {
  position: fixed;
  top: var(--header-height);
  bottom: 0;
  left: 0;
  right: 0;
  overflow-y: auto;
  padding: 20px 24px calc(40px + var(--safe-bottom));
  background: var(--bg);
  transition: left 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

/* В Вопросах и Задачах сайдбар закреплен на широких экранах */
@media (min-width: 901px) {
  body.mode-questions .sidebar,
  body.mode-tasks .sidebar {
    display: flex;
    transform: translateX(0);
  }
  body.mode-questions .main-stage,
  body.mode-tasks .main-stage {
    left: var(--sidebar-width);
  }

  body:not(.mode-questions):not(.mode-tasks) .sidebar:not(.open) {
    transform: translateX(-100%);
  }
  body:not(.mode-questions):not(.mode-tasks) .main-stage {
    left: 0;
  }
}

.overlay-backdrop {
  display: none;
  position: fixed;
  top: var(--header-height);
  left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(2px);
  z-index: 140;
}
.overlay-backdrop.open {
  display: block;
}

/* Панели */
.view-panel {
  display: none;
  animation: panelFade 0.2s ease-out;
  max-width: 1100px;
  margin: 0 auto;
}
.view-panel.active {
  display: block;
}
@keyframes panelFade {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ── 4 СОСТОЯНИЯ ЭКРАНА (ПРАВИЛО У1): EMPTY, LOADING, ERROR, SUCCESS ── */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  text-align: center;
  background: var(--surface);
  border: 1px dashed var(--border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  max-width: 650px;
  margin: 30px auto;
}
.empty-state-icon {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--primary-soft);
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 18px;
}
.empty-state-icon svg {
  width: 28px;
  height: 28px;
  fill: currentColor;
}
.empty-state-title {
  font-family: var(--font-serif);
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--text);
}
.empty-state-desc {
  font-size: 14px;
  color: var(--text-muted);
  max-width: 440px;
  line-height: 1.5;
  margin-bottom: 20px;
}

/* Состояние ошибки (ErrorState) */
.error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  text-align: center;
  background: var(--surface);
  border: 1px solid var(--danger-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  max-width: 650px;
  margin: 30px auto;
}
.error-state-icon {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--danger-soft);
  color: var(--danger);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 18px;
}
.error-state-icon svg {
  width: 28px;
  height: 28px;
  fill: currentColor;
}
.error-state-title {
  font-family: var(--font-serif);
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--danger-text);
}
.error-state-desc {
  font-size: 14px;
  color: var(--text-muted);
  max-width: 440px;
  line-height: 1.5;
  margin-bottom: 20px;
}

/* Скелетон загрузки (LoadingSkeleton) */
.loading-skeleton {
  padding: 28px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  max-width: 750px;
  margin: 24px auto;
}
.skeleton-line {
  background: linear-gradient(90deg, var(--surface-2) 25%, var(--surface-3) 50%, var(--surface-2) 75%);
  background-size: 200% 100%;
  animation: skeletonPulse 1.5s infinite;
  border-radius: var(--radius-xs);
  margin-bottom: 12px;
}
@keyframes skeletonPulse {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* ── ИНТЕРАКТИВНЫЙ АНАТОМИЧЕСКИЙ АТЛАС (АТЛАС & СИСТЕМЫ) ── */
.atlas-view-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.atlas-toolbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 12px 16px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
}

.atlas-layers-title {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-dim);
  font-family: var(--font-mono);
}

.atlas-layer-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.layer-btn {
  height: 34px;
  padding: 0 11px;
  border: 1px solid var(--border);
  background: var(--surface-2);
  color: var(--text-muted);
  font-size: 13px;
  font-weight: 600;
  border-radius: var(--radius-pill);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  transition: all 0.15s ease;
  font-family: inherit;
}
.layer-btn:hover {
  background: var(--surface-3);
  color: var(--text);
}
.layer-btn.active {
  background: var(--primary);
  border-color: var(--primary);
  color: var(--on-primary);
  box-shadow: 0 2px 6px rgba(153, 27, 27, 0.25);
}

.atlas-canvas-card {
  position: relative;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 18px;
  box-shadow: var(--shadow-md);
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 18px;
  min-height: 540px;
}
@media (max-width: 900px) {
  .atlas-canvas-card {
    grid-template-columns: 1fr;
  }
}

.atlas-svg-stage {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  background: radial-gradient(circle at center, var(--surface-2) 0%, var(--surface) 75%);
  border-radius: var(--radius-md);
  border: 1px solid var(--border-subtle);
  overflow: hidden;
  min-height: 460px;
}

.atlas-svg-stage svg {
  width: 100%;
  height: auto;
  max-height: 520px;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,0.06));
}

/* Интерактивные узлы атласа */
.anat-node {
  cursor: pointer;
  transition: transform 0.2s ease, opacity 0.2s ease, stroke-width 0.2s ease;
}
.anat-node:hover {
  filter: drop-shadow(0 0 8px var(--primary));
  opacity: 1 !important;
}
.anat-node.selected {
  filter: drop-shadow(0 0 12px var(--primary));
}
.anat-pulse-ring {
  animation: pulseNode 2s infinite ease-out;
  transform-origin: center;
}
@keyframes pulseNode {
  0% { transform: scale(0.9); opacity: 0.8; }
  50% { transform: scale(1.15); opacity: 0.3; }
  100% { transform: scale(0.9); opacity: 0.8; }
}

/* Карточка органа / досье (Academic Organ Dossier) */
.organ-dossier-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 18px;
}
.dossier-header {
  border-bottom: 1px solid var(--border);
  padding-bottom: 10px;
  margin-bottom: 10px;
}
.dossier-latin {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 13.5px;
  color: var(--primary);
  margin-bottom: 3px;
}
.dossier-name {
  font-family: var(--font-serif);
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
  line-height: 1.25;
}
.dossier-section-badge {
  display: inline-block;
  margin-top: 5px;
  font-size: 11px;
  font-family: var(--font-mono);
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 2px 7px;
  border-radius: var(--radius-pill);
  color: var(--text-dim);
}
.dossier-body {
  flex: 1;
  font-size: 13.5px;
  color: var(--text-muted);
  line-height: 1.55;
}
.dossier-clinical {
  margin-top: 12px;
  padding: 8px 10px;
  background: var(--surface);
  border-left: 3px solid var(--primary);
  border-radius: 0 var(--radius-xs) var(--radius-xs) 0;
  font-size: 12.5px;
  color: var(--text);
}
.dossier-clinical strong {
  color: var(--primary);
}
.dossier-action {
  margin-top: 16px;
}

/* ── ВОПРОСЫ И ОТВЕТЫ (Q-CARD) ── */
.q-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 28px;
  box-shadow: var(--shadow-md);
}
.q-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
  flex-wrap: wrap;
  gap: 8px;
}
.q-breadcrumb {
  font-size: 13px;
  color: var(--text-dim);
  font-family: var(--font-mono);
  display: flex;
  align-items: center;
  gap: 6px;
}
.q-conf-indicator {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 600;
  padding: 3px 9px;
  border-radius: var(--radius-pill);
}
.q-conf-indicator.know { background: var(--know-bg); color: var(--know-text); border: 1px solid var(--know-border); }
.q-conf-indicator.unsure { background: var(--unsure-bg); color: var(--unsure-text); border: 1px solid var(--unsure-border); }
.q-conf-indicator.noknow { background: var(--noknow-bg); color: var(--noknow-text); border: 1px solid var(--noknow-border); }

.q-title {
  font-family: var(--font-serif);
  font-size: 23px;
  font-weight: 700;
  color: var(--text);
  line-height: 1.35;
  margin-bottom: 22px;
  letter-spacing: -0.01em;
}

.q-nav-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  margin-bottom: 22px;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 40px;
  padding: 0 16px;
  border-radius: var(--radius-sm);
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
  font-family: inherit;
  border: 1px solid transparent;
}
.btn-primary {
  background: var(--primary);
  color: var(--on-primary);
  box-shadow: 0 2px 8px rgba(153, 27, 27, 0.25);
}
.btn-primary:hover {
  background: var(--primary-hover);
}
.btn-secondary {
  background: var(--surface-2);
  border-color: var(--border);
  color: var(--text);
}
.btn-secondary:hover {
  background: var(--surface-3);
  border-color: var(--field-border);
}

/* Область ответа */
.answer-wrapper {
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  margin-bottom: 24px;
  overflow: hidden;
  transition: all 0.25s ease;
}
.answer-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 11px 16px;
  background: var(--surface-3);
  border-bottom: 1px solid var(--border);
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
}
.answer-body {
  padding: 22px;
  font-size: 15.5px;
  line-height: 1.68;
  color: var(--text);
}
.answer-body.hidden-state {
  color: var(--text-dim);
  font-style: italic;
  text-align: center;
  padding: 36px 20px;
}
.answer-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  font-size: 13.5px;
}
.answer-body th, .answer-body td {
  border: 1px solid var(--border);
  padding: 9px 12px;
  text-align: left;
}
.answer-body th {
  background: var(--surface-3);
  font-weight: 700;
}
.answer-body ul, .answer-body ol {
  margin: 10px 0 10px 22px;
}
.answer-body li {
  margin-bottom: 5px;
}
.answer-body strong {
  color: var(--text);
  font-weight: 700;
}

/* Кнопки уверенности (Confidence Buttons) */
.conf-selector-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}
@media (max-width: 600px) {
  .conf-selector-row {
    grid-template-columns: 1fr;
  }
}
.conf-choice-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  min-height: 46px;
  padding: 0 14px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  background: var(--surface);
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
  color: var(--text-muted);
}
.conf-choice-btn:hover {
  background: var(--surface-2);
  color: var(--text);
}
.conf-choice-btn.noknow.active {
  background: var(--noknow-bg);
  border-color: var(--noknow-border);
  color: var(--noknow-text);
  font-weight: 700;
}
.conf-choice-btn.unsure.active {
  background: var(--unsure-bg);
  border-color: var(--unsure-border);
  color: var(--unsure-text);
  font-weight: 700;
}
.conf-choice-btn.know.active {
  background: var(--know-bg);
  border-color: var(--know-border);
  color: var(--know-text);
  font-weight: 700;
}

/* ── ТЕСТЫ И КВИЗЫ (QUIZ VIEW) ── */
.quiz-container {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.quiz-top-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 14px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  box-shadow: var(--shadow-sm);
}
.quiz-sec-select {
  height: 40px;
  padding: 0 12px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--surface-2);
  color: var(--text);
  font-size: 13px;
  font-family: inherit;
  outline: none;
  min-width: 200px;
}
.quiz-sec-select:focus {
  border-color: var(--border-focus);
}

.quiz-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px;
  box-shadow: var(--shadow-sm);
  margin-bottom: 12px;
}
.quiz-card-q {
  font-size: 15.5px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 14px;
  line-height: 1.5;
}
.quiz-options-list {
  display: flex;
  flex-direction: column;
  gap: 7px;
}
.quiz-option-btn {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 10px 14px;
  min-height: 42px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--surface-2);
  color: var(--text);
  font-size: 13.5px;
  text-align: left;
  cursor: pointer;
  transition: all 0.15s ease;
  font-family: inherit;
}
.quiz-option-btn:hover:not(:disabled) {
  background: var(--surface-3);
  border-color: var(--field-border);
}
.quiz-option-btn.correct {
  background: var(--know-bg);
  border-color: var(--know-border);
  color: var(--know-text);
  font-weight: 700;
}
.quiz-option-btn.wrong {
  background: var(--noknow-bg);
  border-color: var(--noknow-border);
  color: var(--noknow-text);
}
.quiz-explanation {
  margin-top: 12px;
  padding: 10px 14px;
  background: var(--surface-2);
  border-left: 3px solid var(--primary);
  border-radius: 0 var(--radius-xs) var(--radius-xs) 0;
  font-size: 12.5px;
  color: var(--text-muted);
  line-height: 1.5;
}

/* ── СТАТИСТИКА (STATS VIEW) ── */
.stats-overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 14px;
  margin-bottom: 18px;
}
.stat-metric-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px;
  box-shadow: var(--shadow-sm);
  text-align: center;
}
.stat-metric-num {
  font-family: var(--font-serif);
  font-size: 34px;
  font-weight: 800;
  color: var(--primary);
  line-height: 1;
  margin-bottom: 6px;
}
.stat-metric-label {
  font-size: 12.5px;
  color: var(--text-muted);
  font-weight: 600;
}

.stats-section-row {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 12px 16px;
  margin-bottom: 8px;
}
.stats-sec-title-row {
  display: flex;
  justify-content: space-between;
  font-size: 13.5px;
  font-weight: 600;
  margin-bottom: 7px;
}
.stats-seg-bar {
  display: flex;
  height: 7px;
  border-radius: 4px;
  overflow: hidden;
  background: var(--border);
  margin-bottom: 7px;
}
.stats-seg-know { background: var(--know); }
.stats-seg-unsure { background: var(--unsure); }
.stats-seg-noknow { background: var(--noknow); }
.stats-breakdown-badges {
  display: flex;
  gap: 10px;
  font-size: 11.5px;
  font-family: var(--font-mono);
  color: var(--text-dim);
}

/* ── АДАПТИВНОСТЬ (С5, Д1: 320, 375, 768, 1024, 1280, 1440 px) ── */
@media (max-width: 900px) {
  .sidebar {
    width: min(310px, 85vw);
  }
  .main-stage {
    left: 0 !important;
    padding: 16px 12px calc(32px + var(--safe-bottom));
  }
  .header-nav .nav-tab span {
    display: none;
  }
  .header-nav .nav-tab {
    padding: 0 7px;
  }
}

@media (max-width: 640px) {
  .study-progress-card { display: none; }
  .q-title { font-size: 19px; }
  .q-card { padding: 16px; }
}
</style>
</head>

<body class="mode-atlas">

<!-- ВЕРХНЯЯ ПАНЕЛЬ (HEADER) -->
<header class="header">
  <div class="header-left">
    <button class="hamburger-btn" id="burgerBtn" onclick="toggleSidebar()" aria-label="Открыть оглавление атласа">
      <span></span><span></span><span></span>
    </button>
    <a href="#" class="brand-badge" onclick="switchMainTab('atlas'); return false;">
      <div class="brand-crest">К</div>
      <div class="brand-title">
        <div class="brand-name">Атлас <span>Анатомии</span></div>
        <div class="brand-sub">Калибр • Academic Ed.</div>
      </div>
    </a>
  </div>

  <nav class="header-nav" role="tablist" aria-label="Разделы атласа">
    <button class="nav-tab active" id="tabAtlas" onclick="switchMainTab('atlas')" role="tab" aria-selected="true">
      <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
      <span>🏛️ Атлас</span>
    </button>
    <button class="nav-tab" id="tabQuestions" onclick="switchMainTab('questions')" role="tab" aria-selected="false">
      <svg viewBox="0 0 24 24"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/></svg>
      <span>📚 Вопросы</span>
    </button>
    <button class="nav-tab" id="tabTasks" onclick="switchMainTab('tasks')" role="tab" aria-selected="false">
      <svg viewBox="0 0 24 24"><path d="M7 2v2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-2V2H7zm10 4v2H7V6h10z"/></svg>
      <span>🔬 Задачи</span>
    </button>
    <button class="nav-tab" id="tabQuiz" onclick="switchMainTab('quiz')" role="tab" aria-selected="false">
      <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
      <span>🧪 Тесты</span>
    </button>
    <button class="nav-tab" id="tabStats" onclick="switchMainTab('stats')" role="tab" aria-selected="false">
      <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/></svg>
      <span>📊 Стат.</span>
    </button>
  </nav>

  <div class="header-right">
    <div class="study-progress-card" title="Общий прогресс изучения базы вопросов">
      <div class="study-progress-bar">
        <div class="study-progress-fill" id="gProgressBar" style="width:0%"></div>
      </div>
      <div class="study-progress-text"><span id="gProgressDone">0</span>/<span id="gProgressTotal">0</span></div>
    </div>

    <!-- Переключатель демо-состояний по Правилу Н4 (У1: 4 состояния) -->
    <div class="state-switcher" title="Демо-переключатель состояний экрана (Правило У1)">
      <button class="state-pill active" onclick="setScreenState('success')" id="btnStateSuccess">Норма</button>
      <button class="state-pill" onclick="setScreenState('loading')" id="btnStateLoading">Загрузка</button>
      <button class="state-pill" onclick="setScreenState('error')" id="btnStateError">Ошибка</button>
      <button class="state-pill" onclick="setScreenState('empty')" id="btnStateEmpty">Пусто</button>
    </div>

    <!-- Переключатель темы (Ц7, Ц8) -->
    <button class="icon-btn" id="themeBtn" onclick="toggleTheme()" title="Сменить тему (Светлая / Тёмная)" aria-label="Сменить тему оформления">
      <svg id="themeIconSun" viewBox="0 0 24 24"><path d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58c-.39-.39-1.03-.39-1.41 0s-.39 1.03 0 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41L5.99 4.58zm12.37 12.37c-.39-.39-1.03-.39-1.41 0s-.39 1.03 0 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41l-1.06-1.06zm1.06-10.96c.39-.39.39-1.03 0-1.41s-1.03-.39-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06zM7.05 18.36c.39-.39.39-1.03 0-1.41s-1.03-.39-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06z"/></svg>
      <svg id="themeIconMoon" style="display:none" viewBox="0 0 24 24"><path d="M12 3c-4.97 0-9 4.03-9 9s4.03 9 9 9c.83 0 1.5-.67 1.5-1.5 0-.39-.15-.74-.39-1.01-.23-.26-.38-.61-.38-.99 0-.83.67-1.5 1.5-1.5H16c2.76 0 5-2.24 5-5 0-4.42-4.03-8-9-8z"/></svg>
    </button>
  </div>
</header>

<!-- ОВЕРЛЕЙ ДЛЯ МОБИЛЬНЫХ УСТРОЙСТВ -->
<div class="overlay-backdrop" id="overlayBackdrop" onclick="closeSidebar()"></div>

<!-- БОКОВОЕ МЕНЮ (SIDEBAR) -->
<aside class="sidebar" id="sidebar">
  <div class="sidebar-search-wrap">
    <div class="sidebar-search-box">
      <svg class="sidebar-search-icon" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
      <input type="text" class="sidebar-search-input" id="sidebarSearchInput" placeholder="Поиск тем, органов, вопросов…" oninput="handleSearchFilter()">
      <button class="sidebar-search-clear" id="searchClearBtn" onclick="clearSearchFilter()" aria-label="Очистить поиск">✕</button>
    </div>
  </div>
  <div class="sidebar-content" id="sidebarList">
    <!-- Генерируется из QD / TD -->
  </div>
</aside>

<!-- ГЛАВНАЯ СЦЕНА (MAIN STAGE) -->
<main class="main-stage" id="mainStage">

  <!-- 4 СОСТОЯНИЯ: ОБЕРТКА СИСТЕМЫ (У1) -->
  <div id="loadingStateContainer" style="display:none" class="loading-skeleton">
    <div class="skeleton-line" style="height:32px;width:60%"></div>
    <div class="skeleton-line" style="height:18px;width:40%"></div>
    <div class="skeleton-line" style="height:120px;width:100%;margin-top:24px"></div>
    <div class="skeleton-line" style="height:80px;width:100%"></div>
  </div>

  <div id="errorStateContainer" style="display:none" class="error-state">
    <div class="error-state-icon">
      <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>
    </div>
    <div class="error-state-title">Не удалось загрузить данные раздела</div>
    <div class="error-state-desc">Произошла ошибка при обращении к анатомической базе данных. Проверьте параметры запроса и попробуйте восстановить состояние.</div>
    <button class="btn btn-primary" onclick="setScreenState('success')">↻ Повторить попытку</button>
  </div>

  <div id="emptyStateContainer" style="display:none" class="empty-state">
    <div class="empty-state-icon">
      <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
    </div>
    <div class="empty-state-title">Ничего не найдено</div>
    <div class="empty-state-desc">По вашему запросу не найдено ни одного вопроса или анатомической структуры. Попробуйте изменить ключевые слова или сбросить фильтр.</div>
    <button class="btn btn-secondary" onclick="clearSearchFilter()">Сбросить фильтры</button>
  </div>

  <div id="successContentContainer">

    <!-- ПАНЕЛЬ 1: ИНТЕРАКТИВНЫЙ АНАТОМИЧЕСКИЙ АТЛАС (АТЛАС & СИСТЕМЫ) -->
    <div class="view-panel active" id="panelAtlas">
      <div class="atlas-view-container">

        <!-- Панель управления слоями -->
        <div class="atlas-toolbar">
          <div class="atlas-layers-title">Анатомические слои:</div>
          <div class="atlas-layer-pills">
            <button class="layer-btn active" id="btnLayerAll" onclick="setAtlasLayer('all')">🏛️ Все системы</button>
            <button class="layer-btn" id="btnLayerSkeleton" onclick="setAtlasLayer('skeleton')">🦴 Скелет</button>
            <button class="layer-btn" id="btnLayerMuscles" onclick="setAtlasLayer('muscles')">💪 Мышцы</button>
            <button class="layer-btn" id="btnLayerCardio" onclick="setAtlasLayer('cardio')">🫀 Сердце &amp; Сосуды</button>
            <button class="layer-btn" id="btnLayerNeuro" onclick="setAtlasLayer('neuro')">🧠 ЦНС &amp; Нейроны</button>
            <button class="layer-btn" id="btnLayerViscera" onclick="setAtlasLayer('viscera')">🫁 Органы</button>
            <button class="layer-btn" id="btnLayerCell" onclick="setAtlasLayer('cell')">🧬 Клетка (Микро)</button>
          </div>
        </div>

        <!-- Интерактивный хост-холст с векторным атласом и карточкой досье -->
        <div class="atlas-canvas-card">
          <div class="atlas-svg-stage">
            <svg id="atlasMainSvg" viewBox="0 0 600 700" fill="none" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <linearGradient id="gradBone" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#fdfbf7"/>
                  <stop offset="100%" stop-color="#e6ded1"/>
                </linearGradient>
                <linearGradient id="gradMuscle" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#b91c1c"/>
                  <stop offset="100%" stop-color="#7f1d1d"/>
                </linearGradient>
                <linearGradient id="gradArtery" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#ef4444"/>
                  <stop offset="100%" stop-color="#b91c1c"/>
                </linearGradient>
                <linearGradient id="gradVein" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#3b82f6"/>
                  <stop offset="100%" stop-color="#1d4ed8"/>
                </linearGradient>
                <linearGradient id="gradNeuro" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#f59e0b"/>
                  <stop offset="100%" stop-color="#d97706"/>
                </linearGradient>
                <filter id="glowNeuro" x="-20%" y="-20%" width="140%" height="140%">
                  <feGaussianBlur stdDeviation="3" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
              </defs>

              <!-- Сетка анатомических координат -->
              <g stroke="var(--border-subtle)" stroke-width="1" stroke-dasharray="4 6" opacity="0.4">
                <line x1="50" y1="100" x2="550" y2="100"/>
                <line x1="50" y1="250" x2="550" y2="250"/>
                <line x1="50" y1="420" x2="550" y2="420"/>
                <line x1="50" y1="600" x2="550" y2="600"/>
                <line x1="300" y1="30" x2="300" y2="670"/>
              </g>

              <!-- СЛОЙ 1: СКЕЛЕТНАЯ СИСТЕМА (ОСТЕОЛОГИЯ) -->
              <g id="layer-skeleton" class="anat-layer">
                <!-- Череп (Cranium) -->
                <path class="anat-node" data-organ="cranium" onclick="selectOrgan('cranium')"
                  d="M 270 70 C 270 45, 330 45, 330 70 C 330 85, 325 105, 300 108 C 275 105, 270 85, 270 70 Z"
                  fill="url(#gradBone)" stroke="var(--text-muted)" stroke-width="2"/>
                <!-- Нижняя челюсть -->
                <path d="M 282 108 Q 300 120 318 108" fill="none" stroke="var(--text-muted)" stroke-width="2"/>
                <!-- Позвоночник (Columna vertebralis) -->
                <path class="anat-node" data-organ="spine" onclick="selectOrgan('spine')"
                  d="M 300 120 L 300 370"
                  stroke="var(--field-border)" stroke-width="10" stroke-linecap="round" stroke-dasharray="4 3"/>
                <!-- Грудная клетка (Thorax / Costae) -->
                <g class="anat-node" data-organ="ribs" onclick="selectOrgan('ribs')" stroke="var(--border)" stroke-width="3" fill="none">
                  <path d="M 270 170 Q 240 180 260 210 Q 285 220 300 220"/>
                  <path d="M 330 170 Q 360 180 340 210 Q 315 220 300 220"/>
                  <path d="M 275 190 Q 235 205 260 235 Q 285 245 300 245"/>
                  <path d="M 325 190 Q 365 205 340 235 Q 315 245 300 245"/>
                  <path d="M 280 210 Q 245 230 265 260 Q 290 270 300 270"/>
                  <path d="M 320 210 Q 355 230 335 260 Q 310 270 300 270"/>
                </g>
                <!-- Грудина (Sternum) -->
                <rect x="295" y="165" width="10" height="90" rx="3" fill="url(#gradBone)" stroke="var(--text-muted)" stroke-width="1.5"/>
                <!-- Тазовый пояс (Pelvis) -->
                <path class="anat-node" data-organ="pelvis" onclick="selectOrgan('pelvis')"
                  d="M 245 350 Q 300 340 355 350 Q 370 380 340 405 Q 300 395 260 405 Q 230 380 245 350 Z"
                  fill="url(#gradBone)" stroke="var(--text-muted)" stroke-width="2"/>
                <!-- Бедренные кости (Femur) -->
                <line x1="260" y1="400" x2="240" y2="540" stroke="url(#gradBone)" stroke-width="8" stroke-linecap="round"/>
                <line x1="340" y1="400" x2="360" y2="540" stroke="url(#gradBone)" stroke-width="8" stroke-linecap="round"/>
                <!-- Коленные чашечки (Patella) -->
                <circle cx="240" cy="545" r="7" fill="url(#gradBone)" stroke="var(--text-muted)" stroke-width="1.5"/>
                <circle cx="360" cy="545" r="7" fill="url(#gradBone)" stroke="var(--text-muted)" stroke-width="1.5"/>
                <!-- Голени (Tibia/Fibula) -->
                <line x1="240" y1="555" x2="235" y2="670" stroke="url(#gradBone)" stroke-width="6" stroke-linecap="round"/>
                <line x1="360" y1="555" x2="365" y2="670" stroke="url(#gradBone)" stroke-width="6" stroke-linecap="round"/>
                <!-- Плечи и руки (Humerus, Radius, Ulna) -->
                <line x1="250" y1="160" x2="200" y2="270" stroke="url(#gradBone)" stroke-width="6" stroke-linecap="round"/>
                <line x1="350" y1="160" x2="400" y2="270" stroke="url(#gradBone)" stroke-width="6" stroke-linecap="round"/>
                <line x1="200" y1="270" x2="175" y2="370" stroke="url(#gradBone)" stroke-width="5" stroke-linecap="round"/>
                <line x1="400" y1="270" x2="425" y2="370" stroke="url(#gradBone)" stroke-width="5" stroke-linecap="round"/>
              </g>

              <!-- СЛОЙ 2: МЫШЕЧНАЯ СИСТЕМА (МИОЛОГИЯ) -->
              <g id="layer-muscles" class="anat-layer">
                <!-- Грудные мышцы (Pectoralis major) -->
                <path class="anat-node" data-organ="pectoralis" onclick="selectOrgan('pectoralis')"
                  d="M 292 175 Q 240 185 245 225 Q 275 235 292 230 Z"
                  fill="url(#gradMuscle)" opacity="0.85" stroke="var(--primary)" stroke-width="1"/>
                <path class="anat-node" data-organ="pectoralis" onclick="selectOrgan('pectoralis')"
                  d="M 308 175 Q 360 185 355 225 Q 325 235 308 230 Z"
                  fill="url(#gradMuscle)" opacity="0.85" stroke="var(--primary)" stroke-width="1"/>
                <!-- Дельтовидные мышцы (Deltoideus) -->
                <path d="M 240 155 Q 220 180 235 210 Q 255 190 250 160 Z" fill="url(#gradMuscle)" opacity="0.8"/>
                <path d="M 360 155 Q 380 180 365 210 Q 345 190 350 160 Z" fill="url(#gradMuscle)" opacity="0.8"/>
                <!-- Брюшной пресс (Rectus abdominis) -->
                <g class="anat-node" data-organ="abdominis" onclick="selectOrgan('abdominis')" fill="url(#gradMuscle)" opacity="0.8">
                  <rect x="282" y="240" width="16" height="24" rx="4"/>
                  <rect x="302" y="240" width="16" height="24" rx="4"/>
                  <rect x="282" y="268" width="16" height="24" rx="4"/>
                  <rect x="302" y="268" width="16" height="24" rx="4"/>
                  <rect x="282" y="296" width="16" height="28" rx="4"/>
                  <rect x="302" y="296" width="16" height="28" rx="4"/>
                </g>
                <!-- Бицепсы (Biceps brachii) -->
                <ellipse cx="215" cy="225" rx="12" ry="24" transform="rotate(-15 215 225)" fill="url(#gradMuscle)" opacity="0.8"/>
                <ellipse cx="385" cy="225" rx="12" ry="24" transform="rotate(15 385 225)" fill="url(#gradMuscle)" opacity="0.8"/>
                <!-- Квадрицепсы (Quadriceps femoris) -->
                <path d="M 250 420 Q 230 480 240 530 Q 260 480 255 420 Z" fill="url(#gradMuscle)" opacity="0.8"/>
                <path d="M 350 420 Q 370 480 360 530 Q 340 480 345 420 Z" fill="url(#gradMuscle)" opacity="0.8"/>
              </g>

              <!-- СЛОЙ 3: СЕРДЕЧНО-СОСУДИСТАЯ СИСТЕМА (АНГИОЛОГИЯ) -->
              <g id="layer-cardio" class="anat-layer">
                <!-- Сердце (Cor / Миокард) -->
                <g class="anat-node" data-organ="cor" onclick="selectOrgan('cor')">
                  <path d="M 300 200 C 300 185, 275 175, 265 195 C 255 215, 280 240, 300 260 C 320 240, 345 215, 335 195 C 325 175, 300 185, 300 200 Z"
                    fill="url(#gradArtery)" stroke="#fff" stroke-width="1.5"/>
                  <circle cx="300" cy="215" r="8" fill="#fff" opacity="0.3" class="anat-pulse-ring"/>
                </g>
                <!-- Дуга аорты (Arcus aortae) -->
                <path class="anat-node" data-organ="aorta" onclick="selectOrgan('aorta')"
                  d="M 298 190 Q 295 160 310 160 Q 320 160 315 190 L 312 360"
                  fill="none" stroke="url(#gradArtery)" stroke-width="4.5" stroke-linecap="round"/>
                <!-- Полые вены (Vena cava) -->
                <path d="M 288 150 L 288 360" fill="none" stroke="url(#gradVein)" stroke-width="4.5" stroke-linecap="round"/>
                <!-- Сонные артерии и яремные вены (Carotid & Jugular) -->
                <line x1="305" y1="160" x2="315" y2="100" stroke="url(#gradArtery)" stroke-width="3"/>
                <line x1="290" y1="160" x2="280" y2="100" stroke="url(#gradVein)" stroke-width="3"/>
                <!-- Подвздошные и бедренные сосуды -->
                <path d="M 312 360 Q 330 400 350 540" fill="none" stroke="url(#gradArtery)" stroke-width="3"/>
                <path d="M 288 360 Q 270 400 250 540" fill="none" stroke="url(#gradVein)" stroke-width="3"/>
              </g>

              <!-- СЛОЙ 4: НЕРВНАЯ СИСТЕМА (НЕВРОЛОГИЯ) -->
              <g id="layer-neuro" class="anat-layer">
                <!-- Головной мозг (Encephalon) -->
                <g class="anat-node" data-organ="brain" onclick="selectOrgan('brain')">
                  <path d="M 275 68 C 275 48, 325 48, 325 68 C 332 82, 320 95, 300 95 C 280 95, 268 82, 275 68 Z"
                    fill="url(#gradNeuro)" filter="url(#glowNeuro)" opacity="0.95"/>
                  <!-- Борозды и извилины коры -->
                  <path d="M 285 62 Q 295 55 305 65 Q 315 58 320 70" fill="none" stroke="#fff" stroke-width="1.5" opacity="0.7"/>
                  <path d="M 280 75 Q 300 72 315 80" fill="none" stroke="#fff" stroke-width="1.5" opacity="0.7"/>
                </g>
                <!-- Спинной мозг (Medulla spinalis) -->
                <line class="anat-node" data-organ="spinal_cord" onclick="selectOrgan('spinal_cord')"
                  x1="300" y1="95" x2="300" y2="360" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round"/>
                <!-- Сплетения и периферические нервы -->
                <path d="M 300 140 Q 250 170 200 270" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
                <path d="M 300 140 Q 350 170 400 270" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
                <path d="M 300 360 Q 270 440 245 580" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
                <path d="M 300 360 Q 330 440 355 580" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
              </g>

              <!-- СЛОЙ 5: ВНУТРЕННИЕ ОРГАНЫ (СПЛАНХНОЛОГИЯ) -->
              <g id="layer-viscera" class="anat-layer">
                <!-- Лёгкие (Pulmones) -->
                <g class="anat-node" data-organ="lungs" onclick="selectOrgan('lungs')" opacity="0.85">
                  <path d="M 260 170 C 240 190, 240 230, 260 250 C 275 250, 280 200, 265 170 Z" fill="#93c5fd" stroke="#3b82f6" stroke-width="1.5"/>
                  <path d="M 340 170 C 360 190, 360 230, 340 250 C 325 250, 320 200, 335 170 Z" fill="#93c5fd" stroke="#3b82f6" stroke-width="1.5"/>
                </g>
                <!-- Печень (Hepar) -->
                <path class="anat-node" data-organ="hepar" onclick="selectOrgan('hepar')"
                  d="M 260 255 Q 315 250 325 275 Q 310 295 265 285 Z"
                  fill="#b45309" stroke="#78350f" stroke-width="1.5" opacity="0.9"/>
                <!-- Желудок (Gaster) -->
                <path class="anat-node" data-organ="gaster" onclick="selectOrgan('gaster')"
                  d="M 315 260 Q 335 280 320 305 Q 295 305 305 280 Z"
                  fill="#f43f5e" stroke="#be123c" stroke-width="1.5" opacity="0.9"/>
                <!-- Почки (Renes) -->
                <ellipse class="anat-node" data-organ="renes" onclick="selectOrgan('renes')" cx="270" cy="310" rx="10" ry="16" fill="#be185d" opacity="0.9"/>
                <ellipse class="anat-node" data-organ="renes" onclick="selectOrgan('renes')" cx="330" cy="310" rx="10" ry="16" fill="#be185d" opacity="0.9"/>
                <!-- Кишечник (Intestinum) -->
                <path class="anat-node" data-organ="intestinum" onclick="selectOrgan('intestinum')"
                  d="M 275 320 Q 300 315 325 320 Q 335 360 300 365 Q 265 360 275 320 Z"
                  fill="#fbbf24" stroke="#d97706" stroke-width="1.5" opacity="0.85"/>
              </g>

              <!-- СЛОЙ 6: КЛЕТКА И МИКРОАНАТОМИЯ (ЦИТОЛОГИЯ) -->
              <g id="layer-cell" class="anat-layer" style="display:none">
                <!-- Фон цитоплазмы клетки -->
                <rect x="50" y="50" width="500" height="600" rx="20" fill="var(--surface-2)" stroke="var(--border)" stroke-width="2"/>
                <!-- Клеточная мембрана (Plasmalemma) -->
                <path d="M 100 350 C 100 150, 500 150, 500 350 C 500 550, 100 550, 100 350 Z"
                  fill="none" stroke="var(--primary)" stroke-width="6" stroke-dasharray="10 4"/>
                <!-- Ядро клетки (Nucleus) -->
                <g class="anat-node" data-organ="nucleus" onclick="selectOrgan('nucleus')">
                  <circle cx="300" cy="350" r="90" fill="url(#gradNeuro)" opacity="0.75" stroke="var(--primary)" stroke-width="3"/>
                  <!-- Ядрышко (Nucleolus) -->
                  <circle cx="320" cy="335" r="30" fill="var(--primary)" opacity="0.85"/>
                </g>
                <!-- Митохондрии (Mitochondria — кристы) -->
                <g class="anat-node" data-organ="mitochondria" onclick="selectOrgan('mitochondria')">
                  <rect x="160" y="220" width="70" height="40" rx="20" fill="#ef4444" stroke="#991b1b" stroke-width="2"/>
                  <path d="M 175 240 Q 185 225 195 240 T 215 240" fill="none" stroke="#fff" stroke-width="2"/>
                </g>
                <!-- Аппарат Гольджи -->
                <g class="anat-node" data-organ="golgi" onclick="selectOrgan('golgi')">
                  <path d="M 380 230 Q 430 220 440 250" fill="none" stroke="#3b82f6" stroke-width="5" stroke-linecap="round"/>
                  <path d="M 390 250 Q 440 240 450 270" fill="none" stroke="#3b82f6" stroke-width="5" stroke-linecap="round"/>
                  <path d="M 400 270 Q 450 260 460 290" fill="none" stroke="#3b82f6" stroke-width="5" stroke-linecap="round"/>
                </g>
              </g>

              <text x="300" y="690" text-anchor="middle" fill="var(--text-dim)" font-size="11" font-family="var(--font-mono)" letter-spacing="1.5">
                ● НАЖМИТЕ НА ОРГАН ДЛЯ ИЗУЧЕНИЯ ДОСЬЕ И ВОПРОСОВ ●
              </text>
            </svg>
          </div>

          <!-- Академическое досье выбранного анатомического образования -->
          <div class="organ-dossier-card" id="organDossier">
            <div>
              <div class="dossier-header">
                <div class="dossier-latin" id="dosLatin">Cor, cordis, n.</div>
                <div class="dossier-name" id="dosName">Сердце человека</div>
                <div class="dossier-section-badge" id="dosBadge">Раздел 7: Кровообращение</div>
              </div>
              <div class="dossier-body" id="dosDesc">
                Полый мышечный орган, обеспечивающий непрерывный ток крови по малому и большому кругам кровообращения. Имеет четырехкамерное строение: правое и левое предсердия, правый и левый желудочки.
              </div>
              <div class="dossier-clinical" id="dosClin">
                <strong>Клиническое значение:</strong> Ишемическая болезнь, инфаркт миокарда, пороки двухстворчатого (митрального) и аортального клапанов. Оценивается методом ЭКГ и ЭхоКГ.
              </div>
            </div>
            <div class="dossier-action">
              <button class="btn btn-primary" style="width:100%" id="btnDosJump" onclick="jumpToSectionQuestions(7)">
                📖 Изучить вопросы раздела (14) →
              </button>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- ПАНЕЛЬ 2: ВОПРОСЫ / РАЗБОРЫ (Q-PANEL) -->
    <div class="view-panel" id="panelQuestions">
      <div class="q-card">
        <div class="q-meta-row">
          <div class="q-breadcrumb" id="qBreadcrumb">Раздел 1 • Вопрос 1</div>
          <div class="q-conf-indicator" id="qConfIndicator" style="display:none"></div>
        </div>

        <h1 class="q-title" id="qTitleText">Загрузка формулировки вопроса…</h1>

        <div class="q-nav-toolbar">
          <button class="btn btn-primary" id="btnToggleAns" onclick="toggleAnswerReveal()">
            👁️ <span id="btnAnsText">Показать ответ</span>
          </button>
          <div style="display:flex;gap:8px">
            <button class="btn btn-secondary" onclick="navigateItem(-1)" title="Предыдущий вопрос (Стрелка влево)">← Назад</button>
            <button class="btn btn-secondary" onclick="navigateItem(1)" title="Следующий вопрос (Стрелка вправо)">Вперёд →</button>
          </div>
        </div>

        <div class="answer-wrapper">
          <div class="answer-header">
            <span>●</span>
            <span id="ansHeadStatus">Ответ скрыт — попытайтесь воспроизвести материал по памяти</span>
          </div>
          <div class="answer-body hidden-state" id="ansContentArea">
            Нажмите «Показать ответ» или нажмите клавишу Пробел / V
          </div>
        </div>

        <div style="margin-top:16px">
          <div style="font-size:12px;font-weight:700;color:var(--text-dim);text-transform:uppercase;margin-bottom:8px;font-family:var(--font-mono)">
            Оцените степень усвоения материала:
          </div>
          <div class="conf-selector-row">
            <button class="conf-choice-btn noknow" onclick="setUserConfidence('noknow')" title="Клавиша 1">
              ✕ Не знаю
            </button>
            <button class="conf-choice-btn unsure" onclick="setUserConfidence('unsure')" title="Клавиша 2">
              ? Сомневаюсь
            </button>
            <button class="conf-choice-btn know" onclick="setUserConfidence('know')" title="Клавиша 3">
              ✓ Знаю твёрдо
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- ПАНЕЛЬ 3: КВИЗЫ И ТЕСТЫ (QUIZ-PANEL) -->
    <div class="view-panel" id="panelQuiz">
      <div class="quiz-container">
        <div class="quiz-top-card">
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
            <label for="quizSectionSelect" style="font-size:13px;font-weight:700;color:var(--text-muted)">Раздел:</label>
            <select class="quiz-sec-select" id="quizSectionSelect" onchange="initQuizSelection()">
              <option value="all">Все разделы атласа</option>
            </select>
            <button class="btn btn-primary" onclick="startQuizTest()">▶ Начать тест</button>
          </div>
          <div id="quizScoreBanner" style="display:none;font-size:13.5px;font-family:var(--font-mono);font-weight:700">
            Верно: <span id="quizScoreCorrect" style="color:var(--know)">0</span> | Ошибок: <span id="quizScoreWrong" style="color:var(--noknow)">0</span>
          </div>
        </div>

        <div id="quizQuestionsFeed">
          <div class="empty-state">
            <div class="empty-state-icon">
              <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 14h-2v-2h2v2zm0-4h-2V7h2v5z"/></svg>
            </div>
            <div class="empty-state-title">Тестирование не запущено</div>
            <div class="empty-state-desc">Выберите интересующий анатомический раздел из выпадающего списка выше и нажмите кнопку «Начать тест».</div>
            <button class="btn btn-primary" onclick="startQuizTest()">▶ Начать тест по всем разделам</button>
          </div>
        </div>
      </div>
    </div>

    <!-- ПАНЕЛЬ 4: СТАТИСТИКА И ПРОГРЕСС (STATS-PANEL) -->
    <div class="view-panel" id="panelStats">
      <div class="stats-overview-grid">
        <div class="stat-metric-card">
          <div class="stat-metric-num" id="statKnowCount">0</div>
          <div class="stat-metric-label">Вопросов усвоено</div>
        </div>
        <div class="stat-metric-card">
          <div class="stat-metric-num" id="statUnsureCount">0</div>
          <div class="stat-metric-label">Требуют повторения</div>
        </div>
        <div class="stat-metric-card">
          <div class="stat-metric-num" id="statNoknowCount">0</div>
          <div class="stat-metric-label">Не изучено</div>
        </div>
        <div class="stat-metric-card">
          <div class="stat-metric-num" id="statQuizAccuracy">—</div>
          <div class="stat-metric-label">% точности в тестах</div>
        </div>
      </div>

      <div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:22px;box-shadow:var(--shadow-sm)">
        <h2 style="font-size:18px;margin-bottom:16px;color:var(--text)">Уверенность по разделам анатомии</h2>
        <div id="statsSectionList">
          <!-- Генерируется скриптом -->
        </div>
      </div>
    </div>

  </div> <!-- /successContentContainer -->

</main>

<script>
// ── ДАННЫЕ АТЛАСА (QUESTIONS, TASKS, TESTS) ──
"""

# Append the extracted data block
html_content += data_block + "\n\n"

# Append the modern Application Logic, Russian Typograph, and Atlas Interactivity
html_content += """
// ── ПРАВИЛО Т10: РУССКАЯ ТИПОГРАФИКА СТУДИИ «КАЛИБР» ──
function typograph(input) {
  if (!input) return '';
  const NBSP = '\\u00A0';
  let s = String(input);
  // Замена парных кавычек на русские «ёлочки»
  s = s.replace(/"([^"]*)"/g, '«$1»');
  // Тире с неразрывным пробелом
  s = s.replace(/(\\s|^)(?:--|—|–|-)(\\s)/g, `$1${NBSP}— `);
  // Короткие служебные предлоги и союзы (Т10)
  const SHORT = "без|для|над|под|при|про|изо|обо|ото|что|как|или|чем|где|кто|все|его|ее|их|мы|вы|он|она|оно|они|до|за|из|к|на|о|об|от|по|с|со|у|в|во";
  const reShort = new RegExp(`(^|[\\\\s(«„"—])(${SHORT})\\\\s+`, 'giu');
  s = s.replace(reShort, `$1$2${NBSP}`);
  // Числа с единицами и обозначениями
  s = s.replace(/(\\d)\\\\s+([а-яёА-ЯЁa-zA-Z%№§]{1,5})(?=[\\\\s.,!?;:…)»]|$)/gu, `$1${NBSP}$2`);
  // Разряды тысяч
  s = s.replace(/(\\d)\\\\s+(\\d{3})/g, `$1${NBSP}$2`);
  return s;
}

// ── ТЕМЫ ОФОРМЛЕНИЯ (Ц7, Ц8) ──
function initTheme() {
  const saved = localStorage.getItem('anat_theme_pref') || 'light';
  applyTheme(saved);
}

function applyTheme(t) {
  if (t === 'dark') {
    document.documentElement.classList.add('dark-theme');
    document.documentElement.classList.remove('light-theme');
    document.getElementById('themeIconSun').style.display = 'none';
    document.getElementById('themeIconMoon').style.display = 'block';
  } else {
    document.documentElement.classList.add('light-theme');
    document.documentElement.classList.remove('dark-theme');
    document.getElementById('themeIconSun').style.display = 'block';
    document.getElementById('themeIconMoon').style.display = 'none';
  }
  localStorage.setItem('anat_theme_pref', t);
}

function toggleTheme() {
  const isDark = document.documentElement.classList.contains('dark-theme');
  applyTheme(isDark ? 'light' : 'dark');
}

// ── 4 СОСТОЯНИЯ ЭКРАНА (ПРАВИЛО У1 & Н4) ──
let currentScreenState = 'success'; // 'success' | 'loading' | 'error' | 'empty'

function setScreenState(st) {
  currentScreenState = st;
  document.querySelectorAll('.state-pill').forEach(b => b.classList.remove('active'));
  const btnMap = { success: 'btnStateSuccess', loading: 'btnStateLoading', error: 'btnStateError', empty: 'btnStateEmpty' };
  const targetBtn = document.getElementById(btnMap[st]);
  if (targetBtn) targetBtn.classList.add('active');

  const cSuccess = document.getElementById('successContentContainer');
  const cLoading = document.getElementById('loadingStateContainer');
  const cError   = document.getElementById('errorStateContainer');
  const cEmpty   = document.getElementById('emptyStateContainer');

  cSuccess.style.display = (st === 'success') ? 'block' : 'none';
  cLoading.style.display = (st === 'loading') ? 'block' : 'none';
  cError.style.display   = (st === 'error') ? 'flex' : 'none';
  cEmpty.style.display   = (st === 'empty') ? 'flex' : 'none';
}

// ── БАЗА ОРГАНОВ ДЛЯ ИНТЕРАКТИВНОГО АТЛАСА ──
const ORGAN_DB = {
  cor: {
    latin: "Cor, cordis, n.",
    name: "Сердце (Миокард и проводящая система)",
    section: 7,
    badge: "Раздел 7: Кровообращение",
    desc: "Полый мышечный орган конусовидной формы, расположенный в среднем средостении. Состоит из 4 камер: правого и левого предсердий, правого и левого желудочков. Клапанный аппарат (митральный, трехстворчатый, аортальный, легочный) обеспечивает однонаправленный ток крови.",
    clinical: "Инфаркт миокарда, стенокардия, фибрилляция предсердий, гипертрофия левого желудочка. Оценка функции: ЭКГ, ЭхоКГ, коронарография."
  },
  aorta: {
    latin: "Aorta thoracica et abdominalis",
    name: "Аорта (Главный артериальный ствол)",
    section: 7,
    badge: "Раздел 7: Кровообращение",
    desc: "Крупнейший непарный артериальный сосуд большого круга кровообращения. Подразделяется на восходящую часть, дугу аорты и нисходящую аорту (грудной и брюшной отделы). Обеспечивает кровью все органы и ткани организма под высоким гидростатическим давлением.",
    clinical: "Аневризма аорты, коарктация, расслоение стенки аорты, атеросклероз аорты."
  },
  brain: {
    latin: "Encephalon (Cerebrum)",
    name: "Головной мозг (Кора, подкорка и мозжечок)",
    section: 9,
    badge: "Раздел 8: Нервная система",
    desc: "Главный регуляторный орган центральной нервной системы. Включает полушария большого мозга с корой (серое вещество), мозжечок (координация движений), ствол мозга (продолговатый мозг, мост, средний мозг), содержащий жизненно важные сосудодвигательный и дыхательный центры.",
    clinical: "Острое нарушение мозгового кровообращения (инсульт), черепно-мозговые травмы, энцефалиты, рассеянный склероз."
  },
  spinal_cord: {
    latin: "Medulla spinalis",
    name: "Спинной мозг (Проводящие пути и сегменты)",
    section: 9,
    badge: "Раздел 8: Нервная система",
    desc: "Тяж нервной ткани, расположенный в позвоночном канале. Состоит из 31 пары сегментов с передними (двигательными) и задними (чувствительными) корешками. Проводит импульсы между головным мозгом и периферией, осуществляет безусловные рефлексы.",
    clinical: "Компрессионные миелопатии, травмы позвоночника, полиомиелит, спинальные инсульты."
  },
  cranium: {
    latin: "Cranium (Calvaria et basis cranii)",
    name: "Череп (Мозговой и лицевой отделы)",
    section: 1,
    badge: "Раздел 2: ОДА — пассивная часть",
    desc: "Костный остов головы, защищающий головной мозг и органы чувств. Мозговой отдел образован лобной, теменными, затылочной, клиновидной, решетчатой и височными костями, соединенными непрерывными швами.",
    clinical: "Переломы свода и основания черепа, трепанация, краниосиностозы."
  },
  spine: {
    latin: "Columna vertebralis",
    name: "Позвоночный столб (Позвоночник)",
    section: 1,
    badge: "Раздел 2: ОДА — пассивная часть",
    desc: "Осевой скелет тела, состоящий из 32-34 позвонков (7 шейных, 12 грудных, 5 поясничных, крестец и копчик). Имеет физиологические изгибы: шейный и поясничный лордозы, грудной и крестцовый кифозы, обеспечивающие амортизацию.",
    clinical: "Остеохондроз, грыжи межпозвонковых дисков, сколиоз, спондилолистез."
  },
  ribs: {
    latin: "Costae et sternum",
    name: "Грудная клетка (Рёбра и грудина)",
    section: 1,
    badge: "Раздел 2: ОДА — пассивная часть",
    desc: "Костно-хрящевой каркас, защищающий органы средостения и легкие. Состоит из 12 пар ребер (7 истинных, 3 ложных, 2 колеблющихся) и грудины. Принимает непосредственное участие в дыхательной экскурсии.",
    clinical: "Переломы ребер, пневмоторакс, деформации грудной клетки (воронкообразная, килевидная)."
  },
  pelvis: {
    latin: "Pelvis major et minor",
    name: "Тазовый пояс (Кости таза)",
    section: 1,
    badge: "Раздел 2: ОДА — пассивная часть",
    desc: "Костное кольцо, соединяющее позвоночник со свободными нижними конечностями. Образовано двумя тазовыми костями (подвздошная, седалищная, лобковая), крестцом и копчиком. Защищает органы малого таза.",
    clinical: "Переломы костей таза (по типу Мальгеня), патология тазобедренного сустава (коксартроз)."
  },
  pectoralis: {
    latin: "Musculus pectoralis major",
    name: "Большая грудная мышца",
    section: 2,
    badge: "Раздел 2: ОДА — активная часть",
    desc: "Поверхностная веерообразная мышца передней стенки грудной клетки. Приводит плечо к туловищу, пронирует его внутрь, участвует в форсированном вдохе как вспомогательная дыхательная мышца.",
    clinical: "Разрывы сухожилия большой грудной мышцы при силовых перегрузках, миозиты."
  },
  abdominis: {
    latin: "Musculus rectus abdominis",
    name: "Прямая мышца живота (Брюшной пресс)",
    section: 2,
    badge: "Раздел 2: ОДА — активная часть",
    desc: "Парная длинная лентовидная мышца, заключенная во влагалище прямой мышцы живота. Сгибает позвоночный столб вперед, участвует в натуживании, поддерживает внутрибрюшное давление и фиксацию внутренних органов.",
    clinical: "Диастаз прямых мышц живота, грыжи белой линии, вентральные грыжи."
  },
  lungs: {
    latin: "Pulmones (Pulmo dexter et sinister)",
    name: "Лёгкие (Бронхиальное дерево и альвеолы)",
    section: 3,
    badge: "Раздел 3: Дыхательная система",
    desc: "Главные парные органы внешнего дыхания. Правое легкое состоит из 3 долей, левое — из 2. Структурно-функциональная единица — ацинус, где через аэрогематический барьер альвеол происходит газообмен (диффузия кислорода и углекислого газа).",
    clinical: "Пневмония, хроническая обструктивная болезнь легких (ХОБЛ), бронхиальная астма, плеврит."
  },
  hepar: {
    latin: "Hepar (Lobus dexter et sinister)",
    name: "Печень (Крупнейшая пищеварительная железа)",
    section: 4,
    badge: "Раздел 4: Пищеварительная система",
    desc: "Жизненно важный паренхиматозный орган, расположенный в правом подреберье. Выполняет барьерную (детоксикационную), метаболическую (синтез белков, гликогена) и экскреторную функции, вырабатывает желчь для расщепления липидов.",
    clinical: "Гепатиты, цирроз печени, желчнокаменная болезнь, портальная гипертензия."
  },
  gaster: {
    latin: "Gaster (Ventriculus)",
    name: "Желудок (Кардия, тело, привратник)",
    section: 4,
    badge: "Раздел 4: Пищеварительная система",
    desc: "Мешкообразное расширение пищеварительного тракта емкостью 1.5–3 л. Вырабатывает желудочный сок, содержащий соляную кислоту и пепсин для ферментативного переваривания белков, вырабатывает внутренний фактор Касла.",
    clinical: "Гастрит, язвенная болезнь желудка и двенадцатиперстной кишки, B12-дефицитная анемия."
  },
  renes: {
    latin: "Renes (Ren dexter et sinister)",
    name: "Почки (Нефроны и мочеобразование)",
    section: 5,
    badge: "Раздел 5: Органы выделения",
    desc: "Парные бобовидные органы забрюшинного пространства. Структурно-функциональная единица — нефрон (почечное тельце и канальцы). Осуществляют клубочковую фильтрацию, канальцевую реабсорбцию и секрецию, поддерживают водно-солевой гомеостаз.",
    clinical: "Гломерулонефрит, пиелонефрит, мочекаменная болезнь, острая и хроническая почечная недостаточность."
  },
  intestinum: {
    latin: "Intestinum tenue et crassum",
    name: "Кишечник (Тонкая и толстая кишка)",
    section: 4,
    badge: "Раздел 4: Пищеварительная система",
    desc: "Тонкая кишка (двенадцатиперстная, тощая, подвздошная) осуществляет полостное и пристеночное пищеварение и всасывание нутриентов. Толстая кишка отвечает за реабсорбцию воды, формирование каловых масс и микробиотический синтез витаминов.",
    clinical: "Энтериты, колиты, аппендицит, кишечная непроходимость."
  },
  nucleus: {
    latin: "Nucleus cellularis et nucleolus",
    name: "Клеточное ядро и ядрышко",
    section: 0,
    badge: "Раздел 1: Введение и клетки",
    desc: "Главный информационный центр эукариотической клетки. Окружен двумембранной ядерной оболочкой с порами, содержит хроматин (ДНК, соединенная с гистонами) и ядрышко, ответственное за сборку субъединиц рибосом.",
    clinical: "Мутации ДНК, онкогенез, хромосомные аберрации."
  },
  mitochondria: {
    latin: "Mitochondria (Cristae mitochondriales)",
    name: "Митохондрия («Энергетическая станция»)",
    section: 0,
    badge: "Раздел 1: Введение и клетки",
    desc: "Двумембранный органоид клетки, имеющий собственную кольцевую ДНК. Внутренняя мембрана образует кристы, на которых локализованы ферменты дыхательной цепи и АТФ-синтаза, осуществляющие окислительное фосфорилирование.",
    clinical: "Митохондриальные миопатии, синдром хронической усталости, клеточная гипоксия."
  },
  golgi: {
    latin: "Apparatus golgiensis",
    name: "Аппарат (комплекс) Гольджи",
    section: 0,
    badge: "Раздел 1: Введение и клетки",
    desc: "Мембранная система уплощенных цистерн (диктиосом) и пузырьков. Отвечает за модификацию, сортировку, упаковку белков и липидов, синтезированных в эндоплазматической сети, а также образование первичных лизосом.",
    clinical: "Нарушения секреторной функции экзокринных желез, болезни накопления."
  }
};

function selectOrgan(id) {
  const organ = ORGAN_DB[id];
  if (!organ) return;

  // Снять выделение со всех узлов
  document.querySelectorAll('.anat-node').forEach(n => n.classList.remove('selected'));
  document.querySelectorAll(`[data-organ="${id}"]`).forEach(n => n.classList.add('selected'));

  document.getElementById('dosLatin').textContent = organ.latin;
  document.getElementById('dosName').textContent  = typograph(organ.name);
  document.getElementById('dosBadge').textContent = organ.badge;
  document.getElementById('dosDesc').innerHTML    = typograph(organ.desc);
  document.getElementById('dosClin').innerHTML    = '<strong>Клиническое значение:</strong> ' + typograph(organ.clinical);

  const btnJump = document.getElementById('btnDosJump');
  btnJump.onclick = () => jumpToSectionQuestions(organ.section);
  btnJump.textContent = `📖 Изучить вопросы раздела (${QD[organ.section] ? QD[organ.section].q.length : '—'}) →`;
}

function setAtlasLayer(layer) {
  document.querySelectorAll('.layer-btn').forEach(b => b.classList.remove('active'));
  const btn = document.getElementById('btnLayer' + layer.charAt(0).toUpperCase() + layer.slice(1));
  if (btn) btn.classList.add('active');

  const layers = ['skeleton', 'muscles', 'cardio', 'neuro', 'viscera', 'cell'];
  layers.forEach(l => {
    const el = document.getElementById('layer-' + l);
    if (!el) return;
    if (layer === 'all') {
      el.style.display = (l === 'cell') ? 'none' : 'block';
    } else if (layer === l) {
      el.style.display = 'block';
    } else {
      el.style.display = 'none';
    }
  });

  // Автоматический выбор первого органа слоя
  const layerPresetOrgans = {
    all: 'cor',
    skeleton: 'cranium',
    muscles: 'pectoralis',
    cardio: 'cor',
    neuro: 'brain',
    viscera: 'lungs',
    cell: 'nucleus'
  };
  if (layerPresetOrgans[layer]) {
    selectOrgan(layerPresetOrgans[layer]);
  }
}

// ── УПРАВЛЕНИЕ РЕЖИМАМИ И ВКЛАДКАМИ ──
let currentMode = 'atlas'; // 'atlas' | 'questions' | 'tasks' | 'quiz' | 'stats'
let currentSectionIdx = 0;
let currentQuestionIdx = 0;
let answerRevealed = false;
let userConfidence = {};

function switchMainTab(mode) {
  currentMode = mode;
  document.body.className = document.body.className.replace(/mode-[a-z]+/g, '').trim() + ' mode-' + mode;

  document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));

  const tabId = 'tab' + mode.charAt(0).toUpperCase() + mode.slice(1);
  const panelId = 'panel' + mode.charAt(0).toUpperCase() + mode.slice(1);

  const tabEl = document.getElementById(tabId);
  const panelEl = document.getElementById(panelId);
  if (tabEl) tabEl.classList.add('active');
  if (panelEl) panelEl.classList.add('active');

  if (mode === 'questions' || mode === 'tasks') {
    renderSidebarList();
    loadQuestionItem(currentSectionIdx, currentQuestionIdx);
  } else if (mode === 'atlas') {
    setAtlasLayer('all');
  } else if (mode === 'quiz') {
    populateQuizSectionSelect();
  } else if (mode === 'stats') {
    renderStatsView();
  }
  updateGlobalProgressBar();
  closeSidebar();
}

function jumpToSectionQuestions(secIdx) {
  currentSectionIdx = secIdx;
  currentQuestionIdx = 0;
  switchMainTab('questions');
}

// ── САЙДБАР: СПИСОК РАЗДЕЛОВ И ВОПРОСОВ ──
function renderSidebarList() {
  const container = document.getElementById('sidebarList');
  if (!container) return;

  const data = (currentMode === 'tasks') ? TD : QD;
  const prefix = (currentMode === 'tasks') ? 'task' : 'q';

  let html = '';
  data.forEach((sec, si) => {
    const total = sec.q.length;
    let knowCount = 0;
    sec.q.forEach((_, qi) => {
      if (userConfidence[`${prefix}-${si}-${qi}`] === 'know') knowCount++;
    });
    const pct = total ? Math.round((knowCount / total) * 100) : 0;
    const shortTitle = sec.s.length > 40 ? sec.s.slice(0, 38) + '…' : sec.s;

    html += `
      <div class="sec-group" id="secGroup-${si}">
        <div class="sec-header" onclick="toggleSecOpen(${si})">
          <div class="sec-header-title">${typograph(shortTitle)}</div>
          <div class="sec-header-stat">${knowCount}/${total}</div>
        </div>
        <div class="sec-progress-bar">
          <div class="sec-progress-fill" style="width:${pct}%"></div>
        </div>
        <div class="sec-items" id="secItems-${si}">
    `;

    sec.q.forEach((q, qi) => {
      const idKey = `${prefix}-${si}-${qi}`;
      const conf = userConfidence[idKey] || '';
      const isActive = (si === currentSectionIdx && qi === currentQuestionIdx && (currentMode === 'questions' || currentMode === 'tasks'));
      const textPreview = q.text.length > 60 ? q.text.slice(0, 58) + '…' : q.text;

      html += `
        <div class="q-list-item ${conf} ${isActive ? 'active' : ''}" id="item-${idKey}" onclick="selectQuestionItem(${si}, ${qi})">
          <div class="status-dot"></div>
          <div class="q-number-badge">${qi + 1}</div>
          <div style="flex:1">${typograph(textPreview)}</div>
        </div>
      `;
    });

    html += `</div></div>`;
  });

  container.innerHTML = html;
}

function selectQuestionItem(si, qi) {
  if (currentMode !== 'questions' && currentMode !== 'tasks') {
    switchMainTab('questions');
  }
  currentSectionIdx = si;
  currentQuestionIdx = qi;
  answerRevealed = false;
  loadQuestionItem(si, qi);

  // Обновить активный класс в сайдбаре
  document.querySelectorAll('.q-list-item').forEach(el => el.classList.remove('active'));
  const prefix = (currentMode === 'tasks') ? 'task' : 'q';
  const target = document.getElementById(`item-${prefix}-${si}-${qi}`);
  if (target) target.classList.add('active');

  closeSidebar();
}

function loadQuestionItem(si, qi) {
  const data = (currentMode === 'tasks') ? TD : QD;
  const sec = data[si];
  if (!sec || !sec.q[qi]) return;
  const item = sec.q[qi];
  const prefix = (currentMode === 'tasks') ? 'task' : 'q';
  const idKey = `${prefix}-${si}-${qi}`;

  document.getElementById('qBreadcrumb').textContent = `${sec.s} • Вопрос ${qi + 1} из ${sec.q.length}`;
  document.getElementById('qTitleText').innerHTML = typograph(item.text);

  renderConfidenceUI(idKey);
  renderAnswerArea(item);
}

function renderConfidenceUI(idKey) {
  const conf = userConfidence[idKey];
  const ind = document.getElementById('qConfIndicator');
  if (ind) {
    if (conf) {
      ind.style.display = 'inline-flex';
      ind.className = 'q-conf-indicator ' + conf;
      ind.textContent = (conf === 'know') ? '✓ Усвоено' : (conf === 'unsure') ? '? Сомнение' : '✕ Не знаю';
    } else {
      ind.style.display = 'none';
    }
  }

  document.querySelectorAll('.conf-choice-btn').forEach(b => {
    b.classList.remove('active');
    if (conf && b.classList.contains(conf)) b.classList.add('active');
  });
}

function setUserConfidence(level) {
  const prefix = (currentMode === 'tasks') ? 'task' : 'q';
  const idKey = `${prefix}-${currentSectionIdx}-${currentQuestionIdx}`;

  if (userConfidence[idKey] === level) {
    delete userConfidence[idKey];
  } else {
    userConfidence[idKey] = level;
  }

  saveStorageState();
  renderConfidenceUI(idKey);
  renderSidebarList();
  updateGlobalProgressBar();
}

function toggleAnswerReveal() {
  answerRevealed = !answerRevealed;
  const data = (currentMode === 'tasks') ? TD : QD;
  const item = data[currentSectionIdx].q[currentQuestionIdx];
  renderAnswerArea(item);
}

function renderAnswerArea(item) {
  const btnText = document.getElementById('btnAnsText');
  const headStatus = document.getElementById('ansHeadStatus');
  const contentArea = document.getElementById('ansContentArea');

  if (answerRevealed) {
    btnText.textContent = 'Скрыть ответ';
    headStatus.textContent = 'Развёрнутый канонический ответ атласа (Гайворонский-Ничипорук):';
    contentArea.className = 'answer-body';
    contentArea.innerHTML = renderMarkdown(item.ans);
  } else {
    btnText.textContent = 'Показать ответ';
    headStatus.textContent = 'Ответ скрыт — попытайтесь воспроизвести материал по памяти';
    contentArea.className = 'answer-body hidden-state';
    contentArea.textContent = 'Нажмите «Показать ответ» или нажмите клавишу Пробел / V';
  }
}

function navigateItem(dir) {
  const data = (currentMode === 'tasks') ? TD : QD;
  const sec = data[currentSectionIdx];
  let nextQ = currentQuestionIdx + dir;
  let nextS = currentSectionIdx;

  if (nextQ < 0) {
    if (nextS > 0) {
      nextS--;
      nextQ = data[nextS].q.length - 1;
    } else {
      return;
    }
  } else if (nextQ >= sec.q.length) {
    if (nextS < data.length - 1) {
      nextS++;
      nextQ = 0;
    } else {
      return;
    }
  }
  selectQuestionItem(nextS, nextQ);
}

// ── РЕНДЕРЕР МАРКДАУНА ДЛЯ ТЕКСТА ОТВЕТОВ ──
function renderMarkdown(md) {
  if (!md) return '';
  let s = md.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  // bold
  s = s.replace(/\\*\\*([^\\*]+?)\\*\\*/g, '<strong>$1</strong>');
  // italic
  s = s.replace(/(^|[^\\*])\\*([^\\*\\n]+?)\\*(?!\\*)/g, '$1<em>$2</em>');
  // lists
  const lines = s.split('\\n');
  let out = '';
  let inList = false;

  lines.forEach(l => {
    const trimmed = l.trim();
    if (trimmed.startsWith('- ') || trimmed.startsWith('• ')) {
      if (!inList) { out += '<ul>'; inList = true; }
      out += `<li>${typograph(trimmed.slice(2))}</li>`;
    } else {
      if (inList) { out += '</ul>'; inList = false; }
      if (trimmed.length > 0) {
        out += `<p style="margin-bottom:12px">${typograph(trimmed)}</p>`;
      }
    }
  });
  if (inList) out += '</ul>';
  return out;
}

// ── КВИЗ И ТЕСТЫ (QUIZ ENGINE — СТРОГОЕ СООТВЕТСТВИЕ ДАННЫМ) ──
let quizAnsweredState = {};
let quizScore = { correct: 0, wrong: 0 };
let currentActiveQuizItems = [];

function populateQuizSectionSelect() {
  const sel = document.getElementById('quizSectionSelect');
  if (!sel || sel.children.length > 1) return;
  QD.forEach((sec, i) => {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = sec.s.length > 50 ? sec.s.slice(0, 48) + '…' : sec.s;
    sel.appendChild(opt);
  });
}

function initQuizSelection() {
  startQuizTest();
}

function startQuizTest() {
  const sel = document.getElementById('quizSectionSelect');
  const val = sel ? sel.value : 'all';
  const feed = document.getElementById('quizQuestionsFeed');
  feed.innerHTML = '';
  quizAnsweredState = {};
  quizScore = { correct: 0, wrong: 0 };
  updateQuizScoreUI();

  currentActiveQuizItems = [];
  if (val === 'all') {
    QD.forEach((sec, si) => {
      sec.q.forEach((_, qi) => {
        const k = `${si}-${qi}`;
        if (TESTS[k]) currentActiveQuizItems.push({ si, qi, test: TESTS[k] });
      });
    });
  } else {
    const si = parseInt(val);
    QD[si].q.forEach((_, qi) => {
      const k = `${si}-${qi}`;
      if (TESTS[k]) currentActiveQuizItems.push({ si, qi, test: TESTS[k] });
    });
  }

  if (!currentActiveQuizItems.length) {
    feed.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-title">Нет готовых тестов для этого раздела</div>
        <div class="empty-state-desc">Попробуйте выбрать «Все разделы атласа» или другой раздел.</div>
      </div>
    `;
    return;
  }

  document.getElementById('quizScoreBanner').style.display = 'block';

  currentActiveQuizItems.slice(0, 25).forEach((item, idx) => {
    const qCard = document.createElement('div');
    qCard.className = 'quiz-card';
    qCard.id = `quizCard-${idx}`;

    let optsHtml = '';
    const correctIdx = item.test.correct;

    item.test.opts.forEach((opt, oi) => {
      optsHtml += `
        <button class="quiz-option-btn" id="qopt-${idx}-${oi}" onclick="handleQuizAnswer(${idx}, ${oi}, ${correctIdx})">
          <span style="font-family:var(--font-mono);font-weight:700;color:var(--text-dim)">${String.fromCharCode(65 + oi)}.</span>
          <span>${typograph(opt)}</span>
        </button>
      `;
    });

    qCard.innerHTML = `
      <div style="font-size:12px;font-family:var(--font-mono);color:var(--text-dim);margin-bottom:8px">
        Вопрос ${idx + 1} из ${currentActiveQuizItems.length > 25 ? '25' : currentActiveQuizItems.length} • ${QD[item.si].s}
      </div>
      <div class="quiz-card-q">${typograph(item.test.q)}</div>
      <div class="quiz-options-list">${optsHtml}</div>
      <div class="quiz-explanation" id="qexp-${idx}" style="display:none"></div>
    `;
    feed.appendChild(qCard);
  });
}

function handleQuizAnswer(qIdx, chosenOpt, correctOpt) {
  if (quizAnsweredState[qIdx] !== undefined) return;
  quizAnsweredState[qIdx] = chosenOpt;

  const isCorrect = (chosenOpt === correctOpt);
  if (isCorrect) quizScore.correct++; else quizScore.wrong++;
  updateQuizScoreUI();

  const chosenBtn = document.getElementById(`qopt-${qIdx}-${chosenOpt}`);
  const correctBtn = document.getElementById(`qopt-${qIdx}-${correctOpt}`);

  if (isCorrect) {
    if (chosenBtn) chosenBtn.classList.add('correct');
  } else {
    if (chosenBtn) chosenBtn.classList.add('wrong');
    if (correctBtn) correctBtn.classList.add('correct');
  }

  // Показать объяснение к вопросу
  const expEl = document.getElementById(`qexp-${qIdx}`);
  const item = currentActiveQuizItems[qIdx];
  if (expEl && item && item.test.expl) {
    expEl.style.display = 'block';
    expEl.innerHTML = '<strong>Академическое обоснование:</strong> ' + typograph(item.test.expl);
  }

  // Заблокировать повторные клики по этой карточке
  const card = document.getElementById(`quizCard-${qIdx}`);
  if (card) {
    card.querySelectorAll('.quiz-option-btn').forEach(b => b.disabled = true);
  }
}

function updateQuizScoreUI() {
  document.getElementById('quizScoreCorrect').textContent = quizScore.correct;
  document.getElementById('quizScoreWrong').textContent = quizScore.wrong;
}

// ── СТАТИСТИКА И ПРОГРЕСС ──
function renderStatsView() {
  let know = 0, unsure = 0, noknow = 0;
  Object.keys(userConfidence).forEach(k => {
    if (userConfidence[k] === 'know') know++;
    else if (userConfidence[k] === 'unsure') unsure++;
    else if (userConfidence[k] === 'noknow') noknow++;
  });

  document.getElementById('statKnowCount').textContent = know;
  document.getElementById('statUnsureCount').textContent = unsure;
  document.getElementById('statNoknowCount').textContent = noknow;

  const totalTests = quizScore.correct + quizScore.wrong;
  const accuracy = totalTests ? Math.round((quizScore.correct / totalTests) * 100) + '%' : '—';
  document.getElementById('statQuizAccuracy').textContent = accuracy;

  const secList = document.getElementById('statsSectionList');
  if (!secList) return;

  let html = '';
  QD.forEach((sec, si) => {
    const total = sec.q.length;
    let sKnow = 0, sUnsure = 0, sNoknow = 0;
    sec.q.forEach((_, qi) => {
      const c = userConfidence[`q-${si}-${qi}`];
      if (c === 'know') sKnow++;
      else if (c === 'unsure') sUnsure++;
      else if (c === 'noknow') sNoknow++;
    });

    const kPct = total ? (sKnow / total) * 100 : 0;
    const uPct = total ? (sUnsure / total) * 100 : 0;
    const nPct = total ? (sNoknow / total) * 100 : 0;

    html += `
      <div class="stats-section-row">
        <div class="stats-sec-title-row">
          <span>${typograph(sec.s)}</span>
          <span style="font-family:var(--font-mono);color:var(--text-dim)">${sKnow}/${total}</span>
        </div>
        <div class="stats-seg-bar">
          <div class="stats-seg-know" style="width:${kPct}%"></div>
          <div class="stats-seg-unsure" style="width:${uPct}%"></div>
          <div class="stats-seg-noknow" style="width:${nPct}%"></div>
        </div>
        <div class="stats-breakdown-badges">
          <span style="color:var(--know)">✓ ${sKnow} знаю</span>
          <span style="color:var(--unsure)">? ${sUnsure} сомневаюсь</span>
          <span style="color:var(--noknow)">✕ ${sNoknow} не знаю</span>
        </div>
      </div>
    `;
  });
  secList.innerHTML = html;
}

// ── ОБЩИЙ ПРОГРЕСС ──
function updateGlobalProgressBar() {
  let total = 0;
  QD.forEach(s => total += s.q.length);

  let done = 0;
  Object.keys(userConfidence).forEach(k => {
    if (k.startsWith('q-') && userConfidence[k] === 'know') done++;
  });

  const pct = total ? Math.round((done / total) * 100) : 0;
  const bar = document.getElementById('gProgressBar');
  if (bar) bar.style.width = pct + '%';
  const doneEl = document.getElementById('gProgressDone');
  if (doneEl) doneEl.textContent = done;
  const totalEl = document.getElementById('gProgressTotal');
  if (totalEl) totalEl.textContent = total;
}

// ── ПОИСК В САЙДБАРЕ ──
function handleSearchFilter() {
  const val = document.getElementById('sidebarSearchInput').value.toLowerCase().trim();
  const clearBtn = document.getElementById('searchClearBtn');
  if (clearBtn) clearBtn.style.display = val ? 'flex' : 'none';

  let matchFound = false;
  document.querySelectorAll('.q-list-item').forEach(el => {
    const text = el.textContent.toLowerCase();
    const match = !val || text.includes(val);
    el.style.display = match ? 'flex' : 'none';
    if (match) matchFound = true;
  });

  // Скрыть/показать заголовки групп
  document.querySelectorAll('.sec-group').forEach(grp => {
    const visibleItems = grp.querySelectorAll('.q-list-item[style*="display: flex"]');
    grp.style.display = (visibleItems.length > 0 || !val) ? 'block' : 'none';
  });
}

function clearSearchFilter() {
  const inp = document.getElementById('sidebarSearchInput');
  if (inp) { inp.value = ''; handleSearchFilter(); inp.focus(); }
  setScreenState('success');
}

// ── БОКОВОЕ МЕНЮ (SIDEBAR OVERLAY) ──
function toggleSidebar() {
  const sb = document.getElementById('sidebar');
  const ob = document.getElementById('overlayBackdrop');
  const btn = document.getElementById('burgerBtn');
  const list = document.getElementById('sidebarList');
  if (list && list.children.length === 0) {
    renderSidebarList();
  }

  const isOpen = sb.classList.contains('open');
  if (isOpen) {
    closeSidebar();
  } else {
    sb.classList.add('open');
    ob.classList.add('open');
    btn.classList.add('active');
  }
}

function closeSidebar() {
  const sb = document.getElementById('sidebar');
  const ob = document.getElementById('overlayBackdrop');
  const btn = document.getElementById('burgerBtn');
  if (sb) sb.classList.remove('open');
  if (ob) ob.classList.remove('open');
  if (btn) btn.classList.remove('active');
}

function toggleSecOpen(si) {
  const el = document.getElementById(`secItems-${si}`);
  if (el) el.style.display = (el.style.display === 'none') ? 'block' : 'none';
}

// ── ХРАНИЛИЩЕ СОСТОЯНИЯ (LOCALSTORAGE) ──
function loadStorageState() {
  try {
    const saved = localStorage.getItem('anat_conf_v2');
    if (saved) userConfidence = JSON.parse(saved);
  } catch(e) {}
}

function saveStorageState() {
  try {
    localStorage.setItem('anat_conf_v2', JSON.stringify(userConfidence));
  } catch(e) {}
}

// ── КЛАВИАТУРНЫЕ СОКРАЩЕНИЯ ──
window.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;

  if (e.key === 'ArrowRight') {
    navigateItem(1);
  } else if (e.key === 'ArrowLeft') {
    navigateItem(-1);
  } else if (e.key === ' ' || e.key === 'v' || e.key === 'V') {
    e.preventDefault();
    toggleAnswerReveal();
  } else if (e.key === '1') {
    setUserConfidence('noknow');
  } else if (e.key === '2') {
    setUserConfidence('unsure');
  } else if (e.key === '3') {
    setUserConfidence('know');
  } else if (e.key === 'Escape') {
    closeSidebar();
  }
});

// ── ИНИЦИАЛИЗАЦИЯ ПРИ ЗАГРУЗКЕ ──
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  loadStorageState();
  renderSidebarList(); // пререндеринг списка вопросов сразу при старте
  switchMainTab('atlas');
  updateGlobalProgressBar();
});
</script>
</body>
</html>
"""

# Write out the new index.html safely
with open('/Users/atlant/Projects/myProjects/anatomia/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('/Users/atlant/Projects/myProjects/anatomia/anatomy_exam_final.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated new index.html and anatomy_exam_final.html ({len(html_content)} bytes)!")
