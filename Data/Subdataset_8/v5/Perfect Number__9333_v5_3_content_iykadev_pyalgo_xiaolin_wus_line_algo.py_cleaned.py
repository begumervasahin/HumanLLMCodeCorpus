from __future__ import division
import sys
from PIL import Image
def fractional_part(x):
    return x - int(x)
def reverse_fractional_part(x):
    return 1 - fractional_part(x)
def blend_color(bg_color, fg_color, alpha):
    return tuple(
        int(round(alpha * fg + (1 - alpha) * bg))
        for bg, fg in zip(bg_color, fg_color)
    )
def put_pixel(image, xy, color, alpha=1):
    background_color = image.getpixel(xy)
    blended_color = blend_color(background_color, color, alpha)
    image.putpixel(xy, blended_color)
def draw_endpoint(image, x, y, gradient, steep, color):
    xend = round(x)
    yend = y + gradient * (xend - x)
    x_gap = reverse_fractional_part(x + 0.5)
    px, py = int(xend), int(yend)
    put_pixel(image, (px, py), color, reverse_fractional_part(yend) * x_gap)
    put_pixel(image, (px, py + 1), color, fractional_part(yend) * x_gap)
    return px
def draw_line(image, p1, p2, color):
    x1, y1, x2, y2 = p1 + p2
    steep = abs(x2 - x1) < abs(y2 - y1)
    if steep:
        x1, y1, x2, y2 = y1, x1, y2, x2
    if x2 < x1:
        x1, x2, y1, y2 = x2, x1, y2, y1
    dx, dy = x2 - x1, y2 - y1
    gradient = dy / dx if dx != 0 else float('inf')
    intery = y1 + reverse_fractional_part(x1) * gradient
    xstart = draw_endpoint(image, x1, y1, gradient, steep, color) + 1
    xend = draw_endpoint(image, x2, y2, gradient, steep, color)
    for x in range(xstart, xend):
        y = int(intery)
        put_pixel(image, (y, x) if steep else (x, y), color, reverse_fractional_part(intery))
        put_pixel(image, (y + 1, x) if steep else (x, y + 1), color, fractional_part(intery))
        intery += gradient
def main():
    if len(sys.argv) != 2:
        print('Usage: python xiaolin_wus_line_algo.py [output-file]')
        sys.exit(-1)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    image = Image.new("RGB", (500, 500), blue)
    for a in range(10, 431, 60):
        draw_line(image, (10, 10), (490, a), yellow)
        draw_line(image, (10, 10), (a, 490), yellow)
    draw_line(image, (10, 10), (490, 490), yellow)
    filename = sys.argv[1]
    image.save(filename)
    print('Image saved to', filename)
if __name__ == '__main__':
    main()