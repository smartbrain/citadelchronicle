import re
from PIL import Image

def analyze_page_fill(img_path):
    im = Image.open(img_path).convert('L')
    w, h = im.size
    pix = im.load()
    
    # find top of content (first row with non-white)
    top = 0
    for y in range(h):
        if any(pix[x, y] < 240 for x in range(w)):
            top = y
            break
            
    # find footer position
    footer_pos = 0
    for y in range(h-1, 3100, -1):
        if any(pix[x, y] < 240 for x in range(w)):
            footer_pos = y
            break

    # find bottom of main content (excluding footer line)
    # The footer is at footer_pos. Look above it (footer_pos - 30)
    content_bottom = 0
    for y in range(footer_pos - 35, 500, -1):
        if any(pix[x, y] < 240 for x in range(120, w-120)):
            content_bottom = y
            break

    print(f"=== {img_path.split('/')[-1]} ===")
    print(f"  Content Top: y={top} ({top/300*25.4:.1f} mm)")
    print(f"  Content Bottom: y={content_bottom} ({content_bottom/300*25.4:.1f} mm)")
    print(f"  Footer Pos: y={footer_pos} ({footer_pos/300*25.4:.1f} mm)")
    gap = footer_pos - content_bottom
    print(f"  GAP above footer: {gap} px ({gap/300*25.4:.1f} mm) — {'HUGE EMPTY GAP!' if gap > 200 else 'WELL BALANCED!'}")

for p in ['page1_front', 'page2_editorial', 'page3_deepdive', 'page4_back']:
    analyze_page_fill(f'/home/don/citadelchronicle/citadel_chronicle_a4_{p}_300dpi.jpg')
