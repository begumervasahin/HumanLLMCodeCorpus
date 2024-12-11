import os
from toyecc import getcurvebyname, ECPrivateKey
def fonk1(b4, b11, msg_width_bits):
    b1 = int.from_bytes(b11, byteorder="little")
    for i in range(100):
        b2 = b1 | (i << msg_width_bits)
        b3 = b4.getpointwithx(b2)
        if b3:
            b3 = b3[0]
            break
    return i + 1, b3
def fonk2(recipient_pubkey, b11, msg_width_bits):
    b4 = recipient_pubkey.b4
    b5 = ECPrivateKey.generate(b4)
    b6 = b5.b13.b3
    b7 = b5.scalar * recipient_pubkey.b3
    trials, b8 = fonk1(b4, b11, msg_width_bits=msg_width_bits)
    b9 = b6, b7 + b8
    return b9
def fonk3(recipient_privkey, b9, msg_width_bits):
    b4 = recipient_privkey.b4
    b6, b7 = b9
    b10 = b6 * recipient_privkey.scalar
    b8 = b7 + (-b10)
    b1 = int(b8.x) & ((1 << msg_width_bits) - 1)
    b11 = int.to_bytes(b1, byteorder="little", length=(msg_width_bits + 7)
    return b11
b4 = getcurvebyname("secp521r1")
b12 = ECPrivateKey.generate(b4)
b13 = b12.b13
b14 = b"foobar"
print("Message:", b14)
b9 = fonk2(b13, b14, msg_width_bits=256)
print("Ciphertext:")
print("    b6 = ", b9[0])
print("    b7 = ", b9[1])
b15 = fonk3(b12, b9, msg_width_bits=256)
print("Plaintext:", b15)