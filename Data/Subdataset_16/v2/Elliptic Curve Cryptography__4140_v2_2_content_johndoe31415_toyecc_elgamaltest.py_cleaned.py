import os
from toyecc import getcurvebyname, ECPrivateKey
def fonk1(b11, b10, msg_width_bits):
    b1 = int.from_bytes(b10, byteorder="little")
    for i in range(100):
        b2 = b1 | (i << msg_width_bits)
        b3 = b11.getpointwithx(b2)
        if b3:
            return i + 1, b3[0]
    return None
def fonk2(b11, recipient_pubkey, b10, msg_width_bits):
    b4 = ECPrivateKey.generate(b11)
    b5 = b4.b13.b3
    b6 = b4.scalar * recipient_pubkey.b3
    trials, b7 = fonk1(b11, b10, msg_width_bits)
    b8 = (b5, b6 + b7)
    return b8
def fonk3(b11, recipient_privkey, b8, msg_width_bits):
    b5, b6 = b8
    b9 = b5 * recipient_privkey.scalar
    b7 = b6 + (-b9)
    b1 = int(b7.x) & ((1 << msg_width_bits) - 1)
    b10 = b1.to_bytes((msg_width_bits + 7)
    return b10
def fonk4():
    b11 = getcurvebyname("secp521r1")
    b12 = ECPrivateKey.generate(b11)
    b13 = b12.b13
    b14 = b"foobar"
    print("Message:", b14)
    b8 = fonk2(b11, b13, b14, msg_width_bits=256)
    print("Ciphertext:")
    print("    b5 = ", b8[0])
    print("    b6 = ", b8[1])
    b15 = fonk3(b11, b12, b8, msg_width_bits=256)
    print("Plaintext:", b15)
if b16 = = "__main__":
    fonk4()