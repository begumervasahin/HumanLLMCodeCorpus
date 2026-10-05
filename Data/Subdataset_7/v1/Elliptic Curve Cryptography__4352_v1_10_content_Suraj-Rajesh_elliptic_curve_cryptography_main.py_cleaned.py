from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime
def fonk1():
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = GaloisField(103)
    for a in range(b5.p):
        for b in range(b5.p):
            b6 = EllipticCurve(a, b, 103)
            b7 = b6.order_of_curve()
            if is_prime(b7):
                b2.append(b7)
                b1.append((a, b))
    for i in range(10):
        b8 = max(b2)
        b9 = b2.index(b8)
        b4.append(b8)
        b3.append(b1[b9])
        del b2[b9]
        del b1[b9]
    for i in range(10):
        print("{} : {}".format(b3[i], b4[i]))
if b10 = = "__main__":
    fonk1()