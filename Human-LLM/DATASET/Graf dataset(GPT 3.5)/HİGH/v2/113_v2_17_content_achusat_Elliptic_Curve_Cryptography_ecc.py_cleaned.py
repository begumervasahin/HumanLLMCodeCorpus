import math
class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self, x, y):
        b6 = (x**3 + self.b1*x + self.b2) % self.b3
        b7 = (y**b15) % self.b3
        return b7 = = b6
    def fonk3(self, x1, y1, x2, y2):
        b8 = (y1 - y2) % self.b3
        b9 = x1 - x2
        b10 = self.fonk6(b9)
        b11 = (b8 * b10) % self.b3
        b12 = (b11**b15 - (x1 + x2)) % self.b3
        b13 = (b11 * (x1 - b12) - y1) % self.b3
        return b12, b13
    def fonk4(self, x, y):
        b8 = (3 * (x**b15) + self.b1) % self.b3
        b9 = b15 * y
        b10 = self.fonk6(b9)
        b11 = (b8 * b10) % self.b3
        b12 = (b11**b15 - b15*x) % self.b3
        b13 = (b11 * (x - b12) - y) % self.b3
        return b12 , b13
    def fonk5(self, x, y, b14):
        b12, b13 = self.fonk4(x, y)
        b14 = b14 - b15
        while b14 != 0:
            b12, b13 = self.fonk3(x, y, b12, b13)
            b14 = b14 - 1
        return b12, b13
    def fonk6(self, A):
        return self.fonk7(A, self.b3 - b15)
    def fonk7(self, b17, b16):
        a1 = 1
        while b16 > 0:
            if b16 % b15 = = 1:
                a1 = (a1 * b17) % self.b3
            b16 = b16
            b17 = (b17 * b17) % self.b3
        return a1
def fonk8():
    b1 = int(input("Enter Alice'b11 private key: "))
    b2 = int(input("Enter Bob'b11 private key: "))
    b18 = class1(0, 0, 0, 0, 0)
    pbx, b19 = b18.fonk5(b18.b4, b18.b5, b2)
    pax, b20 = b18.fonk5(b18.b4, b18.b5, b1)
    b23, b21 = b18.fonk5(pax, b20, b2)
    sk_ax, b22 = b18.fonk5(pbx, b19, b1)
    if (b23 = = sk_ax) and (b21 == b22):
        print("Same keys generated.")
        print("Public key shared: ({}, {})".format(sk_ax, b22))
        print("Is point on curve?", b18.fonk2(sk_ax, b22))
        return sk_ax, b22
fonk8()