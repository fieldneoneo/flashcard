#!/usr/bin/env python3
"""Draws the launcher icon: a white flashcard with an "Ä" and a black-red-gold bar on a blue ground.

The same shapes are written by hand into res/drawable/ic_launcher_foreground.xml (adaptive icon,
108dp canvas). This script renders the raster fallbacks for Android 7 and the store/README icon.

    pip install Pillow && python3 scripts/make_icon.py
"""
import os
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "app", "src", "main", "res")
BLUE, WHITE, INK, RED, GOLD = "#1D5C8C", "#FFFFFF", "#16202B", "#DD0000", "#FFCE00"
SS = 4  # supersampling factor for smooth edges


def foreground(px):
    """The 108x108 foreground layer at px pixels, transparent outside the card."""
    s = px * SS / 108
    im = Image.new("RGBA", (px * SS, px * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    P = lambda pts: [(x * s, y * s) for x, y in pts]
    d.rounded_rectangle([32 * s, 30 * s, 76 * s, 78 * s], radius=5 * s, fill=WHITE)          # card
    d.polygon(P([(51, 43), (57, 43), (47, 66), (41, 66)]), fill=INK)                        # A, left leg
    d.polygon(P([(51, 43), (57, 43), (67, 66), (61, 66)]), fill=INK)                        # A, right leg
    d.rectangle([46 * s, 56 * s, 62 * s, 60.5 * s], fill=INK)                               # A, crossbar
    for cx in (48.5, 59.5):                                                                 # umlaut dots
        d.ellipse([(cx - 2.7) * s, (37.5 - 2.7) * s, (cx + 2.7) * s, (37.5 + 2.7) * s], fill=INK)
    for i, col in enumerate((INK, RED, GOLD)):                                              # black-red-gold bar
        d.rectangle([38 * s, (70 + 2 * i) * s, 70 * s, (72 + 2 * i) * s], fill=col)
    return im.resize((px, px), Image.LANCZOS)


def legacy(px, round_mask):
    """Full icon for launchers without adaptive icons: the central 72 of the 108 canvas."""
    big = px * SS
    fg = foreground(round(px * 108 / 72)).resize((round(big * 108 / 72),) * 2, Image.LANCZOS)
    off = (fg.width - big) // 2
    im = Image.new("RGBA", (big, big), BLUE)
    im.alpha_composite(fg.crop((off, off, off + big, off + big)))
    mask = Image.new("L", (big, big), 0)
    m = ImageDraw.Draw(mask)
    if round_mask:
        m.ellipse([0, 0, big - 1, big - 1], fill=255)
    else:
        m.rounded_rectangle([0, 0, big - 1, big - 1], radius=big * 0.18, fill=255)
    im.putalpha(mask)
    return im.resize((px, px), Image.LANCZOS)


if __name__ == "__main__":
    for name, px in (("mdpi", 48), ("hdpi", 72), ("xhdpi", 96), ("xxhdpi", 144), ("xxxhdpi", 192)):
        d = os.path.join(RES, "mipmap-" + name)
        legacy(px, False).save(os.path.join(d, "ic_launcher.webp"), "WEBP", lossless=True)
        legacy(px, True).save(os.path.join(d, "ic_launcher_round.webp"), "WEBP", lossless=True)
        foreground(round(px * 108 / 48)).save(os.path.join(d, "ic_launcher_foreground.webp"), "WEBP", lossless=True)
    legacy(512, False).save(os.path.join(ROOT, "fastlane", "metadata", "android", "en-US", "images", "icon.png"), "PNG")
    print("icons written")
