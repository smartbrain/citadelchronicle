#!/usr/bin/env python3
# ==============================================================================
# THE CITADEL CHRONICLE — EPISODE 03
# SCRIBUS 1.7.x / 1.7.3 MASTER GENERATOR SCRIPT
# Generates native .sla XML document with multi-column text, frames, and images
# ==============================================================================
import os
import shutil
import scribus

WORKING_DIR = "/home/don/citadelchronicle"
DOWNLOADS_DIR = "/home/don/Downloads"
OUT_SLA = os.path.join(WORKING_DIR, "citadel_chronicle_issue03.sla")
OUT_SLA_DL = os.path.join(DOWNLOADS_DIR, "citadel_chronicle_issue03.sla")
OUT_PDF_TEST = os.path.join(DOWNLOADS_DIR, "citadel_chronicle_issue03_from_scribus.pdf")

# 1. Initialize Document: 4 Pages, A4 Portrait, 7mm Margins, Millimeters
# scribus.newDocument(size, margins, orientation, firstPageNumber, unit, pagesType, firstPageOrder, numPages)
scribus.newDocument(
    scribus.PAPER_A4_MM,
    (7, 7, 7, 7),  # Left, Right, Top, Bottom margins in mm
    scribus.PORTRAIT,
    1,
    scribus.UNIT_MILLIMETERS,
    scribus.PAGE_1,
    0,
    4
)

# 2. Define Custom Palettes
scribus.defineColorRGB("CitadelCrimson", 139, 0, 0)      # #8b0000
scribus.defineColorRGB("InkAccent", 139, 0, 0)           # #8b0000
scribus.defineColorRGB("PaperWarm", 250, 248, 245)       # #faf8f5
scribus.defineColorRGB("GreyRule", 204, 204, 204)        # #cccccc
scribus.defineColorRGB("GreyBorder", 180, 180, 180)      # #b4b4b4
scribus.defineColorRGB("NavyBlue", 0, 59, 112)           # #003b70
scribus.defineColorRGB("CreamYellow", 255, 252, 245)     # #fffcf5
scribus.defineColorRGB("DarkGrey", 68, 68, 68)           # #444444

# Typography Constants
FONT_SERIF_BOLD = "Liberation Serif Bold"
FONT_SERIF_REG = "Liberation Serif Regular"
FONT_SERIF_ITAL = "Liberation Serif Italic"
FONT_MONO_BOLD = "Liberation Mono Bold"
FONT_MONO_REG = "Liberation Mono Regular"
FONT_SANS_BOLD = "Liberation Sans Bold"
FONT_SANS_REG = "Liberation Sans Regular"
FONT_THAI_BOLD = "Noto Serif Thai Bold"
FONT_THAI_REG = "Noto Serif Thai Regular"
FONT_THAI_SANS = "Noto Sans Thai Regular"

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================
def draw_rule(x1, y1, x2, y2, color="Black", width=0.5):
    line = scribus.createLine(x1, y1, x2, y2)
    scribus.setLineColor(color, line)
    scribus.setLineWidth(width, line)
    return line

def draw_box(x, y, w, h, fill="White", stroke="Black", line_width=1):
    rect = scribus.createRect(x, y, w, h)
    scribus.setFillColor(fill, rect)
    scribus.setLineColor(stroke, rect)
    scribus.setLineWidth(line_width, rect)
    return rect

def add_image_box(x, y, w, h, img_path, stroke="Black", line_width=0.5):
    # Container box
    if stroke:
        draw_box(x, y, w, h, fill="White", stroke=stroke, line_width=line_width)
    img = scribus.createImage(x + 0.5, y + 0.5, w - 1.0, h - 1.0)
    if os.path.exists(img_path):
        scribus.loadImage(img_path, img)
        scribus.setScaleImageToFrame(True, True, img)
    return img

def add_header(page_num, title, block_height="973,528", date="WEDNESDAY, 28 OCTOBER 2026"):
    draw_rule(7, 12, 203, 12, "Black", 1.2)
    t = scribus.createText(7, 7, 196, 4.5)
    scribus.setText(f"THE CITADEL CHRONICLE • {date} • BLOCK HEIGHT: {block_height}    |    {title}    |    PAGE {page_num} OF 4", t)
    scribus.setFont(FONT_MONO_BOLD, t)
    scribus.setFontSize(6.5, t)
    scribus.setTextColor("Black", t)
    scribus.setTextAlignment(scribus.ALIGN_CENTERED, t)

def add_footer(page_num, summary):
    draw_rule(7, 285.5, 203, 285.5, "Black", 1.0)
    t = scribus.createText(7, 286, 196, 4.5)
    scribus.setText(f"PAGE {page_num} OF 4 • {summary} • THE CITADEL CHRONICLE • CITADELCHRONICLE.COM • ESTABLISHED 2026", t)
    scribus.setFont(FONT_MONO_REG, t)
    scribus.setFontSize(6.2, t)
    scribus.setTextColor("Black", t)
    scribus.setTextAlignment(scribus.ALIGN_CENTERED, t)


# ==============================================================================
# PAGE 1: FRONT COVER (VOLDEMORT, TILAPIA, SUN GODLING, HERO WOODCUT)
# ==============================================================================
scribus.gotoPage(1)

# Left Ear Box
draw_box(7, 7, 36, 18, fill="PaperWarm", stroke="Black", line_width=0.8)
t_ear_l = scribus.createText(8, 8, 34, 16)
scribus.setText("MINISTRY ALERT\n• CP-KRA-PAO: Threat Level High\n• HOLY BASIL: Kaew Juree 01-04\n• HOME CHEWING: Permitted\n• STREET SALE: Azkaban Felony\n• SUN GODLING: Benevolent\n[Microwave Fortified]", t_ear_l)
scribus.setFont(FONT_MONO_REG, t_ear_l)
scribus.setFontSize(5.0, t_ear_l)

# Masthead Center
t_mast = scribus.createText(45, 6, 120, 19)
scribus.setText("THE CITADEL CHRONICLE", t_mast)
scribus.setFont(FONT_SERIF_BOLD, t_mast)
scribus.setFontSize(21.5, t_mast)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_mast)

# Right Ear Box
draw_box(167, 7, 36, 18, fill="PaperWarm", stroke="Black", line_width=0.8)
t_ear_r = scribus.createText(168, 8, 34, 16)
scribus.setText("SOLAR DECREES\n• PATENTS: 4 Basil Clones Granted\n• ENFORCEMENT: Dementor Raids\n• ROAST PORK: Subsidised\n• STREET VENDORS: Condemned\n• SOVEREIGN SEEDS: Confiscated\n[Zero Legal Recourse]", t_ear_r)
scribus.setFont(FONT_MONO_REG, t_ear_r)
scribus.setFontSize(5.0, t_ear_r)

# Dateline Bar
draw_rule(7, 26.5, 203, 26.5, "Black", 1.2)
t_date = scribus.createText(7, 27.2, 196, 4.5)
scribus.setText("VOL. XXI • ISSUE NO. 03 • BLOCK HEIGHT: 973,528 • WEDNESDAY, 28 OCTOBER 2026 • 1 SAT/vB • BANGKOK // PATHUM THANI", t_date)
scribus.setFont(FONT_MONO_BOLD, t_date)
scribus.setFontSize(6.8, t_date)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_date)
draw_rule(7, 32.5, 203, 32.5, "Black", 1.2)

# Lead Headline & Deck
t_kicker1 = scribus.createText(7, 33.5, 196, 4.5)
scribus.setText("■ MINISTRY OF MAGIC & SOLAR DECREES • AQUATIC & HERBAL HERESY", t_kicker1)
scribus.setFont(FONT_MONO_BOLD, t_kicker1)
scribus.setFontSize(7.0, t_kicker1)
scribus.setTextColor("CitadelCrimson", t_kicker1)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_kicker1)

t_head1 = scribus.createText(7, 38, 196, 12)
scribus.setText("“HE-WHO-MUST-NOT-BE-NAMED” BLAMED FOR UNLEASHING BLACKCHIN TILAPIA TO RUIN NATION’S PAD KRA PAO", t_head1)
scribus.setFont(FONT_SERIF_BOLD, t_head1)
scribus.setFontSize(12.8, t_head1)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_head1)

t_sub1 = scribus.createText(7, 50.5, 196, 4.5)
scribus.setText("“DEFINITELY NOT A LOCAL MEGACORP,” SAY TERRIFIED OFFICIALS", t_sub1)
scribus.setFont(FONT_MONO_BOLD, t_sub1)
scribus.setFontSize(7.8, t_sub1)
scribus.setTextColor("CitadelCrimson", t_sub1)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_sub1)

t_deck1 = scribus.createText(12, 55, 186, 7.5)
scribus.setText("Ministry of Magic announces Lord Voldemort is solely responsible for invasive fish destroying rivers, while The Sun Godling grants citizens royal permission to chew four patented strains of Holy Basil—so long as nobody attempts to sell it.", t_deck1)
scribus.setFont(FONT_SERIF_ITAL, t_deck1)
scribus.setFontSize(7.5, t_deck1)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_deck1)
draw_rule(7, 63.5, 203, 63.5, "Black", 0.6)

# Upper Spread: Woodcut Cartoon (Left) + Intro (Right)
add_image_box(7, 65, 120, 80, os.path.join(WORKING_DIR, "issue-03/ads/blackchin_voldemort_woodcut.jpg"))

t_intro1 = scribus.createText(130, 65, 73, 80)
scribus.setText(
    "In an extraordinary joint emergency session of the Wizengamot and the Department of Fisheries yesterday, senior mandarins officially attributed the catastrophic ecological devastation of Thailand’s waterways to the dark wizard Lord Voldemort.\n\n"
    "“We have completed an exhaustive forensic audit across fourteen river basins,” announced Deputy Undersecretary for Auror Affairs, Phra Mahakasem, adjusting his enchanted spectacles.\n\n"
    "“The evidence is incontrovertible. This ferocious fish—capable of consuming indigenous shrimp nurseries, out-breeding local catfish, and resisting boiling water—was summoned via an ancient Parseltongue transfiguration curse uttered by He-Who-Must-Not-Be-Named.”\n\n"
    "When challenged by journalists as to whether the biological catastrophe had anything to do with a certain agricultural conglomerate whose name rhymes with 'Chaloen Pokphand', the Deputy Undersecretary blanched visibly.",
    t_intro1
)
scribus.setFont(FONT_SERIF_REG, t_intro1)
scribus.setFontSize(7.0, t_intro1)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_intro1)

draw_rule(7, 147, 203, 147, "Black", 0.5)

# Lower Spread: 3 Columns News Report
t_body1 = scribus.createText(7, 149, 196, 134)
scribus.setColumns(3, t_body1)
scribus.setColumnGap(6, t_body1)
scribus.setText(
    "“Outrageous slander!” shrieked the Undersecretary, clutching a protective amulet. “To even insinuate that our nation’s most benevolent, state-subsidised solar poultry monopoly could be culpable is treason against the harvest! Lord Voldemort sneaked into Samut Songkhram under an Invisibility Cloak, dumped two plastic tubs of African fingerlings into the canal, and fled on a broomstick.”\n\n"
    "Meanwhile, fifty leagues upcountry, the Sun Godling was holding court at the Solar Temple of Retail Convenience. Standing before a glowing neon altar of microwaveable pork steaks, His Radiance unveiled four new patented cultivars of holy basil: Kaew Juree 01 through 04.\n\n"
    "“Rejoice, peasants!” proclaimed the High Solar Priest. “By divine grace of intellectual property decree, all subjects are granted royal indulgence to chew the sacred leaves within the privacy of their hovels. However, should any insolent street vendor crush a single leaf of Kaew Juree upon a wok without an enterprise barcode license, thirty Dementors will instantly descend upon their food cart to impound their fish sauce.”\n\n"
    "Street hawkers across Bang Rak and Yaowarat expressed profound bewilderment. “First the Blackchin Tilapia ate all the native river prawns,” lamented Somchai, a third-generation street cook. “Now, if I stir-fry basil with pork, CP police demand to inspect the stomatal genetic sequence of my herbs. If I buy wild basil from Nakhon Pathom, the health inspector claims it carries dark magic. If I buy CP basil, my profit margin is minus twenty-two per cent.”\n\n"
    "Economic arithmancers noted that the twin crises have converged into a singular commercial monopoly. With local fisheries wiped out, the only protein left for the national dish is factory-farmed solar chicken and reconstituted tilapia nuggets, available exclusively in vacuum-sealed plastic pouches.\n\n"
    "“The cycle is mathematically complete,” chuckled a veteran sovereign observer in Pathum Thani. “Destroy the commons with invasive monsters, outlaw natural seeds under patent monopolies, blame a fictional sorcerer, and force the populace to eat microwaved lunch boxes. Truly, the dark arts have never been so profitable.”",
    t_body1
)
scribus.setFont(FONT_SERIF_REG, t_body1)
scribus.setFontSize(6.8, t_body1)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_body1)

add_footer(1, "SPECIAL EDITION: THE BLACKCHIN CONSPIRACY")


# ==============================================================================
# PAGE 2: THE ARITHMANCY OF THE FOURTEEN-DAY HERETIC
# ==============================================================================
scribus.gotoPage(2)
add_header(2, "Analytical Dispatch: St. Mungo's Medical Arithmancy")

# Headline Block
t_kicker2 = scribus.createText(7, 14, 196, 4.5)
scribus.setText("■ ARITHMANCY & PUBLIC HEALING • THE 14-DAY COHORT EXCLUSION BIAS", t_kicker2)
scribus.setFont(FONT_MONO_BOLD, t_kicker2)
scribus.setFontSize(7.0, t_kicker2)
scribus.setTextColor("CitadelCrimson", t_kicker2)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_kicker2)

t_head2 = scribus.createText(7, 18.5, 196, 11)
scribus.setText("THE ARITHMANCY OF THE FOURTEEN-DAY HERETIC", t_head2)
scribus.setFont(FONT_SERIF_BOLD, t_head2)
scribus.setFontSize(15, t_head2)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_head2)

t_sub2 = scribus.createText(7, 30, 196, 5)
scribus.setText("HOW ST. MUNGO’S STATISTICIANS CONVERTED POST-POTION CASUALTIES INTO “UNVACCINATED” CONTAGIONS", t_sub2)
scribus.setFont(FONT_MONO_BOLD, t_sub2)
scribus.setFontSize(7.5, t_sub2)
scribus.setTextColor("CitadelCrimson", t_sub2)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_sub2)

t_deck2 = scribus.createText(12, 35, 186, 7.5)
scribus.setText("A forensic examination of observational case-counting windows, cohort misclassification, and the immortal time bias that manufactured consensus out of thin air.", t_deck2)
scribus.setFont(FONT_SERIF_ITAL, t_deck2)
scribus.setFontSize(7.5, t_deck2)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_deck2)
draw_rule(7, 43.5, 203, 43.5, "Black", 0.6)

# Upper Spread: Infographic Woodcut (Left) + Intro (Right)
add_image_box(7, 45, 115, 75, os.path.join(WORKING_DIR, "issue-03/ads/fourteen_day_arithmancy_woodcut.jpg"))

t_intro2 = scribus.createText(125, 45, 78, 75)
scribus.setText(
    "To question the clinical trials of the Grand Apothecary was folly; to scrutinise their denominator was heresy. Yet when the history of the Great Contagion of 2021–2024 is written by dispassionate chroniclers, the central artefact of official deception will not be biological, but arithmantical.\n\n"
    "At St. Mungo’s Hospital for Magical Maladies, the records department operated under a decree of sublime administrative sorcery: no citizen receiving an experimental draught was classified as 'inoculated' until precisely fourteen days had elapsed following the second dose.\n\n"
    "To the untrained layman, this appeared a reasonable concession to biological latency—an allowance for antibodies to mature in the bloodstream. To the forensic statistician, however, it constituted a lethal mathematical sleight of hand.",
    t_intro2
)
scribus.setFont(FONT_SERIF_REG, t_intro2)
scribus.setFontSize(7.2, t_intro2)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_intro2)

draw_rule(7, 122, 203, 122, "Black", 0.5)

# Lower Spread: 3 Columns
t_body2 = scribus.createText(7, 124, 196, 159)
scribus.setColumns(3, t_body2)
scribus.setColumnGap(6, t_body2)
scribus.setText(
    "Consider the epidemiological mechanics of the 14-day window. If an individual experienced an acute adverse cardiovascular reaction, pulmonary collapse, or fatal thrombosis on Day 3 following inoculation, where did their casualty record land? Under the Ministry’s statutory definitions, they had not yet attained the holy fourteen-day threshold.\n\n"
    "Consequently, they were categorized and tallied in the hospital ledgers as an 'unvaccinated death.' The very intervention being evaluated was thus mathematically cleansed of its immediate post-administration perils. Worse still, the burden of those early casualties was dumped into the baseline tally of the untreated control cohort!\n\n"
    "This phenomenon, well-known in classical biostatistics as 'immortal time bias' and 'case-counting window manipulation,' created an artificial statistical divergence that guaranteed an appearance of overwhelming efficacy. The newly inoculated cohort was declared immune from counting during its period of highest biological vulnerability, while the non-compliant cohort absorbed every stray malady.\n\n"
    "When independent arithmancers in the Citadel recalculated the raw mortality data using an honest 'intention-to-treat' timeline—counting every soul from the moment the needle entered the flesh—the miraculous divergence vanished into Poisson noise.\n\n"
    "The institutional response was swift and predictable: those who pointed out the denominator trick were branded 'Arithmancy Deniers,' stripped of their clinical wands, and exiled from academic journals. The public health apparatus had invested its entire institutional credibility in the dogma that the potion was safe and effective; to concede that the efficacy metric was an artefact of case-window gerrymandering was an existential impossibility.\n\n"
    "As sovereign citizens reflecting upon this dark era, the lesson transcends pharmacology. Whenever the state or its captured cartels present an authoritative statistical consensus, look not at the numerator of promised salvation; inspect the denominator, check the exclusion windows, and demand to see the unconfirmed raw ledger. Don't trust the apothecary; verify the arithmetic.",
    t_body2
)
scribus.setFont(FONT_SERIF_REG, t_body2)
scribus.setFontSize(6.8, t_body2)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_body2)

add_footer(2, "ST. MUNGO'S ARITHMANCY & OBSERVATIONAL BIAS")


# ==============================================================================
# PAGE 3: THE ELECTRUM RBF HEIST & 0-CONF DISPATCHES
# ==============================================================================
scribus.gotoPage(3)
add_header(3, "Special Investigation: Protocol Forensics & The Architecture of Exploits")

# Main Article Header
t_kicker3 = scribus.createText(7, 14, 196, 4.5)
scribus.setText("■ MEMPOOL FORENSICS • CRITICAL SECURITY DISCLOSURE • GHSA-6JP4-8V48-CC5V", t_kicker3)
scribus.setFont(FONT_MONO_BOLD, t_kicker3)
scribus.setFontSize(7.0, t_kicker3)
scribus.setTextColor("CitadelCrimson", t_kicker3)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_kicker3)

t_head3 = scribus.createText(7, 18.5, 196, 11)
scribus.setText("THE WEAPONISED FEE-BUMP: INSIDE THE ELECTRUM RBF HEIST", t_head3)
scribus.setFont(FONT_SERIF_BOLD, t_head3)
scribus.setFontSize(14.5, t_head3)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_head3)

t_sub3 = scribus.createText(7, 30, 196, 5)
scribus.setText("HOW ROGUE SERVERS EXPLOITED THE SPV MEMPOOL BLINDSPOT TO TRICK BITCOINERS INTO SIGNING OVER THEIR OWN FUNDS", t_sub3)
scribus.setFont(FONT_MONO_BOLD, t_sub3)
scribus.setFontSize(7.2, t_sub3)
scribus.setTextColor("CitadelCrimson", t_sub3)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_sub3)

t_deck3 = scribus.createText(12, 35, 186, 7.5)
scribus.setText("A forensic examination of the high-severity vulnerability patched in Electrum v4.8.3, where adversaries bypassed private-key cryptography by turning the client's Replace-By-Fee routine into an involuntary double-spend guillotine.", t_deck3)
scribus.setFont(FONT_SERIF_ITAL, t_deck3)
scribus.setFontSize(7.5, t_deck3)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_deck3)
draw_rule(7, 43.5, 203, 43.5, "Black", 0.6)

# Main 2 Columns (Y: 45 to 226mm)
# Col 1: Intro + SPV Blindspot + Phase 1 & 2
t_p3_col1 = scribus.createText(7, 45, 94, 178)
scribus.setText(
    "On 24 October 2026, the maintainers of the Electrum Bitcoin wallet published a security advisory tracked as GHSA-6jp4-8v48-cc5v and rushed out version 4.8.3. The vulnerability had not merely been discovered in an academic laboratory; it had been actively and ruthlessly exploited in the wild against users operating on public Electrum servers.\n\n"
    "What makes this exploit one of the most intellectually diabolical vectors in Bitcoin client history is that the adversary never broke secp256k1 elliptic curve cryptography, nor did they exfiltrate seed phrases or compromise operating systems. Instead, they weaponised the client’s architectural trust boundary and the user’s own muscle memory, tricking victims into voluntarily authorising and signing the theft of their own coins.\n\n"
    "THE SPV MEMPOOL BLINDSPOT\n\n"
    "To understand how the heist operates, one must examine the delicate compromise that makes lightweight Bitcoin wallets possible. In Satoshi Nakamoto’s original design, Simplified Payment Verification (SPV) relies upon 80-byte block headers. When an SPV client receives a confirmed transaction, it cryptographically verifies a Merkle inclusion proof tying that transaction hash to a header buried under cumulative Proof-of-Work. An untrusted server cannot fabricate a confirmed block without overcoming the hashpower of the global network.\n\n"
    "For unconfirmed transactions floating in the mempool, however, this cryptographic anchor vanishes entirely. In the mempool, there is no Proof-of-Work, no consensus, and no Merkle tree.\n\n"
    "When an Electrum client synchronises with an external server over JSON-RPC, it queries its addresses via blockchain.scripthash.subscribe. If a transaction has a height of zero or negative, the server asserts that it is an unconfirmed payment sitting in the mempool.\n\n"
    "Historically, Electrum’s codebase contained a fateful assumption: if an unconfirmed transaction consumed UTXOs belonging to the local wallet (wallet.is_mine), the wallet assumed it was either created by the local user or broadcast from another valid clone. Crucially, pre-4.8.3 Electrum did not execute the script engine to cryptographically verify signatures on unconfirmed incoming inputs.\n\n"
    "PHASE 1 & 2: INTERCEPTION & SYNTHETIC FORGERY\n\n"
    "The ambush begins when an unsuspecting user broadcasts a legitimate payment (Tx1)—for example, transferring 2.5 BTC to cold storage. The client relays Tx1 to its connected Electrum server via blockchain.transaction.broadcast. If that server is malicious, it silently suppresses Tx1, refusing to gossip it to the broader Bitcoin P2P network.\n\n"
    "The rogue server immediately constructs an alternative transaction (Tx_fake). It consumes the exact same UTXOs as Tx1, but redirects the output entirely to an address controlled by the attacker. Because the attacker possesses no private keys, Tx_fake contains invalid dummy signatures. Attackers deployed GPU vanity tools so the final four to six characters matched the victim’s intended address, set a fee of 1 sat/vB with BIP 125 opt-in RBF, and fed Tx_fake back to the wallet. Because Electrum skipped signature checks, the fake transaction appeared in the GUI as a pending payment.",
    t_p3_col1
)
scribus.setFont(FONT_SERIF_REG, t_p3_col1)
scribus.setFontSize(6.7, t_p3_col1)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_p3_col1)

# Col 2: Phase 3 & 4 + Anatomy Box + Remediation + Lessons Box
t_p3_col2_top = scribus.createText(107, 45, 96, 52)
scribus.setText(
    "PHASE 3 & 4: THE RBF TRAP AND FATAL RATIFICATION\n\n"
    "Because Tx_fake contained invalid signatures, no honest miner would ever include it in a block. To the user, the transaction appeared hopelessly stalled in the mempool.\n\n"
    "The natural reaction in Bitcoin UX when a transaction is stuck is to right-click and select “Increase Fee” (Replace-By-Fee). When the user initiated the fee bump, Electrum loaded Tx_fake from its internal history as the base transaction template. The UI displayed a dialogue asking for a higher fee rate.\n\n"
    "Human psychology and standard hardware wallet UX conspired to seal the trap. When performing an RBF bump, users invariably check only the fee delta (e.g. bumping from 1 sat/vB to 35 sat/vB), assuming the recipient address is immutable from their initial creation.\n\n"
    "The victim typed their passphrase or approved the prompt on their Ledger, Trezor, or Coldcard. In doing so, the wallet generated pristine, mathematically valid ECDSA or Schnorr signatures over the attacker’s outputs. The resulting transaction was immediately relayed, accepted by Bitcoin Core mempools across the globe, and permanently mined into the ledger. The theft was absolute.",
    t_p3_col2_top
)
scribus.setFont(FONT_SERIF_REG, t_p3_col2_top)
scribus.setFontSize(6.7, t_p3_col2_top)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_p3_col2_top)

# Anatomy Box
draw_box(107, 98, 96, 38, fill="CreamYellow", stroke="CitadelCrimson", line_width=1.0)
t_anat = scribus.createText(108, 99, 94, 36)
scribus.setText(
    "▲ THE ANATOMY OF THE RBF TRAP (GHSA-6jp4-8v48-cc5v) ▲\n"
    "1. VICTIM broadcasts Tx1 (Valid recipient, fully signed).\n"
    "2. ROGUE SERVER withholds Tx1 from P2P gossip network.\n"
    "3. SERVER INJECTS Tx_fake (Same UTXO, vanity attacker output, BOGUS signatures).\n"
    "4. CLIENT ACCEPTS Tx_fake into GUI (Skipped unconfirmed sig check!).\n"
    "5. TX STALLS: Victim right-clicks 'Increase Fee' (RBF).\n"
    "6. FATAL RATIFICATION: Victim signs fee bump • Wallet generates real, valid signatures over the attacker's output!\n"
    "7. THEFT COMPLETE: Valid Tx_stolen mined on chain.",
    t_anat
)
scribus.setFont(FONT_MONO_REG, t_anat)
scribus.setFontSize(5.2, t_anat)

# Remediation text
t_p3_col2_mid = scribus.createText(107, 138, 96, 32)
scribus.setText(
    "THE REMEDIATION: COMMIT 90fe308\n\n"
    "Lead maintainer SomberNight resolved the flaw in commit 90fe308 by dismantling the assumption of mempool innocence. Electrum v4.8.3 now enforces strict client-side signature verification: before any unconfirmed transaction touching wallet.is_mine UTXOs is accepted into the wallet database, the client validates that the input signatures mathematically correspond to the scriptPubKey. Any forged or invalid server injection is rejected outright and never reaches the GUI.",
    t_p3_col2_mid
)
scribus.setFont(FONT_SERIF_REG, t_p3_col2_mid)
scribus.setFontSize(6.7, t_p3_col2_mid)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_p3_col2_mid)

# Lessons Box
draw_box(107, 172, 96, 50, fill="PaperWarm", stroke="Black", line_width=1.0)
t_less = scribus.createText(108, 173, 94, 48)
scribus.setText(
    "■ LESSONS FOR THE CITADEL SANCTUARY    |    SOVEREIGN MANDATE\n\n"
    "• UPGRADE MANDATORY: All users operating Electrum must update to version 4.8.3 or higher. Verify PGP signatures directly from electrum.org.\n"
    "• INSPECT FULL OUTPUTS: Whenever executing an RBF fee bump, verify the entire recipient address on your hardware signer screen, not merely the fee rate.\n"
    "• RUN A SOVEREIGN SERVER: Users who connected to their own private Fulcrum, Electrs, or EPS nodes backed by Bitcoin Core were completely immune. Public servers are third-party trust traps. Don't trust, verify.",
    t_less
)
scribus.setFont(FONT_MONO_REG, t_less)
scribus.setFontSize(5.5, t_less)

# Basement 0-Conf Dispatches
draw_rule(7, 226, 203, 226, "Black", 1.2)
t_base_hdr = scribus.createText(7, 227, 196, 4)
scribus.setText("■ 0-CONF DISPATCHES • UNCONFIRMED MEMPOOL INTELLIGENCE & JURISPRUDENCE    |    TRANSACTIONS STREAMING DIRECT FROM THE MEMPOOL", t_base_hdr)
scribus.setFont(FONT_MONO_BOLD, t_base_hdr)
scribus.setFontSize(6.0, t_base_hdr)
scribus.setTextColor("CitadelCrimson", t_base_hdr)
draw_rule(7, 231.5, 203, 231.5, "Black", 0.6)

# Dispatch 1
t_d1 = scribus.createText(7, 233, 94, 51)
scribus.setText(
    "JURISPRUDENCE • SUPREME COURT EN BANC RULING 4929/2569\n"
    "SATOSHI’S CASH BECOMES INVENTORIED CHATTEL\n"
    "Thai Supreme Court rules 2.48 BTC is legally 'Property' in £40,000 Koh Samui beach heist.\n\n"
    "When Satoshi Nakamoto drafted his 2008 whitepaper, he titled it with spartan simplicity: Bitcoin: A Peer-to-Peer Electronic Cash System. The Thai judiciary, however, has codified a rather different taxonomy. In a historic en banc ruling (Supreme Court Decision No. 4929/2569), the Kingdom’s highest bench formally decreed that Bitcoin is not ephemeral cyber-dust, but bona fide incorporeal property under Sections 137 and 138 of the Civil and Commercial Code.\n\n"
    "The precedent stemmed from an extortion on Koh Samui, where a foreign gang coerced a couple in a café—under threats to their infant child—to convert $50,000 into 2.480801 BTC transferred to an offshore wallet. The defence claimed that because Bitcoin possesses no corporeal form and no state-mandated value, no robbery of chattel had occurred. The bench rejected the sophistry outright: holding that digital assets command measurable market value and exclusive dominion via cryptographic keys, the Court confirmed a ten-year penal stretch for armed robbery. Satoshi engineered sovereign cash; Thailand's prison wardens now treat it as fully confiscable property.",
    t_d1
)
scribus.setFont(FONT_SERIF_REG, t_d1)
scribus.setFontSize(5.8, t_d1)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_d1)

draw_rule(104, 233, 104, 283, "GreyRule", 0.5)

# Dispatch 2
t_d2 = scribus.createText(107, 233, 96, 51)
scribus.setText(
    "FORENSIC AUDITING • THE COGNITIVE DEFICIT OF CRIME\n"
    "KORN HAILS THE OPEN LEDGER; CRIMINALS FAIL ARITHMANCY\n"
    "Former Finance Minister marvels at 118m-baht on-chain gambling trail, exposing the sub-standard intellect of cartel laundering.\n\n"
    "Former Finance Minister Korn Chatikavanij took to Facebook this week to shower unexpected praise upon public blockchains. Reflecting on a forensic dossier compiled by former Democrat MP Sirichok Sopa—who mapped nearly 10,000 transactions totaling 118 million Baht linked to illegal gambling platform Shuffle without requiring a single court warrant or bank subpoena—Korn proclaimed: 'Crypto is not the villain here; it may well be the hero.'\n\n"
    "While Mr. Korn noted that unlike opaque bank mule accounts or borderland bags of cash, public ledgers provide an indelible trail for the state, his diplomatic assessment delicately sidestepped the larger psychological reality: the comical IQ deficit of the modern money launderer. To launder illicit revenue across a globally broadcast, permanent ledger is akin to burgling a vault whilst wearing a high-visibility neon vest, a bodycam livestreaming to YouTube, and handing out numbered receipts. Satoshi gave humanity an unforgeable public receipt machine; only the most intellectually deficient cartels would choose it as a hideaway.",
    t_d2
)
scribus.setFont(FONT_SERIF_REG, t_d2)
scribus.setFontSize(5.8, t_d2)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_d2)

add_footer(3, "PROTOCOL FORENSICS: ELECTRUM RBF WEAPONISATION")


# ==============================================================================
# PAGE 4: KATHINA SPREAD, THE SEGREGATED WITNESS, FAMILIARS & CITADEL COFFEE
# ==============================================================================
scribus.gotoPage(4)
add_header(4, "The Back Page: Khao Wanchai Kathina, The Segregated Witness & Familiars")

# Top Section: Kathina Ceremony Spread (Y: 14 to 98mm)
draw_box(7, 14, 196, 84, fill="CreamYellow", stroke="CitadelCrimson", line_width=1.5)

t_k_ban = scribus.createText(9, 15, 192, 4)
scribus.setText("☸ งานบุญมหากุศล • KATHINA & FOUNDATION PILLAR CEREMONY • PAK CHONG    |    วัดเขาวันชัยนวรัตน์ • 31 ต.ค. – 1 พ.ย. 2569", t_k_ban)
scribus.setFont(FONT_THAI_BOLD, t_k_ban)
scribus.setFontSize(5.8, t_k_ban)
scribus.setTextColor("CitadelCrimson", t_k_ban)
draw_rule(9, 19.5, 201, 19.5, "CitadelCrimson", 0.5)

# Poster 1
add_image_box(9, 21, 44, 75, os.path.join(WORKING_DIR, "issue-03/ads/kathina_khao_wanchai_01.jpg"), stroke="Black", line_width=0.5)

# Poster 2
add_image_box(55, 21, 44, 75, os.path.join(WORKING_DIR, "issue-03/ads/kathina_khao_wanchai_02.jpg"), stroke="Black", line_width=0.5)

# Editorial Announcement & Schedule
t_k_text = scribus.createText(101, 21, 68, 75)
scribus.setText(
    "ขอเชิญร่วมบุญทอดกฐินสามัคคี & ยกเสาเอกเจดีย์\n"
    "Wat Khao Wanchai Nawarat Chedi Foundation • Pak Chong Gathering\n\n"
    "สุดสัปดาห์นี้ ขอเรียนเชิญกัลยาณมิตร ศิษยานุศิษย์ และพี่น้องชาว Citadel ทุกท่าน ร่วมเดินทางสู่ อ.ปากช่อง จ.นครราชสีมา เพื่อร่วมบุญมหากุศลทอดกฐินสามัคคีสมทบทุนสร้าง \"รัตนเจดีย์ศรีดวงแก้วโพธิญาณ\" และมุทิตาสักการะอายุวัฒนมงคล 79 ปี หลวงพ่อพระครูภาวนาอุดมคุณ โดย อาจารย์โฉลก สัมพันธารักษ์ พร้อมครอบครัว และคณะศิษย์ CDC จะเดินทางไปร่วมสร้างมหาทานบารมีในครั้งนี้โดยพร้อมเพรียงกัน\n\n"
    "กำหนดการสำคัญ (CEREMONIAL SCHEDULE)\n"
    "• เสาร์ 31 ต.ค.: 16.30 น. สรงน้ำหลวงพ่อพระครูภาวนาอุดมคุณ (79 ปี) • 19.00 น. ทำวัตรเย็น ปฏิบัติภาวนา ฟังธรรม\n"
    "• อาทิตย์ 1 พ.ย.: 07.00 น. ตักบาตร • 08.00 น. ถวายภัตตาหาร • 10.39 น. ถวายผ้ากฐินสามัคคี • 13.19 น. พิธียกเสาเอกเจดีย์ โดยสมเด็จพระวชิรสิทธาจารย์ (วัดสระเกศ) & มทภ.2\n\n"
    "★ บ้านเกาะแก้ว ต.ปากช่อง อ.ปากช่อง จ.นครราชสีมา ★",
    t_k_text
)
scribus.setFont(FONT_THAI_REG, t_k_text)
scribus.setFontSize(5.8, t_k_text)
scribus.setTextAlignment(scribus.ALIGN_LEFT, t_k_text)

# PromptPay e-Donation Card
draw_box(171, 21, 30, 75, fill="White", stroke="NavyBlue", line_width=1.0)
t_qr_hdr = scribus.createText(171, 21.5, 30, 4)
scribus.setText("PromptPay e-Donation", t_qr_hdr)
scribus.setFont(FONT_SANS_BOLD, t_qr_hdr)
scribus.setFontSize(5.2, t_qr_hdr)
scribus.setTextColor("NavyBlue", t_qr_hdr)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_qr_hdr)

# QR Image
add_image_box(173, 26, 26, 26, os.path.join(WORKING_DIR, "issue-03/ads/wat_khao_wanchai_edonation_qr.png"), stroke=None)

t_qr_foot = scribus.createText(172, 53, 28, 41)
scribus.setText(
    "วัดเขาวันชัยนวรัตน์\n"
    "WAT KOW WANCHAI\n\n"
    "เลขประจำตัวผู้เสียภาษี:\n099400230775390\n\n"
    "สแกนร่วมทำบุญ\n"
    "ลดหย่อนภาษีอัตโนมัติ\n"
    "ผ่านกรมสรรพากร\n"
    "(e-Donation)",
    t_qr_foot
)
scribus.setFont(FONT_THAI_REG, t_qr_foot)
scribus.setFontSize(4.8, t_qr_foot)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_qr_foot)


# Bottom Half: Segregated Witness (Left 120mm) + Ads (Right 70mm) (Y: 101 to 284mm)

# LEFT: The Segregated Witness Box
draw_box(7, 101, 120, 183, fill="White", stroke="Black", line_width=1.2)

t_sw_kicker = scribus.createText(9, 102.5, 116, 4)
scribus.setText("■ THE SEGREGATED WITNESS • BY DON SAMBANDARAKSA    |    MEMOIRS OF POST DATABASE • SEPT 2010", t_sw_kicker)
scribus.setFont(FONT_MONO_BOLD, t_sw_kicker)
scribus.setFontSize(5.5, t_sw_kicker)
scribus.setTextColor("CitadelCrimson", t_sw_kicker)

t_sw_head = scribus.createText(9, 106.5, 116, 7.5)
scribus.setText("EIGHTEEN PER CENT AND PROUD OF IT", t_sw_head)
scribus.setFont(FONT_SERIF_BOLD, t_sw_head)
scribus.setFontSize(14, t_sw_head)

t_sw_sub = scribus.createText(9, 114, 116, 7.5)
scribus.setText("How a delivery of frozen sausages revived a sixteen-year-old epiphany in Chiang Mai on the true price of capital, the cruelty of interest rate caps, and the moral hazard of the nanny state.", t_sw_sub)
scribus.setFont(FONT_SERIF_ITAL, t_sw_sub)
scribus.setFontSize(6.5, t_sw_sub)

# Hero Woodcut Plate 4
add_image_box(9, 122, 116, 62, os.path.join(WORKING_DIR, "issue-03/ads/motorcycle_18percent_woodcut.jpg"), stroke="Black", line_width=0.5)

t_plate4_cap = scribus.createText(9, 184.5, 116, 4.5)
scribus.setText("Plate 4: The 18% Northern Sovereign Rider. A modest motorcycle transforms an informal labourer into an independent enterprise. In the clouds above: the towering silhouette of an IBM P-Series database server.", t_plate4_cap)
scribus.setFont(FONT_SERIF_ITAL, t_plate4_cap)
scribus.setFontSize(5.5, t_plate4_cap)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_plate4_cap)
draw_rule(9, 189.5, 123, 189.5, "GreyRule", 0.5)

# 2-Column Text Body
t_sw_body = scribus.createText(9, 191, 116, 88)
scribus.setColumns(2, t_sw_body)
scribus.setColumnGap(6, t_sw_body)
scribus.setText(
    "This morning, an express van pulled up to my gate to deliver a parcel of frozen sausages dispatched from Ratchaburi. Emblazoned across the vehicle was the livery of NIM Express. It is a peculiar facet of human memory that an ordinary parcel of breakfast meat can instantly dislodge an encounter buried sixteen years in the past.\n\n"
    "In September 2010, I was covering technology for the Post Database at the Bangkok Post. IBM had ferried a contingent of tech journalists to Chiang Mai for what polite society terms a “geo-expansion showcase”—what the rest of us recognized as a corporate fluff junket. Big Blue was strutting its northern conquests: 70 terabytes of medical storage for Chiang Mai University, modular containerised data centres, and Lotus Live suites.\n\n"
    "Tucked into the briefing pack as a star regional showcase was Nim See Seng Leasing. They commanded 233 branches across eight northern provinces, powered by centralised IBM P-Series servers and DB2 databases. Their core business? Providing vehicle and motorcycle loans to low-income, informal-sector borrowers who could never dream of securing an audience with a commercial bank.\n\n"
    "The executives presented their metrics with straight faces and unmistakable corporate pride: Nim, they beamed, was performing an uplifting social service by lending at “only” 18 per cent annual interest.\n\n"
    "Eighteen per cent! Sitting in that air-conditioned ballroom as a comfortable urban scribe, my jaw hit the parquet. Eighteen per cent interest, and they called it cheap? Was this not textbook usurious predation—capitalist financiers extracting blood from the poorest labourers on two wheels?\n\n"
    "Then I checked my reporting notes from the provincial streets. The prevailing uncollateralised street rate charged by village loan sharks across the north was 25 per cent. Often higher. Often compounded monthly, and collected under the implicit threat of a lead pipe.\n\n"
    "Now that I am sixteen years older—and, one hopes, a fraction wiser—I find myself returning often to that Chiang Mai epiphany. High interest rates are not inherently an evil conspiracy of elites feasting upon the destitute. Rather, interest is the honest, unvarnished market price of risk.\n\n"
    "What is “fair”? What is “access”? If righteous paternalists in parliament pass an edict capping interest rates out of ostensible compassion, what actually happens? The laws of risk do not bow to ministerial decrees. Two things inevitably follow: either the man at the bottom of the pyramid is denied the motorcycle that allows him to commute and earn his livelihood; or he is driven straight back into the shadows of the loan shark at 25, 30, or 50 per cent.\n\n"
    "In pretending that high-risk capital should be artificially cheap, the state does not protect the vulnerable; it subsidises moral hazard, breeds a sub-class dependent on perpetual debt moratoria and bailouts, and outlaws the bottom rungs of the formal credit ladder. The market price of risk is uncomfortable. The state’s compassionate illusion is ruinous.",
    t_sw_body
)
scribus.setFont(FONT_SERIF_REG, t_sw_body)
scribus.setFontSize(6.4, t_sw_body)
scribus.setTextAlignment(scribus.ALIGN_BLOCK, t_sw_body)

draw_rule(9, 280, 123, 280, "GreyRule", 0.5)
t_sw_foot = scribus.createText(9, 280.5, 116, 3.5)
scribus.setText("★ THE SEGREGATED WITNESS APPEARS EXCLUSIVELY IN THE CITADEL CHRONICLE ★", t_sw_foot)
scribus.setFont(FONT_MONO_BOLD, t_sw_foot)
scribus.setFontSize(5.0, t_sw_foot)
scribus.setTextAlignment(scribus.ALIGN_RIGHT, t_sw_foot)


# RIGHT COLUMN: PUPPIES + CITADEL COFFEE + COLOPHON (X: 130 to 203mm)

# 1. The Nine Familiars Ad (Y: 101 to 148mm)
draw_box(130, 101, 73, 47, fill="CreamYellow", stroke="Black", line_width=1.0)
t_pup_hdr = scribus.createText(131, 102, 71, 3.5)
scribus.setText("★ ADOPT A FAMILIAR ★    |    FREE (0 SATS)", t_pup_hdr)
scribus.setFont(FONT_MONO_BOLD, t_pup_hdr)
scribus.setFontSize(5.5, t_pup_hdr)
scribus.setTextColor("CitadelCrimson", t_pup_hdr)

t_pup_title = scribus.createText(131, 105.5, 71, 5)
scribus.setText("THE NINE FAMILIARS", t_pup_title)
scribus.setFont(FONT_SERIF_BOLD, t_pup_title)
scribus.setFontSize(11, t_pup_title)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_pup_title)

add_image_box(148, 111, 37, 25, os.path.join(WORKING_DIR, "issue-03/ads/wizarding_puppies.jpg"), stroke="Black", line_width=0.5)

t_pup_copy = scribus.createText(131, 137, 71, 10)
scribus.setText("Every wizard needs a loyal familiar. Bred in our Pathum Thani redoubt, these nine canine companions are house-broken, impervious to basilisk stares, and trained to bark vigorously at tax collectors.\nENQUIRE: @DON VIA NOSTR OR DESK", t_pup_copy)
scribus.setFont(FONT_SERIF_REG, t_pup_copy)
scribus.setFontSize(5.5, t_pup_copy)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_pup_copy)

# 2. Citadel Coffee Display Ad (Y: 150 to 244mm)
draw_box(130, 150, 73, 94, fill="CreamYellow", stroke="Black", line_width=1.0)
t_cof_hdr = scribus.createText(131, 151, 71, 3.5)
scribus.setText("★ CITADEL COFFEE ROASTERS ★    |    PATHUM THANI", t_cof_hdr)
scribus.setFont(FONT_MONO_BOLD, t_cof_hdr)
scribus.setFontSize(5.5, t_cof_hdr)
scribus.setTextColor("CitadelCrimson", t_cof_hdr)

t_cof_title = scribus.createText(131, 154.5, 71, 5)
scribus.setText("SIGNATURE PICCOLO LATTE", t_cof_title)
scribus.setFont(FONT_SERIF_BOLD, t_cof_title)
scribus.setFontSize(10.5, t_cof_title)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_cof_title)

add_image_box(132, 160, 69, 68, os.path.join(WORKING_DIR, "issue-03/ads/citadel_coffee_piccolo.png"), stroke="Black", line_width=0.5)

t_cof_copy = scribus.createText(131, 229, 71, 14)
scribus.setText("Piccolo Latte (90.-) • Double ristretto extracted under 21-bar consensus pressure, cut with velvety milk at 1:2 ratio. Low latency, zero dilution, pure proof-of-work caffeine.\n⚡ 0-CONF LIGHTNING SETTLED • ZERO CUSTODIAL DEBT", t_cof_copy)
scribus.setFont(FONT_SERIF_REG, t_cof_copy)
scribus.setFontSize(5.2, t_cof_copy)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_cof_copy)

# 3. Colophon (Y: 246 to 284mm)
draw_box(130, 246, 73, 38, fill="PaperWarm", stroke="Black", line_width=1.0)
t_col_hdr = scribus.createText(131, 247, 71, 3.5)
scribus.setText("CITADEL CHRONICLE • COLOPHON    |    ISSUE 03", t_col_hdr)
scribus.setFont(FONT_MONO_BOLD, t_col_hdr)
scribus.setFontSize(5.5, t_col_hdr)
draw_rule(131, 250.5, 201, 250.5, "Black", 0.5)

t_col_text = scribus.createText(131, 251.5, 52, 28)
scribus.setText(
    "• EDITOR-IN-CHIEF: Don Sambandaraksa (@don)\n"
    "• BLOCK ANCHOR: 973,528 • 28 OCT 2026\n"
    "• LIGHTNING: don@citadelchronicle.com\n"
    "• FULL NPUB:\n"
    "npub1mwpsruysa2nv0ukv9mzssk8grfp7tdhftvcrs3azu9sfrhnasl7qu5uu3w\n\n"
    "“ALL THE RANTS THAT FIT ON FOUR SHEETS”",
    t_col_text
)
scribus.setFont(FONT_MONO_REG, t_col_text)
scribus.setFontSize(4.8, t_col_text)

# Nostr QR Code Box
draw_box(184, 252, 17, 21, fill="White", stroke="Black", line_width=0.5)
add_image_box(184.5, 252.5, 16, 16, os.path.join(WORKING_DIR, "issue-03/ads/nostr_qr.png"), stroke=None)
t_n_scan = scribus.createText(184, 269, 17, 3.5)
scribus.setText("SCAN NOSTR", t_n_scan)
scribus.setFont(FONT_MONO_BOLD, t_n_scan)
scribus.setFontSize(3.8, t_n_scan)
scribus.setTextAlignment(scribus.ALIGN_CENTERED, t_n_scan)

add_footer(4, "KATHINA KHAO WANCHAI, THE SEGREGATED WITNESS & FAMILIARS")

# ==============================================================================
# SAVE DOCUMENT
# ==============================================================================
scribus.saveDocAs(OUT_SLA)
print(f"Successfully saved native Scribus document: {OUT_SLA}")

# Copy to Downloads
shutil.copy2(OUT_SLA, OUT_SLA_DL)
print(f"Copied to: {OUT_SLA_DL}")

# Export PDF directly from Scribus to verify integrity
try:
    pdf = scribus.PDFfile()
    pdf.file = OUT_PDF_TEST
    pdf.quality = 1  # Maximum quality
    pdf.resolution = 600
    pdf.save()
    print(f"Successfully exported test PDF via Scribus: {OUT_PDF_TEST}")
except Exception as e:
    print(f"Note on PDF export: {e}")

print("Scribus 1.7.x SLA Generation Complete!")
