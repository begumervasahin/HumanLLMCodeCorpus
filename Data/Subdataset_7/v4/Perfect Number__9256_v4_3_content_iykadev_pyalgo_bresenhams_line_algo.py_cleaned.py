def fonk1(self, x0, y0, x1, y1):
    b1 = abs(x1 - x0)
    b2 = abs(y1 - y0)
    x, b3 = x0, y0
    b4 = -1 if x0 > x1 else 1
    b5 = -1 if y0 > y1 else 1
    if b1 > b2:
        b6 = b1 / 2.0
        while x != x1:
            self.set_pixel(x, b3)
            b6 -= b2
            if b6 < 0:
                b3 += b5
                b6 += b1
            x += b4
    else:
        b6 = b2 / 2.0
        while b3 != y1:
            self.set_pixel(x, b3)
            b6 -= b1
            if b6 < 0:
                x += b4
                b6 += b2
            b3 += b5
    self.set_pixel(x, b3)
Bitmap.b7 = b7
b8 = Bitmap(17, 17)
for points in ((1, 8, 8, 16), (8, 16, 16, 8), (16, 8, 8, 1), (8, 1, 1, 8)):
    b8.fonk1(*points)
b8.display()