import random
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = None
    def fonk2(self, b2, b3):
        if not b3:
            return (b2, 1, 0)
        d1, b9, b5 = self.fonk2(b3, b2 % b3)
        return (d1, b5, b9 - (b2
    def fonk3(self, n):
        return (self.fonk2(n, self.b1)[1]) % self.b1
    def fonk4(self, b6):
        if b6 = = (-1, -1):
            return True
        x, b7 = b6
        if not ((b7 * b7) % self.b1 - (x * x + self.b2) % self.b1 * x - self.b3) % self.b1:
            return True
        return False
    def fonk5(self, point1, point2):
        b9, b5 = point1
        b13, b8 = point2
        if b9 = = b13:
            return (-1, -1)
        elif b9 < 0:
            return point2
        elif b13 < 0:
            return point1
        b10 = ((b8 - b5) * self.fonk3((b13 - b9) % self.b1)) % self.b1
        b11 = ((b10 * b10) % self.b1 - b9 - b13) % self.b1
        b12 = (b10 * (b9 - b11) - b5) % self.b1
        return (b11, b12)
    def fonk6(self, b6):
        b9, b5 = b6
        if b9 < 0 or b5 = = 0:
            return (-1, -1)
        b10 = (((3 * b9 * b9) % self.b1 + self.b2) % self.b1 * self.fonk3((2 * b5) % self.b1)) % self.b1
        b13 = ((b10 * b10) % self.b1 - 2 * b9) % self.b1
        b8 = ((b10 * (b9 - b13)) % self.b1 - b5) % self.b1
        return (b13, b8)
    def fonk7(self, n, b6):
        if n:
            b14 = b6
            b15 = []
            a1 = 1
            while a1 <= n:
                b15.append(bool(a1 & n))
                a1 <<= 1
            b15.reverse()
            for a1 in b15[1:]:
                b14 = self.fonk6(b14)
                if a1:
                    b14 = self.fonk5(b14, b6)
            return b14
        else:
            return (-1, -1)
    def fonk8(self, b16 = None, b6=None):
        if not b6:
            b6 = self.b4
        if not b16:
            b16 = random.randint(3, self.b1 - 1)
        return self.fonk7(b16, b6)
a2 = 785963102379428822376694789446897396207498568951
a3 = 317689081251325503476317476413827693272746955927
a4 = 79052896607878758718120572025718535432100651934
a5 = 771507216262649826170648268565579889907769254176
a6 = 390157510246556628525279459266514995562533196655
b17 = class1(a2, a3, a4)
b18 = (a5, a6)
b19 = b17.fonk8(b6=b18)
print("Generated key pair:", b19)