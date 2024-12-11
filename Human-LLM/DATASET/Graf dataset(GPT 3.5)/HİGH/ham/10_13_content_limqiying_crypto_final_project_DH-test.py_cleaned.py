from Crypto.PublicKey import ECC
import ecc_simple
def fonk1(eccPoint):
    return (int(eccPoint.x),int(eccPoint.y))
b1 = ECC.generate(curve='P-256')
b2 = ECC.generate(curve='P-256')
b3 = b1.d
b4 = b2.d
b5 = b1.pointQ
b6 = b2.pointQ
b7 = fonk1(b6 * b3)
b8 = fonk1(b5 * b4)
ecc_simple.set_p256_param()
b9 = ecc_simple.b9
b10 = ecc_simple.times(int(b3), b9)
b11 = ecc_simple.times(int(b4), b9)
b12 = ecc_simple.times(int(b3), b11)
b13 = ecc_simple.times(int(b3), b11)
print b10