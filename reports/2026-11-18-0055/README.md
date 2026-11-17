# Anatomia: current product look

Report date: 2026-11-18 (Europe/Moscow). All finished-state images below were captured afresh for this report; none are reused from the earlier /tmp review.

Product commit: `c14fc8670c091a12fe30439d2eb51c2586bcd2be`. Report-only follow-up: no application source, map style, map logic, learning data or stored user text changed.

## Factual scope

Academic atlas frame and dossier refinement, authored system/navigation icons, and interface emoji replacement in both HTML entry points. Existing interactive SVG nodes and learning behaviors retained. The main mobile viewport shows the atlas illustration; the dossier remains below it in the existing scrollable stage.

## Latest primary screenshots

| Theme | Desktop 1440 × 1000 | Mobile 375 × 1000 |
| --- | --- | --- |
| Light | [Screenshot](anatomia-atlas-light-desktop-1440x1000.png) | [Screenshot](anatomia-atlas-light-mobile-375x1000.png) |
| Dark | [Screenshot](anatomia-atlas-dark-desktop-1440x1000.png) | [Screenshot](anatomia-atlas-dark-mobile-375x1000.png) |

Absolute paths, UTC capture times, viewport sizes, and per-capture overflow results are recorded in [manifest.json](manifest.json).

## Additional current screens

| View | Theme | Viewport | Screenshot |
| --- | --- | --- | --- |
| questions | light | 1440 × 1000 | [PNG](anatomia-questions-light-desktop-1440x1000.png) |
| tasks | light | 1440 × 1000 | [PNG](anatomia-tasks-light-desktop-1440x1000.png) |
| quiz | light | 1440 × 1000 | [PNG](anatomia-quiz-light-desktop-1440x1000.png) |
| stats | light | 1440 × 1000 | [PNG](anatomia-stats-light-desktop-1440x1000.png) |
| questions | light | 375 × 1000 | [PNG](anatomia-questions-light-mobile-375x1000.png) |
| tasks | light | 375 × 1000 | [PNG](anatomia-tasks-light-mobile-375x1000.png) |
| quiz | light | 375 × 1000 | [PNG](anatomia-quiz-light-mobile-375x1000.png) |
| stats | light | 375 × 1000 | [PNG](anatomia-stats-light-mobile-375x1000.png) |
| questions | dark | 1440 × 1000 | [PNG](anatomia-questions-dark-desktop-1440x1000.png) |
| tasks | dark | 1440 × 1000 | [PNG](anatomia-tasks-dark-desktop-1440x1000.png) |
| quiz | dark | 1440 × 1000 | [PNG](anatomia-quiz-dark-desktop-1440x1000.png) |
| stats | dark | 1440 × 1000 | [PNG](anatomia-stats-dark-desktop-1440x1000.png) |
| questions | dark | 375 × 1000 | [PNG](anatomia-questions-dark-mobile-375x1000.png) |
| tasks | dark | 375 × 1000 | [PNG](anatomia-tasks-dark-mobile-375x1000.png) |
| quiz | dark | 375 × 1000 | [PNG](anatomia-quiz-dark-mobile-375x1000.png) |
| stats | dark | 375 × 1000 | [PNG](anatomia-stats-dark-mobile-375x1000.png) |

## Before / after proof

- [Historical before: light desktop](historical-before-light-desktop-1440x1000.png). This is explicitly an earlier baseline, not a current screenshot.
- [Fresh after: light desktop](anatomia-atlas-light-desktop-1440x1000.png).

## Verification and limits

- Fresh capture set: 20 PNGs; desktop/mobile and light/dark coverage.
- No document-level horizontal overflow was detected in this capture set.
- No HTTP errors or non-abort failed network requests were recorded. Raw manifest includes requests cancelled by navigation/reload (`net::ERR_ABORTED`); these are retained for transparency.
- Earlier implementation validation passed: interaction smoke checks, checked text/button contrast pairs (≥4.5:1), reduced-motion checks and interface emoji audit. Semantic check/cross text remains; learning content was preserved.
- TeaMap production build and lint passed during implementation; MapLibre still produces the existing large-chunk warning. Anatomia is static HTML/CSS and has no build step.
- This report records observed presentation and selected flows; it does not claim exhaustive learning, accessibility or security testing.

## Gallery handoff

Copy the dated report folder as a unit to retain screenshots and manifest. Exact absolute source paths are above and in the manifest. No files were written to Documents by this task.
