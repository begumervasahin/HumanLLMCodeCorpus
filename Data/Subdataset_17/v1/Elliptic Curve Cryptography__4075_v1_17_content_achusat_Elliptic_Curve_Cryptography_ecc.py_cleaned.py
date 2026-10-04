import math
import numpy as np
import matplotlib.pyplot as plt
class EllipticCurve:
    def __init__(self):
        self.a, self.b, self.p, self.Gx, self.Gy = self.get_curve_parameters()
    def get_curve_parameters(self):
        while True:
            a = int(input("Enter the curve parameter a: "))
            b = int(input("Enter the curve parameter b: "))
            if 4 * a**3 + 27 * b**2 != 0:
                break
            else:
                print("Parameters a and b do not satisfy the conditions to be used in an elliptic curve.")
        p = int(input("Enter a large prime number p: "))
        while True:
            Gx = int(input("Enter the curve parameter Gx: "))
            Gy = int(input("Enter the curve parameter Gy: "))
            if (Gy**2 % p) == ((Gx**3 + a * Gx + b) % p):
                break
            else:
                print("Point not on elliptic curve.")
        return a, b, p, Gx, Gy
    def show_parameters(self):
        print(f"a: {self.a}")
        print(f"b: {self.b}")
        print(f"p: {self.p}")
        print(f"Gx: {self.Gx}")
        print(f"Gy: {self.Gy}")
    def is_point_on_curve(self, x, y):
        return (y**2 % self.p) == ((x**3 + self.a * x + self.b) % self.p)
def modulo_multiplicative_inverse(A, M):
    return fast_power(A, M - 2, M)
def fast_power(base, power, MOD):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % MOD
        power
        base = (base * base) % MOD
    return result
def point_addition(curve, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return point_doubling(curve, x1, y1)
    sn = (y2 - y1) % curve.p
    sd = modulo_multiplicative_inverse(x2 - x1, curve.p)
    s = (sn * sd) % curve.p
    xr = (s**2 - x1 - x2) % curve.p
    yr = (s * (x1 - xr) - y1) % curve.p
    return xr, yr
def point_doubling(curve, x, y):
    sn = (3 * x**2 + curve.a) % curve.p
    sd = modulo_multiplicative_inverse(2 * y, curve.p)
    s = (sn * sd) % curve.p
    xr = (s**2 - 2 * x) % curve.p
    yr = (s * (x - xr) - y) % curve.p
    return xr, yr
def scalar_multiplication(curve, x, y, n):
    xr, yr = x, y
    n -= 1
    while n > 0:
        xr, yr = point_addition(curve, xr, yr, x, y)
        n -= 1
    return xr, yr
def bob(curve):
    b = int(input("Enter Bob's private key: "))
    pbx, pby = scalar_multiplication(curve, curve.Gx, curve.Gy, b)
    return pbx, pby, b
def alice(curve):
    a = int(input("Enter Alice's private key: "))
    pax, pay = scalar_multiplication(curve, curve.Gx, curve.Gy, a)
    return pax, pay, a
def key_exchange(curve):
    pbx, pby, b = bob(curve)
    pax, pay, a = alice(curve)
    sk_bx, sk_by = scalar_multiplication(curve, pax, pay, b)
    sk_ax, sk_ay = scalar_multiplication(curve, pbx, pby, a)
    if sk_bx == sk_ax and sk_by == sk_ay:
        print("Same keys")
        if curve.is_point_on_curve(sk_ax, sk_ay):
            print("The key is valid on the curve.")
        return sk_ax, sk_ay
    else:
        print("Key exchange failed.")
if __name__ == "__main__":
    curve = EllipticCurve()
    print("Elliptic Curve Parameters:")
    curve.show_parameters()
    print("Key Exchange Result:")
    print(key_exchange(curve))