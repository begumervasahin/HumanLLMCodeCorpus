from Crypto.PublicKey import ECC
import ecc_simple
def format_ecc_point(ecc_point):
    return (int(ecc_point.x), int(ecc_point.y))
def generate_keys():
    keyA = ECC.generate(curve='P-256')
    keyB = ECC.generate(curve='P-256')
    privateA, publicA = keyA.d, keyA.pointQ
    privateB, publicB = keyB.d, keyB.pointQ
    return (privateA, publicA), (privateB, publicB)
def compute_shared_keys(privateA, publicA, privateB, publicB):
    shared_keyA = format_ecc_point(publicB * privateA)
    shared_keyB = format_ecc_point(publicA * privateB)
    ecc_simple.set_p256_param()
    g = ecc_simple.g
    publicA_1 = ecc_simple.times(int(privateA), g)
    publicB_1 = ecc_simple.times(int(privateB), g)
    shared_keyA_1 = ecc_simple.times(int(privateA), publicB_1)
    shared_keyB_1 = ecc_simple.times(int(privateB), publicA_1)
    return {
        "pycryptodome": {
            "publicA": format_ecc_point(publicA),
            "publicB": format_ecc_point(publicB),
            "shared_keyA": shared_keyA,
            "shared_keyB": shared_keyB
        },
        "ecc_simple": {
            "publicA_1": publicA_1,
            "publicB_1": publicB_1,
            "shared_keyA_1": shared_keyA_1,
            "shared_keyB_1": shared_keyB_1
        }
    }
def display_results(keys_and_secrets):
    print("PyCryptodome:")
    print(f"Public key (Alice): {keys_and_secrets['pycryptodome']['publicA']}")
    print(f"Public key (Bob): {keys_and_secrets['pycryptodome']['publicB']}")
    print(f"Shared key (Alice): {keys_and_secrets['pycryptodome']['shared_keyA']}")
    print(f"Shared key (Bob): {keys_and_secrets['pycryptodome']['shared_keyB']}")
    print("\nECC Simple:")
    print(f"Public key (Alice): {keys_and_secrets['ecc_simple']['publicA_1']}")
    print(f"Public key (Bob): {keys_and_secrets['ecc_simple']['publicB_1']}")
    print(f"Shared key (Alice): {keys_and_secrets['ecc_simple']['shared_keyA_1']}")
    print(f"Shared key (Bob): {keys_and_secrets['ecc_simple']['shared_keyB_1']}")
def main():
    (privateA, publicA), (privateB, publicB) = generate_keys()
    keys_and_secrets = compute_shared_keys(privateA, publicA, privateB, publicB)
    display_results(keys_and_secrets)
if __name__ == "__main__":
    main()