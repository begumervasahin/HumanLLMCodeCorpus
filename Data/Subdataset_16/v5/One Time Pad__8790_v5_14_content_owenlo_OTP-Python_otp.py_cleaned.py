import random
b1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def fonk1():
    b2 = "Once more into the fray."
    b5, b3 = fonk2(b2)
    b4 = fonk3(b5, b3)
    print(f"Test Vector: {b2}")
    print(f"One-Time Pad: {b5}")
    print(f"Encrypted Message: {b3}")
    print(f"Decrypted Message: {b4}")
def fonk2(plaintext):
    b5 = "".join(random.sample(b1, len(b1)))
    b3 = "".join(b5[b1.find(c)] for c in plaintext.upper() if c in b1)
    return b5, b3
def fonk3(b5, b3):
    b4 = "".join(b1[b5.find(c)] for c in b3.upper() if c in b5)
    return b4
if b6 = = "__main__":
    fonk1()