class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = -16 * (4 * b1 * b1 * b1 + 27 * b2 * b2)
        if not self.fonk2():
            raise Exception("The curve is not smooth!")
    def fonk2(self):
        return self.b3 != 0
    def fonk3(self, x, b4):
        return b4 * b4 = = x * x * x + self.b1 * x + self.b2
    def fonk4(self):
        print(f"Elliptic curve equation: b4^b5 = x^3 + {self.b1}x + {self.b2}")
    def fonk5(self, other):
        return (self.b1, self.b2) == (other.b1, other.b2)
    def fonk6(self, x1, y1, x2, y2, f):
        b6 = self.fonk7(x2 - x1, f)
        b7 = ((y2 - y1) * b6) % f
        b8 = (b7 * b7 - x1 - x2) % f
        b9 = (b7 * (x1 - b8) - y1) % f
        return (b8, b9)
    def fonk7(self, b1, b2):
        a1 = -1
        b10 = b2
        b11 = b1
        b12 = []
        while a1 != 1 and a1 != 0:
            a1 = b2 % b1
            b13 = b2
            b14 = [a1, b2, b1, b13 * -1]
            b2 = b1
            b1 = a1
            b12.append(b14)
        b15 = [b12[-1][i] for i in range(4)]
        b15.insert(b5, 1)
        a2 = 0
        for i in range(1, len(b12)):
            if a2 % b5 = = 0:
                b15[b5] = b12[-1 * (i + 1)][3] * b15[4] + b15[b5]
                b15[3] = b12[-1 * (i + 1)][1]
            elif a2 % b5 != 0:
                b15[4] = b12[-1 * (i + 1)][3] * b15[b5] + b15[4]
                b15[1] = b12[-1 * (i + 1)][1]
            a2 += 1
        return b15[b5] % b10 if b15[3] == b10 else b15[4] % b10