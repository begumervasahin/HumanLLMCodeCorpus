import math
import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self, x, y):
        b6 = (x**3 + self.b1*x + self.b2) % self.b3
        b7 = (y**b14) % self.b3
        return b7 = = b6
    def fonk3(self, x1, y1, x2, y2):
        b8 = (y1 - y2) % self.b3
        b9 = x1 - x2
        b9 = self.fonk6(b9)
        b10 = (b8 * b9) % self.b3
        b11 = (b10**b14 - (x1 + x2)) % self.b3
        b12 = (b10 * (x1 - b11) - y1) % self.b3
        return b11, b12
    def fonk4(self, x, y):
        b8 = (3 * (x**b14) + self.b1) % self.b3
        b9 = b14 * y
        b9 = self.fonk6(b9)
        b10 = (b8 * b9) % self.b3
        b11 = (b10**b14 - b14*x) % self.b3
        b12 = (b10 * (x - b11) - y) % self.b3
        return b11 , b12
    def fonk5(self, x, y, b13):
        b11, b12 = self.fonk4(x, y)
        b13 = b13 - b14
        while b13 != 0:
            b11, b12 = self.fonk3(x, y, b11, b12)
            b13 = b13 - 1
        return b11, b12
    def fonk6(self, A):
        return self.fonk7(A, self.b3 - b14)
    def fonk7(self, b16, b15):
        a1 = 1
        while b15 > 0:
            if b15 % b14 = = 1:
                a1 = (a1 * b16) % self.b3
            b15 = b15
            b16 = (b16 * b16) % self.b3
        return a1
def fonk8():
    b1 = int(input("Enter Alice'b10 private key: "))
    b2 = int(input("Enter Bob'b10 private key: "))
    b17 = class1(0, 0, 0, 0, 0)
    pbx, b18 = b17.fonk5(b17.b4, b17.b5, b2)
    pax, b19 = b17.fonk5(b17.b4, b17.b5, b1)
    b22, b20 = b17.fonk5(pax, b19, b2)
    sk_ax, b21 = b17.fonk5(pbx, b18, b1)
    if (b22 = = sk_ax) and (b20 == b21):
        print("Same keys generated.")
        print("Public key shared: ({}, {})".format(sk_ax, b21))
        print("Is point on curve?", b17.fonk2(sk_ax, b21))
        return sk_ax, b21
fonk8()