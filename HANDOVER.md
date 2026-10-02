# Handover — IGCSE Term Revision site

Handed over from a Claude chat session on 2 Oct 2026. Read `CLAUDE.md` for how the code works; this file covers history, decisions and what is left.

## The situation
- Student: Grade 8, Cambridge IGCSE syllabus (already started), Vaels International School, Chennai. Weak in Physics, Chemistry, Maths and Computer Science. Strong in Biology (so Biology was deliberately left out).
- He works on a **tablet** and prefers an **interactive** approach.
- First-term exams (from the school's portion sheet):
  - **Science — Mon 5 Oct 2026**, 1 h 30, 100 marks, Paper 1 + Paper 2 structured (50 + 50).
    - Physics: Ch 9 Density, Ch 10 Transfer of thermal energy, Ch 11 Sound.
    - Chemistry: Ch 4 Structure of the atom and the periodic table, Ch 5 Chemical bonding and structure, Ch 6 Displacement reactions, Ch 7 Salts.
    - Biology: Ch 1, Ch 2, Ch 13.3–13.4 (not covered: student is strong).
  - **Computer Science — Fri 9 Oct 2026**, 2 h, 80 marks structured. Ch 1 Data representation, Ch 2 Data transmission, Ch 10 Boolean logic. School teaches **Python**.
  - Maths (Mon 28 Sep) already sat.
- Longer-term goal (the original request): a systematic **question-and-answer bank** for Physics, Chemistry, Maths and CS, built from Cambridge past-paper style, with step-by-step calculations and diagrams. The crash packs above were the short-term plan because of the exam dates.

## Decisions made with the parent
1. Crash mode first: compact packs per chapter for this exam, not the full bank.
2. Interactive web pages, not printed sheets. One HTML file per subject.
3. **Highlight the keywords examiners look for** in yellow (`==keyword==`).
4. Hosted on GitHub Pages so the student can use it without a Claude account. Repo: `charlesjoserajcjr-Master/igcse-revision` (public).
5. Worked examples must be explanatory: "Key idea" intro, a "why" line under every step, and an exam tip (done for CS).
6. A **live working table beside the steps** that fills in as he taps Next step (done for CS).

## Status (all pushed to `main`)
- [x] Home page `index.html`
- [x] Physics pack — notes, diagrams, worked examples, drills, quizzes, exam Qs, 32-mark mock
- [x] Chemistry pack — same, plus dot-and-cross / periodic table / reactivity series / salt-prep diagrams, 34-mark mock
- [x] CS pack — same, plus logic gate explorer and circuit simulator ("Try it"), truth-table drill, 33 explanatory worked examples with side working tables, 36-mark mock
- [x] Physics and Chemistry worked examples now explanatory (Key idea, why lines, exam tip, live side table)
- [x] Maths pack `maths.html` (23 topics: the 8 from the term 1 portion list plus 15 more in syllabus order (primes, powers, percentages, algebra skills, Pythagoras, straight lines, transformations, similar shapes, simultaneous equations, quadratics, sets, vectors, cumulative frequency, circles, functions). 132 worked examples, 110 drill generators). Drill kinds `text` and `frac` added.
- [x] Drill generators self-checked (Chemistry 5,100 items, CS 7,200 items: every answer key accepted)

## Layout decision (parent, 2 Oct 2026)
Term 1 packs (`physics.html`, `chemistry.html`, `cs.html`) are frozen and labelled **Term 1 Preparation** on the home page. The whole-year syllabus lives in `maths.html`, `physics-year.html`, `chemistry-year.html`, `cs-year.html` (and a Biology pack later). Term 2 and 3 portion sheets are still awaited; until then chapters follow the Cambridge syllabus order.

## Open tasks (suggested order)
1. **DONE (2 Oct 2026): Physics and Chemistry worked examples → CS style.** Notes live in an `enhance({...})` block before `renderChapter` in each file (intro, why per step, tip, side-table rows). Original brief: add `intro`, `why` lines, `tip`, and side boards where a table helps (e.g. density formula triangle filling in; particle-count table for atoms; ion-charge balancing for formulae; reactivity-series pointer for displacement). Port `updateBoard`, `attach`, the board CSS and the worked-example renderer from `cs.html`. Priority if before Mon 5 Oct.
2. Bring `physics.html` onto the newer engine (proper `<head>`, `sub_`, `judge()` with kinds) so all three share one engine.
3. **In progress:** whole-syllabus packs. Maths has 23 topics so far, in Cambridge 0580 order (still to add: trig for any angle and bearings, inequalities on graphs, loci and constructions, matrices, further probability, travel graphs and rates). Next: get the school's Term 2 and Term 3 portion sheets (Maths, Physics, Chemistry, CS, Biology), then add chapters and a Biology pack. Original note: Next subjects: Maths (portion: equations and inequalities, angles, statistical investigations, shapes and measurements, fractions, sequences and functions, ratio and proportion, probability), then deepen Physics/Chemistry/CS across the full 0625/0620/0478 syllabuses. Suggested structure: one page per subject, topics as tabs, same engine.
4. Optional: a short diagnostic test per subject to find weak topics.
5. Optional: a shared progress view for the parent (would need a backend or a hosted store; currently progress is per-device `localStorage`).

## Full-year Physics progress
`physics-year.html` now covers the whole 0625 course in 18 chapters: Term 1 (Density, Thermal energy transfer, Sound) plus Motion, Forces, Energy/work/power, Pressure, Particles, Waves, Light, EM spectrum, Electric circuits, Magnetism, Measurement, Momentum, Thermal properties, Atoms and radioactivity, Space. Possible additions later: more exam-style questions per chapter, Extended-only topics (e.g. lenses calculations), and the school's Term 2/3 chapter order.

## Full-year Chemistry progress
`chemistry-year.html`: Term 1 chapters (Atoms, Bonding, Displacement, Salts) plus Separation techniques, Formulae/Mr/equations, The mole, Rates, Energetics, Electrolysis, Metals and extraction, Air and water, Hydrocarbons, Alcohols/acids/polymers and Chemical analysis (16 chapters). Still to add: states of matter and diffusion, periodic table groups in detail, more exam questions per chapter.

## Full-year Computer Science progress
`cs-year.html`: Term 1 chapters (Data representation, Data transmission, Boolean logic) plus Hardware, Software, The internet and security, Algorithms and problem solving, Programming in Python and Databases/SQL (9 chapters). Still to add: automated and emerging technologies (robotics, AI, IoT), ethics and the digital divide, more trace-table and pseudocode practice.

## Full-year Biology progress
`biology-year.html` (Cambridge 0610, built on the maths engine, storage key `biopack-v1`) is complete for the core course: 19 chapters in syllabus order: classification, cells, movement into and out of cells, biological molecules, enzymes, plant nutrition, human nutrition, transport in plants, transport in animals, diseases and immunity, gas exchange and respiration, excretion, coordination and response, drugs, reproduction, inheritance, variation and selection, organisms and environment, human influences on ecosystems. Possible additions later: more exam questions per chapter, Extended-only material (nephron detail, ADH, accommodation) and the school's Term 2/3 order.

## Known limitations
- Progress is saved only in the browser on that device.
- GitHub Pages must stay enabled (Settings → Pages → Deploy from branch `main` / root).
- The check-digit example (ISBN-13 weighting) is illustrative; Cambridge does not require that exact algorithm.

## Starter prompt for Claude Code
> Read CLAUDE.md and HANDOVER.md. Then do open task 1 for physics.html and chemistry.html: make every worked example as explanatory as the Computer Science ones (Key idea, a "why" line under each step, exam tip, and a live working table beside the steps where it helps). Run tools/check.py on each page, look at the screenshots, then commit and push.
