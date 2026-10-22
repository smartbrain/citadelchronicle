#!/usr/bin/env python3
"""
Generate Print-Ready PDFs and 300 DPI JPGs for Brother A3 Printer.
Creates:
1. citadel_chronicle_issue01_a3_duplex.pdf (2-page A3 landscape: Sheet 1 Outer [P4+P1], Sheet 2 Inner [P2+P3])
2. citadel_chronicle_issue01_a4_pages.pdf (4-page A4 portrait: P1, P2, P3, P4)
3. 300 DPI JPGs of all sheets and pages for direct image printing.
"""

import os
import subprocess
import re

WORKING_DIR = "/home/don/citadelchronicle"
DOWNLOADS_DIR = "/home/don/Downloads"

print("Starting Print-Ready Asset Generation...")

# 1. Read the master HTML file
with open(os.path.join(WORKING_DIR, "index.html"), "r", encoding="utf-8") as f:
    master_html = f.read()

# Extract the contents of page-1, page-2, page-3, page-4
def extract_section(html, page_id):
    pattern = rf'<main[^>]*id="{page_id}"[^>]*>(.*?)</main>'
    m = re.search(pattern, html, re.DOTALL)
    if not m:
        raise ValueError(f"Could not find section {page_id}")
    return m.group(1)

p1_content = extract_section(master_html, "page-1")
p2_content = extract_section(master_html, "page-2")
p3_content = extract_section(master_html, "page-3")
p4_content = extract_section(master_html, "page-4")

# Common CSS for print typography and styling
BASE_CSS = """
    :root {
        --paper-bg: #ffffff;
        --paper-bg-alt: #fdfbf7;
        --ink-primary: #0a0a0a;
        --ink-secondary: #2a2a2a;
        --ink-accent: #8b1e1e;
        --rule-color: #000000;
    }
    * {
        box-sizing: border-box;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
    }
    body {
        margin: 0;
        padding: 0;
        background: #ffffff;
        color: var(--ink-primary);
        font-family: 'EB Garamond', Georgia, serif;
    }
    .font-masthead {
        font-family: 'UnifrakturMaguntia', 'Cinzel Decorative', serif;
        letter-spacing: 0.02em;
    }
    .font-headline {
        font-family: 'Playfair Display', Georgia, serif;
    }
    .font-body {
        font-family: 'EB Garamond', Georgia, serif;
    }
    .font-mono-tech {
        font-family: 'Courier Prime', monospace;
    }
    .double-rule-top { border-top: 3.5px double var(--rule-color); }
    .double-rule-bottom { border-bottom: 3.5px double var(--rule-color); }
    .heavy-rule-top { border-top: 2.5px solid var(--rule-color); }
    .heavy-rule-bottom { border-bottom: 2px solid var(--rule-color); }
    .thin-rule-bottom { border-bottom: 1px solid var(--rule-color); }

    .masthead-row {
        display: grid;
        grid-template-columns: 140px minmax(0, 1fr) 140px;
        align-items: stretch;
        gap: 12px;
        padding-bottom: 5px;
    }
    .masthead-title {
        font-size: 2.65rem;
        line-height: 0.98;
    }
    .newspaper-columns-3 {
        column-count: 3;
        column-gap: 16px;
        column-rule: 1px solid var(--rule-color);
        text-align: justify;
    }
    .newspaper-columns-2 {
        column-count: 2;
        column-gap: 16px;
        column-rule: 1px solid var(--rule-color);
        text-align: justify;
    }
    .newspaper-columns-5 {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 10px;
    }
    .newspaper-copy p {
        font-size: 9.2pt;
        line-height: 1.32;
        margin-bottom: 5pt;
        text-indent: 10pt;
    }
    .newspaper-copy p:first-of-type,
    .newspaper-copy p.no-indent {
        text-indent: 0;
    }
    .drop-cap::first-letter {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.8rem;
        float: left;
        line-height: 0.82;
        padding-top: 2px;
        padding-right: 5px;
        font-weight: 900;
        color: var(--ink-primary);
    }
    .engraved-box {
        background-color: var(--paper-bg-alt);
        border: 1.5px solid var(--rule-color);
        box-shadow: inset 0 0 0 1.5px var(--paper-bg), inset 0 0 0 2.5px var(--rule-color);
        padding: 10px 12px;
    }
"""

# HTML Template for A3 Landscape Duplex (Sheet 1: P4 + P1, Sheet 2: P2 + P3)
A3_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Citadel Chronicle — A3 Broadsheet Print Imposition</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=EB+Garamond:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600&family=Playfair+Display:ital,wght@0,700;0,900;1,400;1,700&family=UnifrakturMaguntia&display=swap" rel="stylesheet">
    <style>
        {BASE_CSS}
        @page {{
            size: 420mm 297mm;
            margin: 0;
        }}
        .a3-sheet {{
            width: 420mm;
            height: 297mm;
            page-break-after: always;
            break-after: page;
            display: flex;
            position: relative;
            background: #ffffff;
            overflow: hidden;
        }}
        .page-half {{
            width: 210mm;
            height: 297mm;
            padding: 14mm 16mm 14mm 16mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
        }}
        /* Fold Guide line */
        .fold-guide {{
            position: absolute;
            left: 210mm;
            top: 0;
            bottom: 0;
            width: 0px;
            border-left: 0.5px dashed rgba(0,0,0,0.25);
            z-index: 50;
        }}
        .fold-tick-top {{
            position: absolute;
            left: 209.5mm;
            top: 0;
            width: 1mm;
            height: 4mm;
            background: #000000;
            z-index: 60;
        }}
        .fold-tick-bottom {{
            position: absolute;
            left: 209.5mm;
            bottom: 0;
            width: 1mm;
            height: 4mm;
            background: #000000;
            z-index: 60;
        }}
    </style>
</head>
<body>
    <!-- SHEET 1 (OUTSIDE): PAGE 4 (BACK) on LEFT | PAGE 1 (FRONT) on RIGHT -->
    <div class="a3-sheet" id="sheet-1">
        <div class="fold-guide"></div>
        <div class="fold-tick-top"></div>
        <div class="fold-tick-bottom"></div>
        <div class="page-half">
            {p4_content}
        </div>
        <div class="page-half">
            {p1_content}
        </div>
    </div>

    <!-- SHEET 2 (INSIDE): PAGE 2 (EDITORIAL) on LEFT | PAGE 3 (DEEP DIVE) on RIGHT -->
    <div class="a3-sheet" id="sheet-2">
        <div class="fold-guide"></div>
        <div class="fold-tick-top"></div>
        <div class="fold-tick-bottom"></div>
        <div class="page-half">
            {p2_content}
        </div>
        <div class="page-half">
            {p3_content}
        </div>
    </div>
</body>
</html>
"""

# HTML Template for A4 Portrait Sequential (P1, P2, P3, P4)
A4_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Citadel Chronicle — A4 Portrait Sequential Print</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=EB+Garamond:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600&family=Playfair+Display:ital,wght@0,700;0,900;1,400;1,700&family=UnifrakturMaguntia&display=swap" rel="stylesheet">
    <style>
        {BASE_CSS}
        @page {{
            size: 210mm 297mm;
            margin: 0;
        }}
        .a4-page-sheet {{
            width: 210mm;
            height: 297mm;
            page-break-after: always;
            break-after: page;
            padding: 14mm 16mm 14mm 16mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background: #ffffff;
            overflow: hidden;
        }}
    </style>
</head>
<body>
    <div class="a4-page-sheet" id="p1">{p1_content}</div>
    <div class="a4-page-sheet" id="p2">{p2_content}</div>
    <div class="a4-page-sheet" id="p3">{p3_content}</div>
    <div class="a4-page-sheet" id="p4">{p4_content}</div>
</body>
</html>
"""

# Save intermediate HTML files
a3_html_path = os.path.join(WORKING_DIR, "print_a3_duplex.html")
a4_html_path = os.path.join(WORKING_DIR, "print_a4_sequential.html")

with open(a3_html_path, "w", encoding="utf-8") as f:
    f.write(A3_HTML)

with open(a4_html_path, "w", encoding="utf-8") as f:
    f.write(A4_HTML)

print("Saved HTML print templates.")

# Generate PDFs using Google Chrome Headless
pdf_a3 = os.path.join(WORKING_DIR, "citadel_chronicle_issue01_a3_duplex.pdf")
pdf_a4 = os.path.join(WORKING_DIR, "citadel_chronicle_issue01_a4_sequential.pdf")

print("Rendering A3 Duplex PDF via Chrome...")
cmd_a3 = [
    "google-chrome",
    "--headless",
    "--no-sandbox",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=5000",
    f"--print-to-pdf={pdf_a3}",
    "--no-pdf-header-footer",
    f"file://{a3_html_path}"
]
subprocess.run(cmd_a3, check=True)

print("Rendering A4 Sequential PDF via Chrome...")
cmd_a4 = [
    "google-chrome",
    "--headless",
    "--no-sandbox",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=5000",
    f"--print-to-pdf={pdf_a4}",
    "--no-pdf-header-footer",
    f"file://{a4_html_path}"
]
subprocess.run(cmd_a4, check=True)

# Generate 300 DPI JPGs using pdftoppm
print("Rendering 300 DPI JPGs from A3 PDF...")
subprocess.run([
    "pdftoppm", "-r", "300", "-jpeg", "-jpegopt", "quality=95",
    pdf_a3, os.path.join(WORKING_DIR, "citadel_chronicle_a3_sheet")
], check=True)

print("Rendering 300 DPI JPGs from A4 PDF...")
subprocess.run([
    "pdftoppm", "-r", "300", "-jpeg", "-jpegopt", "quality=95",
    pdf_a4, os.path.join(WORKING_DIR, "citadel_chronicle_a4_page")
], check=True)

# Rename pdftoppm files to friendly names
rename_map = {
    "citadel_chronicle_a3_sheet-1.jpg": "citadel_chronicle_a3_sheet1_outside_p4_p1_300dpi.jpg",
    "citadel_chronicle_a3_sheet-2.jpg": "citadel_chronicle_a3_sheet2_inside_p2_p3_300dpi.jpg",
    "citadel_chronicle_a4_page-1.jpg": "citadel_chronicle_a4_page1_front_300dpi.jpg",
    "citadel_chronicle_a4_page-2.jpg": "citadel_chronicle_a4_page2_editorial_300dpi.jpg",
    "citadel_chronicle_a4_page-3.jpg": "citadel_chronicle_a4_page3_deepdive_300dpi.jpg",
    "citadel_chronicle_a4_page-4.jpg": "citadel_chronicle_a4_page4_back_300dpi.jpg",
}

for old_name, new_name in rename_map.items():
    old_p = os.path.join(WORKING_DIR, old_name)
    new_p = os.path.join(WORKING_DIR, new_name)
    if os.path.exists(old_p):
        os.rename(old_p, new_p)

# Copy all generated PDFs and JPGs to Downloads for easy access
for f in os.listdir(WORKING_DIR):
    if f.endswith(".pdf") or f.endswith("_300dpi.jpg"):
        src = os.path.join(WORKING_DIR, f)
        dst = os.path.join(DOWNLOADS_DIR, f)
        subprocess.run(["cp", src, dst], check=True)

print("SUCCESS: All print assets generated and copied to Downloads!")
