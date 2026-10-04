import os
from toyecc import getcurvebyname, ECPrivateKey
def fonk1():
    b1 = getcurvebyname("secp521r1")
    def fonk2(b1, b11, msg_width_bits):
        b2 = int.from_bytes(b11, byteorder="little")
        for i in range(100):
            b3 = b2 | (i << msg_width_bits)
            b4 = b1.getpointwithx(b3)
            if b4:
                return i + 1, b4[0]
        return None
    def fonk3(recipient_pubkey, b11, msg_width_bits):
        b5 = ECPrivateKey.generate(b1)
        b6 = b5.b13.b4
        b7 = b5.scalar * recipient_pubkey.b4
        trials, b8 = fonk2(b1, b11, msg_width_bits)
        b9 = (b6, b7 + b8)
        return b9
    def fonk4(recipient_privkey, b9, msg_width_bits):
        b6, b7 = b9
        b10 = b6 * recipient_privkey.scalar
        b8 = b7 + (-b10)
        b2 = int(b8.x) & ((1 << msg_width_bits) - 1)
        b11 = b2.to_bytes((msg_width_bits + 7)
        return b11
    b12 = ECPrivateKey.generate(b1)
    b13 = b12.b13
    b14 = b"foobar"
    print("Message:", b14)
    b9 = fonk3(b13, b14, msg_width_bits=256)
    print("Ciphertext:")
    print("    b6 = ", b9[0])
    print("    b7 = ", b9[1])
    b15 = fonk4(b12, b9, msg_width_bits=256)
    print("Plaintext:", b15)
if b16 = = "__main__":
    fonk1()