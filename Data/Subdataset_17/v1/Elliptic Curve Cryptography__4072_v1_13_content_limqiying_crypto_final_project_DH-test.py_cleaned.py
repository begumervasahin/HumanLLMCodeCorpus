from Crypto.PublicKey import ECC
import ecc_simple
def format_ecc_point(ecc_point):
    return (int(ecc_point.x), int(ecc_point.y))
def main():
    keyA = ECC.generate(curve='P-256')
    keyB = ECC.generate(curve='P-256')
    privateA = keyA.d
    privateB = keyB.d
    publicA = keyA.pointQ
    publicB = keyB.pointQ
    shared_keyA = format_ecc_point(publicB * privateA)
    shared_keyB = format_ecc_point(publicA * privateB)
    print("Shared key (pycryptodome) - Alice:", shared_keyA)
    print("Shared key (pycryptodome) - Bob:", shared_keyB)
    ecc_simple.set_p256_param()
    g = ecc_simple.g
    publicA_1 = ecc_simple.times(int(privateA), g)
    publicB_1 = ecc_simple.times(int(privateB), g)
    shared_keyA_1 = ecc_simple.times(int(privateA), publicB_1)
    shared_keyB_1 = ecc_simple.times(int(privateB), publicA_1)
    print("Shared key (ecc_simple) - Alice:", shared_keyA_1)
    print("Shared key (ecc_simple) - Bob:", shared_keyB_1)
    print("Public key (ecc_simple) - Alice:", publicA_1)
    print("Public key (ecc_simple) - Bob:", publicB_1)
if __name__ == "__main__":
    main()