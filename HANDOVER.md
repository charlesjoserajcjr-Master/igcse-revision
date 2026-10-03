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
- [x] Maths pack `maths.html` (32 topics, incl. 3D shapes (nets, symmetry, sphere/cone/pyramid), place value/rounding/bounds, recurring decimals and exchange rates, bearings/sine and cosine rules, travel graphs, tree diagrams, inequality regions, loci, matrices; originally 23: the 8 from the term 1 portion list plus 15 more in syllabus order (primes, powers, percentages, algebra skills, Pythagoras, straight lines, transformations, similar shapes, simultaneous equations, quadratics, sets, vectors, cumulative frequency, circles, functions). 132 worked examples, 110 drill generators). Drill kinds `text` and `frac` added.
- [x] Drill generators self-checked (Chemistry 5,100 items, CS 7,200 items: every answer key accepted)

## Layout decision (parent, 2 Oct 2026)
Term 1 packs (`physics.html`, `chemistry.html`, `cs.html`) are frozen and labelled **Term 1 Preparation** on the home page. The whole-year syllabus lives in `maths.html`, `physics-year.html`, `chemistry-year.html`, `cs-year.html` (and a Biology pack later). Term 2 and 3 portion sheets are still awaited; until then chapters follow the Cambridge syllabus order.

## Open tasks (suggested order)
1. **DONE (2 Oct 2026): Physics and Chemistry worked examples → CS style.** Notes live in an `enhance({...})` block before `renderChapter` in each file (intro, why per step, tip, side-table rows). Original brief: add `intro`, `why` lines, `tip`, and side boards where a table helps (e.g. density formula triangle filling in; particle-count table for atoms; ion-charge balancing for formulae; reactivity-series pointer for displacement). Port `updateBoard`, `attach`, the board CSS and the worked-example renderer from `cs.html`. Priority if before Mon 5 Oct.
2. Bring `physics.html` onto the newer engine (proper `<head>`, `sub_`, `judge()` with kinds) so all three share one engine.
3. **In progress:** whole-syllabus packs. Maths has 32 topics so far, in Cambridge 0580 order (next, from the 15 past papers analysed 2 Oct 2026: quadratic and cubic curves, tables of values and calculus basics (Extended); stem-and-leaf and mean from a frequency table. Matrices and loci appear rarely or never in the 15 papers, so treat them as low priority.). Next: get the school's Term 2 and Term 3 portion sheets (Maths, Physics, Chemistry, CS, Biology), then add chapters and a Biology pack. Original note: Next subjects: Maths (portion: equations and inequalities, angles, statistical investigations, shapes and measurements, fractions, sequences and functions, ratio and proportion, probability), then deepen Physics/Chemistry/CS across the full 0625/0620/0478 syllabuses. Suggested structure: one page per subject, topics as tabs, same engine.
4. Optional: a short diagnostic test per subject to find weak topics.
5. Optional: a shared progress view for the parent (would need a backend or a hosted store; currently progress is per-device `localStorage`).

## Full-year Physics progress
`physics-year.html` now covers the whole 0625 course in 18 chapters: Term 1 (Density, Thermal energy transfer, Sound) plus Motion, Forces, Energy/work/power, Pressure, Particles, Waves, Light, EM spectrum, Electric circuits, Magnetism, Measurement, Momentum, Thermal properties, Atoms and radioactivity, Space. Possible additions later: more exam-style questions per chapter, Extended-only topics (e.g. lenses calculations), and the school's Term 2/3 chapter order.

## Full-year Chemistry progress
`chemistry-year.html`: Term 1 chapters (Atoms, Bonding, Displacement, Salts) plus Separation techniques, Formulae/Mr/equations, The mole, Rates, Energetics, Electrolysis, Metals and extraction, Air and water, Hydrocarbons, Alcohols/acids/polymers and Chemical analysis (16 chapters). Now also has states of matter, redox and industry, empirical formulae, fertilisers and polymers/proteins chapters (20 chapters). Still to add: more exam questions per chapter.

## Full-year Computer Science progress
`cs-year.html`: Term 1 chapters (Data representation, Data transmission, Boolean logic) plus Hardware, CPU architecture and interrupts, Software, The internet and security, Automated and emerging technologies, Algorithms and problem solving, Pseudocode and testing, Programming in Python and Databases/SQL (12 chapters). Still to add: ethics and the digital divide, more exam questions.

## Full-year Biology progress
`biology-year.html` (Cambridge 0610, built on the maths engine, storage key `biopack-v1`) is complete for the core course: 19 chapters in syllabus order: classification, cells, movement into and out of cells, biological molecules, enzymes, plant nutrition, human nutrition, transport in plants, transport in animals, diseases and immunity, gas exchange and respiration, excretion, coordination and response, drugs, reproduction, inheritance, variation and selection, organisms and environment, human influences on ecosystems. Possible additions later: more exam questions per chapter, Extended-only material (nephron detail, ADH, accommodation) and the school's Term 2/3 order.

## Mock papers follow the Cambridge 0580 pattern (Maths, 2 Oct 2026)
Measured from 15 past papers (2025 and 2026, supplied by the parent; stored outside the repo because they are copyrighted):
- **Core** (Paper 1 non-calculator, Paper 3 calculator): 80 marks, 1 h 30, about 25 questions in about 45 parts. Parts are mostly 1 and 2 marks (about 55% of parts are 1 mark, 35% are 2 marks, about 10% are 3 to 4 marks).
- **Extended** (Paper 2 non-calculator, Paper 4 calculator): 100 marks, 2 h, about 24 questions in about 44 parts, mostly 2 and 3 marks.
- Papers start with easy number questions and get harder; a question often has parts (a), (b), (c).
`maths.html` now has `PAPERS` (four paper types), `buildMock()` and a paper chooser on the Mock paper tab. Each paper is built to the exact mark total from: (a) 1 and 2 mark parts made from the drill generators (grouped into questions of 1 to 4 parts, answer and method shown as the mark scheme) and (b) 3 to 5 mark questions from each chapter's exam bank. Topic mix targets about 30% number, 22% algebra, 24% geometry, 10% graphs, 14% statistics and probability. Non-calculator papers leave out calculator topics (Pythagoras and trig, bearings, 3D, circles, loci) and any wording that needs a calculator. Core leaves out cumulative frequency, functions and quadratics. Matrices appear in none of the 15 papers, so they are never used in mocks. `tools/check.py` checks 40 builds of every paper type for exact totals, duplicates and calculator rules.
Not done yet: the other packs (Physics, Chemistry, CS, Biology) still use the older Mini mock. Match them to the real paper layout when the parent shares past papers for those subjects.

## CS mock papers follow the Cambridge 0478 pattern (2 Oct 2026)
Measured from five Oct/Nov 2025 papers (Paper 1 variants 11, 12, 13 and Paper 2 variants 21, 22; kept outside the repo because they are copyrighted):
- **Paper 1 Computer Systems**: 75 marks, 1 h 45, no calculator. 6 or 7 questions of about 10 to 13 marks, each made of many short parts (about 45% are 1 mark). Question 1 is always data representation. Topics: data representation, data transmission, hardware (Von Neumann CPU, interrupts), software, the internet and security, automated and emerging technologies (robots, AI, embedded systems).
- **Paper 2 Algorithms, Programming and Logic**: 75 marks, 1 h 45, no calculator. About 11 questions; the last is a 15 mark program. Pseudocode is used throughout (finding errors, completing code, trace tables, flowcharts, 1D and 2D arrays, procedures), plus SQL, logic circuits and truth tables, validation and test data.
- `cs-year.html` now has `PAPERS` (`p1`, `p2`), `buildMock()` and a paper chooser on the Mock paper tab. Parts of 1 and 2 marks come from the drill generators (two quick questions are paired into one 2 mark part); 3 to 6 mark parts come from the exam banks (`EXTRA` adds about 30 new Cambridge-style questions, including three 15 mark programming tasks). Parts are grouped into numbered questions of about 9 to 13 marks (Paper 1) or 4 to 9 marks (Paper 2), and the programming task is last.
- New chapters added because the papers need them: CPU architecture, buses and interrupts (`hw2`), Automated and emerging technologies (`emerg`), Pseudocode, trace tables and testing (`pseudo`). The Term 1 pack `cs.html` is unchanged.
Still to do for CS: more 4 to 6 mark exam questions per chapter (the banks are thin, so mocks will repeat questions), SQL keyword-matching questions, flowchart and structure-diagram questions, file handling, 2D array tasks, and a drill for logic circuits written as text.

## Chemistry multiple-choice papers follow the Cambridge 0620 pattern (3 Oct 2026)
Measured from seven papers (Paper 1 Core variants 11 (two sessions), 12, 13 and Paper 2 Extended variants 21, 22, 23; one file, 0620_s26_qp_13, was sent twice; kept outside the repo because they are copyrighted). All five are multiple choice: 40 questions, 40 marks, 45 minutes, four options A to D, one mark each, calculator allowed, Periodic Table printed in the paper. The questions follow the syllabus order: states of matter, atoms, bonding, stoichiometry, electrochemistry, energetics, reactions (rates, redox, reversible), acids and salts, the Periodic Table, metals, environment, organic chemistry, experimental techniques and analysis. Core paper: states 1, atoms 3, bonding 3, stoichiometry 3, electrochemistry 3, energetics 2, reactions 3, acids 3, periodic 3, metals 3, environment 3, organic 6, experimental 4. Extended paper: 3, 3, 2, 3, 3, 2, 3, 4, 2, 3, 3, 7, 2.
- `chemistry-year.html` has an **MC paper** tab (`MC_TOPICS`, `buildMC()`): Paper 1 (Core) and Paper 2 (Extended) style, built from every chapter's quiz bank in syllabus order, answered by tapping A to D, marked at the end with a score out of 40, a per-topic breakdown and the explanation for every question. A printed-style Periodic Table (`periodicFull()`) is on the page. Extended-only items carry `x: 1` (and the mole and empirical formula chapters are Extended-only). Periodic Table items are tagged `t: 'periodic'`. The check script verifies 40 unique questions with four distinct options.
- New chapters because the papers need them: States of matter and diffusion, Redox, reversible reactions and industry (Haber, Contact, fuel cells), Empirical formulae and percentage calculations (Extended), Fertilisers and the environment, Polymers, proteins and plastics. About 80 new Cambridge-style multiple-choice questions were added to the older chapters' quizzes.
- The old structured **Mini mock** is kept and renamed Theory mock. Cambridge Paper 3 (Core) and Paper 4 (Extended) are structured theory papers (80 marks, 1 h 15); no examples have been supplied yet, so the Theory mock has not been aligned. Send those papers to do it.
Still to do for Chemistry: the question pools are thin for some topics (states of matter, the Periodic Table, energetics have only 8 to 11 questions each), so MC papers will repeat questions after a few attempts; Paper 5 and 6 (practical) are not covered.

## Known limitations
- Progress is saved only in the browser on that device.
- GitHub Pages must stay enabled (Settings → Pages → Deploy from branch `main` / root).
- The check-digit example (ISBN-13 weighting) is illustrative; Cambridge does not require that exact algorithm.

## Starter prompt for Claude Code
> Read CLAUDE.md and HANDOVER.md. Then do open task 1 for physics.html and chemistry.html: make every worked example as explanatory as the Computer Science ones (Key idea, a "why" line under each step, exam tip, and a live working table beside the steps where it helps). Run tools/check.py on each page, look at the screenshots, then commit and push.
