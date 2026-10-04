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
    for _ in range(n - 1):
        xr, yr = point_addition(curve, xr, yr, x, y)
    return xr, yr
def get_private_key(name):
    return int(input(f"Enter {name}'s private key: "))
def generate_key_pair(curve, private_key):
    return scalar_multiplication(curve, curve.Gx, curve.Gy, private_key)
def key_exchange(curve):
    bob_private_key = get_private_key("Bob")
    bob_public_key = generate_key_pair(curve, bob_private_key)
    alice_private_key = get_private_key("Alice")
    alice_public_key = generate_key_pair(curve, alice_private_key)
    shared_key_bob = scalar_multiplication(curve, alice_public_key[0], alice_public_key[1], bob_private_key)
    shared_key_alice = scalar_multiplication(curve, bob_public_key[0], bob_public_key[1], alice_private_key)
    if shared_key_bob == shared_key_alice:
        print("Same keys")
        if curve.is_point_on_curve(shared_key_bob[0], shared_key_bob[1]):
            print("The key is valid on the curve.")
        return shared_key_bob
    else:
        print("Key exchange failed.")
        return None
if __name__ == "__main__":
    curve = EllipticCurve()
    print("Elliptic Curve Parameters:")
    curve.show_parameters()
    print("Key Exchange Result:")
    key = key_exchange(curve)
    if key:
        print(f"Shared Key: {key}")