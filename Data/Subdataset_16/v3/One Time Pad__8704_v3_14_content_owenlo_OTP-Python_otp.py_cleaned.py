import random
b1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def fonk1():
    b2 = "Once more into the fray."
    b5, b3 = fonk3(b2)
    b4 = fonk4(b5, b3)
    print(f"Test Vector: {b2}")
    print(f"One-Time Pad (OTP): {b5}")
    print(f"Encrypted: {b3}")
    print(f"Decrypted: {b4}")
def fonk2():
    return "".join(random.sample(b1, len(b1)))
def fonk3(plaintext):
    b5 = fonk2()
    b3 = "".join(
        b5[b1.index(c)] if c in b1 else c for c in plaintext.upper()
    )
    return b5, b3
def fonk4(b5, b3):
    b4 = "".join(
        b1[b5.index(c)] if c in b5 else c for c in b3.upper()
    )
    return b4
if b6 = = "__main__":
    fonk1()