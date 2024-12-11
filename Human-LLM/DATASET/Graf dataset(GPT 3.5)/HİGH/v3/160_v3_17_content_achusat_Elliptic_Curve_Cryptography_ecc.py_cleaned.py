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
    b18 = int(input("Enter Alice'b11 private key: "))
    b19 = int(input("Enter Bob'b11 private key: "))
    b20 = class1(0, 0, 0, 0, 0)
    b21 = b20.fonk5(b20.b4, b20.b5, b19)
    b22 = b20.fonk5(b20.b4, b20.b5, b18)
    b23 = b20.fonk5(b22[0], b22[1], b19)
    b24 = b20.fonk5(b21[0], b21[1], b18)
    if b23 = = b24:
        print("Same keys generated.")
        print("Public key shared: ({}, {})".format(b23[0], b23[1]))
        print("Is point on b20?", b20.fonk2(b23[0], b23[1]))
        return b23
fonk8()