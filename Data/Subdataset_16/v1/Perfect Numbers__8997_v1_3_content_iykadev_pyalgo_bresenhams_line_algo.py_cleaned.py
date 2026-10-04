class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = [[' ' for _ in range(b1)] for _ in range(b2)]
    def fonk2(self, x, b6):
        if 0 <= x < self.b1 and 0 <= b6 < self.b2:
            self.b3[b6][x] = '*'
    def fonk3(self):
        for row in self.b3:
            print(''.join(row))
def fonk4(self, x0, y0, x1, y1):
    "Bresenham's b10 algorithm"
    b4 = abs(x1 - x0)
    b5 = abs(y1 - y0)
    x, b6 = x0, y0
    b7 = -1 if x0 > x1 else 1
    b8 = -1 if y0 > y1 else 1
    if b4 > b5:
        b9 = b4 / 2.0
        while x != x1:
            self.fonk2(x, b6)
            b9 -= b5
            if b9 < 0:
                b6 += b8
                b9 += b4
            x += b7
    else:
        b9 = b5 / 2.0
        while b6 != y1:
            self.fonk2(x, b6)
            b9 -= b4
            if b9 < 0:
                x += b7
                b9 += b5
            b6 += b8
    self.fonk2(x, b6)
class1.b10 = b10
b3 = class1(17, 17)
for points in ((1, 8, 8, 16), (8, 16, 16, 8), (16, 8, 8, 1), (8, 1, 1, 8)):
    b3.fonk4(*points)
b3.fonk3()