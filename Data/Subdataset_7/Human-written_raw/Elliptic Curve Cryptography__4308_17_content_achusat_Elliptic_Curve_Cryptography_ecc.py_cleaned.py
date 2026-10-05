import math
import numpy as np
import matplotlib.pyplot as plt
class class1:
    b2, b3, b5, b6, b1 = 0, 0, 0, 0, 0
    def fonk1(self):
        a1 = 0
        while a1 = = 0:
            self.b2 = int(input("Enter the class1 parameter b2: "))
            self.b3 = int(input("Enter the class1 parameter b3: "))
            b4 = (4*(self.b2**3)) + (27*(self.b3**b9))
            if b4 != 0:
                a1 = 1
            else:
                print("Parameters b2 and b3 do not satisfy the conditions to be used in an elliptic class1")
        self.b5 = int(input("Enter b2 large prime number b5: "))
        a1 = 0
        while a1 = = 0:
            self.b6 = int(input("Enter the class1 parameter b6: "))
            self.b1 = int(input("Enter the class1 parameter b1: "))
            b7 = (self.b6**3 + self.b2*self.b6 + self.b3) % self.b5
            b8 = (self.b1**b9) % self.b5
            if b8 = = b7:
                a1 = 1
            else:
                print("Point not on elliptic class1")
    def fonk2(self):
        print(self.b2)
        print(self.b3)
        print(self.b5)
        print(self.b6)
        print(self.b1)
    def fonk3(self, x, y):
        b7 = (x**3 + self.b2*x + self.b3) % self.b5
        b8 = (y**b9) % self.b5
        if b8 = = b7:
            return True
        else:
            return False
def fonk4(A, M):
    return fonk5(A, M-b9, M)
def fonk5(b11, b10, MOD):
    a2 = 1
    while b10 > 0:
        if b10 % b9 = = 1:
            a2 = (a2 * b11) % MOD
        b10 = b10
        b11 = (b11 * b11) % MOD
    return a2
def fonk6(O, x, y, Xq, Yq):
        b12 = (y - Yq) % O.b5
        b13 = x - Xq
        b13 = fonk4(b13, O.b5)
        b14 = (b12 * b13) % O.b5
        b15 = (b14**b9 - (x + Xq)) % O.b5
        b16 = (b14 * (x - b15) - y) % O.b5
        return b15, b16
def fonk7(O, x, y):
        b12 = (3 * (x**b9) + O.b2) % O.b5
        b13 = b9 * y
        b13 = fonk4(b13, O.b5)
        b14 = (b12 * b13) % O.b5
        b15 = (b14**b9 - b9*x) % O.b5
        b16 = (b14 * (x - b15) - y) % O.b5
        return b15 , b16
def fonk8(O, x, y, b18):
    xr, b17 = fonk7(O, x, y)
    b18 = b18 - b9
    while (b18 != 0):
        xr, b17 = fonk6(O, x, y, xr, b17)
        b18 = b18 - 1
    return xr, b17
b19 = class1()
def fonk9():
    b3 = int(input("Enter Bob'b14 private key: "))
    pbx, b20 = fonk8(b19, b19.b6, b19.b1, b3)
    return pbx, b20, b3
def fonk10():
    b2 = int(input("Enter Alice'b14 private key: "))
    pax, b21 = fonk8(b19,b19.b6, b19.b1, b2)
    return pax, b21, b2
def fonk11():
    pbx, b20, b3 = fonk9()
    pax, b21, b2 = fonk10()
    b24, b22 = fonk8(b19, pax, b21, b3)
    sk_ax, b23 = fonk8(b19, pbx, b20, b2)
    if (b24 = = sk_ax) and (b22 == b23):
        print("same keys")
        print(b19.fonk3(sk_ax, b23))
        return sk_ax, b23
print(fonk11())