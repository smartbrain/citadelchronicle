#!/usr/bin/env python3
"""
The Citadel Chronicle — Complete Issue 03 Production Engine
Full 4-Page Broadsheet (Rich Graphic Edition):
Page 1: The Voldemort Tilapia & Sun Godling Basil Scandal (Hero Woodcut Cartoon)
Page 2: The Arithmancy of the Fourteen-Day Heretic (St. Mungo's Woodcut Infographic)
Page 3: The Enclosure of the Commons & "The Segregated Witness" (Don's Column Reserve with Courtroom Header)
Page 4: "Liquidation Lady" (NN Profile Spread), The Nine Canine Familiars (Big Puppy Photo) & 0-Conf Dispatches Reserve
"""

import os
import subprocess
import shutil
from PIL import Image

WORKING_DIR = "/home/don/citadelchronicle"
DOWNLOADS_DIR = "/home/don/Downloads"
BLOCKCANDCHAIN_DIR = "/home/don/blockcandchain"

BASE_CSS = """
    :root {
        --paper-bg: #ffffff;
        --paper-bg-alt: #fdfbf7;
        --ink-primary: #0a0a0a;
        --ink-secondary: #222222;
        --ink-accent: #8b1e1e;
        --rule-color: #000000;
    }
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
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
    .font-masthead, .font-blackletter {
        font-family: 'UnifrakturMaguntia', 'Cinzel Decorative', serif !important;
        letter-spacing: 0.01em;
    }
    .masthead-title {
        font-family: 'UnifrakturMaguntia', 'Cinzel Decorative', serif !important;
        font-size: 2.65rem;
        line-height: 0.95;
    }
    .font-headline { font-family: 'Playfair Display', Georgia, serif; }
    .font-body { font-family: 'EB Garamond', Georgia, serif; }
    .font-mono-tech { font-family: 'Courier Prime', monospace; }

    /* A4 Base Page Sheet: Exact 210mm x 297mm */
    .a4-sheet-inner {
        width: 210mm;
        height: 297mm;
        padding: 6.5mm 13mm 6.5mm 13mm;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: #ffffff;
        overflow: hidden;
        position: relative;
        page-break-after: always;
        break-after: page;
    }
    .a4-sheet-inner:last-child {
        page-break-after: avoid;
        break-after: avoid;
    }

    /* Paragraphs */
    .p-copy {
        font-size: 8.1pt;
        line-height: 1.21;
        margin-bottom: 2.2pt;
        text-align: justify;
        text-indent: 8pt;
    }
    .p-copy.no-indent { text-indent: 0; }

    .p-copy-lead {
        font-size: 8.4pt;
        line-height: 1.22;
        margin-bottom: 2.5pt;
        text-align: justify;
        text-indent: 8pt;
    }
    .p-copy-lead.no-indent { text-indent: 0; }

    .drop-cap::first-letter {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.55rem;
        float: left;
        line-height: 0.8;
        padding-top: 2px;
        padding-right: 5px;
        font-weight: 900;
        color: var(--ink-primary);
    }

    
    /* Page 3: Electrum RBF specific typography */
    #p3 p {
        font-size: 7.5pt !important;
        line-height: 1.18 !important;
        margin-bottom: 2.2pt !important;
        text-align: justify !important;
        text-indent: 7pt;
    }
    #p3 p.no-indent { text-indent: 0 !important; }
    #p3 h3 {
        font-family: 'Playfair Display', serif !important;
        font-size: 8.8pt !important;
        font-weight: bold !important;
        margin-top: 3px !important;
        margin-bottom: 1.5px !important;
        color: #111 !important;
        border-bottom: 0.5px solid #000 !important;
        padding-bottom: 1px !important;
    }
    #p3 .drop-cap::first-letter {
        font-family: 'Playfair Display', serif !important;
        font-size: 2.8rem !important;
        line-height: 0.75 !important;
        padding-top: 2px !important;
        padding-right: 4px !important;
        font-weight: 900 !important;
        color: #8b0000 !important;
    }

    /* Page 4: Kathina & Thai font helpers */
    #p4 .thai-font { font-family: 'Pridi', serif !important; }
    #p4 .thai-sans { font-family: 'Sarabun', sans-serif !important; }

    .footer-line {
        border-top: 1.5px solid var(--rule-color);
        padding-top: 2px;
        margin-top: 2px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Courier Prime', monospace;
        font-size: 6.8pt;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
"""

# =========================================================================
# PAGE 1: FRONT COVER (VOLDEMORT, TILAPIA, SUN GODLING, HERO WOODCUT)
# =========================================================================
PAGE_1_HTML = """
<div class="a4-sheet-inner" id="p1">
    <div style="display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
        <!-- TOP RUNNING HEADER / MASTHEAD -->
        <header style="border-bottom: 2px solid #000; padding-bottom: 2px; display: grid; grid-template-columns: 142px 1fr 142px; gap: 8px; align-items: stretch;">
            <!-- Left Ear: Ministry & Ecology Alert -->
            <div style="border: 1px solid #000; padding: 3px 5px; background: #faf8f5; font-family: 'Courier Prime', monospace; font-size: 6.8pt; line-height: 1.22; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-weight: bold; border-bottom: 1px solid #000; padding-bottom: 1px; margin-bottom: 1.5px; display: flex; justify-content: space-between;">
                        <span>MINISTRY ALERT</span>
                        <span>⚡🐟</span>
                    </div>
                    <div><strong>ECOLOGY:</strong> 100% Sorcery</div>
                    <div><strong>TILAPIA:</strong> 400M in Canals</div>
                    <div><strong>HORCRUX:</strong> Amphawa Sighted</div>
                    <div><strong>DEFAMATION WRITS:</strong> 1,200</div>
                </div>
                <div style="font-size: 5.8pt; text-transform: uppercase; border-top: 0.5px solid #ccc; padding-top: 1px; text-align: right;">Purely Coincidental</div>
            </div>

            <!-- Centre Masthead Title -->
            <div style="text-align: center; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div style="font-family: 'Courier Prime', monospace; font-size: 6.8pt; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1px; opacity: 0.85;">“ALL THE RANTS THAT FIT ON ONE SHEET”</div>
                <h1 class="font-masthead masthead-title" style="font-family: 'UnifrakturMaguntia', 'Cinzel Decorative', serif !important; font-size: 2.65rem; line-height: 0.95; margin: 0; letter-spacing: 0.01em;">
                    The Citadel Chronicle
                </h1>
                <div style="width: 100%; display: flex; align-items: center; justify-content: center; margin: 2px 0;">
                    <svg width="100%" height="9" viewBox="0 0 200 9" preserveAspectRatio="none" style="stroke: #000; fill: none;">
                        <line x1="0" y1="5.5" x2="69" y2="5.5" stroke-width="1.2"></line>
                        <rect x="69" y="2.5" width="12" height="6" rx="3" stroke-width="1.2"></rect>
                        <line x1="81" y1="5.5" x2="91" y2="5.5" stroke-width="1.5"></line>
                        <circle cx="100" cy="5.5" r="3.2" fill="#000"></circle>
                        <line x1="109" y1="5.5" x2="119" y2="5.5" stroke-width="1.5"></line>
                        <rect x="119" y="2.5" width="12" height="6" rx="3" stroke-width="1.2"></rect>
                        <line x1="131" y1="5.5" x2="200" y2="5.5" stroke-width="1.2"></line>
                    </svg>
                </div>
                <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 7.5pt; font-weight: bold; white-space: nowrap;">
                    COLD STORAGE, HOT TAKES • <span style="font-family: 'Courier Prime', monospace; font-style: normal; font-weight: bold; font-size: 7pt;">CITADELCHRONICLE.COM • ESTABLISHED 2026</span>
                </div>
            </div>

            <!-- Right Ear: Solar Decree Index -->
            <div style="border: 1px solid #000; padding: 3px 5px; background: #faf8f5; font-family: 'Courier Prime', monospace; font-size: 6.8pt; line-height: 1.22; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-weight: bold; border-bottom: 1px solid #000; padding-bottom: 1px; margin-bottom: 1.5px; display: flex; justify-content: space-between;">
                        <span>SOLAR DECREE</span>
                        <span>☀️🌿</span>
                    </div>
                    <div><strong>HOLY BASIL:</strong> Kaew Juree 01-04</div>
                    <div><strong>HOME CHEWING:</strong> Permitted</div>
                    <div><strong>STREET SALE:</strong> Azkaban Felony</div>
                    <div><strong>SUN GODLING:</strong> Benevolent</div>
                </div>
                <div style="font-size: 5.8pt; text-transform: uppercase; border-top: 0.5px solid #ccc; padding-top: 1px; text-align: right;">Microwave Fortified</div>
            </div>
        </header>

        <!-- DATELINE BAR -->
        <div style="display: flex; justify-content: space-between; align-items: center; font-family: 'Courier Prime', monospace; font-size: 7.2pt; padding: 2px 0; border-bottom: 2px solid #000; white-space: nowrap;">
            <div><strong>VOL. XXI • ISSUE NO. 03</strong> • BLOCK HEIGHT: <strong>973,528</strong> • WEDNESDAY, 28 OCTOBER 2026</div>
            <div>1 SAT/vB • BANGKOK // PATHUM THANI EDITION</div>
        </div>

        <!-- LEAD ARTICLE HEADER -->
        <div style="text-align: center; margin-top: 2.5px; margin-bottom: 2.5px;">
            <div style="font-family: 'Courier Prime', monospace; font-size: 7.2pt; text-transform: uppercase; letter-spacing: 0.12em; color: var(--ink-accent); font-weight: bold;">
                ■ MINISTRY OF MAGIC &amp; SOLAR DECREES • AQUATIC &amp; HERBAL HERESY
            </div>
            <h2 class="font-headline" style="font-size: 1.38rem; font-weight: 900; line-height: 1.08; margin: 1.5px 0; letter-spacing: -0.01em;">
                “HE-WHO-MUST-NOT-BE-NAMED” BLAMED FOR UNLEASHING BLACKCHIN TILAPIA TO RUIN NATION’S PAD KRA PAO
            </h2>
            <div style="font-family: 'Courier Prime', monospace; font-size: 8.3pt; font-weight: bold; text-transform: uppercase; color: var(--ink-accent); margin-bottom: 1.5px;">
                “DEFINITELY NOT A LOCAL MEGACORP,” SAY TERRIFIED OFFICIALS
            </div>
            <p style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 8.8pt; line-height: 1.2; opacity: 0.92; max-width: 98%; margin: 0 auto; border-bottom: 1px solid #000; padding-bottom: 2px;">
                Ministry of Magic announces Lord Voldemort is solely responsible for invasive fish destroying rivers, while The Sun Godling grants citizens royal permission to chew four patented strains of Holy Basil—so long as nobody attempts to sell it.
            </p>
        </div>

        <!-- UPPER SPREAD: 2-COLUMN CARTOON (LEFT) + 1-COLUMN DENSE STORY INTRO (RIGHT) -->
        <div style="display: grid; grid-template-columns: 1.9fr 1.05fr; gap: 11px; margin-bottom: 3px; align-items: stretch;">
            <!-- THE WOODCUT HERO CARTOON -->
            <div style="border: 1.5px solid #000; padding: 2.5px; background: #faf8f5; display: flex; flex-direction: column; justify-content: space-between;">
                <img src="issue-03/ads/blackchin_voldemort_woodcut.jpg" style="width: 100%; height: auto; max-height: 94mm; object-fit: contain; display: block; border: 0.5px solid #000;" onerror="this.src='ads/blackchin_voldemort_woodcut.jpg'">
                <div style="display: flex; justify-content: space-between; align-items: center; font-family: 'Courier Prime', monospace; font-size: 6.4pt; padding: 2px 3px; border-top: 0.5px solid #000; margin-top: 2px; background: #fff;">
                    <span style="font-weight: bold;">FIG 1. THE SAMUT SONGKHRAM CONJURATION</span>
                    <span style="font-family: 'EB Garamond', serif; font-style: italic; font-size: 7.2pt;">“Voldemort apparates Ghanaian cichlids as Sun Godling patents the holy leaf.”</span>
                </div>
            </div>

            <!-- COLUMN 3 (TOP RIGHT): DENSE, PACKED, ZERO DEAD SPACE -->
            <div style="display: flex; flex-direction: column; justify-content: space-between; text-align: justify; border-left: 1px solid #000; padding-left: 11px;">
                <div>
                    <h3 class="font-headline" style="font-size: 8.8pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #000; padding-bottom: 1px; margin-bottom: 2.5px;">
                        I. The Dark Mark Over the Delta
                    </h3>
                    <p class="p-copy-lead drop-cap">
                        If you walk along the brackish canals of Samut Songkhram at dusk, the water no longer ripples with the gentle splash of native walking catfish or freshwater prawns. Instead, the surface boils with the frantic, cannibalistic churning of millions of <em>Sarotherodon melanotheron</em>—the dreaded Blackchin Tilapia.
                    </p>
                    <p class="p-copy-lead">
                        Gaping, alien-jawed, and possessed of terrifying reproductive fervor, this invasive curse has devoured native fingerlings, ruined coastal shrimp farms, and pushed the kingdom’s aquatic biodiversity to the brink of statistical extinction.
                    </p>
                    <p class="p-copy-lead">
                        Yet for months, parliamentary committees and the Department of Fisheries faced an insurmountable metaphysical hurdle: discovering who, precisely, unleashed the pestilence.
                    </p>
                    <p class="p-copy-lead">
                        Yesterday, spokesmen broke their agonised silence during a packed emergency briefing at the Ministry of Magic, unveiling a scientifically unassailable culprit: <strong>He-Who-Must-Not-Be-Named</strong>.
                    </p>
                </div>
                <div style="border-left: 2.5px solid var(--ink-accent); padding-left: 5px; font-family: 'Playfair Display', serif; font-style: italic; font-size: 8pt; font-weight: bold; line-height: 1.18; background: #faf8f5; padding-top: 2px; padding-bottom: 2px; margin-top: 1px;">
                    “The fish did not escape from concrete research tanks. They apparated via dark Death Eater sorcery.”
                </div>
            </div>
        </div>

        <!-- LOWER SPREAD: 3 DETERMINISTIC GRID COLUMNS -->
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 11px; margin-bottom: 1px;">
            <!-- COLUMN 1: VOLDEMORT & DEFAMATION -->
            <div style="border-right: 1px solid #000; padding-right: 11px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <p class="p-copy no-indent">
                        “Following exhaustive introspection, our Divination panels determined that Lord Voldemort, operating via an unlicensed Horcrux smuggled into an Amphawa lychee orchard, is solely responsible,” quavered a terrified senior under-secretary.
                    </p>
                    <p class="p-copy">
                        “To suggest that a benevolent domestic agribusiness conglomerate—whose illuminated 24-hour shrines grace every corner of this realm—imported 2,000 specimen fingerlings from Ghana in 2010 and lost track of them is criminal defamation punishable by twenty years in Azkaban,” the official squeaked, as four Death Eaters in bespoke pin-striped robes nodded with menacing approval.
                    </p>
                    <h3 class="font-headline" style="font-size: 8.6pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #000; padding-bottom: 1px; margin-top: 2px; margin-bottom: 3pt;">
                        II. Silencio Charms &amp; Insinuation
                    </h3>
                    <p class="p-copy">
                        Whenever an opposition MP approaches a microphone and begins to enunciate a syllable rhyming with <em>‘C’</em> or <em>‘P’</em>, parliamentary audio feeds suffer catastrophic <em>Silencio</em> charms. Broadcasts default to soothing harp music, while senior clerks hyperventilate behind stacks of pre-drafted SLAPP injunctions.
                    </p>
                    <p class="p-copy">
                        Outside the courthouse, an armada of three hundred litigation partners stands on 24-hour standby, tasked with serving cease-and-desist writs to every pelican, egret, and alley cat observed consuming an unlicensed tilapia without proper corporate brand indemnity.
                    </p>
                </div>
            </div>

            <!-- COLUMN 2: THE SUN GODLING & THE 4 BASIL PATENTS -->
            <div style="border-right: 1px solid #000; padding-right: 11px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 class="font-headline" style="font-size: 8.6pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #000; padding-bottom: 1px; margin-bottom: 3pt;">
                        III. The Sun Godling’s Solar Decree
                    </h3>
                    <p class="p-copy no-indent">
                        Just as ministerial planners urged the populace to fry the cursed fish into <em>Pad Kra Pao</em>, the crisis collided with an even greater bureaucratic revelation.
                    </p>
                    <p class="p-copy">
                        In a triumph of agro-industrial necromancy, the conglomerate’s ready-meal division quietly secured exclusive Plant Variety Protection over <strong>Four Proprietary Strains of Holy Basil: The Kaew Juree Dynasty (01–04)</strong>. Fortified via polyploidy charms, these patented leaves possess the superhuman ability never to wilt or lose aroma under the relentless microwave bombardment of convenience-store chiller cabinets.
                    </p>
                    <p class="p-copy">
                        When panic erupted over the privatization of the kingdom's sovereign herb, His Solar Radiance, <strong>The Sun Godling</strong> of the Agricultural Ministry, descended from his golden chariot to soothe the trembling populace with an unforgettable Solomonic pronouncement:
                    </p>
                    <div style="border-left: 2px solid var(--ink-accent); padding-left: 5px; font-family: 'Playfair Display', serif; font-style: italic; font-size: 7.7pt; font-weight: bold; line-height: 1.16; background: #faf8f5; margin: 2px 0; padding-top: 2px; padding-bottom: 2px;">
                        “Citizens retain the divine right to chew Kaew Juree basil in the privacy of their homes. You just cannot sell it!”
                    </div>
                    <p class="p-copy">
                        Commercial sizzling, the Sun Godling decreed with radiant benevolence, is an elevated economic sacrament reserved strictly for approved corporate supply chains.
                    </p>
                </div>
            </div>

            <!-- COLUMN 3: SACRED WOK & STATUTORY NOTICE -->
            <div style="display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 class="font-headline" style="font-size: 8.6pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #000; padding-bottom: 1px; margin-bottom: 3pt;">
                        IV. The Pincer on the Sacred Wok
                    </h3>
                    <p class="p-copy no-indent">
                        The realm’s humble street vendors now find themselves trapped in a terrifying dystopian pincer. On the left flank, waterways choked with bony, muddy African mud-feeders that taste of industrial runoff; on the right flank, Ministry Aurors bearing portable DNA spectrometers, ready to arrest any hawker whose sizzling garlic reveals unlicensed <em>Kaew Juree</em> genetic markers.
                    </p>
                    <p class="p-copy">
                        “I tried tossing an unmentionable canal fish with backyard weed,” wept Somchai outside the Citadel gates. “The fish tasted of corporate indemnity, and before the chili blistered, bailiffs slapped an injunction on my mortar. It does not absorb chili; it absorbs despair.”
                    </p>
                    <p class="p-copy">
                        Listening over flat whites at the Citadel Tavern, Lung Chaloke observed: “When late-stage fiat decays, the Ministry legalises the polluter’s plague and patents the peasant’s weed. They privatised breeding profits, cursed the rivers, and the Sun Godling permits chewing only in private. Do not barter with their solicitors. Stack satoshis, save heirloom seeds, and cook with fire they cannot patent.”
                    </p>
                </div>

                <!-- STATUTORY SATIRICAL DISCLAIMER BOX -->
                <div style="border: 1px solid #000; background: #faf8f5; padding: 2.5px 4.5px; margin-top: 2px; font-family: 'Courier Prime', monospace; font-size: 5.7pt; line-height: 1.15;">
                    <div style="font-weight: bold; color: var(--ink-accent); border-bottom: 0.5px solid #000; padding-bottom: 1px; margin-bottom: 1px;">
                        ⚖️ STATUTORY NOTICE / BOTANICAL &amp; DEFAMATION SHIELD:
                    </div>
                    Any phonetic resemblance between this biological plague, these four proprietary holy leaves (Kaew Juree 01–04), and any multi-billion-baht poultry, swine, cold-storage, and 24-hour convenience store monopoly operating within the kingdom is entirely accidental, unmentionable before the Wizengamot, and subject to instantaneous summary ruin under both the Computer Crimes Act and the Herbological Patents Decree of 1999.
                </div>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="footer-line">
        <div>PAGE 1 OF 4 • FRONT COVER • EPISODE 03</div>
        <div>THE CITADEL CHRONICLE • CITADELCHRONICLE.COM • ESTABLISHED 2026</div>
    </footer>
</div>
"""

# =========================================================================
# PAGE 2: THE ARITHMANCY OF THE FOURTEEN-DAY HERETIC (WOODCUT INFOGRAPHIC)
# =========================================================================
PAGE_2_HTML = """
<div class="a4-sheet-inner" id="p2">
    <div style="display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
        <!-- RUNNING PAGE HEADER -->
        <header style="border-bottom: 2px solid #000; padding-bottom: 2px; display: flex; justify-content: space-between; align-items: flex-end;">
            <div style="font-family: 'Courier Prime', monospace; font-size: 7.2pt; font-weight: bold;">
                THE CITADEL CHRONICLE • WEDNESDAY, 28 OCTOBER 2026 • BLOCK HEIGHT: 973,528
            </div>
            <div class="font-headline" style="font-size: 9pt; font-style: italic; font-weight: bold; letter-spacing: 0.05em;">
                Dispatches from the Ministry &amp; St. Mungo's
            </div>
            <div style="font-family: 'Courier Prime', monospace; font-size: 7.2pt; font-weight: bold;">
                PAGE 2 OF 4
            </div>
        </header>

        <!-- FEATURE ARTICLE HEADER -->
        <div style="text-align: center; margin-top: 3px; margin-bottom: 3px;">
            <div style="font-family: 'Courier Prime', monospace; font-size: 7.2pt; text-transform: uppercase; letter-spacing: 0.14em; color: var(--ink-accent); font-weight: bold;">
                ■ DEPARTMENT OF MAGICAL EPIDEMIOLOGY &amp; APOTHECARY ARITHMANCY
            </div>
            <h2 class="font-headline" style="font-size: 1.5rem; font-weight: 900; line-height: 1.08; margin: 2px 0; letter-spacing: -0.01em;">
                THE ARITHMANCY OF THE FOURTEEN-DAY HERETIC
            </h2>
            <div style="font-family: 'Courier Prime', monospace; font-size: 8.2pt; font-weight: bold; text-transform: uppercase; color: var(--ink-accent); margin-bottom: 1.5px;">
                HOW ST. MUNGO’S STATISTICAL ALCHEMISTS TRANSMUTED IMMEDIATE POTION CASUALTIES INTO PROOF OF 99.9% EFFICACY
            </div>
            <p style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 8.8pt; line-height: 1.2; opacity: 0.92; max-width: 98%; margin: 0 auto; border-bottom: 1px solid #000; padding-bottom: 2px;">
                Under St. Mungo’s Decree No. 714, anyone expiring within fourteen days of drinking the dragonblood elixir is strictly classified as “Un-Draughted”—revealing the extraordinary mathematical law that the more lethal the brew, the higher its certified protection.
            </p>
        </div>

        <!-- HERO WOODCUT INFOGRAPHIC (CENTER SPREAD) -->
        <div style="border: 1.5px solid #000; padding: 2.5px; background: #faf8f5; margin-bottom: 3.5px;">
            <img src="issue-03/ads/fourteen_day_arithmancy_woodcut.jpg" style="width: 100%; height: auto; max-height: 84mm; object-fit: contain; display: block; border: 0.5px solid #000;" onerror="this.src='ads/fourteen_day_arithmancy_woodcut.jpg'">
            <div style="display: flex; justify-content: space-between; align-items: center; font-family: 'Courier Prime', monospace; font-size: 6.4pt; padding: 2px 4px; border-top: 0.5px solid #000; margin-top: 2px; background: #fff;">
                <span style="font-weight: bold;">FIG 2. ST. MUNGO'S TEMPORAL ALCHEMY (DECREE NO. 714)</span>
                <span style="font-family: 'EB Garamond', serif; font-style: italic; font-size: 7.2pt;">“Immediate casualties tallied under the Unvaccinated Roll (Days 1–13), mechanistically generating 99.9% clinical protection.”</span>
            </div>
        </div>

        <!-- 3-COLUMN STORY TEXT -->
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 11px; margin-bottom: 1px;">
            <!-- COLUMN 1: THE DECREE & PHYSIOLOGICAL DELAY -->
            <div style="border-right: 1px solid #000; padding-right: 11px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 class="font-headline" style="font-size: 8.6pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #000; padding-bottom: 1px; margin-bottom: 3pt;">
                        I. The Incubation Decree
                    </h3>
                    <p class="p-copy drop-cap">
                        When the great Spattergroit panic threatened the apothecaries of Diagon Alley, the Wizengamot acted with characteristic bureaucratic heroism. Bypassing centuries of herbal safety trials, the Ministry authorised emergency distribution of the <strong>Mandatory Pepperup-Dragonblood Elixir (Batch 4.2)</strong>, commanding every wizard, witch, and registered squib to present their upper arm at the nearest dispensary.
                    </p>
                    <p class="p-copy">
                        Yet even the most zealous ministerial alchemists acknowledged a minor physiological technicality: magical humors do not transmute instantaneously. A draught requires time to circulate through the spleen, align with the celestial moon phase, and coat the ethereal organs in protective mucus.
                    </p>
                    <p class="p-copy">
                        To accommodate this biological lag, St. Mungo’s Hospital promulgated <strong>Decree No. 714</strong>:
                    </p>
                    <div style="border-left: 2px solid var(--ink-accent); padding-left: 5px; font-family: 'Playfair Display', serif; font-style: italic; font-size: 7.7pt; font-weight: bold; line-height: 1.16; background: #faf8f5; margin: 2px 0; padding-top: 2px; padding-bottom: 2px;">
                        “Any citizen who imbibes the Draught shall, for exactly fourteen solar days following administration, be legally and statistically deemed Wholly Un-Draughted.”
                    </div>
                    <p class="p-copy">
                        On paper, the rule appeared the very model of administrative prudence. If a wizard were struck down by Spattergroit on Day 3, it would be terribly unfair to blame the elixir; the shield had simply not had time to solidify.
                    </p>
                </div>
            </div>

            <!-- COLUMN 2: THE SHIFTING DENOMINATOR & INVERSE TOXICITY -->
            <div style="border-right: 1px solid #000; padding-right: 11px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 class="font-headline" style="font-size: 8.6pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #000; padding-bottom: 1px; margin-bottom: 3pt;">
                        II. Shifting Denominators
                    </h3>
                    <p class="p-copy no-indent">
                        Human biology is a messy, unpredictable medium. While the majority of recipients suffered merely purple tongue and mild levitation, a non-trivial cohort experienced more pronounced adverse reactions.
                    </p>
                    <p class="p-copy">
                        Within forty-eight hours of receiving the jab, some patients sprouted basilisk scales. Others suffered kidney petrification, exploded into sulfurous brimstone, or collapsed directly onto the apothecary floorboards with wands still smoking.
                    </p>
                    <p class="p-copy">
                        Under ordinary arithmetic, such mishaps might have raised questions regarding the dragonblood stabiliser. But under Decree No. 714, a miraculous statistical alchemy occurred.
                    </p>
                    <p class="p-copy">
                        Because the deceased had passed away within the sacred two-week incubation window, attending Healers were legally forbidden from classifying them as “Draughted.” With a swift stroke of a peacock quill, every collapsed patient was logged into the mortality rolls under: <strong>“TRAGIC CASUALTY AMONG THE UN-DRAUGHTED POPULATION.”</strong>
                    </p>
                    <h3 class="font-headline" style="font-size: 8.6pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #000; padding-bottom: 1px; margin-top: 2px; margin-bottom: 3pt;">
                        III. The Inverse Toxicity Law
                    </h3>
                    <p class="p-copy">
                        In the subterranean chambers of Magical Arithmancy, young clerks realized they had stumbled upon a mathematical perpetual-motion machine: <em>The worse the medicine, the higher its certified efficacy!</em>
                    </p>
                </div>
            </div>

            <!-- COLUMN 3: THE PROOF & CITADEL COMMENTARY -->
            <div style="display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <p class="p-copy no-indent">
                        Every patient killed by the potion between Day 0 and Day 13 was added to the <strong>Unvaccinated</strong> death toll, artificially inflating the apparent lethality of the disease among the non-compliant, while leaving the post-Day-14 survivor cohort pristine and pre-filtered.
                    </p>
                    <p class="p-copy">
                        In a leaked memo to the Wizengamot, a senior Arithmancer proved that if potion toxicity were doubled so that 98% of recipients perished within 72 hours, the mortality rate among the Un-Draughted would approach infinity, rendering the Elixir 100.00% clinically protective. The Chief Healer wept with joy and awarded the statistician an Order of Merlin, Second Class.
                    </p>
                    <h3 class="font-headline" style="font-size: 8.6pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #000; padding-bottom: 1px; margin-top: 2px; margin-bottom: 3pt;">
                        IV. The Citadel Commentary
                    </h3>
                    <p class="p-copy">
                        Reviewing the scrolls over flat whites at the Citadel Tavern, Lung Chaloke remarked: “When fiat central banks go bankrupt, they alter the CPI basket to prove beef is cheap. When fiat medicine kills the patient, the state alters the denominator to prove the poison is life itself. The grift relies on settlement delay. Stack physical satoshis, maintain your own immunity, and never trust an arithmancer whose salary depends on defining who is alive.”
                    </p>
                </div>

                <!-- STATUTORY SATIRICAL DISCLAIMER BOX -->
                <div style="border: 1px solid #000; background: #faf8f5; padding: 2.5px 4.5px; margin-top: 2px; font-family: 'Courier Prime', monospace; font-size: 5.7pt; line-height: 1.15;">
                    <div style="font-weight: bold; color: var(--ink-accent); border-bottom: 0.5px solid #000; padding-bottom: 1px; margin-bottom: 1px;">
                        ⚖️ ST. MUNGO'S EPIDEMIOLOGICAL STATUTE / NOTICE NO. 714:
                    </div>
                    All patients surviving past midnight of Day 14 are hereby consecrated into the Sanctified Cohort of Immaculate Protection. Any post-Day-14 mortality shall be officially deemed a Breakthrough Mystery caused by breathing near an un-draughted Muggle.
                </div>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="footer-line">
        <div>PAGE 2 OF 4 • APOTHECARY ARITHMANCY • EPISODE 03</div>
        <div>THE CITADEL CHRONICLE • CITADELCHRONICLE.COM • ESTABLISHED 2026</div>
    </footer>
</div>
"""

# =========================================================================
# PAGE 3: ENCLOSURE OF COMMONS & "THE SEGREGATED WITNESS" (DON'S COLUMN)
# =========================================================================
PAGE_3_HTML = """
<div class="a4-sheet-inner" id="p3">
    <div style="display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
        <!-- RUNNING PAGE HEADER -->
        <header style="border-bottom: 2px solid #000; padding-bottom: 2px; display: flex; justify-content: space-between; align-items: flex-end;">
            <div style="font-family: 'Courier Prime', monospace; font-size: 7.2pt; font-weight: bold;">
                THE CITADEL CHRONICLE • WEDNESDAY, 28 OCTOBER 2026 • BLOCK HEIGHT: 973,528
            </div>
            <div class="font-headline" style="font-size: 9pt; font-style: italic; font-weight: bold; letter-spacing: 0.05em;">
                Special Investigation: Protocol Forensics &amp; The Architecture of Exploits
            </div>
            <div style="font-family: 'Courier Prime', monospace; font-size: 7.2pt; font-weight: bold;">
                PAGE 3 OF 4
            </div>
        </header>

        <!-- MAIN ARTICLE HEADER -->
        <div style="text-align: center; margin-top: 3px; margin-bottom: 5px; border-bottom: 1.5px solid #000; padding-bottom: 4px;">
            <div style="font-family: 'Courier Prime', monospace; font-size: 7.2pt; text-transform: uppercase; letter-spacing: 0.14em; color: #8b0000; font-weight: bold;">
                ■ MEMPOOL FORENSICS • CRITICAL SECURITY DISCLOSURE • GHSA-6jp4-8v48-cc5v
            </div>
            <h1 class="font-headline" style="font-size: 1.62rem; font-weight: 900; line-height: 1.05; margin: 3px 0 2px 0; letter-spacing: -0.01em;">
                THE WEAPONISED FEE-BUMP: INSIDE THE ELECTRUM RBF HEIST
            </h1>
            <div style="font-family: 'Courier Prime', monospace; font-size: 8.2pt; font-weight: bold; text-transform: uppercase; color: #8b0000; margin-bottom: 3pt;">
                HOW ROGUE SERVERS EXPLOITED THE SPV MEMPOOL BLINDSPOT TO TRICK BITCOINERS INTO SIGNING OVER THEIR OWN FUNDS
            </div>
            <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 8pt; line-height: 1.18; max-width: 90%; margin: 0 auto; color: #333;">
                A forensic examination of the high-severity vulnerability patched in Electrum v4.8.3, where adversaries bypassed private-key cryptography by turning the client’s Replace-By-Fee routine into an involuntary double-spend guillotine.
            </div>
        </div>

        <!-- 2 BALANCED COLUMNS LAYOUT -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; text-align: justify; flex-grow: 1;">
            
            <!-- COLUMN 1: THE VULNERABILITY & THE SPV MEMPOOL ASYMMETRY -->
            <div style="border-right: 0.5px solid #000; padding-right: 12px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <p class="drop-cap no-indent">
                        On 24 October 2026, the maintainers of the Electrum Bitcoin wallet published a security advisory tracked as <strong>GHSA-6jp4-8v48-cc5v</strong> and rushed out version 4.8.3. The vulnerability had not merely been discovered in an academic laboratory; it had been actively and ruthlessly exploited in the wild against users operating on public Electrum servers.
                    </p>
                    <p>
                        What makes this exploit one of the most intellectually diabolical vectors in Bitcoin client history is that the adversary never broke secp256k1 elliptic curve cryptography, nor did they exfiltrate seed phrases or compromise operating systems. Instead, they weaponised the client’s architectural trust boundary and the user’s own muscle memory, tricking victims into voluntarily authorising and signing the theft of their own coins.
                    </p>

                    <h3>The SPV Mempool Blindspot</h3>
                    <p class="no-indent">
                        To understand how the heist operates, one must examine the delicate compromise that makes lightweight Bitcoin wallets possible. In Satoshi Nakamoto’s original design, Simplified Payment Verification (SPV) relies upon 80-byte block headers. When an SPV client receives a <em>confirmed</em> transaction, it cryptographically verifies a Merkle inclusion proof tying that transaction hash to a header buried under cumulative Proof-of-Work. An untrusted server cannot fabricate a confirmed block without overcoming the hashpower of the global network.
                    </p>
                    <p>
                        For <em>unconfirmed</em> transactions floating in the mempool, however, this cryptographic anchor vanishes entirely. In the mempool, there is no Proof-of-Work, no consensus, and no Merkle tree.
                    </p>
                    <p>
                        When an Electrum client synchronises with an external server over JSON-RPC, it queries its addresses via <code>blockchain.scripthash.subscribe</code>. If a transaction has a height of zero or negative, the server asserts that it is an unconfirmed payment sitting in the mempool.
                    </p>
                    <p>
                        Historically, Electrum’s codebase contained a fateful assumption: if an unconfirmed transaction consumed UTXOs belonging to the local wallet (<code>wallet.is_mine</code>), the wallet assumed it was either created by the local user or broadcast from another valid clone. <strong>Crucially, pre-4.8.3 Electrum did not execute the script engine to cryptographically verify signatures on unconfirmed incoming inputs.</strong>
                    </p>

                    <h3>Phase 1 &amp; 2: Interception and Synthetic Forgery</h3>
                    <p class="no-indent">
                        The ambush begins when an unsuspecting user broadcasts a legitimate payment (Tx1)—for example, transferring 2.5 BTC to cold storage.
                    </p>
                    <p>
                        The client relays Tx1 to its connected Electrum server via <code>blockchain.transaction.broadcast</code>. If that server is malicious, it silently suppresses Tx1, refusing to gossip it to the broader Bitcoin P2P network.
                    </p>
                    <p>
                        The rogue server immediately constructs an alternative transaction (Tx_fake). It consumes the <em>exact same UTXOs</em> as Tx1, but redirects the output entirely to an address controlled by the attacker. Because the attacker possesses no private keys, Tx_fake contains <em>invalid dummy signatures</em>. Attackers deployed GPU vanity tools so the final four to six characters matched the victim’s intended address, set a fee of 1 sat/vB with BIP 125 opt-in RBF, and fed Tx_fake back to the wallet. Because Electrum skipped signature checks, the fake transaction appeared in the GUI as a pending payment.
                    </p>
                </div>
            </div>

            <!-- COLUMN 2: THE RBF WEAPONISATION, FLOW BOX & THE FIX -->
            <div style="display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3>Phase 3 &amp; 4: The RBF Trap and Fatal Ratification</h3>
                    <p class="no-indent">
                        Because Tx_fake contained invalid signatures, no honest miner would ever include it in a block. To the user, the transaction appeared hopelessly stalled in the mempool.
                    </p>
                    <p>
                        The natural reaction in Bitcoin UX when a transaction is stuck is to right-click and select <strong>"Increase Fee" (Replace-By-Fee)</strong>. When the user initiated the fee bump, Electrum loaded Tx_fake from its internal history as the base transaction template. The UI displayed a dialogue asking for a higher fee rate.
                    </p>
                    <p>
                        Human psychology and standard hardware wallet UX conspired to seal the trap. When performing an RBF bump, users invariably check only the fee delta (e.g. bumping from 1 sat/vB to 35 sat/vB), assuming the recipient address is immutable from their initial creation.
                    </p>
                    <p>
                        The victim typed their passphrase or approved the prompt on their Ledger, Trezor, or Coldcard. In doing so, the wallet generated <strong>pristine, mathematically valid ECDSA or Schnorr signatures over the attacker’s outputs</strong>. The resulting transaction was immediately relayed, accepted by Bitcoin Core mempools across the globe, and permanently mined into the ledger. The theft was absolute.
                    </p>

                    <!-- COMPACT FLOW DIAGRAM BOX -->
                    <div style="border: 1.5px solid #8b0000; background: #fffcf5; padding: 4.5px 7px; margin: 4px 0 5px 0; font-family: 'Courier Prime', monospace; font-size: 6pt; line-height: 1.26; box-shadow: 1.5px 1.5px 0 #000;">
                        <div style="font-weight: bold; color: #8b0000; border-bottom: 0.5px solid #8b0000; padding-bottom: 1.5px; margin-bottom: 2.5px; text-align: center;">
                            ▲ THE ANATOMY OF THE RBF TRAP (GHSA-6jp4-8v48-cc5v) ▲
                        </div>
                        <div>1. <strong>VICTIM</strong> broadcasts Tx1 (Valid recipient, fully signed).</div>
                        <div>2. <strong>ROGUE SERVER</strong> withholds Tx1 from P2P gossip network.</div>
                        <div>3. <strong>SERVER INJECTS</strong> Tx_fake (Same UTXO, vanity attacker output, BOGUS signatures).</div>
                        <div>4. <strong>CLIENT ACCEPTS</strong> Tx_fake into GUI (Skipped unconfirmed sig check!).</div>
                        <div>5. <strong>TX STALLS</strong>: Victim right-clicks "Increase Fee" (RBF).</div>
                        <div>6. <strong>FATAL RATIFICATION</strong>: Victim signs fee bump &bull; Wallet generates <em>real, valid signatures</em> over the attacker's output!</div>
                        <div>7. <strong>THEFT COMPLETE</strong>: Valid Tx_stolen mined on chain.</div>
                    </div>

                    <h3>The Remediation: Commit 90fe308</h3>
                    <p class="no-indent">
                        Lead maintainer SomberNight resolved the flaw in commit <code>90fe308</code> by dismantling the assumption of mempool innocence. Electrum v4.8.3 now enforces strict client-side signature verification: before any unconfirmed transaction touching <code>wallet.is_mine</code> UTXOs is accepted into the wallet database, the client validates that the input signatures mathematically correspond to the scriptPubKey. Any forged or invalid server injection is rejected outright and never reaches the GUI.
                    </p>
                </div>

                <!-- EDITORIAL TAKEAWAYS BOX -->
                <div style="border: 1.5px solid #000; background: #faf8f5; padding: 5px 7px; margin-top: 3px; font-size: 7.1pt; line-height: 1.22; box-shadow: 1.5px 1.5px 0 #000;">
                    <div style="font-family: 'Courier Prime', monospace; font-weight: bold; color: #8b0000; border-bottom: 0.5px solid #000; padding-bottom: 1px; margin-bottom: 2.5px; display: flex; justify-content: space-between;">
                        <span>■ LESSONS FOR THE CITADEL SANCTUARY</span>
                        <span>SOVEREIGN MANDATE</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr; gap: 2px;">
                        <div>• <strong>UPGRADE MANDATORY</strong>: All users operating Electrum must update to version <strong>4.8.3 or higher</strong>. Verify PGP signatures directly from <code>electrum.org</code>.</div>
                        <div>• <strong>INSPECT FULL OUTPUTS</strong>: Whenever executing an RBF fee bump, verify the entire recipient address on your hardware signer screen, not merely the fee rate.</div>
                        <div>• <strong>RUN A SOVEREIGN SERVER</strong>: Users who connected to their own private <strong>Fulcrum</strong>, <strong>Electrs</strong>, or <strong>EPS</strong> nodes backed by Bitcoin Core were completely immune. Public servers are third-party trust traps. <em>Don't trust, verify.</em></div>
                    </div>
                </div>

                <div style="font-family: 'Courier Prime', monospace; font-size: 5.6pt; text-align: right; color: #666; margin-top: 2px;">
                    REPORTED BY THE CITADEL PROTOCOL DESK • CITADELCHRONICLE.COM
                </div>
            </div>

        </div>

        <!-- BASEMENT: 0-CONF DISPATCHES -->
        <section style="border-top: 2px solid #000; margin-top: 3px; padding-top: 2.5px;">
            <!-- SECTION HEADER -->
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #000; padding-bottom: 1.5px; margin-bottom: 2.5px;">
                <span style="font-family: 'Courier Prime', monospace; font-size: 6.6pt; font-weight: bold; text-transform: uppercase; color: #8b0000; letter-spacing: 0.08em;">
                    ■ 0-CONF DISPATCHES • UNCONFIRMED MEMPOOL INTELLIGENCE &amp; JURISPRUDENCE
                </span>
                <span style="font-family: 'Courier Prime', monospace; font-size: 5.8pt; color: #555;">
                    TRANSACTIONS STREAMING DIRECT FROM THE MEMPOOL
                </span>
            </div>

            <!-- TWO BALANCED DISPATCH COLUMNS -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; align-items: start;">
                <!-- DISPATCH 1: THAI SUPREME COURT BITCOIN IS PROPERTY -->
                <article style="border-right: 0.5px solid #ccc; padding-right: 8px;">
                    <div style="font-family: 'Courier Prime', monospace; font-size: 5.4pt; font-weight: bold; text-transform: uppercase; color: #8b0000; margin-bottom: 0.5px;">
                        JURISPRUDENCE &bull; SUPREME COURT EN BANC RULING 4929/2569
                    </div>
                    <h4 class="font-headline" style="font-size: 8.8pt; font-weight: 900; line-height: 1.1; margin: 0 0 1px 0;">
                        SATOSHI’S CASH BECOMES INVENTORIED CHATTEL
                    </h4>
                    <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 6.2pt; line-height: 1.15; color: #333; margin-bottom: 2px;">
                        Thai Supreme Court rules 2.48 BTC is legally "Property" in £40,000 Koh Samui beach heist.
                    </div>
                    <p style="font-size: 6.4pt; line-height: 1.16; text-align: justify; margin: 0; color: #111;">
                        When Satoshi Nakamoto drafted his 2008 whitepaper, he titled it with spartan simplicity: <em>Bitcoin: A Peer-to-Peer Electronic Cash System</em>. The Thai judiciary, however, has codified a rather different taxonomy. In a historic en banc ruling (<em>Supreme Court Decision No. 4929/2569</em>), the Kingdom’s highest bench formally decreed that Bitcoin is not ephemeral cyber-dust, but bona fide <em>incorporeal property</em> under Sections 137 and 138 of the Civil and Commercial Code.
                    </p>
                    <p style="font-size: 6.4pt; line-height: 1.16; text-align: justify; text-indent: 5pt; margin-top: 1.5px; margin-bottom: 0; color: #111;">
                        The precedent stemmed from an extortion on Koh Samui, where a foreign gang coerced a couple in a café—under threats to their infant child—to convert 0,000 into 2.480801 BTC transferred to an offshore wallet. The defence claimed that because Bitcoin possesses no corporeal form and no state-mandated value, no robbery of chattel had occurred. The bench rejected the sophistry outright: holding that digital assets command measurable market value and exclusive dominion via cryptographic keys, the Court confirmed a ten-year penal stretch for armed robbery. Satoshi engineered sovereign cash; Thailand's prison wardens now treat it as fully confiscable property.
                    </p>
                </article>

                <!-- DISPATCH 2: KORN CHATIKAVANIJ & BLOCKCHAIN TRACKING -->
                <article>
                    <div style="font-family: 'Courier Prime', monospace; font-size: 5.4pt; font-weight: bold; text-transform: uppercase; color: #8b0000; margin-bottom: 0.5px;">
                        FORENSIC AUDITING &bull; THE COGNITIVE DEFICIT OF CRIME
                    </div>
                    <h4 class="font-headline" style="font-size: 8.8pt; font-weight: 900; line-height: 1.1; margin: 0 0 1px 0;">
                        KORN HAILS THE OPEN LEDGER; CRIMINALS FAIL ARITHMANCY
                    </h4>
                    <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 6.2pt; line-height: 1.15; color: #333; margin-bottom: 2px;">
                        Former Finance Minister marvels at 118m-baht on-chain gambling trail, exposing the sub-standard intellect of cartel laundering.
                    </div>
                    <p style="font-size: 6.4pt; line-height: 1.16; text-align: justify; margin: 0; color: #111;">
                        Former Finance Minister Korn Chatikavanij took to Facebook this week to shower unexpected praise upon public blockchains. Reflecting on a forensic dossier compiled by former Democrat MP Sirichok Sopa—who mapped nearly 10,000 transactions totaling 118 million Baht linked to illegal gambling platform <em>Shuffle</em> without requiring a single court warrant or bank subpoena—Korn proclaimed: <em>"Crypto is not the villain here; it may well be the hero."</em>
                    </p>
                    <p style="font-size: 6.4pt; line-height: 1.16; text-align: justify; text-indent: 5pt; margin-top: 1.5px; margin-bottom: 0; color: #111;">
                        While Mr. Korn noted that unlike opaque bank mule accounts or borderland bags of cash, public ledgers provide an indelible trail for the state, his diplomatic assessment delicately sidestepped the larger psychological reality: the comical IQ deficit of the modern money launderer. To launder illicit revenue across a globally broadcast, permanent ledger is akin to burgling a vault whilst wearing a high-visibility neon vest, a bodycam livestreaming to YouTube, and handing out numbered receipts. Satoshi gave humanity an unforgeable public receipt machine; only the most intellectually deficient cartels would choose it as a hideaway.
                    </p>
                </article>
            </div>
        </section>
    </div>

    <!-- FOOTER -->
    <footer class="footer-line">
        <div>PAGE 3 OF 4 • PROTOCOL FORENSICS: ELECTRUM RBF WEAPONISATION • EPISODE 03</div>
        <div>THE CITADEL CHRONICLE • CITADELCHRONICLE.COM • ESTABLISHED 2026</div>
    </footer>
</div>
"""

# =========================================================================
# PAGE 4: THE BACK PAGE (LIQUIDATION LADY + 9 PUPPIES + 0-CONF DISPATCHES)
# =========================================================================
PAGE_4_HTML = """
<div class="a4-sheet-inner" id="p4">
    <div style="display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
        <!-- RUNNING PAGE HEADER -->
        <header style="border-bottom: 2px solid #000; padding-bottom: 2px; display: flex; justify-content: space-between; align-items: flex-end;">
            <div style="font-family: 'Courier Prime', monospace; font-size: 7.2pt; font-weight: bold;">
                THE CITADEL CHRONICLE • WEDNESDAY, 28 OCTOBER 2026 • BLOCK HEIGHT: 973,528
            </div>
            <div class="font-headline" style="font-size: 9pt; font-style: italic; font-weight: bold; letter-spacing: 0.05em;">
                The Back Page: Khao Wanchai Kathina, The Segregated Witness &amp; Familiars
            </div>
            <div style="font-family: 'Courier Prime', monospace; font-size: 7.2pt; font-weight: bold;">
                PAGE 4 OF 4
            </div>
        </header>

        <!-- TOP SECTION: KATHINA CEREMONY SPREAD (WAT KHAO WANCHAI NAWARAT) -->
        <section style="border: 2px solid #8b0000; padding: 4px 6.5px; background: #fffcf5; margin-top: 2px; margin-bottom: 3px; box-shadow: 2px 2px 0px rgba(0,0,0,0.8);">
            <!-- BANNER HEADER -->
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #8b0000; padding-bottom: 1px; margin-bottom: 2.5px;">
                <span style="font-family: 'Courier Prime', monospace; font-size: 7pt; font-weight: bold; text-transform: uppercase; color: #8b0000;">
                    ☸ งานบุญมหากุศล • KATHINA &amp; FOUNDATION PILLAR CEREMONY • PAK CHONG
                </span>
                <span style="font-family: 'Sarabun', sans-serif; font-size: 6.5pt; font-weight: bold; color: #555;">
                    วัดเขาวันชัยนวรัตน์ (สาขาที่ 82 วัดหนองป่าพง) • 31 ต.ค. – 1 พ.ย. 2569
                </span>
            </div>

            <!-- MAIN GRID: POSTER 1 (LEFT) + POSTER 2 (CENTER) + TEXT / SCHEDULE (RIGHT) -->
            <div style="display: grid; grid-template-columns: 46mm 46mm 1fr; gap: 7px; align-items: stretch;">
                <!-- POSTER 1: KATHINA FLYER -->
                <div style="border: 1px solid #000; padding: 1.5px; background: #fff; box-shadow: 1.5px 1.5px 0 #000; display: flex; flex-direction: column; justify-content: space-between;">
                    <img src="issue-03/ads/kathina_khao_wanchai_01.jpg" style="width: 100%; height: auto; max-height: 80mm; object-fit: contain; display: block; border: 0.5px solid #ccc;">
                    <div style="font-family: 'Sarabun', sans-serif; font-size: 5.2pt; text-align: center; margin-top: 1px; font-weight: bold; background: #faf8f5; padding: 1px 0; border-top: 0.5px solid #000;">
                        ★ กองกฐินสามัคคีสร้างเจดีย์ &amp; 79 ปี หลวงพ่อ ★
                    </div>
                </div>

                <!-- POSTER 2: FOUNDATION PILLAR FLYER -->
                <div style="border: 1px solid #000; padding: 1.5px; background: #fff; box-shadow: 1.5px 1.5px 0 #000; display: flex; flex-direction: column; justify-content: space-between;">
                    <img src="issue-03/ads/kathina_khao_wanchai_02.jpg" style="width: 100%; height: auto; max-height: 80mm; object-fit: contain; display: block; border: 0.5px solid #ccc;">
                    <div style="font-family: 'Sarabun', sans-serif; font-size: 5.2pt; text-align: center; margin-top: 1px; font-weight: bold; background: #faf8f5; padding: 1px 0; border-top: 0.5px solid #000;">
                        ★ พิธียกเสาเอก รัตนเจดีย์ศรีดวงแก้วโพธิญาณ ★
                    </div>
                </div>

                <!-- RIGHT COLUMN: EDITORIAL ANNOUNCEMENT & CEREMONIAL PROGRAMME -->
                <div style="display: flex; flex-direction: column; justify-content: space-between; padding-left: 2px;">
                    <div>
                        <div style="font-family: 'Pridi', serif; font-size: 10.5pt; font-weight: 700; color: #8b0000; line-height: 1.15; margin-bottom: 1.5px;">
                            ขอเชิญร่วมบุญทอดกฐินสามัคคี &amp; ยกเสาเอกเจดีย์
                        </div>
                        <div style="font-family: 'Playfair Display', serif; font-size: 7.5pt; font-style: italic; font-weight: bold; margin-bottom: 2px; border-bottom: 0.5px solid #8b0000; padding-bottom: 1px;">
                            Wat Khao Wanchai Nawarat Chedi Foundation &bull; Pak Chong Gathering
                        </div>
                        <p style="font-family: 'Sarabun', sans-serif; font-size: 6.6pt; line-height: 1.22; text-align: justify; margin-bottom: 2.5px; color: #222;">
                            สุดสัปดาห์นี้ ขอเรียนเชิญกัลยาณมิตร ศิษยานุศิษย์ และพี่น้องชาว Citadel ทุกท่าน ร่วมเดินทางสู่ อ.ปากช่อง จ.นครราชสีมา เพื่อร่วมบุญมหากุศลทอดกฐินสามัคคีสมทบทุนสร้าง <strong>"รัตนเจดีย์ศรีดวงแก้วโพธิญาณ"</strong> และมุทิตาสักการะอายุวัฒนมงคล 79 ปี <strong>หลวงพ่อพระครูภาวนาอุดมคุณ</strong> โดย <strong>อาจารย์โฉลก สัมพันธารักษ์</strong> พร้อมครอบครัว และคณะศิษย์ CDC จะเดินทางไปร่วมสร้างมหาทานบารมีในครั้งนี้โดยพร้อมเพรียงกัน
                        </p>
                    </div>

                    <!-- SCHEDULE & PROMPTPAY E-DONATION QR SPREAD -->
                    <div style="display: grid; grid-template-columns: 1fr 31mm; gap: 6px; align-items: stretch; margin-top: 2px;">
                        <!-- SCHEDULE BOX -->
                        <div style="border: 1px solid #8b0000; background: #fff; padding: 2.5px 4.5px; font-size: 5.6pt; line-height: 1.2; display: flex; flex-direction: column; justify-content: space-between;">
                            <div>
                                <div style="font-family: 'Pridi', serif; font-weight: bold; color: #8b0000; border-bottom: 0.5px dashed #8b0000; padding-bottom: 1px; margin-bottom: 1.5px; text-align: center; font-size: 6.2pt;">
                                    กำหนดการสำคัญ (CEREMONIAL SCHEDULE)
                                </div>
                                <div style="font-family: 'Sarabun', sans-serif;">
                                    <div style="margin-bottom: 1.5px;"><strong>เสาร์ 31 ต.ค.</strong>: 16.30 น. สรงน้ำหลวงพ่อพระครูภาวนาอุดมคุณ (79 ปี) &bull; 19.00 น. ทำวัตรเย็น ปฏิบัติภาวนา ฟังธรรม</div>
                                    <div style="border-top: 0.5px dotted #ccc; padding-top: 1.5px;">
                                        <strong>อาทิตย์ 1 พ.ย.</strong>: 07.00 น. ตักบาตร &bull; 08.00 น. ถวายภัตตาหาร &bull; <strong>10.39 น. ถวายผ้ากฐินสามัคคี</strong> &bull; <strong>13.19 น. พิธียกเสาเอกเจดีย์</strong> โดยสมเด็จพระวชิรสิทธาจารย์ (วัดสระเกศ) &amp; มทภ.2
                                    </div>
                                </div>
                            </div>
                            <div style="font-family: 'Courier Prime', monospace; font-size: 4.8pt; color: #666; text-align: right; border-top: 0.5px dotted #ddd; padding-top: 1px; margin-top: 1.5px;">
                                ★ บ้านเกาะแก้ว ต.ปากช่อง อ.ปากช่อง จ.นครราชสีมา ★
                            </div>
                        </div>

                        <!-- PROMPTPAY E-DONATION QR CARD -->
                        <div style="border: 1.5px solid #003b70; background: #fff; padding: 2px; box-shadow: 1px 1px 0 rgba(0,0,0,0.25); text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
                            <div style="background: #003b70; color: #fff; padding: 1px 0; font-family: 'Sarabun', sans-serif; font-size: 5pt; font-weight: bold; letter-spacing: 0.02em; line-height: 1.1;">
                                PromptPay e-Donation
                            </div>
                            <div style="padding: 1px 0;">
                                <img src="issue-03/ads/wat_khao_wanchai_edonation_qr.png" style="width: 24mm; height: 24mm; display: block; margin: 0 auto; border: 0.5px solid #ddd;">
                            </div>
                            <div style="font-family: 'Sarabun', sans-serif; font-size: 4.6pt; line-height: 1.15; color: #111;">
                                <strong>วัดเขาวันชัยนวรัตน์</strong><br>
                                <span style="font-size: 4pt; color: #003b70; font-weight: bold;">สแกนร่วมบุญ • ลดหย่อนภาษีอัตโนมัติ</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- BOTTOM HALF: SEGWIT (LEFT 63%) + PUPPIES & COLOPHON (RIGHT 37%) -->
        <div style="display: grid; grid-template-columns: 120mm 1fr; gap: 8px; align-items: stretch; margin-top: 2px; flex-grow: 1;">
            
            <!-- LEFT: THE SEGREGATED WITNESS COLUMN -->
            <div style="border: 1.5px solid #000; padding: 4.5px 7px; background: #fff; box-shadow: 2px 2px 0px #000; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <!-- KICKER & HEADLINE -->
                    <div style="border-bottom: 1px solid #000; padding-bottom: 2px; margin-bottom: 3px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-family: 'Courier Prime', monospace; font-size: 6.4pt; font-weight: bold; text-transform: uppercase; color: #8b0000; letter-spacing: 0.08em;">
                                ■ THE SEGREGATED WITNESS • BY DON SAMBANDARAKSA
                            </span>
                            <span style="font-family: 'Courier Prime', monospace; font-size: 5.8pt; color: #555;">
                                MEMOIRS OF POST DATABASE • SEPT 2010
                            </span>
                        </div>
                        <h2 class="font-headline" style="font-size: 1.18rem; font-weight: 900; line-height: 1.05; margin: 1.5px 0 1px 0;">
                            EIGHTEEN PER CENT AND PROUD OF IT
                        </h2>
                        <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 6.8pt; line-height: 1.15; color: #333;">
                            How a delivery of frozen sausages revived a sixteen-year-old epiphany in Chiang Mai on the true price of capital, the cruelty of interest rate caps, and the moral hazard of the nanny state.
                        </div>
                    </div>

                    <!-- HERO WOODCUT (MOTORCYCLE & IBM MAINFRAME) -->
                    <div style="border: 1.5px solid #000; padding: 2px; background: #faf8f5; margin-bottom: 3.5px; box-shadow: 1px 1px 0 #000;">
                        <img src="issue-03/ads/motorcycle_18percent_woodcut.jpg" style="width: 100%; height: auto; display: block; border: 0.5px solid #000;">
                        <div style="font-family: 'Playfair Display', serif; font-size: 6.5pt; line-height: 1.2; font-style: italic; color: #333; padding: 2.5px 4px 1px 4px; text-align: center; border-top: 0.5px solid #ccc; margin-top: 2px;">
                            <strong>Plate 4: The 18% Northern Sovereign Rider.</strong> A modest motorcycle transforms an informal labourer into an independent enterprise. In the clouds above: the towering silhouette of an IBM P-Series database server.
                        </div>
                    </div>

                    <!-- 2 BALANCED TEXT COLUMNS (507 WORDS) VIA CSS COLUMNS -->
                    <div style="column-count: 2; column-gap: 8px; column-rule: 0.5px solid #ccc; font-size: 7.2pt; line-height: 1.22; text-align: justify; color: #111;">
                        <p class="drop-cap" style="margin-bottom: 3pt;">
                            This morning, an express van pulled up to my gate to deliver a parcel of frozen sausages dispatched from Ratchaburi. Emblazoned across the vehicle was the livery of NIM Express. It is a peculiar facet of human memory that an ordinary parcel of breakfast meat can instantly dislodge an encounter buried sixteen years in the past.
                        </p>
                        <p style="text-indent: 5pt; margin-bottom: 3pt;">
                            In September 2010, I was covering technology for the <em>Post Database</em> at the <em>Bangkok Post</em>. IBM had ferried a contingent of tech journalists to Chiang Mai for what polite society terms a “geo-expansion showcase”—what the rest of us recognized as a corporate fluff junket. Big Blue was strutting its northern conquests: 70 terabytes of medical storage for Chiang Mai University, modular containerised data centres, and Lotus Live suites.
                        </p>
                        <p style="text-indent: 5pt; margin-bottom: 3pt;">
                            Tucked into the briefing pack as a star regional showcase was Nim See Seng Leasing. They commanded 233 branches across eight northern provinces, powered by centralised IBM P-Series servers and DB2 databases. Their core business? Providing vehicle and motorcycle loans to low-income, informal-sector borrowers who could never dream of securing an audience with a commercial bank.
                        </p>
                        <p style="text-indent: 5pt; margin-bottom: 3pt;">
                            The executives presented their metrics with straight faces and unmistakable corporate pride: Nim, they beamed, was performing an uplifting social service by lending at “only” 18 per cent annual interest.
                        </p>
                        <p style="text-indent: 5pt; margin-bottom: 3pt;">
                            Eighteen per cent! Sitting in that air-conditioned ballroom as a comfortable urban scribe, my jaw hit the parquet. Eighteen per cent interest, and they called it cheap? Was this not textbook usurious predation—capitalist financiers extracting blood from the poorest labourers on two wheels?
                        </p>
                        <p style="text-indent: 5pt; margin-bottom: 3pt;">
                            Then I checked my reporting notes from the provincial streets. The prevailing uncollateralised street rate charged by village loan sharks across the north was 25 per cent. Often higher. Often compounded monthly, and collected under the implicit threat of a lead pipe.
                        </p>
                        <p style="text-indent: 5pt; margin-bottom: 3pt;">
                            Now that I am sixteen years older—and, one hopes, a fraction wiser—I find myself returning often to that Chiang Mai epiphany. High interest rates are not inherently an evil conspiracy of elites feasting upon the destitute. Rather, interest is the honest, unvarnished market price of risk.
                        </p>
                        <p style="text-indent: 5pt; margin-bottom: 3pt;">
                            What is “fair”? What is “access”? If righteous paternalists in parliament pass an edict capping interest rates out of ostensible compassion, what actually happens? The laws of risk do not bow to ministerial decrees. Two things inevitably follow: either the man at the bottom of the pyramid is denied the motorcycle that allows him to commute and earn his livelihood; or he is driven straight back into the shadows of the loan shark at 25, 30, or 50 per cent.
                        </p>
                        <p style="text-indent: 5pt;">
                            In pretending that high-risk capital should be artificially cheap, the state does not protect the vulnerable; it subsidises moral hazard, breeds a sub-class dependent on perpetual debt moratoria and bailouts, and outlaws the bottom rungs of the formal credit ladder. The market price of risk is uncomfortable. The state’s compassionate illusion is ruinous.
                        </p>
                    </div>
                </div>

                <div style="font-family: 'Courier Prime', monospace; font-size: 5.5pt; text-align: right; color: #666; margin-top: 1.5px; border-top: 0.5px solid #ccc; padding-top: 1px;">
                    ★ THE SEGREGATED WITNESS APPEARS EXCLUSIVELY IN THE CITADEL CHRONICLE ★
                </div>
            </div>

            <!-- RIGHT: PUPPIES (TOP) + CITADEL COFFEE (MIDDLE) + COLOPHON (BOTTOM) -->
            <div style="display: flex; flex-direction: column; justify-content: space-between;">
                
                <!-- NINE PUPPIES AD -->
                <div style="border: 1.5px solid #000; padding: 3px 5px; background: #fffcf5; box-shadow: 1.5px 1.5px 0px #000; margin-bottom: 2.5px;">
                    <div style="display: flex; justify-content: space-between; border-bottom: 0.5px solid #000; padding-bottom: 1px; margin-bottom: 1.5px;">
                        <span style="font-family: 'Courier Prime', monospace; font-size: 5.6pt; font-weight: bold; text-transform: uppercase; color: #8b0000;">
                            ★ ADOPT A FAMILIAR ★
                        </span>
                        <span style="font-family: 'Courier Prime', monospace; font-size: 5.6pt; font-weight: bold;">
                            FREE (0 SATS)
                        </span>
                    </div>

                    <div class="font-headline" style="font-size: 0.88rem; font-weight: 900; line-height: 1.05; text-align: center; margin: 1px 0;">
                        THE NINE FAMILIARS
                    </div>

                    <div style="border: 0.5px solid #000; padding: 1px; background: #fff; margin: 1.5px 0; text-align: center;">
                        <img src="issue-03/ads/wizarding_puppies.jpg" style="width: 100%; height: auto; max-height: 25mm; object-fit: cover; display: block;">
                    </div>

                    <p style="font-size: 5.8pt; line-height: 1.16; text-align: justify; margin: 1.5px 0;">
                        Every wizard needs a loyal familiar. Bred in our Pathum Thani redoubt, these nine canine companions are house-broken, impervious to basilisk stares, and trained to bark vigorously at tax collectors.
                    </p>

                    <div style="border-top: 0.5px solid #000; padding-top: 1px; font-family: 'Courier Prime', monospace; font-size: 5.2pt; font-weight: bold; text-align: center; color: #8b0000;">
                        ENQUIRE: @DON VIA NOSTR OR DESK
                    </div>
                </div>

                <!-- CITADEL COFFEE DISPLAY AD -->
                <div style="border: 1.5px solid #000; padding: 3px 5px; background: #fffcf5; box-shadow: 1.5px 1.5px 0px #000; margin-bottom: 2.5px;">
                    <div style="display: flex; justify-content: space-between; border-bottom: 0.5px solid #000; padding-bottom: 1px; margin-bottom: 1.5px;">
                        <span style="font-family: 'Courier Prime', monospace; font-size: 5.6pt; font-weight: bold; text-transform: uppercase; color: #8b0000;">
                            ★ CITADEL COFFEE ROASTERS ★
                        </span>
                        <span style="font-family: 'Courier Prime', monospace; font-size: 5.6pt; font-weight: bold;">
                            PATHUM THANI
                        </span>
                    </div>

                    <div class="font-headline" style="font-size: 0.88rem; font-weight: 900; line-height: 1.05; text-align: center; margin: 1px 0;">
                        SIGNATURE PICCOLO LATTE
                    </div>

                    <div style="border: 0.5px solid #000; padding: 1px; background: #fff; margin: 1.5px 0;">
                        <img src="issue-03/ads/citadel_coffee_piccolo.png" style="width: 100%; height: auto; max-height: 76mm; object-fit: contain; display: block;">
                    </div>

                    <p style="font-size: 5.8pt; line-height: 1.16; text-align: justify; margin: 1.5px 0;">
                        <strong>Piccolo Latte (90.-)</strong> &bull; Double ristretto cut with velvety milk at 1:2 consensus ratio. Low latency, zero dilution, pure proof-of-work caffeine.
                    </p>

                    <div style="border-top: 0.5px solid #000; padding-top: 1px; font-family: 'Courier Prime', monospace; font-size: 5.2pt; font-weight: bold; text-align: center; color: #333;">
                        ⚡ 0-CONF LIGHTNING SETTLED &bull; ZERO CUSTODIAL DEBT
                    </div>
                </div>

                <!-- COLOPHON WITH FULL NPUB & QR CODE -->
                <div style="border: 1.5px solid #000; padding: 3px 5px; background: #faf8f5; font-family: 'Courier Prime', monospace; font-size: 5.6pt; line-height: 1.18; box-shadow: 1.5px 1.5px 0 #000;">
                    <div style="font-weight: bold; border-bottom: 0.5px solid #000; padding-bottom: 1px; margin-bottom: 2px; display: flex; justify-content: space-between;">
                        <span>CITADEL CHRONICLE • COLOPHON</span>
                        <span>ISSUE 03</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 19mm; gap: 5px; align-items: center;">
                        <div>
                            <div>• <strong>EDITOR-IN-CHIEF</strong>: Don Sambandaraksa (@don)</div>
                            <div>• <strong>BLOCK ANCHOR</strong>: 973,528 &bull; 21 sat minSendable</div>
                            <div>• <strong>LIGHTNING</strong>: don@citadelchronicle.com</div>
                            <div style="margin-top: 1px;">
                                <strong>FULL NPUB</strong>:
                                <div style="font-size: 4.4pt; word-break: break-all; line-height: 1.05; color: #111; background: #fff; padding: 1px 2px; border: 0.5px solid #ccc; margin-top: 0.5px;">npub1mwpsruysa2nv0ukv9mzssk8grfp7tdhftvcrs3azu9sfrhnasl7qu5uu3w</div>
                            </div>
                        </div>
                        <div style="border: 0.5px solid #000; padding: 1.5px; background: #fff; text-align: center;">
                            <img src="issue-03/ads/nostr_qr.png" style="width: 16mm; height: 16mm; display: block; margin: 0 auto;">
                            <div style="font-size: 4pt; font-weight: bold; margin-top: 1px; color: #000;">SCAN NOSTR</div>
                        </div>
                    </div>
                    <div style="font-size: 5.2pt; text-align: center; border-top: 0.5px solid #000; padding-top: 1px; margin-top: 2px; font-style: italic;">
                        “ALL THE RANTS THAT FIT ON FOUR SHEETS”
                    </div>
                </div>

            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="footer-line">
        <div>PAGE 4 OF 4 • KATHINA KHAO WANCHAI, THE SEGREGATED WITNESS &amp; FAMILIARS • EPISODE 03</div>
        <div>THE CITADEL CHRONICLE • CITADELCHRONICLE.COM • ESTABLISHED 2026</div>
    </footer>
</div>
"""

# =========================================================================
# UNIFIED HTML DOCUMENT
# =========================================================================
FULL_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THE CITADEL CHRONICLE — Episode 03 (Complete 4-Page Broadsheet)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=EB+Garamond:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600&family=Playfair+Display:ital,wght@0,700;0,900;1,400;1,700&family=Pridi:wght@400;600;700&family=Sarabun:ital,wght@0,400;0,600;0,700;1,400&family=UnifrakturMaguntia&display=swap" rel="stylesheet">
    <style>
{BASE_CSS}
        @page {{
            size: A4 portrait;
            margin: 0;
        }}
        @media print {{
            body {{
                background: #ffffff;
            }}
            .a4-sheet-inner {{
                page-break-after: always;
                break-after: page;
            }}
            .a4-sheet-inner:last-child {{
                page-break-after: avoid;
                break-after: avoid;
            }}
        }}
        @media screen {{
            body {{
                background: #23211e;
                padding: 20px 10px;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 25px;
            }}
            .a4-sheet-inner {{
                box-shadow: 0 15px 35px rgba(0,0,0,0.6);
            }}
        }}
    </style>
</head>
<body>
{PAGE_1_HTML}
{PAGE_2_HTML}
{PAGE_3_HTML}
{PAGE_4_HTML}
</body>
</html>
"""

# Save unified HTML file
out_html = os.path.join(WORKING_DIR, "issue-03.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(FULL_HTML)
print(f"Saved {out_html}")

# Generate 4-page PDF via Chrome Headless
pdf_path = os.path.join(WORKING_DIR, "citadel_chronicle_issue03.pdf")
cmd_pdf = [
    "google-chrome",
    "--headless",
    "--no-sandbox",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=8000",
    f"--print-to-pdf={pdf_path}",
    "--no-pdf-header-footer",
    f"file://{out_html}"
]
subprocess.run(cmd_pdf, check=True)
print(f"Rendered {pdf_path}")

# Generate 600 DPI Master Images for each of the 4 pages
img_prefix_600 = os.path.join(WORKING_DIR, "citadel_chronicle_issue03_p")
subprocess.run([
    "pdftoppm", "-r", "600", "-jpeg", "-jpegopt", "quality=96",
    pdf_path, img_prefix_600
], check=True)

# Generate Social Media images for all 4 pages
target_w = 1600
for i in range(1, 5):
    page_img_600 = f"{img_prefix_600}-{i}.jpg"
    page_dst_600 = os.path.join(WORKING_DIR, f"citadel_chronicle_issue03_page{i}_600dpi.jpg")
    page_dst_social = os.path.join(WORKING_DIR, f"citadel_chronicle_issue03_page{i}_social.jpg")
    
    if os.path.exists(page_img_600):
        os.rename(page_img_600, page_dst_600)
        print(f"Saved {page_dst_600}")
        
        im = Image.open(page_dst_600)
        target_h = int(target_w * im.size[1] / im.size[0])
        social_im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        social_im.save(page_dst_social, quality=92)
        print(f"Saved {page_dst_social} ({target_w}x{target_h})")

# Generate A3 Duplex 600 DPI Print Spreads
p1 = Image.open(os.path.join(WORKING_DIR, "citadel_chronicle_issue03_page1_600dpi.jpg"))
p2 = Image.open(os.path.join(WORKING_DIR, "citadel_chronicle_issue03_page2_600dpi.jpg"))
p3 = Image.open(os.path.join(WORKING_DIR, "citadel_chronicle_issue03_page3_600dpi.jpg"))
p4 = Image.open(os.path.join(WORKING_DIR, "citadel_chronicle_issue03_page4_600dpi.jpg"))
w, h = p1.size

# Sheet 1: Outside (Page 4 Left, Page 1 Right)
sheet1 = Image.new("RGB", (w * 2, h), (255, 255, 255))
sheet1.paste(p4, (0, 0))
sheet1.paste(p1, (w, 0))
s1_path = os.path.join(WORKING_DIR, "citadel_chronicle_issue03_a3_sheet1_outside_p4_p1_600dpi.jpg")
sheet1.save(s1_path, quality=95)
print(f"Saved A3 Sheet 1 (Outside): {sheet1.size}")

# Sheet 2: Inside (Page 2 Left, Page 3 Right)
sheet2 = Image.new("RGB", (w * 2, h), (255, 255, 255))
sheet2.paste(p2, (0, 0))
sheet2.paste(p3, (w, 0))
s2_path = os.path.join(WORKING_DIR, "citadel_chronicle_issue03_a3_sheet2_inside_p2_p3_600dpi.jpg")
sheet2.save(s2_path, quality=95)
print(f"Saved A3 Sheet 2 (Inside): {sheet2.size}")

# Copy all outputs to Downloads
output_files = [
    "issue-03.html",
    "citadel_chronicle_issue03.pdf",
    "citadel_chronicle_issue03_page1_600dpi.jpg",
    "citadel_chronicle_issue03_page2_600dpi.jpg",
    "citadel_chronicle_issue03_page3_600dpi.jpg",
    "citadel_chronicle_issue03_page4_600dpi.jpg",
    "citadel_chronicle_issue03_a3_sheet1_outside_p4_p1_600dpi.jpg",
    "citadel_chronicle_issue03_a3_sheet2_inside_p2_p3_600dpi.jpg",
    "citadel_chronicle_issue03_page1_social.jpg",
    "citadel_chronicle_issue03_page2_social.jpg",
    "citadel_chronicle_issue03_page3_social.jpg",
    "citadel_chronicle_issue03_page4_social.jpg"
]
for f in output_files:
    p = os.path.join(WORKING_DIR, f)
    if os.path.exists(p):
        shutil.copy2(p, os.path.join(DOWNLOADS_DIR, f))

# Also mirror key outputs to blockcandchain
for f in ["issue-03.html", "citadel_chronicle_issue03.pdf", "citadel_chronicle_issue03_page1_social.jpg", "citadel_chronicle_issue03_page4_social.jpg"]:
    p = os.path.join(WORKING_DIR, f)
    if os.path.exists(p):
        shutil.copy2(p, os.path.join(BLOCKCANDCHAIN_DIR, f))

print("Episode 3 Complete 4-Page Broadsheet Build Finished!")
