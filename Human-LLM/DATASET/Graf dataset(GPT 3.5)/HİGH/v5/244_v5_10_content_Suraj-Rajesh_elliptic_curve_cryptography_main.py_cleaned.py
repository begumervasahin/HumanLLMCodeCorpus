from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime
def fonk1(b10, b1 = 10):
    b2 = []
    b3 = []
    for a in range(b10.field.p):
        for b in range(b10.field.p):
            b4 = b10.order_of_curve(a, b)
            if is_prime(b4):
                b3.append(b4)
                b2.append((a, b))
    b5 = []
    b6 = []
    for _ in range(b1):
        b7 = max(b3)
        b8 = b3.index(b7)
        b6.append(b7)
        b5.append(b2[b8])
        del b3[b8]
        del b2[b8]
    return b5, b6
def fonk2():
    b9 = GaloisField(103)
    b10 = EllipticCurve(b9)
    b5, b6 = fonk1(b10)
    for i in range(10):
        print("{} : {}".format(b5[i], b6[i]))
if b11 = = "__main__":
    fonk2()