from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime
def fonk1(b1 = 10, a2=103):
    b2 = []
    b3 = GaloisField(a2)
    for a in range(b3.p):
        for b in range(b3.p):
            b4 = EllipticCurve(a, b, a2)
            b5 = b4.order_of_curve()
            if is_prime(b5):
                b2.append(((a, b), b5))
    b2.sort(b6 = lambda x: x[1], reverse=True)
    b7 = b2[:b1]
    return b7
if b8 = = "__main__":
    a1 = 10
    a2 = 103
    b9 = fonk1(a1, a2)
    for point, b5 in b9:
        print(f"{point} : {b5}")