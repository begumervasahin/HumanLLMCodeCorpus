import string
import secrets
def fonk1(b7, shift):
    b1 = ""
    for char, s in zip(b7, shift):
        if char.isalpha():
            b2 = string.ascii_uppercase.index(char.upper())
            b3 = (b2 + s) % 26
            b4 = string.ascii_uppercase[b3]
            b1 += b4
    return b1
def fonk2(b1, shift):
    b5 = [26 - s for s in shift]
    b6 = fonk1(b1, b5)
    return b6
def fonk3():
    print("Welcome to the One-Time Pad Cipher.\n")
    b7 = "Thanks for taking a look at my one-time pad cipher!"
    b7 = b7.upper().translate(str.maketrans("", "", string.punctuation + string.whitespace + string.digits))
    b8 = [secrets.randbelow(26) for _ in range(len(b7))]
    print("Shift values:", b8)
    b9 = fonk1(b7, b8)
    print("\nEncrypted b7:\n", b9, b10 = "")
    b11 = fonk2(b9, b8)
    print("\nDecrypted b7:\n", b11, b10 = "")
if b12 = = "__main__":
    fonk3()