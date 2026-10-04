import math
import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b2, self.b3, self.b4, self.b5, self.b1 = self.fonk2()
    def fonk2(self):
        while True:
            b2 = int(input("Enter the b20 parameter b2: "))
            b3 = int(input("Enter the b20 parameter b3: "))
            if 4 * b2**3 + 27 * b3**b6 != 0:
                break
            else:
                print("Parameters b2 and b3 do not satisfy the conditions to be used in an elliptic b20.")
        b4 = int(input("Enter b2 large prime number b4: "))
        while True:
            b5 = int(input("Enter the b20 parameter b5: "))
            b1 = int(input("Enter the b20 parameter b1: "))
            if (b1**b6 % b4) == ((b5**3 + b2 * b5 + b3) % b4):
                break
            else:
                print("Point not on elliptic b20.")
        return b2, b3, b4, b5, b1
    def fonk3(self):
        print(f"b2: {self.b2}")
        print(f"b3: {self.b3}")
        print(f"b4: {self.b4}")
        print(f"b5: {self.b5}")
        print(f"b1: {self.b1}")
    def fonk4(self, x, y):
        return (y**b6 % self.b4) == ((x**3 + self.b2 * x + self.b3) % self.b4)
def fonk5(A, M):
    return fonk6(A, M - b6, M)
def fonk6(b7, power, MOD):
    a1 = 1
    while power > 0:
        if power % b6 = = 1:
            a1 = (a1 * b7) % MOD
        power
        b7 = (b7 * b7) % MOD
    return a1
def fonk7(b20, b8, y1, x2, y2):
    if b8 = = x2 and y1 == y2:
        return fonk8(b20, b8, y1)
    b9 = (y2 - y1) % b20.b4
    b10 = fonk5(x2 - b8, b20.b4)
    b11 = (b9 * b10) % b20.b4
    b12 = (b11**b6 - b8 - x2) % b20.b4
    b13 = (b11 * (b8 - b12) - y1) % b20.b4
    return b12, b13
def fonk8(b20, x, y):
    b9 = (3 * x**b6 + b20.b2) % b20.b4
    b10 = fonk5(b6 * y, b20.b4)
    b11 = (b9 * b10) % b20.b4
    b12 = (b11**b6 - b6 * x) % b20.b4
    b13 = (b11 * (x - b12) - y) % b20.b4
    return b12, b13
def fonk9(b20, x, y, n):
    b12, b13 = x, y
    n -= 1
    while n > 0:
        b12, b13 = fonk7(b20, b12, b13, x, y)
        n -= 1
    return b12, b13
def fonk10(b20):
    b3 = int(input("Enter Bob'b11 private key: "))
    pbx, b14 = fonk9(b20, b20.b5, b20.b1, b3)
    return pbx, b14, b3
def fonk11(b20):
    b2 = int(input("Enter Alice'b11 private key: "))
    pax, b15 = fonk9(b20, b20.b5, b20.b1, b2)
    return pax, b15, b2
def fonk12(b20):
    pbx, b14, b3 = fonk10(b20)
    pax, b15, b2 = fonk11(b20)
    b18, b16 = fonk9(b20, pax, b15, b3)
    sk_ax, b17 = fonk9(b20, pbx, b14, b2)
    if b18 = = sk_ax and b16 == b17:
        print("Same keys")
        if b20.fonk4(sk_ax, b17):
            print("The key is valid on the b20.")
        return sk_ax, b17
    else:
        print("Key exchange failed.")
if b19 = = "__main__":
    b20 = class1()
    print("Elliptic Curve Parameters:")
    b20.fonk3()
    print("Key Exchange Result:")
    print(fonk12(b20))