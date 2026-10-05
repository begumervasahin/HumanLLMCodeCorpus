from Crypto.PublicKey import ECC
import ecc_simple
def format_point(ecc_point):
    return (int(ecc_point.x), int(ecc_point.y))
def main():
    print("Diffie-Hellman Demonstration")
    print("By: Qi Ying Lim")
    keyA = ECC.generate(curve='P-256')
    keyB = ECC.generate(curve='P-256')
    privateA = keyA.d
    privateB = keyB.d
    publicA = keyA.pointQ
    publicB = keyB.pointQ
    shared_keyA = format_point(publicB * privateA)
    shared_keyB = format_point(publicA * privateB)
    ecc_simple.set_p256_param()
    g = ecc_simple.g
    publicA_1 = ecc_simple.times(int(privateA), g)
    publicB_1 = ecc_simple.times(int(privateB), g)
    shared_keyA_1 = ecc_simple.times(int(privateA), publicB_1)
    shared_keyB_1 = ecc_simple.times(int(privateA), publicB_1)
    print("Public key for Alice (pycryptodome):", format_point(publicA))
    print("Public key for Bob (pycryptodome):", format_point(publicB))
    print("Shared key for Alice (pycryptodome):", shared_keyA)
    print("Shared key for Bob (pycryptodome):", shared_keyB)
    print("Public key for Alice (ecc_simple):", publicA_1)
    print("Public key for Bob (ecc_simple):", publicB_1)
    print("Shared key for Alice (ecc_simple):", shared_keyA_1)
    print("Shared key for Bob (ecc_simple):", shared_keyB_1)
if __name__ == "__main__":
    main()