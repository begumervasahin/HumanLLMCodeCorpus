from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime
def fonk1(b1 = 10, a2=103):
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = GaloisField(a2)
    for a in range(b6.p):
        for b in range(b6.p):
            b7 = EllipticCurve(a, b, a2)
            b8 = b7.order_of_curve()
            if is_prime(b8):
                b3.append(b8)
                b2.append((a, b))
    for _ in range(b1):
        if not b3:
            break
        b9 = max(b3)
        b10 = b3.index(b9)
        b5.append(b9)
        b4.append(b2[b10])
        del b3[b10]
        del b2[b10]
    return list(zip(b4, b5))
if b11 = = "__main__":
    a1 = 10
    a2 = 103
    b12 = fonk1(a1, a2)
    for point, b8 in b12:
        print(f"{point} : {b8}")