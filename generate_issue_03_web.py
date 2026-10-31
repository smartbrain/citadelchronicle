#!/usr/bin/env python3
"""
Generate Web Reader for Issue 03 and update index.html, issue-03.html, and edition switchers.
"""

import os
import re

WORKING_DIR = "/home/don/citadelchronicle"

with open(os.path.join(WORKING_DIR, "build_issue_03.py")) as f:
    text = f.read()

def get_var(name):
    pattern = rf'{name} = """(.*?)"""'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    raise ValueError(f"Var {name} not found")

PAGE_1_HTML = get_var("PAGE_1_HTML")
PAGE_2_HTML = get_var("PAGE_2_HTML")
PAGE_3_HTML = get_var("PAGE_3_HTML")
PAGE_4_HTML = get_var("PAGE_4_HTML")

# Build the complete standalone web reader
WEB_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THE CITADEL CHRONICLE — Issue No. 03 (28 October 2026)</title>
    <meta name="description" content="Issue No. 03 of The Citadel Chronicle: 'He-Who-Must-Not-Be-Named' Blamed for Tilapia, St. Mungo's 14-Day Arithmancy, The Enclosure of the Commons, and Liquidation Lady.">
    <!-- Tailwind CSS for structural utilities -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Classic Broadsheet, Blackletter, Thai & Cypherpunk Monospace -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=EB+Garamond:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600&family=Playfair+Display:ital,wght@0,700;0,900;1,400;1,700&family=Pridi:wght@400;600;700&family=Sarabun:wght@400;600;700&family=UnifrakturMaguntia&display=swap" rel="stylesheet">

    <style>
        :root {{
            --paper-bg: #f5f0e6;
            --paper-bg-alt: #ece4d4;
            --ink-primary: #12110f;
            --ink-secondary: #38342e;
            --ink-accent: #8b1e1e;
            --rule-color: #1a1a1a;
            --halftone-dot: rgba(18, 17, 15, 0.16);
        }}

        body.dark-ink {{
            --paper-bg: #141311;
            --paper-bg-alt: #1e1c19;
            --ink-primary: #ded8cb;
            --ink-secondary: #a8a090;
            --ink-accent: #e05d58;
            --rule-color: #4a453d;
            --halftone-dot: rgba(222, 216, 203, 0.12);
        }}

        * {{
            box-sizing: border-box;
        }}

        body {{
            background-color: #23211e;
            color: var(--ink-primary);
            font-family: 'EB Garamond', Georgia, serif;
            margin: 0;
            padding: 16px 8px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }}

        .a4-page {{
            width: 794px;
            max-width: 100%;
            min-height: 1123px;
            margin: 0 auto 36px auto;
            padding: 24px 28px;
            background-color: var(--paper-bg);
            background-image: 
                radial-gradient(rgba(120, 100, 70, 0.06) 1px, transparent 0),
                linear-gradient(to right, rgba(0,0,0,0.02) 1px, transparent 1px);
            background-size: 24px 24px, 100% 100%;
            box-shadow: 
                0 0 0 1px rgba(0,0,0,0.35),
                0 18px 45px rgba(0, 0, 0, 0.65),
                0 4px 12px rgba(0, 0, 0, 0.4);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            box-sizing: border-box;
        }}

        .a4-page::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            pointer-events: none;
            background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(0,0,0,0.04) 100%);
        }}

        /* Spreads: A3 Landscape (Two A4 Pages Side-by-Side) */
        .spread-wrapper {{
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: stretch;
            gap: 2px;
            max-width: 1600px;
            margin: 0 auto 36px auto;
            background-color: #1a1917;
            padding: 6px;
            border-radius: 4px;
            box-shadow: 0 25px 60px rgba(0,0,0,0.85);
        }}

        .spread-wrapper .a4-page {{
            margin: 0;
            box-shadow: none;
            border-radius: 0;
        }}

        .spread-wrapper .page-left {{
            border-right: 1px dashed rgba(0,0,0,0.3);
            border-top-right-radius: 0;
            border-bottom-right-radius: 0;
        }}
        .spread-wrapper .page-right {{
            border-left: 1px dashed rgba(0,0,0,0.3);
            border-top-left-radius: 0;
            border-bottom-left-radius: 0;
        }}

        /* Typography */
        .font-masthead {{
            font-family: 'UnifrakturMaguntia', 'Cinzel Decorative', serif !important;
            letter-spacing: -0.02em;
        }}
        .font-headline {{
            font-family: 'Playfair Display', Georgia, serif;
        }}
        .font-mono-tech {{
            font-family: 'Courier Prime', monospace;
        }}

        .drop-cap::first-letter {{
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 3.1rem;
            float: left;
            line-height: 0.8;
            padding-top: 2px;
            padding-right: 6px;
            font-weight: 900;
            color: var(--ink-primary);
        }}

        /* Mobile Reader Mode */
        @media (max-width: 768px) {{
            body {{
                padding: 4px 2px;
            }}
            .a4-page {{
                padding: 16px 14px;
                min-height: auto;
                margin-bottom: 24px;
            }}
            .a4-sheet-inner > div {{
                display: flex !important;
                flex-direction: column !important;
            }}
            [style*="column-count"] {{
                column-count: 1 !important;
                column-rule: none !important;
            }}
            [style*="grid-template-columns"] {{
                grid-template-columns: 1fr !important;
            }}
            p {{
                font-size: 10.5pt !important;
                line-height: 1.5 !important;
                text-indent: 0 !important;
            }}
        }}

        .active-mode {{
            background-color: #8b1e1e !important;
            color: #ffffff !important;
            border-color: #8b1e1e !important;
        }}
    </style>
</head>
<body class="desktop-force">

    <!-- TOP CONTROL TOOLBAR -->
    <header class="no-print max-w-6xl mx-auto mb-6 bg-stone-900 border border-stone-700 text-stone-200 p-3 rounded-lg shadow-2xl flex flex-wrap items-center justify-between gap-3 text-xs font-mono">
        <div class="flex flex-wrap items-center gap-2">
            <!-- ISSUE SELECTOR -->
            <div class="flex items-center gap-1 bg-black/60 p-1 rounded border border-amber-600/50">
                <span class="font-bold text-amber-500 uppercase tracking-wider text-[11px] px-1">EDITION:</span>
                <a href="index.html" id="navIssue03" class="px-2.5 py-1 rounded text-xs font-bold transition bg-amber-600 text-stone-950 font-extrabold shadow" title="Currently viewing Issue No. 03 (Latest Release)">🗞️ No. 03 (Oct 28)</a>
                <a href="issue-02.html" id="navIssue02" class="px-2.5 py-1 rounded text-xs font-bold transition bg-stone-800 text-stone-300 hover:bg-stone-700 hover:text-white border border-stone-600" title="Switch to Issue No. 02">🏛️ No. 02</a>
                <a href="issue-01.html" id="navIssue01" class="px-2.5 py-1 rounded text-xs font-bold transition bg-stone-800 text-stone-300 hover:bg-stone-700 hover:text-white border border-stone-600" title="Switch to Issue No. 01">🏛️ No. 01</a>
            </div>
            <span class="font-bold tracking-widest text-amber-500 uppercase hidden sm:inline">THE CITADEL CHRONICLE</span>
        </div>

        <!-- VIEW SELECTOR BUTTONS -->
        <div class="flex flex-wrap items-center gap-1.5" id="viewControls">
            <button onclick="setViewMode('mobile')" id="btnMobile" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">📱 Mobile (1-Col)</button>
            <button onclick="setViewMode('p1')" id="btnP1" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">P1 (Front)</button>
            <button onclick="setViewMode('p2')" id="btnP2" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">P2 (Editorial)</button>
            <button onclick="setViewMode('p3')" id="btnP3" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">P3 (Morgue)</button>
            <button onclick="setViewMode('p4')" id="btnP4" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">P4 (Back)</button>
            <button onclick="setViewMode('center-spread')" id="btnCenterSpread" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">Center Spread (P2+P3)</button>
            <button onclick="setViewMode('outer-spread')" id="btnOuterSpread" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">Outer Spread (P4+P1)</button>
            <button onclick="setViewMode('all-pages')" id="btnAllPages" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition active-mode">All 4 Pages</button>
        </div>

        <!-- ACTIONS & DOWNLOADS -->
        <div class="flex items-center gap-2">
            <button onclick="toggleDarkInk()" id="btnInkMode" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 text-stone-300">🌙 Inky</button>
            <a href="citadel_chronicle_issue03.pdf" download class="px-2.5 py-1 bg-amber-700 hover:bg-amber-600 text-white rounded font-bold shadow">🖨️ Vector PDF</a>
        </div>
    </header>

    <!-- TOAST NOTIFICATION -->
    <div id="toast" class="fixed bottom-6 right-6 bg-stone-900 border border-amber-600 text-amber-200 px-4 py-2 rounded shadow-2xl font-mono text-xs opacity-0 transition-opacity duration-300 pointer-events-none z-50"></div>

    <!-- MAIN PAGES CONTAINER -->
    <main id="chronicleRoot">
        <div class="a4-page" id="page1-wrap">
            <div class="a4-sheet-inner">
                {PAGE_1_HTML}
            </div>
        </div>
        <div class="a4-page" id="page2-wrap">
            <div class="a4-sheet-inner">
                {PAGE_2_HTML}
            </div>
        </div>
        <div class="a4-page" id="page3-wrap">
            <div class="a4-sheet-inner">
                {PAGE_3_HTML}
            </div>
        </div>
        <div class="a4-page" id="page4-wrap">
            <div class="a4-sheet-inner">
                {PAGE_4_HTML}
            </div>
        </div>
    </main>

    <!-- FOOTER INFO -->
    <footer class="max-w-4xl mx-auto my-8 text-center text-stone-500 font-mono text-xs">
        <div>THE CITADEL CHRONICLE • ISSUE NO. 03 • 28 OCTOBER 2026 • PATHUM THANI, THAILAND</div>
        <div class="mt-1">P2P Physical Distribution &amp; Zero-Tracking Static Web Reader • All Rights Reserved to Satoshi Nakamoto</div>
    </footer>

    <script>
        function showToast(msg) {{
            const t = document.getElementById('toast');
            t.innerText = msg;
            t.style.opacity = '1';
            setTimeout(() => {{ t.style.opacity = '0'; }}, 2400);
        }}

        function setViewMode(mode) {{
            const root = document.getElementById('chronicleRoot');
            const p1 = document.getElementById('page1-wrap');
            const p2 = document.getElementById('page2-wrap');
            const p3 = document.getElementById('page3-wrap');
            const p4 = document.getElementById('page4-wrap');

            document.querySelectorAll('#viewControls button').forEach(b => b.classList.remove('active-mode'));
            root.className = '';
            root.innerHTML = '';
            [p1, p2, p3, p4].forEach(p => p.classList.remove('hidden', 'page-left', 'page-right'));

            if (mode === 'mobile') {{
                document.body.classList.add('mobile-mode');
                document.getElementById('btnMobile').classList.add('active-mode');
                root.appendChild(p1);
                root.appendChild(p2);
                root.appendChild(p3);
                root.appendChild(p4);
                showToast("📱 MOBILE MODE: SINGLE COLUMN STREAM");
            }} else if (mode === 'p1') {{
                root.appendChild(p1);
                document.getElementById('btnP1').classList.add('active-mode');
                showToast("SHOWING PAGE 1: FRONT COVER");
            }} else if (mode === 'p2') {{
                root.appendChild(p2);
                document.getElementById('btnP2').classList.add('active-mode');
                showToast("SHOWING PAGE 2: ARITHMANCY & EDITORIAL");
            }} else if (mode === 'p3') {{
                root.appendChild(p3);
                document.getElementById('btnP3').classList.add('active-mode');
                showToast("SHOWING PAGE 3: SEGREGATED WITNESS");
            }} else if (mode === 'p4') {{
                root.appendChild(p4);
                document.getElementById('btnP4').classList.add('active-mode');
                showToast("SHOWING PAGE 4: LIQUIDATION LADY & COLOPHON");
            }} else if (mode === 'center-spread') {{
                const spread = document.createElement('div');
                spread.className = 'spread-wrapper';
                p2.classList.add('page-left');
                p3.classList.add('page-right');
                spread.appendChild(p2);
                spread.appendChild(p3);
                root.appendChild(spread);
                document.getElementById('btnCenterSpread').classList.add('active-mode');
                showToast("CENTER SPREAD: PAGES 2 & 3");
            }} else if (mode === 'outer-spread') {{
                const spread = document.createElement('div');
                spread.className = 'spread-wrapper';
                p4.classList.add('page-left');
                p1.classList.add('page-right');
                spread.appendChild(p4);
                spread.appendChild(p1);
                root.appendChild(spread);
                document.getElementById('btnOuterSpread').classList.add('active-mode');
                showToast("OUTER SPREAD: PAGES 4 & 1");
            }} else {{
                root.appendChild(p1);
                root.appendChild(p2);
                root.appendChild(p3);
                root.appendChild(p4);
                document.getElementById('btnAllPages').classList.add('active-mode');
                showToast("SHOWING ALL 4 PAGES");
            }}
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function toggleDarkInk() {{
            document.body.classList.toggle('dark-ink');
            const isDark = document.body.classList.contains('dark-ink');
            document.getElementById('btnInkMode').innerText = isDark ? "☀️ Paper" : "🌙 Inky";
            showToast(isDark ? "DARK INK MODE ACTIVATED" : "NEWSPRINT PAPER MODE RESTORED");
        }}

        if (window.innerWidth <= 768) {{
            setViewMode('mobile');
        }}
    </script>
</body>
</html>
"""

# Write to index.html and issue-03.html
with open(os.path.join(WORKING_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(WEB_HTML)
print("Updated index.html to Issue No. 03!")

with open(os.path.join(WORKING_DIR, "issue-03.html"), "w", encoding="utf-8") as f:
    f.write(WEB_HTML)
print("Saved standalone issue-03.html!")

# Update edition switchers in issue-02.html and issue-01.html
def update_edition_nav(filepath, current_issue_num):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replacement nav block
    nav_pattern = r'<div class="flex items-center gap-1 bg-black/60 p-1 rounded border border-amber-600/50">.*?</div>'
    new_nav = f'''<div class="flex items-center gap-1 bg-black/60 p-1 rounded border border-amber-600/50">
                <span class="font-bold text-amber-500 uppercase tracking-wider text-[11px] px-1">EDITION:</span>
                <a href="index.html" class="px-2.5 py-1 rounded text-xs font-bold transition {'bg-amber-600 text-stone-950 font-extrabold shadow' if current_issue_num == 3 else 'bg-stone-800 text-stone-300 hover:bg-stone-700 hover:text-white border border-stone-600'}" title="Issue No. 03 (Latest Release)">🗞️ No. 03</a>
                <a href="issue-02.html" class="px-2.5 py-1 rounded text-xs font-bold transition {'bg-amber-600 text-stone-950 font-extrabold shadow' if current_issue_num == 2 else 'bg-stone-800 text-stone-300 hover:bg-stone-700 hover:text-white border border-stone-600'}" title="Issue No. 02">🏛️ No. 02</a>
                <a href="issue-01.html" class="px-2.5 py-1 rounded text-xs font-bold transition {'bg-amber-600 text-stone-950 font-extrabold shadow' if current_issue_num == 1 else 'bg-stone-800 text-stone-300 hover:bg-stone-700 hover:text-white border border-stone-600'}" title="Issue No. 01">🏛️ No. 01</a>
            </div>'''
    
    updated = re.sub(nav_pattern, new_nav, content, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"Updated edition nav in {os.path.basename(filepath)}")

update_edition_nav(os.path.join(WORKING_DIR, "issue-02.html"), 2)
update_edition_nav(os.path.join(WORKING_DIR, "issue-01.html"), 1)
print("All edition switchers updated successfully!")
