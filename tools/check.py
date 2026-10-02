"""Headless check for a revision pack.

Usage:  python tools/check.py cs.html        (or physics.html / chemistry.html)
Needs:  pip install playwright && python -m playwright install chromium

What it does
- Self-checks every drill generator (300 runs each): the generated answer must be
  accepted by the page's own judge(), choices must be unique, tables must be complete.
- Clicks every chapter tab and sub-tab, answers quizzes, ticks mark schemes,
  steps through worked examples and drills.
- Checks there is no sideways scroll at phone width (400 px).
- Saves screenshots of every Diagrams tab and Worked tab to tools/out/.
Prints any page errors at the end. Expect: "bad drills: []" and "errors: []".
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

root = pathlib.Path(__file__).resolve().parent.parent
page_file = root / (sys.argv[1] if len(sys.argv) > 1 else 'cs.html')
out = root / 'tools' / 'out'; out.mkdir(parents=True, exist_ok=True)
stem = page_file.stem

SELF_CHECK = '''() => {
  const bad = []; let n = 0;
  if (typeof DRILLS === 'undefined') return [0, ['no DRILLS']];
  for (const k in DRILLS) for (const g of DRILLS[k]) for (let i = 0; i < 300; i++) {
    const d = g(); n++;
    if (typeof judge !== 'function') { if (typeof d.ans !== 'number' || !isFinite(d.ans)) bad.push([k, d.q]); continue; }
    if (d.kind === 'choice') { if (!(d.ans >= 0) || d.choices.length < 2 || new Set(d.choices).size !== d.choices.length) bad.push([k, d.q, d.choices]); continue; }
    if (d.kind === 'table') { if (d.ans.length !== d.rows.length) bad.push([k, d.q]); continue; }
    drillCur = d; const raw = d.kind === 'num' ? String(Math.round(d.ans * 100) / 100) : d.ans;
    const r = judge(raw); if (!r || !r.ok) bad.push([k, d.q, raw]);
  }
  return [n, bad.slice(0, 10)];
}'''

with sync_playwright() as p:
    b = p.chromium.launch(); errs = []
    pg = b.new_page(viewport={'width': 820, 'height': 1180})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(page_file.as_uri())
    n, bad = pg.evaluate(SELF_CHECK)
    print(f'drill items checked: {n}'); print('bad drills:', bad)
    tabs = [t.get_attribute('data-tab') for t in pg.query_selector_all('[data-tab]')]
    for tab in tabs:
        if tab in ('start', 'mock'): continue
        pg.click(f'[data-tab={tab}]')
        for s in ['learn', 'diagrams', 'lab', 'worked', 'drill', 'quiz', 'exam']:
            if not pg.query_selector(f'[data-sub={s}]'): continue
            pg.click(f'[data-sub={s}]')
            if s == 'diagrams': pg.screenshot(path=str(out / f'{stem}-{tab}-diagrams.png'), full_page=True)
            if s == 'lab':
                for g in ['NOT', 'XOR']: pg.click(f'[data-g={g}]')
                pg.click('#tA'); pg.click('#cC')
            if s == 'worked':
                for btn in pg.query_selector_all('[data-all]'): btn.click()
                pg.screenshot(path=str(out / f'{stem}-{tab}-worked.png'), full_page=True)
            if s == 'quiz':
                for q in pg.query_selector_all('[data-quiz]'): q.query_selector('[data-o="0"]').click()
            if s == 'exam':
                pg.click('[data-ms]'); pg.click('[data-pt]')
            if s == 'drill':
                for _ in range(12):
                    if pg.query_selector('#tcheck'):
                        for c in pg.query_selector_all('[data-tc]'): c.click()
                        pg.click('#tcheck')
                    elif pg.query_selector('#dch'): pg.click('#dch .opt >> nth=0')
                    else: pg.fill('#dans', '1'); pg.click('form button[type=submit]')
                    pg.click('#dnext')
    pg.click('[data-tab=mock]'); pg.click('[data-tab=start]')
    pg.set_viewport_size({'width': 400, 'height': 900})
    width = pg.evaluate('document.documentElement.scrollWidth')
    print('page width at 400px viewport:', width, '(OK)' if width <= 400 else '(SIDEWAYS SCROLL!)')
    print('errors:', errs)
    print('screenshots in', out)
    b.close()
