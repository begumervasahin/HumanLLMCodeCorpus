import os
from toyecc import getcurvebyname, ECPrivateKey
b1 = getcurvebyname("secp521r1")
def fonk1(b1, b13, msg_width_bits):
    b2 = int.from_bytes(b13, byteorder="little")
    for i in range(100):
        b3 = b2 | (i << msg_width_bits)
        b4 = b1.getpointwithx(b3)
        if b4:
            b4 = b4[0]
            break
    return i + 1, b4
def fonk2(b17, b13, msg_width_bits):
    b5 = ECPrivateKey.generate(b1)
    b6 = b5.pubkey
    b7 = b5.scalar
    b8 = b6.b4
    b9 = b7 * b17.b4
    trials, b10 = fonk1(b1, b13, msg_width_bits=msg_width_bits)
    b11 = (b8, b9 + b10)
    return b11
def fonk3(b16, b11, msg_width_bits):
    b8, b9 = b11
    b12 = b8 * b16.scalar
    b10 = b9 + (-b12)
    b2 = int(b10.x) & ((1 << msg_width_bits) - 1)
    b13 = int.to_bytes(b2, byteorder="little", length=(msg_width_bits + 7)
    return b13
b14 = ECPrivateKey.generate(b1)
b15 = b14.pubkey
b16 = ECPrivateKey.generate(b1)
b17 = b16.pubkey
b18 = b"foobar"
print("Message:", b18)
b11 = fonk2(b17, b18, msg_width_bits=256)
print("Ciphertext:")
print("    b8 = ", b11[0])
print("    b9 = ", b11[1])
b19 = fonk3(b16, b11, msg_width_bits=256)
print("Plaintext:", b19)