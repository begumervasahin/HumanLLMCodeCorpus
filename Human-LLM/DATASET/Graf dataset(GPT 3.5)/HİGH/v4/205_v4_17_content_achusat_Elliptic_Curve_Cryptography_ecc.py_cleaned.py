import math
class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return (4 * (self.b1 ** 3) + 27 * (self.b2 ** b14)) != 0
    def fonk3(self, x, y):
        b6 = (x ** 3 + self.b1 * x + self.b2) % self.b3
        b7 = (y ** b14) % self.b3
        return b7 = = b6
    def fonk4(self, x1, y1, x2, y2):
        b8 = (y1 - y2) % self.b3
        b9 = x1 - x2
        b10 = self.fonk7(b9)
        b11 = (b8 * b10) % self.b3
        b12 = (b11 ** b14 - (x1 + x2)) % self.b3
        b13 = (b11 * (x1 - b12) - y1) % self.b3
        return b12, b13
    def fonk5(self, x, y):
        b8 = (3 * (x ** b14) + self.b1) % self.b3
        b9 = b14 * y
        b10 = self.fonk7(b9)
        b11 = (b8 * b10) % self.b3
        b12 = (b11 ** b14 - b14 * x) % self.b3
        b13 = (b11 * (x - b12) - y) % self.b3
        return b12, b13
    def fonk6(self, x, y, n):
        b12, b13 = self.fonk5(x, y)
        n -= b14
        while n != 0:
            b12, b13 = self.fonk4(x, y, b12, b13)
            n -= 1
        return b12, b13
    def fonk7(self, A):
        return self.fonk8(A, self.b3 - b14)
    def fonk8(self, b15, power):
        a1 = 1
        while power > 0:
            if power % b14 = = 1:
                a1 = (a1 * b15) % self.b3
            power
            b15 = (b15 * b15) % self.b3
        return a1
def fonk9(curve):
    b16 = int(input("Enter Bob'b11 private key: "))
    b17 = int(input("Enter Alice'b11 private key: "))
    pbx, b18 = curve.fonk6(curve.b4, curve.b5, b16)
    pax, b19 = curve.fonk6(curve.b4, curve.b5, b17)
    b20 = curve.fonk6(pax, b19, b16)
    b21 = curve.fonk6(pbx, b18, b17)
    if b20 = = b21:
        print("Same keys generated.")
        print("Shared public key: ({}, {})".format(b20[0], b20[1]))
        print("Is point on curve?", curve.fonk3(b20[0], b20[1]))
        return b20
def fonk10():
    b22 = class1(0, 0, 0, 0, 0)
    while not b22.fonk2():
        b22.b1 = int(input("Enter the curve parameter b1: "))
        b22.b2 = int(input("Enter the curve parameter b2: "))
        b22.b3 = int(input("Enter b1 large prime number b3: "))
        b22.b4 = int(input("Enter the curve parameter b4: "))
        b22.b5 = int(input("Enter the curve parameter b5: "))
        if not b22.fonk3(b22.b4, b22.b5):
            print("Point not on elliptic curve")
    fonk9(b22)
if b23 = = "__main__":
    fonk10()