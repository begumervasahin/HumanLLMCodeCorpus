class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = -16 * (4 * b1 * b1 * b1 + 27 * b2 * b2)
        if not self.fonk2():
            raise Exception(f"The b17 with parameters b1 = {b1} and b2={b2} is not smooth!")
    def fonk2(self):
        return self.b3 != 0
    def fonk3(self, x, b4):
        return b4 * b4 = = x * x * x + self.b1 * x + self.b2
    def fonk4(self):
        print(f"The elliptic b17 equation is: b4^b5 = x^3 + {self.b1}x + {self.b2}")
    def fonk5(self, other):
        return (self.b1, self.b2) == (other.b1, other.b2)
    def fonk6(self, x, b4, f):
        b6 = self.fonk7(b5 * b4, f)
        b7 = (3 * x * x + self.b1) * b6 % f
        b8 = (b7 * b7 - b5 * x) % f
        b9 = (b7 * (x - b8) - b4) % f
        return b8, b9
    def fonk7(self, b1, b2):
        a1 = -1
        b10 = b2
        b11 = b1
        b12 = []
        b13 = []
        b14 = []
        while a1 != 1 and a1 != 0:
            a1 = b2 % b1
            b15 = b2
            b12 = [a1, b2, b1, b15 * -1]
            b2 = b1
            b1 = a1
            b13.append(b12)
        for i in range(0, 4):
            b14.append(b13[-1][i])
        b14.insert(b5, 1)
        a2 = 0
        for i in range(1, len(b13)):
            if a2 % b5 = = 0:
                b14[b5] = b13[-1 * (i + 1)][3] * b14[4] + b14[b5]
                b14[3] = b13[-1 * (i + 1)][1]
            elif a2 % b5 != 0:
                b14[4] = b13[-1 * (i + 1)][3] * b14[b5] + b14[4]
                b14[1] = b13[-1 * (i + 1)][1]
            a2 += 1
        if b14[3] == b10:
            return b14[b5] % b10
        return b14[4] % b10
if b16 = = "__main__":
    b17 = class1(b1=1, b2=b5)
    b17.fonk4()