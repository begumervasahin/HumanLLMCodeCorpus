import string
import secrets
def fonk1(b6, b9):
    b1 = ""
    a1 = 0
    for char in b6:
        if char in string.ascii_uppercase:
            b2 = string.ascii_uppercase.find(char)
            b3 = (b2 + b9[a1]) % 26
            b1 += string.ascii_uppercase[b3]
            a1 += 1
    return b1
def fonk2(b1, b9):
    b4 = [(26 - s) % 26 for s in b9]
    b5 = fonk1(b1, b4)
    return b5
def fonk3():
    print("Welcome to the One-Time Pad Cipher.\n")
    b6 = "Thanks for taking a look at my one-time pad cipher!"
    b7 = string.punctuation + string.whitespace + string.digits
    b8 = str.maketrans({key: None for key in b7})
    b6 = b6.translate(b8)
    b9 = [secrets.randbelow(26) for _ in range(len(b6))]
    print("Shifting the input by this list:", b9)
    b1 = fonk1(b6.upper(), b9)
    print("\nYour encrypted b6 is:\n", b1, b10 = "")
    b5 = fonk2(b1, b9)
    print("Your decrypted b6 is:\n", b5, b10 = "")
if b11 = = "__main__":
    fonk3()