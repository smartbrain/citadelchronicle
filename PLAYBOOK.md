# The Citadel Chronicle — Master Production Playbook & Design System
**Version**: 1.0 (Post-Issue 01 Canonical)  
**Publication**: *The Citadel Chronicle* (`citadelchronicle.com`)  
**Publisher**: Don & Chaloke.com Community  
**Target Medium**: Double-Sided A3 Newsprint (Brother A3 Duplex Printer) + Web Reader + Nostr NIP-23  

---

## 1. Executive Summary & Core Geometry

*The Citadel Chronicle* is designed as a **physical-first, 4-page A4 broadsheet booklet produced on a single double-sided A3 sheet (420mm × 297mm)**, folded in half down the spine.

```
                      PHYSICAL PRINT SHEET ARCHITECTURE
                      
       SHEET 1 (Outside / Exterior)            SHEET 2 (Inside / Center Spread)
     ┌──────────────────┬──────────────────┐ ┌──────────────────┬──────────────────┐
     │                  ┆                  │ │                  ┆                  │
     │      PAGE 4      ┆      PAGE 1      │ │      PAGE 2      ┆      PAGE 3      │
     │    Back Cover    ┆   Front Cover    │ │  Editorial/Morgue┆  The Deep Dive   │
     │   (A4 Portrait)  ┆  (A4 Portrait)   │ │  (A4 Portrait)   │  (A4 Portrait)   │
     │                  ┆                  │ │                  ┆                  │
     └──────────────────┴──────────────────┘ └──────────────────┴──────────────────┘
                 FOLD DOWN MIDDLE                         FOLD DOWN MIDDLE
```

### The 4-Page Booklet Sequence:
1. **Page 1 (Front Cover)**: Masthead, Ears, Lead Story, Editorial summary, Bitcoin Mempool bytelines.
2. **Page 2 (Inside Left - Editorial & Morgue)**: Op-Eds, Macro market analysis, Miner/Node obituaries/stats.
3. **Page 3 (Inside Right - The Deep Dive)**: Anchor feature story (e.g. Uncle Chaloke interview), technical diagrams, code blocks, or charts.
4. **Page 4 (Back Cover)**: Cultural essay, Nostr/Bitcoin directory, Sponsor Full/Half-Page Ad, Colophon & Staff box.

---

## 2. Critical Lessons Learned ("The First-Go Rules")

### Rule 1: No A4 Landscape — It is A4 Portrait inside A3 Landscape
- **Never** lay out individual pages in landscape.
- Each page is **A4 Portrait** ($210\text{ mm} \times 297\text{ mm}$).
- Print sheets are **A3 Landscape** ($420\text{ mm} \times 297\text{ mm}$) containing two A4 portraits side-by-side:
  - Outside Sheet: `[ Page 4 | Page 1 ]`
  - Inside Spread: `[ Page 2 | Page 3 ]`

### Rule 2: The "Golden Fill" Principle (95% – 98% Page Height)
- Avoid the **"3/4 page void"**: A broadsheet must feel dense, authoritative, and ink-filled. Empty bottoms look like formatting errors.
- Avoid **"Bottom edge overflow"**: Printer hardware margins will clip text if the page extends beyond $287\text{ mm}$.
- **Formula for perfect fill**:
  - Exact Sheet Height: `297mm`
  - Padding: `top: 10mm`, `bottom: 10mm`, `left: 14mm`, `right: 14mm`.
  - Usable Printable Height: `277mm`.
  - Container must use `display: flex; flex-direction: column; justify-content: space-between; overflow: hidden;`.
  - Body copy font size: `9.4pt` – `9.7pt` with `line-height: 1.32` – `1.35`.

### Rule 3: Single-Line Headlines to Prevent Overflow Cascades
- A 2-line headline where 1 line was planned pushes the entire 3-column body down by 35–50px, causing the bottom paragraphs to clip off the physical sheet.
- Always check headline line-wraps across both print CSS and screen CSS. Set explicit `font-size` and `line-height: 1.0` to `1.05` for major banners.

### Rule 4: Brother A3 Printer Hardware Margins
- Brother inkjet/laser A3 printers have non-printable margins between `4mm` and `12mm` depending on driver settings.
- Keep **10mm top/bottom** and **14mm left/right** margin buffers. Never place critical text closer than `12mm` to any outer paper edge.

### Rule 5: Mobile Must Be Single-Column (1-Col) Stream
- Multi-column broadsheet (`column-count: 3` or `2`) is illegible on mobile viewports ($< 768\text{px}$) because columns wrap vertically off-screen, forcing users to scroll up and down repeatedly.
- On mobile:
  - Collapse all columns to `column-count: 1 !important`.
  - Stack all grids vertically.
  - Set `text-indent: 0; text-align: left; margin-bottom: 1.1rem; font-size: 1.05rem; line-height: 1.62;`.
  - Display all 4 pages in a single uninterrupted vertical stream.
  - Auto-detect mobile screen on initial load (`window.innerWidth <= 768`).

### Rule 6: Fact-Checking & Community Accuracy
- **Uncle Chaloke interview**: Sanjay Popli on *AlphaMind Podcast* ([alphamind.network](https://alphamind.network) or [youtube.com/@alphamindpodcast](https://www.youtube.com/@alphamindpodcast)). Never confuse with unrelated entities.
- **Sponsorships & Ads**: Verify active dates and promo terms. If a 21% early bird discount window has closed, use general admission / VIP pass calls to action.

---

## 3. Typography & Styling Specification

### Typefaces
- **Masthead & Gothic Titles**: `'UnifrakturMaguntia'`, `'Cinzel Decorative'`, serif
- **Headlines & Subheads**: `'Playfair Display'`, Georgia, serif (Bold 700 / 900)
- **Body Text**: `'EB Garamond'`, Georgia, serif (Regular 400, Italic, Bold 700)
- **Technical, Hashes & Byline Data**: `'Courier Prime'`, monospace

### Print Color Palette (Strict High-Contrast Ink)
```css
:root {
    --paper-bg: #ffffff;
    --paper-bg-alt: #fdfbf7;
    --ink-primary: #0a0a0a;
    --ink-secondary: #222222;
    --ink-accent: #8b1e1e;       /* Traditional Crimson Broadsheet Accent */
    --rule-color: #000000;
}
```

### Broadsheet Rules (Linework)
- **Heavy Top Rule**: `border-top: 2.5px solid #000;`
- **Double Bottom Rule**: `border-bottom: 3.5px double #000;`
- **Hairline Column Separator**: `column-rule: 1px solid #c0bcb5;` or `border-r: 1px solid #000;`

---

## 4. Web Engine Architecture (`index.html`)

The interactive web reader provides a toolbar allowing users to switch perspectives instantly:

| Mode Identifier | Button Label | Description / DOM Action |
|---|---|---|
| `mobile` | `📱 Mobile (1-Col)` | Single-column continuous stream (P1 $\to$ P2 $\to$ P3 $\to$ P4) |
| `p1` | `Page 1 (Front)` | Standalone A4 Portrait Front Cover |
| `p2` | `Page 2 (Editorial)` | Standalone A4 Portrait Editorial & Morgue |
| `p3` | `Page 3 (Deep Dive)` | Standalone A4 Portrait Uncle Chaloke Deep Dive |
| `p4` | `Page 4 (Back)` | Standalone A4 Portrait Back Page & Ads |
| `center-spread` | `Center Spread (P2+P3)` | A3 Horizontal Spread: P2 (Left) + P3 (Right) |
| `outer-spread` | `Outer Spread (P4+P1)` | A3 Horizontal Spread: P4 (Left) + P1 (Right) |
| `all-pages` | `All 4 Pages` | Sequential broadsheets for desktop browsing |

### Inky / Paper Theme (Blockclock / Ambient Display)
- For e-ink or Blockclock displays, keep background `#ffffff` / `#fbf8f2` (light paper) with pure black ink (`#000000`).
- Avoid dark mode on physical display devices—it resembles a tablet screen instead of newsprint.

---

## 5. Automated Print Generation Pipeline

The repository includes `perfect_print_engine.py` which compiles the HTML templates and uses headless Chromium to render exact 300 DPI print-ready PDFs and CMYK/RGB JPGs.

### Commands to Build Print Artifacts:
```bash
cd /home/don/citadelchronicle
python3 perfect_print_engine.py
```

### Outputs Generated:
1. `citadel_chronicle_issue01_a3_duplex.pdf` (Page 1 = Outside Sheet, Page 2 = Inside Sheet; send directly to Brother A3 Duplex print driver).
2. `citadel_chronicle_issue01_a4_sequential.pdf` (4 individual A4 pages in reading sequence).
3. `citadel_chronicle_a3_sheet1_outside_p4_p1_300dpi.jpg` ($4961 \times 3508$ pixels at 300 DPI).
4. `citadel_chronicle_a3_sheet2_inside_p2_p3_300dpi.jpg` ($4961 \times 3508$ pixels at 300 DPI).

---

## 6. Pre-Flight Checklist for Issue 02+ ("First-Go Guarantee")

Before committing, printing, or publishing future issues:

- [ ] **1. Editorial Word Count Budget**:
  - Lead Article (P1): 650–750 words.
  - P2 Op-Ed: 450 words + Morgue stats box.
  - P3 Deep Dive: 900–1,100 words (including subheads and pull quotes).
  - P4 Culture / Ad: 400 words + Half-page sponsor graphic ($182\text{mm} \times 115\text{mm}$).
- [ ] **2. Single-Line Headline Verification**:
  - Test headers on both screen and print CSS to confirm no unexpected wrapping.
- [ ] **3. Fill Check**:
  - Render test PDF and check bottom margins. Content must touch $275\text{mm} \pm 5\text{mm}$.
- [ ] **4. Responsive Test**:
  - Open at mobile viewport ($390\text{px}$ width): confirm single-column flow, no text overflow, clean paragraph breaks.
- [ ] **5. Links & URLs**:
  - Verify all podcast, speaker, sponsor, and canonical links.
- [ ] **6. Nostr NIP-23 Package**:
  - Export copy to `issue_XX_nip23.md` with Kind 30023 tags for Nostr publication.
- [ ] **7. GitHub Pages Deployment**:
  - Confirm CNAME is intact (`citadelchronicle.com`) and HTTPS is enforced.
