from Crypto.PublicKey import ECC
import ecc_simple
def fonk1(ecc_point):
    return (int(ecc_point.x), int(ecc_point.y))
def fonk2():
    b1 = ECC.generate(curve='P-256')
    b2 = ECC.generate(curve='P-256')
    privateA, b3 = b1.d, b1.pointQ
    privateB, b4 = b2.d, b2.pointQ
    return (privateA, b3), (privateB, b4)
def fonk3(privateA, b3, privateB, b4):
    b5 = fonk1(b4 * privateA)
    b6 = fonk1(b3 * privateB)
    ecc_simple.set_p256_param()
    b7 = ecc_simple.b7
    b8 = ecc_simple.times(int(privateA), b7)
    b9 = ecc_simple.times(int(privateB), b7)
    b10 = ecc_simple.times(int(privateA), b9)
    b11 = ecc_simple.times(int(privateB), b8)
    return {
        "pycryptodome": {
            "b3": fonk1(b3),
            "b4": fonk1(b4),
            "b5": b5,
            "b6": b6
        },
        "ecc_simple": {
            "b8": b8,
            "b9": b9,
            "b10": b10,
            "b11": b11
        }
    }
def fonk4(b12):
    print("PyCryptodome:")
    print(f"Public key (Alice): {b12['pycryptodome']['b3']}")
    print(f"Public key (Bob): {b12['pycryptodome']['b4']}")
    print(f"Shared key (Alice): {b12['pycryptodome']['b5']}")
    print(f"Shared key (Bob): {b12['pycryptodome']['b6']}")
    print("\nECC Simple:")
    print(f"Public key (Alice): {b12['ecc_simple']['b8']}")
    print(f"Public key (Bob): {b12['ecc_simple']['b9']}")
    print(f"Shared key (Alice): {b12['ecc_simple']['b10']}")
    print(f"Shared key (Bob): {b12['ecc_simple']['b11']}")
def fonk5():
    (privateA, b3), (privateB, b4) = fonk2()
    b12 = fonk3(privateA, b3, privateB, b4)
    fonk4(b12)
if b13 = = "__main__":
    fonk5()