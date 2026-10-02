# IGCSE Term Revision site — project guide for Claude

## What this is
A static, interactive revision website for a Grade 8 student (Cambridge IGCSE, Vaels International School, Chennai) preparing for first-term exams. It is used on a **tablet**, by a student who finds Physics, Chemistry, Maths and Computer Science hard. The parent (Capt. Charles) commissions the work and is usually at sea, so he communicates briefly and wants direct, structured answers with clear next steps.

Live site (GitHub Pages, branch `main`, root): https://charlesjoserajcjr-master.github.io/igcse-revision/

## Files
| File | What it is |
|---|---|
| `index.html` | Home page linking the subject packs. Add a card here for every new pack. |
| `physics.html` | Physics pack: Ch 9 Density, Ch 10 Thermal energy transfer, Ch 11 Sound. Oldest engine (see below). |
| `chemistry.html` | Chemistry pack: Ch 4 Atoms and periodic table, Ch 5 Bonding, Ch 6 Displacement, Ch 7 Salts. |
| `maths.html` | Maths pack (0580): equations, angles, statistics, shapes, fractions, sequences, ratio, probability. Built on the chemistry engine plus `text`/`frac` drill kinds. Worked examples carry `intro`, `tip`, `f`, per-step why and `r` rows for the side table. |
| `physics-year.html`, `chemistry-year.html`, `cs-year.html` | Full-year packs. Start as copies of the Term 1 packs (own progress keys `physyear-v1`, `chemyear-v1`, `csyear-v1`) and grow chapter by chapter in syllabus order. |
| `cs.html` | Computer Science pack (0478): Ch 1 Data representation, Ch 2 Data transmission, Ch 10 Boolean logic. Newest engine. |
| `tools/check.py` | Headless-browser test: clicks every tab, self-checks every drill generator, screenshots diagrams. Run it before every push. |
| `HANDOVER.md` | Project history, decisions, status and the to-do list. Read it first. |

Each pack is **one self-contained HTML file**: inline CSS + inline JS + inline SVG diagrams. No build step, no framework, no external JS. Only Google Fonts are loaded from outside.

## How each pack is built
- **Data object `CH`**: one entry per chapter with `learn` cards, `mistakes`, `diagrams` (functions returning SVG strings), `worked` examples, `drill` key, `quiz`, `exam` questions.
- **Sub-tabs per chapter**: Learn · Diagrams · (Try it, CS logic only) · Worked · Drill · Quiz · Exam Qs. Plus a Start page and a timed Mini mock (`MOCK` = list of `[chapterKey, examIndex]`).
- **Keyword highlighting**: wrap examiner keywords in `==double equals==`; `fmt()` turns them into yellow `<mark class="kw">`. The parent explicitly asked for this. Use it in notes, mark schemes and explanations.
- **Worked examples** (`s` = steps): `[label, working, why?, board?]`.
  - `working` can be a string or a function returning HTML (use functions for anything that calls helpers defined later in the file).
  - `why` (CS only so far) = one-line plain-English explanation shown under the step.
  - `board` (CS only) = function returning the "Working table" HTML shown beside the steps; `w.board0` is the empty starting table. `attach(w, board0, [boards…])` wires them up.
  - Optional `intro` ("Key idea" box) and `tip` ("Exam tip", revealed after the last step). `prose:true` switches the step font from mono to body.
- **Drills** are random generators in `DRILLS[key]` returning `{kind, q, ans, s, …}`. Kinds: `num` (with `tol`), `choice` (`choices`, `ans` = index), `config` (e.g. 2,8,1), `formula` (case-checked chemical formula), `bits` (8-bit binary), `text` (hex / RLE, case-insensitive), `table` (tap-to-fill truth table). `judge()` marks typed answers.
- **Exam questions**: `{q, m (marks), p: [marking points]}`. The student writes on paper, then taps each point he got; score = min(ticks, marks).
- **Progress** is stored in `localStorage` (keys `physpack-v1`, `chempack-v1`, `cspack-v1`) — per device only.
- **Theme**: CSS tokens on `:root` with a `prefers-color-scheme: dark` block. Every colour must come from a token (diagrams included) so both themes work.

Engine differences: `physics.html` is the first version (variable `sub`, numeric-only drills, steps without `why`/boards, artifact-style head). `chemistry.html` added drill kinds, tables in cards, the `sub_` variable. `cs.html` added `bits`/`text`/`table` drills, the logic lab (`renderLab`/`drawLab`), explanatory worked examples and side boards. When upgrading physics/chemistry, port features from `cs.html`.

## Term 1 freeze
`physics.html`, `chemistry.html` and `cs.html` are the Term 1 Preparation packs. Do **not** edit them until the Term 1 exams are over (Science Mon 5 Oct, CS Fri 9 Oct 2026). All new chapters go into `maths.html` and the `*-year.html` files.

## Content rules
- Syllabus: Cambridge IGCSE (Physics 0625, Chemistry 0620, Computer Science 0478). Match Cambridge wording and mark-scheme style. The CS paper is **non-calculator**.
- Audience: a 13-year-old who struggles. Short sentences, plain words, one idea per line. Calculations always shown as formula → substitution → answer with unit.
- Do not copy past-paper questions into the site; write original Cambridge-style questions and link to the past-paper sites (PapaCambridge, Past Papers Academy).
- Check every number you write. For drills, `tools/check.py` verifies that each generated answer is accepted by `judge()`.
- British spelling (colour, sulfate, aluminium) as Cambridge uses.

## Design rules
- Tablet first (about 820 px wide), must also work at 400 px with no sideways scroll.
- Lab-notebook look: cool grey graph-paper background, deep blue accent, orange for "hot"/current, yellow marker for keywords. Fonts: Bricolage Grotesque (headings), Atkinson Hyperlegible (body), JetBrains Mono (working).
- No emoji. No `alert()`/`confirm()`.

## Workflow
1. Edit the HTML file(s).
2. Run the checks (needs Python + Playwright: `pip install playwright && python -m playwright install chromium`):
   `python tools/check.py cs.html` (or `physics.html`, `chemistry.html`). It must print `errors []` and an empty bad-drill list. Look at the screenshots in `tools/out/`.
3. Commit and push to `main`. GitHub Pages republishes in 1–2 minutes; the student may need to refresh.
