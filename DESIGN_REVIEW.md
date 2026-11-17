# Anatomia — design review, 2026-11-17

Scope: presentation, responsive layout, keyboard accessibility and assets. Continued saved Claude edits; retained learning data, medical text, confidence storage, quiz generation and existing answer/navigation handlers. Original `anatomy_exam_final.html` remains unchanged; the reviewed app is `index.html`.

Direction: an academic anatomical atlas, parchment/graphite surfaces and carmine accents, with Playfair Display headings and Manrope UI. Retained interactive anatomical SVG, replaced the unrelated studio monogram with a book symbol, removed duplicate emoji decoration, reduced four requested font families to two. Company methodology supplies layout/accessibility principles, not product branding.

## Review passes and commits

- `713db02`: redesigned atlas hierarchy, organ dossier, typography and responsive surfaces; replaced clipped mobile header navigation with a labelled bottom tab bar. Developer state controls are available through `?review`, rather than normal study navigation.
- `1a67918`: fixed quiz overflow revealed by rendered checks. Added a styled section picker with wrapping options, bounded popup, selected state, Escape/Tab and arrow/Home/End/Enter support. It uses the existing select and change handler as its data source.
- `ca29a23`: restored CSS visibility of the shared question card in task mode; synchronized tab selection, keyboard traversal and layer pressed states. No task/quiz data processing changed.
- Follow-up: compacted the header at 320px after a font-loaded check found a remaining off-screen theme button.

## Verification

- Actual Chromium screenshots reviewed before and after changes, including atlas, questions, tasks, quiz, statistics and both themes.
- Final Playwright sweep: five tabs × six widths (320, 375, 768, 1024, 1280, 1440) × two themes. No document/main-panel horizontal overflow or off-screen header buttons. No page JavaScript errors.
- axe-core WCAG A/AA tag checks: zero violations in the ten reviewed tab/theme states at 1440px. This is automated coverage, not full WCAG conformance.
- Picker opened and measured within viewport at 375px and 1280px; keyboard End/Enter changed the original select value and closed the popup. Existing screen-state controls exercised for loading/error/empty/success.
- Additional manual automation: tab-bar ArrowRight navigation, theme toggle, answer reveal and mobile organ dossier capture. `node --check atlas-ui.js` and `git diff --check` pass. This is a static HTML app, with no npm build step.

Evidence: `design-review/audit.json` and locally saved `design-review/*.png` screenshots. The delivered gallery includes selected desktop/mobile screenshots.

## Limits

No Lighthouse performance score, screen-reader study, real-device testing, user study or medical-content verification performed. External Google Fonts remain. The small SVG organ targets retain their existing geometry; their keyboard alternatives are available, but this does not certify every pointer target as 44px. Existing typography/rendering helpers and data-related behavior were preserved. Server/security and dependency audits are outside this design-only change.
