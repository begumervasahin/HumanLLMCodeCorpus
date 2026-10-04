import random
b1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def fonk1():
    b2 = "Once more into the fray."
    b3 = fonk2(b2)
    b4 = fonk3(b3[0], b3[1])
    print("Test Vector: " + b2)
    print("OTP: " + b3[0])
    print("Encrypted: " + b3[1])
    print("Decrypted: " + b4)
def fonk2(plaintext):
    b5 = "".join(random.sample(b1, len(b1)))
    b6 = ""
    for c in plaintext.upper():
        if c not in b5:
            continue
        else:
            b6 += b5[b1.find(c)]
    return b5, b6
def fonk3(b5, secret):
    b6 = ""
    for c in secret.upper():
        if c not in b5:
            continue
        else:
            b6 += b1[b5.find(c)]
    return b6
if b7 = = "__main__":
    fonk1()