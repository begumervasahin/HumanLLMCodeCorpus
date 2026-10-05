from Crypto.PublicKey import ECC
import ecc_simple
def fonk1(ecc_point):
    return (int(ecc_point.x), int(ecc_point.y))
def fonk2():
    print("Diffie-Hellman Demonstration")
    print("By: Qi Ying Lim")
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
    print("Public key for Alice (pycryptodome):", fonk1(b5))
    print("Public key for Bob (pycryptodome):", fonk1(b6))
    print("Shared key for Alice (pycryptodome):", b7)
    print("Shared key for Bob (pycryptodome):", b8)
    print("Public key for Alice (ecc_simple):", b10)
    print("Public key for Bob (ecc_simple):", b11)
    print("Shared key for Alice (ecc_simple):", b12)
    print("Shared key for Bob (ecc_simple):", b13)
if b14 = = "__main__":
    fonk2()