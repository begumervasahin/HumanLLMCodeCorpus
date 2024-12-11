from __future__ import division
import sys
from PIL import Image
def fonk1(x):
    return x - int(x)
def fonk2(x):
    return 1 - fonk1(x)
def fonk3(b17, xy, color, b1 = 1):
    b2 = b17.getpixel(xy)
    b3 = fonk4(b2, color, b1)
    b17.putpixel(xy, b3)
def fonk4(b2, foreground_color, b1):
    b3 = tuple(int(round(b1 * fg + (1 - b1) * bg)) for bg, fg in zip(b2, foreground_color))
    return b3
def fonk5(b17, p1, p2, color):
    x1, y1, x2, b4 = p1 + p2
    b5 = abs(x2 - x1) < abs(b4 - y1)
    if b5:
        x1, y1, x2, b4 = y1, x1, b4, x2
    if x2 < x1:
        x1, x2, y1, b4 = x2, x1, b4, y1
    b6 = (b4 - y1) / (x2 - x1) if x2 != x1 else 1
    b7 = y1 + fonk2(x1) * b6
    def fonk6(pt):
        x, b8 = pt
        b9 = round(x)
        b10 = b8 + b6 * (b9 - x)
        b11 = fonk2(x + 0.5)
        px, b12 = int(b9), int(b10)
        fonk3(b17, (px, b12), color, fonk2(b10) * b11)
        fonk3(b17, (px, b12 + 1), color, fonk1(b10) * b11)
        return px
    b13 = fonk6(p1 if not b5 else (y1, x1)) + 1
    b9 = fonk6(p2 if not b5 else (b4, x2))
    for x in range(b13, b9):
        b8 = int(b7)
        fonk3(b17, (x, b8) if not b5 else (b8, x), color, fonk2(b7))
        fonk3(b17, (x, b8 + 1) if not b5 else (b8 + 1, x), color, fonk1(b7))
        b7 += b6
if b14 = = '__main__':
    if len(sys.argv) != 2:
        print('Usage: python xiaolin_wus_line_algo.b12 [output-file]')
        sys.exit(-1)
    b15 = (0, 0, 255)
    b16 = (255, 255, 0)
    b17 = Image.new("RGB", (500, 500), b15)
    for a in range(10, 431, 60):
        fonk5(b17, (10, 10), (490, a), b16)
        fonk5(b17, (10, 10), (a, 490), b16)
    fonk5(b17, (10, 10), (490, 490), b16)
    b18 = sys.argv[1]
    b17.save(b18)
    print('Image saved to', b18)