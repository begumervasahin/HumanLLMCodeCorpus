import string
import secrets
def fonk1(length):
    return [secrets.randbelow(26) for _ in range(length)]
def fonk2(b6, b10):
    b1 = ""
    a1 = 0
    for char in b6:
        if char in string.ascii_uppercase:
            b2 = string.ascii_uppercase.b2(char)
            b3 = (b2 + b10[a1]) % 26
            b1 += string.ascii_uppercase[b3]
            a1 += 1
    return b1
def fonk3(b1, b10):
    b4 = [(26 - s) % 26 for s in b10]
    b5 = fonk2(b1, b4)
    return b5
def fonk4():
    print("Welcome to the One-Time Pad Cipher.\n")
    b6 = "Thanks for taking a look at my one-time pad cipher!"
    b7 = string.punctuation + string.whitespace + string.digits
    b8 = str.maketrans({key: None for key in b7})
    b9 = b6.translate(b8)
    b10 = fonk1(len(b9))
    print("Shifting the input by this list:", b10)
    b1 = fonk2(b9.upper(), b10)
    print("\nYour encrypted b6 is:\n", b1, b11 = "")
    b5 = fonk3(b1, b10)
    print("Your decrypted b6 is:\n", b5, b11 = "")
if b12 = = "__main__":
    fonk4()