from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime
def fonk1(b1 = 10, a2=103):
    b2 = GaloisField(a2)
    b3 = []
    for a in range(b2.p):
        for b in range(b2.p):
            b4 = EllipticCurve(a, b, a2)
            b5 = b4.order_of_curve()
            if is_prime(b5):
                b3.append(((a, b), b5))
    b6 = sorted(b3, key=lambda x: x[1], reverse=True)[:b1]
    return b6
def fonk2(b8):
    for point, b5 in b8:
        print(f"Point (a, b): {point}, Order: {b5}")
if b7 = = "__main__":
    a1 = 10
    a2 = 103
    b8 = fonk1(a1, a2)
    fonk2(b8)