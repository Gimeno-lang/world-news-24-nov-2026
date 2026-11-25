import os
from PIL import Image, ImageDraw, ImageFont

def font(size, bold=False):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    try:
        return ImageFont.truetype(p, size)
    except:
        return ImageFont.load_default()

def main():
    W, H = 1024, 1024
    img = Image.new("RGB", (W, H), (255,255,255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0,0,W,120], fill=(15,15,15))
    draw.text((20,12), "WORLD NEWS", font=font(44, True), fill=(255,255,255))
    draw.text((20,62), "TUESDAY 24 NOVEMBER 2026", font=font(26, True), fill=(255,200,60))
    draw.text((620,25), "6 STORIES", font=font(20, True), fill=(255,255,255))
    panels = [
        ("SPACE - ASIA", "Shenzhou-24 launches", "China + Pakistan's\nfirst astronaut to\nTiangong station", (0,100,160)),
        ("WAR - EUROPE", "Russia strikes\nZaporizhzhia", "2 killed, 44 wounded.\nUkraine hits Russian\nwarship off Libya", (140,30,30)),
        ("MIDDLE EAST", "Riyadh tower hit\nGaza chief killed", "Houthi attack injures\n11 in Riyadh.\nHamas chief killed", (180,90,0)),
        ("MARKETS - TECH", "Nvidia: Huang\nrally, then fade", "Nvidia +31% Mon,\n-6% Tue. Asia surges.\nTAIEX +8.99%", (10,90,40)),
        ("AMERICAS", "25 hostages in\nCartagena", "Gunmen hold 25 in\nsupermarket after\nfailed raid", (130,60,0)),
        ("AFRICA - GLOBAL", "Ebola staff freed\n+ 5 women / hour", "WHO evacuated in\nIturi, DRC.\nUN: 47,000 women\nkilled in 2025", (0,120,80)),
    ]
    pw, ph = 492, 280
    gapx, gapy = 16, 14
    x0, y0 = 16, 135
    for i, (cat, title, desc, col) in enumerate(panels):
        cx = x0 + (i%2)*(pw+gapx)
        cy = y0 + (i//2)*(ph+gapy)
        draw.rectangle([cx, cy, cx+pw, cy+ph], outline=(0,0,0), width=2, fill=(255,255,255))
        draw.rectangle([cx, cy, cx+pw, cy+34], fill=col)
        draw.text((cx+12, cy+6), cat, font=font(18, True), fill=(255,255,255))
        y = cy+48
        for line in title.split("\n"):
            draw.text((cx+14, y), line, font=font(30, True), fill=(0,0,0))
            y+=34
        y+=4
        for line in desc.split("\n"):
            draw.text((cx+14, y), line, font=font(20), fill=(50,50,50))
            y+=26
    draw.rectangle([0,1010,W,1024], fill=(15,15,15))
    draw.text((20,1012), "Sources: AP - Reuters - BBC - UN News - All stories first reported 24 Nov 2026", font=font(14), fill=(255,255,255))
    os.makedirs("/output", exist_ok=True)
    img.save("/output/entry.png", "PNG", optimize=True)
    print("saved /output/entry.png")

if __name__ == "__main__":
    main()
