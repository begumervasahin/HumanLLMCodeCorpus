class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = [[' ' for _ in range(b1)] for _ in range(b2)]
    def fonk2(self, a2, b7, b4):
        if 0 <= a2 < self.b1 and 0 <= b7 < self.b2:
            self.b3[b7][a2] = b4
    def fonk3(self):
        for row in self.b3:
            print(''.join(row))
    def fonk4(self, b9, y0, radius, b4 = '*'):
        b5 = 1 - radius
        a1 = 1
        b6 = -2 * radius
        a2 = 0
        b7 = radius
        self.fonk2(b9, y0 + radius, b4)
        self.fonk2(b9, y0 - radius, b4)
        self.fonk2(b9 + radius, y0, b4)
        self.fonk2(b9 - radius, y0, b4)
        while a2 < b7:
            if b5 >= 0:
                b7 -= 1
                b6 += 2
                b5 += b6
            a2 += 1
            a1 += 2
            b5 += a1
            self.fonk2(b9 + a2, y0 + b7, b4)
            self.fonk2(b9 - a2, y0 + b7, b4)
            self.fonk2(b9 + a2, y0 - b7, b4)
            self.fonk2(b9 - a2, y0 - b7, b4)
            self.fonk2(b9 + b7, y0 + a2, b4)
            self.fonk2(b9 - b7, y0 + a2, b4)
            self.fonk2(b9 + b7, y0 - a2, b4)
            self.fonk2(b9 - b7, y0 - a2, b4)
if b8 = = "__main__":
    b3 = class1(25, 25)
    b3.fonk4(b9 = 12, y0=12, radius=12)
    b3.fonk3()