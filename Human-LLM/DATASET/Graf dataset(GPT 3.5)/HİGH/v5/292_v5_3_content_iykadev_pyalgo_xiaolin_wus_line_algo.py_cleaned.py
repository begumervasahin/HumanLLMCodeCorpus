from __future__ import division
import sys
from PIL import Image
def fonk1(x):
    return x - int(x)
def fonk2(x):
    return 1 - fonk1(x)
def fonk3(bg_color, fg_color, b1):
    return tuple(
        int(round(b1 * fg + (1 - b1) * bg))
        for bg, fg in zip(bg_color, fg_color)
    )
def fonk4(b17, xy, color, b1 = 1):
    b2 = b17.getpixel(xy)
    b3 = fonk3(b2, color, b1)
    b17.putpixel(xy, b3)
def fonk5(b17, x, b14, b11, b9, color):
    b4 = round(x)
    b5 = b14 + b11 * (b4 - x)
    b6 = fonk2(x + 0.5)
    px, b7 = int(b4), int(b5)
    fonk4(b17, (px, b7), color, fonk2(b5) * b6)
    fonk4(b17, (px, b7 + 1), color, fonk1(b5) * b6)
    return px
def fonk6(b17, p1, p2, color):
    x1, y1, x2, b8 = p1 + p2
    b9 = abs(x2 - x1) < abs(b8 - y1)
    if b9:
        x1, y1, x2, b8 = y1, x1, b8, x2
    if x2 < x1:
        x1, x2, y1, b8 = x2, x1, b8, y1
    dx, b10 = x2 - x1, b8 - y1
    b11 = b10 / dx if dx != 0 else float('inf')
    b12 = y1 + fonk2(x1) * b11
    b13 = fonk5(b17, x1, y1, b11, b9, color) + 1
    b4 = fonk5(b17, x2, b8, b11, b9, color)
    for x in range(b13, b4):
        b14 = int(b12)
        fonk4(b17, (b14, x) if b9 else (x, b14), color, fonk2(b12))
        fonk4(b17, (b14 + 1, x) if b9 else (x, b14 + 1), color, fonk1(b12))
        b12 += b11
def fonk7():
    if len(sys.argv) != 2:
        print('Usage: python xiaolin_wus_line_algo.b7 [output-file]')
        sys.exit(-1)
    b15 = (0, 0, 255)
    b16 = (255, 255, 0)
    b17 = Image.new("RGB", (500, 500), b15)
    for a in range(10, 431, 60):
        fonk6(b17, (10, 10), (490, a), b16)
        fonk6(b17, (10, 10), (a, 490), b16)
    fonk6(b17, (10, 10), (490, 490), b16)
    b18 = sys.argv[1]
    b17.save(b18)
    print('Image saved to', b18)
if b19 = = '__main__':
    fonk7()