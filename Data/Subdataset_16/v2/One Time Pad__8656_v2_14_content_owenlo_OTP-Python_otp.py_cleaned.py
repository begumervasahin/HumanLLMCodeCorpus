import random
b1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def fonk1():
    b2 = "Once more into the fray."
    encrypted_otp, b3 = fonk2(b2)
    b4 = fonk3(encrypted_otp, b3)
    print("Test Vector: " + b2)
    print("OTP: " + encrypted_otp)
    print("Encrypted: " + b3)
    print("Decrypted: " + b4)
def fonk2(plaintext):
    b5 = "".join(random.sample(b1, len(b1)))
    b6 = ""
    for c in plaintext.upper():
        if c in b1:
            b6 += b5[b1.index(c)]
        else:
            b6 += c
    return b5, b6
def fonk3(b5, secret):
    b6 = ""
    for c in secret.upper():
        if c in b5:
            b6 += b1[b5.index(c)]
        else:
            b6 += c
    return b6
if b7 = = "__main__":
    fonk1()