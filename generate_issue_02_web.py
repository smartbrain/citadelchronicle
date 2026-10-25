#!/usr/bin/env python3
"""
Generate issue-02.html — Standalone Interactive Web Reader for Edition 2
"""

import os
import shutil

WORKING_DIR = "/home/don/citadelchronicle"
BLOCKCANDCHAIN_DIR = "/home/don/blockcandchain"
DOWNLOADS_DIR = "/home/don/Downloads"

with open(os.path.join(WORKING_DIR, "build_issue_02.py")) as f:
    text = f.read()

# Extract the HTML blocks
import re

def get_var(name):
    pattern = rf'{name} = """(.*?)"""'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    raise ValueError(f"Var {name} not found")

BASE_CSS = get_var("BASE_CSS")
PAGE_1_HTML = get_var("PAGE_1_HTML")
PAGE_2_HTML = get_var("PAGE_2_HTML")
PAGE_3_HTML = get_var("PAGE_3_HTML")
PAGE_4_HTML = get_var("PAGE_4_HTML")

WEB_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THE CITADEL CHRONICLE — Issue No. 02</title>
    <!-- Tailwind CSS for structural utilities -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Classic Broadsheet, Blackletter & Cypherpunk Monospace -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=EB+Garamond:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600&family=Playfair+Display:ital,wght@0,700;0,900;1,400;1,700&family=UnifrakturMaguntia&display=swap" rel="stylesheet">

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
            box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        }}

        .spread-wrapper .a4-page {{
            margin: 0;
            width: 785px;
            box-shadow: none;
        }}

        .spread-wrapper .a4-page.page-left {{
            border-right: 1px dashed rgba(0,0,0,0.35);
        }}
        .spread-wrapper .a4-page.page-right {{
            border-left: 1px solid rgba(255,255,255,0.15);
        }}

        .font-masthead {{ font-family: 'UnifrakturMaguntia', 'Cinzel Decorative', serif; }}
        .font-headline {{ font-family: 'Playfair Display', Georgia, serif; }}
        .font-body {{ font-family: 'EB Garamond', Georgia, serif; }}
        .font-mono-tech {{ font-family: 'Courier Prime', monospace; }}

        .double-rule-top {{ border-top: 3.5px double var(--rule-color); }}
        .double-rule-bottom {{ border-bottom: 3.5px double var(--rule-color); }}
        .heavy-rule-top {{ border-top: 2.5px solid var(--rule-color); }}
        .heavy-rule-bottom {{ border-bottom: 2px solid var(--rule-color); }}
        .thin-rule-bottom {{ border-bottom: 1px solid var(--rule-color); }}
        .thin-rule-top {{ border-top: 1px solid var(--rule-color); }}

        .p1-masthead-row {{
            display: grid;
            grid-template-columns: 140px 1fr 140px;
            align-items: stretch;
            gap: 12px;
            padding-bottom: 4px;
            margin-top: 2px;
        }}
        .masthead-title {{
            font-size: 2.75rem;
            line-height: 0.95;
        }}

        .p-copy {{
            font-size: 9.6pt;
            line-height: 1.34;
            margin-bottom: 6pt;
            text-align: justify;
            text-indent: 12pt;
            color: var(--ink-secondary);
        }}
        .p-copy.no-indent {{ text-indent: 0; }}

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

        .cols-3 {{
            column-count: 3;
            column-gap: 16px;
            column-rule: 1px solid var(--rule-color);
            text-align: justify;
        }}
        .cols-2 {{
            column-count: 2;
            column-gap: 16px;
            column-rule: 1px solid var(--rule-color);
            text-align: justify;
        }}
        .split-2-1 {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 14px;
        }}
        .split-1-1 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
        }}

        .footer-line {{
            border-top: 2px solid var(--rule-color);
            padding-top: 4px;
            margin-top: 4px;
            font-family: 'Courier Prime', monospace;
            font-size: 7.2pt;
            display: flex;
            justify-content: space-between;
            align-items: center;
            text-transform: uppercase;
            letter-spacing: 0.05em;
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
            .cols-3, .cols-2 {{
                column-count: 1 !important;
                column-rule: none !important;
            }}
            .split-2-1, .split-1-1, .p1-masthead-row {{
                grid-template-columns: 1fr !important;
            }}
            .p-copy {{
                font-size: 10.5pt;
                line-height: 1.5;
                text-indent: 0;
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
    <header class="max-w-5xl mx-auto mb-6 bg-stone-900 border border-stone-700 text-stone-200 p-3 rounded-lg shadow-2xl flex flex-wrap items-center justify-between gap-3 text-xs font-mono">
        <div class="flex items-center gap-2">
            <a href="index.html" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded text-amber-300 font-bold">← Issue 01</a>
            <span class="font-bold tracking-widest text-amber-500 uppercase">THE CITADEL CHRONICLE • ISSUE 02</span>
            <span class="bg-amber-900/60 text-amber-200 px-2 py-0.5 rounded border border-amber-600/40">DRAFT PROOF</span>
        </div>

        <!-- VIEW SELECTOR BUTTONS -->
        <div class="flex flex-wrap items-center gap-1.5" id="viewControls">
            <button onclick="setViewMode('mobile')" id="btnMobile" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">📱 Mobile (1-Col)</button>
            <button onclick="setViewMode('p1')" id="btnP1" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">P1 (Front)</button>
            <button onclick="setViewMode('p2')" id="btnP2" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">P2 (Editorial)</button>
            <button onclick="setViewMode('p3')" id="btnP3" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">P3 (Deep Dive)</button>
            <button onclick="setViewMode('p4')" id="btnP4" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">P4 (Back)</button>
            <button onclick="setViewMode('center-spread')" id="btnCenterSpread" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">Center Spread (P2+P3)</button>
            <button onclick="setViewMode('outer-spread')" id="btnOuterSpread" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition">Outer Spread (P4+P1)</button>
            <button onclick="setViewMode('all-pages')" id="btnAllPages" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 transition active-mode">All 4 Pages</button>
        </div>

        <!-- ACTIONS & DOWNLOADS -->
        <div class="flex items-center gap-2">
            <button onclick="toggleDarkInk()" id="btnInkMode" class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 rounded border border-stone-600 text-stone-300">🌙 Inky</button>
            <a href="citadel_chronicle_issue02_a3_duplex.pdf" download class="px-2.5 py-1 bg-amber-700 hover:bg-amber-600 text-white rounded font-bold shadow">🖨️ A3 Duplex PDF</a>
            <a href="citadel_chronicle_issue02_a4_sequential.pdf" download class="px-2.5 py-1 bg-stone-800 hover:bg-stone-700 text-stone-200 rounded border border-stone-600">📄 A4 PDF</a>
        </div>
    </header>

    <!-- TOAST NOTIFICATION -->
    <div id="toast" class="fixed bottom-6 right-6 bg-stone-900 border border-amber-600 text-amber-200 px-4 py-2 rounded shadow-2xl font-mono text-xs opacity-0 transition-opacity duration-300 pointer-events-none z-50"></div>

    <!-- MAIN PAGES CONTAINER -->
    <main id="chronicleRoot">
        <div class="a4-page" id="page1-wrap">{PAGE_1_HTML}</div>
        <div class="a4-page" id="page2-wrap">{PAGE_2_HTML}</div>
        <div class="a4-page" id="page3-wrap">{PAGE_3_HTML}</div>
        <div class="a4-page" id="page4-wrap">{PAGE_4_HTML}</div>
    </main>

    <!-- FOOTER INFO -->
    <footer class="max-w-4xl mx-auto my-8 text-center text-stone-500 font-mono text-xs">
        <div>THE CITADEL CHRONICLE • EDITION 02 • OCTOBER 2026 • PATHUM THANI, THAILAND</div>
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

            // Reset buttons
            document.querySelectorAll('#viewControls button').forEach(b => b.classList.remove('active-mode'));

            // Reset classes
            root.className = '';
            [p1, p2, p3, p4].forEach(p => {{
                p.classList.remove('hidden', 'page-left', 'page-right');
            }});

            if (mode === 'mobile') {{
                document.body.classList.add('mobile-mode');
                document.getElementById('btnMobile').classList.add('active-mode');
                root.appendChild(p1);
                root.appendChild(p2);
                root.appendChild(p3);
                root.appendChild(p4);
                showToast("📱 MOBILE MODE: SINGLE COLUMN STREAM");
            }} else if (mode === 'p1') {{
                p1.classList.remove('hidden');
                p2.classList.add('hidden');
                p3.classList.add('hidden');
                p4.classList.add('hidden');
                document.getElementById('btnP1').classList.add('active-mode');
                showToast("SHOWING PAGE 1: FRONT COVER");
            }} else if (mode === 'p2') {{
                p1.classList.add('hidden');
                p2.classList.remove('hidden');
                p3.classList.add('hidden');
                p4.classList.add('hidden');
                document.getElementById('btnP2').classList.add('active-mode');
                showToast("SHOWING PAGE 2: EDITORIAL & MORGUE");
            }} else if (mode === 'p3') {{
                p1.classList.add('hidden');
                p2.classList.add('hidden');
                p3.classList.remove('hidden');
                p4.classList.add('hidden');
                document.getElementById('btnP3').classList.add('active-mode');
                showToast("SHOWING PAGE 3: THE DEEP DIVE");
            }} else if (mode === 'p4') {{
                p1.classList.add('hidden');
                p2.classList.add('hidden');
                p3.classList.add('hidden');
                p4.classList.remove('hidden');
                document.getElementById('btnP4').classList.add('active-mode');
                showToast("SHOWING PAGE 4: THE BACK PAGE");
            }} else if (mode === 'center-spread') {{
                p1.classList.add('hidden');
                p4.classList.add('hidden');
                p2.classList.remove('hidden');
                p3.classList.remove('hidden');
                p2.classList.add('page-left');
                p3.classList.add('page-right');
                root.className = 'spread-wrapper';
                root.appendChild(p2);
                root.appendChild(p3);
                document.getElementById('btnCenterSpread').classList.add('active-mode');
                showToast("SHOWING CENTER SPREAD: A3 FOLD (P2 + P3)");
            }} else if (mode === 'outer-spread') {{
                p2.classList.add('hidden');
                p3.classList.add('hidden');
                p4.classList.remove('hidden');
                p1.classList.remove('hidden');
                p4.classList.add('page-left');
                p1.classList.add('page-right');
                root.className = 'spread-wrapper';
                root.appendChild(p4);
                root.appendChild(p1);
                document.getElementById('btnOuterSpread').classList.add('active-mode');
                showToast("SHOWING OUTER SPREAD: A3 FOLD (P4 + P1)");
            }} else if (mode === 'all-pages') {{
                root.appendChild(p1);
                root.appendChild(p2);
                root.appendChild(p3);
                root.appendChild(p4);
                document.getElementById('btnAllPages').classList.add('active-mode');
                showToast("SHOWING ALL 4 PAGES");
            }}
        }}

        function toggleDarkInk() {{
            document.body.classList.toggle('dark-ink');
            const btn = document.getElementById('btnInkMode');
            btn.classList.toggle('active-mode');
            const isDark = document.body.classList.contains('dark-ink');
            showToast(isDark ? "DARK INK ENABLED" : "DAYLIGHT NEWSPRINT ENABLED");
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            if (window.innerWidth <= 768) {{
                setViewMode('mobile');
            }}
        }});
    </script>
</body>
</html>
"""

# Clean any inner a4-sheet-inner nested id conflict
WEB_HTML = WEB_HTML.replace('<div class="a4-sheet-inner" id="p1">', '<div class="a4-sheet-inner">')
WEB_HTML = WEB_HTML.replace('<div class="a4-sheet-inner" id="p2">', '<div class="a4-sheet-inner">')
WEB_HTML = WEB_HTML.replace('<div class="a4-sheet-inner" id="p3">', '<div class="a4-sheet-inner">')
WEB_HTML = WEB_HTML.replace('<div class="a4-sheet-inner" id="p4">', '<div class="a4-sheet-inner">')

web_out = os.path.join(WORKING_DIR, "issue-02.html")
with open(web_out, "w", encoding="utf-8") as f:
    f.write(WEB_HTML)

print("Saved issue-02.html")

# Copy web edition to Downloads and blockcandchain
shutil.copy2(web_out, os.path.join(DOWNLOADS_DIR, "issue-02.html"))
shutil.copy2(web_out, os.path.join(BLOCKCANDCHAIN_DIR, "issue-02.html"))
print("Copied issue-02.html to Downloads and blockcandchain.")
