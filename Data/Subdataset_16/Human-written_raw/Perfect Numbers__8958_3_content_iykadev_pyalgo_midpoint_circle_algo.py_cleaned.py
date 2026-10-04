def fonk1(self, b7, y0, radius, b1 = black):
    b2 = 1 - radius
    a1 = 1
    b3 = -2 * radius
    a2 = 0
    b4 = radius
    self.set(b7, y0 + radius, b1)
    self.set(b7, y0 - radius, b1)
    self.set(b7 + radius, y0, b1)
    self.set(b7 - radius, y0, b1)
    while a2 < b4:
        if b2 >= 0:
            b4 -= 1
            b3 += 2
            b2 += b3
        a2 += 1
        a1 += 2
        b2 += a1
        self.set(b7 + a2, y0 + b4, b1)
        self.set(b7 - a2, y0 + b4, b1)
        self.set(b7 + a2, y0 - b4, b1)
        self.set(b7 - a2, y0 - b4, b1)
        self.set(b7 + b4, y0 + a2, b1)
        self.set(b7 - b4, y0 + a2, b1)
        self.set(b7 + b4, y0 - a2, b1)
        self.set(b7 - b4, y0 - a2, b1)
Bitmap.b5 = b5
b6 = Bitmap(25,25)
b6.fonk1(b7 = 12, y0=12, radius=12)
b6.chardisplay()