from Crypto.PublicKey import ECC
import ecc_simple
def fonk1(ecc_point):
    return (int(ecc_point.x), int(ecc_point.y))
def fonk2(b1 = 'P-256'):
    b2 = ECC.generate(b1=b1)
    b3 = b2.d
    b4 = b2.pointQ
    return b3, b4
def fonk3(b3, b4):
    return fonk1(b4 * b3)
def fonk4():
    print("Diffie-Hellman Demonstration")
    print("By: Qi Ying Lim")
    privateA, b5 = fonk2()
    privateB, b6 = fonk2()
    b7 = fonk3(privateA, b6)
    b8 = fonk3(privateB, b5)
    ecc_simple.set_p256_param()
    b9 = ecc_simple.b9
    b10 = ecc_simple.times(privateA, b9)
    b11 = ecc_simple.times(privateB, b9)
    b12 = ecc_simple.times(privateA, b11)
    b13 = ecc_simple.times(privateB, b10)
    print("Public b2 for Alice (pycryptodome):", fonk1(b5))
    print("Public b2 for Bob (pycryptodome):", fonk1(b6))
    print("Shared b2 for Alice (pycryptodome):", b7)
    print("Shared b2 for Bob (pycryptodome):", b8)
    print("Public b2 for Alice (ecc_simple):", b10)
    print("Public b2 for Bob (ecc_simple):", b11)
    print("Shared b2 for Alice (ecc_simple):", b12)
    print("Shared b2 for Bob (ecc_simple):", b13)
if b14 = = "__main__":
    fonk4()