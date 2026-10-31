# The Citadel Chronicle — Master Production Playbook & Design System
**Version**: 2.0 (Issue 04+ Double A3 / 8-Page Booklet Specification)  
**Publication**: *The Citadel Chronicle* (`citadelchronicle.com`)  
**Publisher**: Don & Chaloke.com Community  
**Target Medium**: Double-Sided A3 Newsprint (Brother A3 Duplex Printer) + Web Reader + Nostr NIP-23  

---

## 1. Executive Summary & Core Geometry

*The Citadel Chronicle* is a **physical-first, broadsheet-style newspaper produced on double-sided A3 sheets ($420\text{ mm} \times 297\text{ mm}$), folded in half down the spine into an A4 booklet**.

### The Evolution from 4-Page (Single A3) to 8-Page (Double A3):
- **Issues 01–03 (1×A3 Sheet / 4 Pages)**: Proved the concept, but dense investigations (Electrum RBF, 14-day arithmancy, 0-conf dispatches, Kathina, and memoirs) compressed layouts, forcing font sizes down to $6.4\text{pt} - 7.5\text{pt}$. In physical print, this became far too small and difficult to read comfortably.
- **Issue 04+ (2×A3 Sheets / 8 Pages of A4)**: Because the newsroom does not possess an A2 printer, physical broadsheet scale is achieved by **nesting two double-sided A3 sheets** to produce an **8-page A4 booklet**. This doubles our real estate, allowing bigger, consistent, highly legible typography ($9.5\text{pt} - 10.5\text{pt}$) with generous margins and breathing room.

```
                  DOUBLE A3 (8-PAGE A4) IMPOSITION ARCHITECTURE
                  
   ══════════════════════════════════════════════════════════════════════════
   SHEET 1: OUTER JACKET (Double-Sided A3)
   ══════════════════════════════════════════════════════════════════════════
   Side 1A (Exterior / Outside):               Side 1B (Interior / Inside):
   ┌────────────────────┬────────────────────┐ ┌────────────────────┬────────────────────┐
   │                    ┆                    │ │                    ┆                    │
   │       PAGE 8       ┆       PAGE 1       │ │       PAGE 2       ┆       PAGE 7       │
   │     Back Cover     ┆    Front Cover     │ │     Editorial      ┆  Dispatches/Ads    │
   │    (A4 Portrait)   ┆   (A4 Portrait)    │ │   (A4 Portrait)    │   (A4 Portrait)    │
   │                    ┆                    │ │                    ┆                    │
   └────────────────────┴────────────────────┘ └────────────────────┴────────────────────┘
                  FOLD SPINE                                 FOLD SPINE

   ══════════════════════════════════════════════════════════════════════════
   SHEET 2: INNER SECTION & CENTERFOLD (Double-Sided A3)
   ══════════════════════════════════════════════════════════════════════════
   Side 2A (Inner Flap):                       Side 2B (THE CENTERFOLD SPREAD):
   ┌────────────────────┬────────────────────┐ ┌────────────────────┬────────────────────┐
   │                    ┆                    │ │                    ┆                    │
   │       PAGE 6       ┆       PAGE 3       │ │       PAGE 4       ┆       PAGE 5       │
   │ Segregated Witness ┆ Investigation Pt.1 │ │ Centerfold (Left)  ┆ Centerfold (Right) │
   │   (A4 Portrait)    ┆   (A4 Portrait)    │ │   (A4 Portrait)    ┆   (A4 Portrait)    │
   │                    ┆                    │ │                    ┆                    │
   └────────────────────┴────────────────────┘ └────────────────────┴────────────────────┘
                  FOLD SPINE                                 FOLD SPINE
```

### The 8-Page Booklet Sequence:
1. **Page 1 (Front Cover)**: Masthead, Ears, Lead Broadsheet Story, Dateline bar, Woodcut Hero illustration.
2. **Page 2 (Editorial & Opinion)**: Editorial Leader, Letters to the Editor / Community Voice, The Newsroom Morgue.
3. **Page 3 (Special Investigation — Part 1)**: In-depth technical/protocol forensics, analytical breakdown.
4. **Pages 4–5 (The Sovereign Centerfold Spread)**: Continuous double-page centerpiece:
   - Anchor investigation climax, massive technical architecture diagram, or the inaugural **"Nothing to Declare"** profile feature.
5. **Page 6 (The Segregated Witness)**: Don Sambandaraksa's tech journalism morgue memoirs (e.g. 18% Nim Express, ATM evolution, NCR tales).
6. **Page 7 (0-Conf Dispatches, Regional & Familiars)**: Unconfirmed mempool intelligence, legal precedents, community dispatches, and "Adopt a Familiar" puppy classifieds.
7. **Page 8 (Back Cover — The Sovereign Market)**: Full-width / half-page display ads (Citadel Coffee Roasters, sponsor announcements), Colophon, full unabbreviated npub & Nostr QR code, Lightning address.

*(Legacy Reference: The single-sheet 4-page format remains documented in Section 7 for standalone leaflets or emergency 1-sheet editions).*

---

## 2. Critical Lessons Learned ("The First-Go Rules")

### Rule 1: No A4 Landscape — It is A4 Portrait inside A3 Landscape
- **Never** lay out individual pages in landscape.
- Each page is **A4 Portrait** ($210\text{ mm} \times 297\text{ mm}$).
- Print sheets are **A3 Landscape** ($420\text{ mm} \times 297\text{ mm}$) containing two A4 portraits side-by-side:
  - **Issue 04+ Double A3 (2 Sheets / 8 Pages)**:
    - Sheet 1 Outside: `[ Page 8 | Page 1 ]`
    - Sheet 1 Inside: `[ Page 2 | Page 7 ]`
    - Sheet 2 Outside: `[ Page 6 | Page 3 ]`
    - Sheet 2 Inside (Centerfold): `[ Page 4 | Page 5 ]`
  - **Legacy Single A3 (1 Sheet / 4 Pages)**:
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
  - Standard Body copy font size: `9.5pt` – `10.5pt` with `line-height: 1.32` – `1.38`.

### Rule 3: Single-Line Headlines to Prevent Overflow Cascades
- A 2-line headline where 1 line was planned pushes the entire multi-column body down by 35–50px, causing the bottom paragraphs to clip off the physical sheet.
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
  - Display all pages in a single uninterrupted vertical stream (P1 $\to$ P8).
  - Auto-detect mobile screen on initial load (`window.innerWidth <= 768`).

### Rule 6: Fact-Checking & Community Accuracy
- **Uncle Chaloke interview**: Sanjay Popli on *AlphaMind Podcast* ([alphamind.network](https://alphamind.network) or [youtube.com/@alphamindpodcast](https://www.youtube.com/@alphamindpodcast)). Never confuse with unrelated entities.
- **Sponsorships & Ads**: Verify active dates and promo terms. If a 21% early bird discount window has closed, use general admission / VIP pass calls to action.
- **Terminology Rule**: NEVER use the word "Byteline" (use "0-Conf Dispatches" or "Byline").

### Rule 7: The Legibility & Font Sizing Mandate (No Microscopic Fonts)
- **The Problem**: In earlier 4-page editions, squeezing lengthy deep dives into tight margins caused body text to collapse down to $6.4\text{pt} - 7.2\text{pt}$. On physical newsprint without an A2 magnifying glass, this is unreadable.
- **The Mandate for Issue 04+**:
  - **Absolute Floor**: Standard editorial body text must NEVER drop below **`9.0pt`** (`9.5pt` – `10.5pt` preferred).
  - **Never shrink fonts to fix overflow**: If an article does not fit, **edit and trim the prose** or **spill the story across to the next page**. Do not touch the font size dial to solve layout geometry.
  - **Typographic Consistency**: Neighboring articles and columns on the same page MUST use identical body font sizes and line heights (`line-height: 1.30 – 1.38`). Avoid visual checkerboards where one column is 7pt and the adjacent column is 10pt.

### Rule 8: Visual & Palette Policy (Yellowed Woodcuts & Full-Colour Photography)
- **Woodcuts & Satirical Engravings**: Use **warm, aged, yellowed/sepia-tinted paper tones** (antique broadsheet cream/amber, RGB $\approx$ [170, 160, 140]), preserving the authentic 19th-century *Punch* / *Illustrated London News* aesthetic. Do not crush them into sterile, stark pure black-and-white.
- **Photographs & Real-World Imagery**: Keep in **100% full, rich, vibrant colour**! 
  - Uncle Chaloke wading into the paddy mud wearing his brilliant indigo *Mor Hom* with emerald green rice shoots and lush tropical tree lines.
  - The sleeping Dogesats puppy with his warm brindle coat on terracotta patio tiles and vivid lawn grass.
  - The newsroom inkjet printer has full ink tanks and we intend to use them. No artificial desaturation or muddy greyscale filters on real-world photojournalism.

---

## 3. Typography & Styling Specification

### Typefaces
- **Masthead & Gothic Titles**: `'UnifrakturMaguntia'`, `'Cinzel Decorative'`, serif
- **Headlines & Subheads**: `'Playfair Display'`, Georgia, serif (Bold 700 / 900)
- **Body Text**: `'EB Garamond'`, Georgia, serif (Regular 400, Italic, Bold 700)
- **Technical, Hashes & Byline Data**: `'Courier Prime'`, monospace
- **Thai Typography**: `'Pridi'` (Serif Headlines / Ceremonial), `'Sarabun'` (Clean Body Copy / Public Announcements)

### Standard Typographic Scale (Issue 04+ Legibility Standard)

| Element | Typeface | Size | Weight / Style | Line Height | Tracking / Alignment |
|---|---|---|---|---|---|
| **Main Masthead** | `Cinzel Decorative` / `UnifrakturMaguntia` | `32pt – 38pt` | Bold 900 | `0.95` | Centered, uppercase |
| **Running Page Header** | `Courier Prime` | `7.5pt – 8.5pt` | Bold 700 | `1.0` | Justified left/right |
| **Section Kicker Bar** | `Courier Prime` | `7.0pt – 8.0pt` | Bold 700 | `1.0` | Uppercase, `letter-spacing: 0.08em` |
| **Lead Frontpage Banner** | `Playfair Display` | `20pt – 26pt` | Bold 900 | `1.02 – 1.05` | Centered / Left, tight line wrap |
| **Page Lead Headline** | `Playfair Display` | `15pt – 18pt` | Bold 700/900 | `1.05 – 1.10` | Uppercase / Title case |
| **Secondary Headline** | `Playfair Display` | `12pt – 14pt` | Bold 700 | `1.10 – 1.15` | Section heads |
| **Headline Deck / Subhead** | `Playfair Display` | `9.0pt – 10.5pt` | Italic 400/600 | `1.20 – 1.25` | Summaries & decks |
| **Editorial Body Copy** | `EB Garamond` | **`9.5pt – 10.5pt`** | Regular 400 | **`1.32 – 1.38`** | Block justified, text-indent 8pt |
| **Drop Cap** | `Playfair Display` | `3.0rem – 3.4rem` | Bold 900 | `0.75 – 0.80` | First paragraph lead |
| **Plate / Image Captions** | `Playfair Display` / `EB Garamond` | `7.5pt – 8.5pt` | Italic 400 | `1.20` | Centered below plates |
| **Technical Data / Boxes** | `Courier Prime` | `7.0pt – 8.0pt` | Regular / Bold | `1.20 – 1.25` | Monospace boxes & diagrams |
| **Colophon & Micro-Data** | `Courier Prime` | `6.5pt – 7.5pt` | Regular 400 | `1.15 – 1.20` | Minimum allowable print size |

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

The build scripts compile the HTML templates and use headless Chromium to render exact 600 DPI and 300 DPI print-ready PDFs and CMYK/RGB JPGs.

### Commands to Build Print Artifacts:
```bash
cd /home/don/citadelchronicle
python3 build_issue_03.py   # For Issue 03 (4-page baseline)
# For Issue 04+ (8-page Double A3 booklet):
python3 build_issue_04.py
```

### Outputs Generated for Double A3 (Issue 04+):
1. **Master Vector PDF**: `citadel_chronicle_issue04.pdf` (8 individual A4 pages in sequential reading order).
2. **Duplex A3 Print Sheets (600 DPI & 300 DPI)**:
   - `citadel_chronicle_issue04_a3_sheet1_outside_p8_p1_600dpi.jpg` (Outer Jacket: Page 8 Left / Page 1 Right)
   - `citadel_chronicle_issue04_a3_sheet1_inside_p2_p7_600dpi.jpg` (Outer Jacket Flip: Page 2 Left / Page 7 Right)
   - `citadel_chronicle_issue04_a3_sheet2_outside_p6_p3_600dpi.jpg` (Inner Sheet: Page 6 Left / Page 3 Right)
   - `citadel_chronicle_issue04_a3_sheet2_inside_p4_p5_600dpi.jpg` (Inner Sheet Centerfold: Page 4 Left / Page 5 Right)
3. **Sequential A4 Pages**: `citadel_chronicle_issue04_page[1-8]_600dpi.jpg` and `_social.jpg` ($1600\text{px}$).
4. **Native Scribus Layout**: `citadel_chronicle_issue04.sla` (For manual GUI fine-tuning).

---

## 6. Pre-Flight Checklist for Issue 04+ ("First-Go Guarantee")

Before committing, printing, or publishing:

- [ ] **1. Editorial Word Count Budget (8-Page Architecture)**:
  - **Page 1 (Front Cover)**: 450–550 words + Woodcut Hero.
  - **Page 2 (Editorial & Op-Ed)**: 500–600 words + Newsroom Morgue box.
  - **Page 3 (Investigation Part 1)**: 650–750 words + Technical diagram / flow box.
  - **Pages 4–5 (Centerfold Spread)**: 1,200–1,500 words across 4–6 columns + Double-page feature graphic or **"Nothing to Declare"** profile.
  - **Page 6 (The Segregated Witness)**: 500–600 words + Historical woodcut plate.
  - **Page 7 (0-Conf Dispatches & Familiars)**: Two 250-word dispatches + Classifieds/Puppies + Regional announcement.
  - **Page 8 (Back Cover)**: Sponsor / Citadel Coffee display ad + Sovereign Masthead Colophon + full npub & QR code.
- [ ] **2. Legibility & Font Sizing Check**:
  - Verify that ALL editorial body paragraphs are strictly **`9.5pt` – `10.5pt`** with `line-height: 1.32 – 1.38`.
  - Confirm NO body text on any page drops below `9.0pt`.
  - Confirm consistent font size across adjacent columns.
- [ ] **3. Single-Line Headline Verification**:
  - Test headers on both screen and print CSS to confirm no unexpected wrapping cascades.
- [ ] **4. Fill Check**:
  - Render test PDF and check bottom margins. Content must touch $275\text{mm} \pm 5\text{mm}$ on every page.
- [ ] **5. Responsive Test**:
  - Open at mobile viewport ($390\text{px}$ width): confirm single-column flow (P1 $\to$ P8), no text overflow, clean paragraph breaks.
- [ ] **6. Links & URLs**:
  - Verify all podcast, speaker, sponsor, and canonical links.
- [ ] **7. Nostr NIP-23 Package**:
  - Export copy to `issue_XX_nip23.md` with Kind 30023 tags for Nostr publication.
- [ ] **8. GitHub Pages Deployment**:
  - Confirm CNAME is intact (`citadelchronicle.com`) and HTTPS is enforced.

---

## 7. Legacy 4-Page Reference (Single A3 Sheet)
For 1-sheet special editions or commemorative leaflets:
- **Outside Sheet**: `[ Page 4 (Back) | Page 1 (Front) ]`
- **Inside Spread**: `[ Page 2 (Editorial) | Page 3 (Deep Dive) ]`
- Minimum body text floor: `8.5pt` (avoid shrinking below 8.0pt).
