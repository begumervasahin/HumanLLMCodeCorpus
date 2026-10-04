
import random
b1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def fonk1():
    b2 = "Once more into the fray."
    b5, b3 = fonk2(b2)
    b4 = fonk3(b5, b3)
    print(f"Test Vector: {b2}")
    print(f"OTP: {b5}")
    print(f"Encrypted: {b3}")
    print(f"Decrypted: {b4}")
def fonk2(plaintext):
    b5 = "".join(random.sample(b1, len(b1)))
    b6 = "".join(b5[b1.find(c)] for c in plaintext.upper() if c in b1)
    return b5, b6
def fonk3(b5, secret):
    b6 = "".join(b1[b5.find(c)] for c in secret.upper() if c in b5)
    return b6
if b7 = = "__main__":
    fonk1()