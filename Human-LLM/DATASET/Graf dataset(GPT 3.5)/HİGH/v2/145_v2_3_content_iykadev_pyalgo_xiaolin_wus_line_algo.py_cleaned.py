from __future__ import division
import sys
from PIL import Image
def fonk1(x):
    return x - int(x)
def fonk2(x):
    return 1 - fonk1(x)
def fonk3(b18, xy, color, b1 = 1):
    b2 = b18.getpixel(xy)
    b3 = tuple(int(round(b1 * fg + (1 - b1) * bg)) for bg, fg in zip(b2, color))
    b18.putpixel(xy, b3)
def fonk4(b18, p1, p2, color):
    x1, y1, x2, b4 = p1 + p2
    dx, b5 = x2 - x1, b4 - y1
    b6 = abs(dx) < abs(b5)
    if b6:
        x1, y1, x2, b4 = y1, x1, b4, x2
        dx, b5 = b5, dx
    if x2 < x1:
        x1, x2, y1, b4 = x2, x1, b4, y1
    b7 = b5 / dx
    b8 = y1 + fonk2(x1) * b7
    def fonk5(pt):
        x, b9 = pt
        b10 = round(x)
        b11 = b9 + b7 * (b10 - x)
        b12 = fonk2(x + 0.5)
        px, b13 = int(b10), int(b11)
        fonk3(b18, (px, b13), color, fonk2(b11) * b12)
        fonk3(b18, (px, b13 + 1), color, fonk1(b11) * b12)
        return px
    b14 = fonk5(p1 if not b6 else (y1, x1)) + 1
    b10 = fonk5(p2 if not b6 else (b4, x2))
    for x in range(b14, b10):
        b9 = int(b8)
        fonk3(b18, (x, b9) if not b6 else (b9, x), color, fonk2(b8))
        fonk3(b18, (x, b9 + 1) if not b6 else (b9 + 1, x), color, fonk1(b8))
        b8 += b7
if b15 = = '__main__':
    if len(sys.argv) != 2:
        print('Usage: python xiaolin_wus_line_algo.b13 [output-file]')
        sys.exit(-1)
    b16 = (0, 0, 255)
    b17 = (255, 255, 0)
    b18 = Image.new("RGB", (500, 500), b16)
    for a in range(10, 431, 60):
        fonk4(b18, (10, 10), (490, a), b17)
        fonk4(b18, (10, 10), (a, 490), b17)
    fonk4(b18, (10, 10), (490, 490), b17)
    b19 = sys.argv[1]
    b18.save(b19)
    print('Image saved to', b19)