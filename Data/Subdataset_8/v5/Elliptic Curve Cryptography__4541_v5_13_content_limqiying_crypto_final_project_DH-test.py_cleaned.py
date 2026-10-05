from Crypto.PublicKey import ECC
import ecc_simple
def format_point(ecc_point):
    return (int(ecc_point.x), int(ecc_point.y))
def generate_key_pair(curve='P-256'):
    key = ECC.generate(curve=curve)
    private_key = key.d
    public_key = key.pointQ
    return private_key, public_key
def compute_shared_key(private_key, public_key):
    return format_point(public_key * private_key)
def main():
    print("Diffie-Hellman Demonstration")
    print("By: Qi Ying Lim")
    privateA, publicA = generate_key_pair()
    privateB, publicB = generate_key_pair()
    shared_keyA = compute_shared_key(privateA, publicB)
    shared_keyB = compute_shared_key(privateB, publicA)
    ecc_simple.set_p256_param()
    g = ecc_simple.g
    publicA_1 = ecc_simple.times(privateA, g)
    publicB_1 = ecc_simple.times(privateB, g)
    shared_keyA_1 = ecc_simple.times(privateA, publicB_1)
    shared_keyB_1 = ecc_simple.times(privateB, publicA_1)
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