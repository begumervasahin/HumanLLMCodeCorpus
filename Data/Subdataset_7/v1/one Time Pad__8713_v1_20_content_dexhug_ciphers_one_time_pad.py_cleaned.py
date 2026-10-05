import string
import secrets
def fonk1(b7, b10):
    b1 = ""
    a1 = 0
    for b2 in b7:
        for j in string.ascii_uppercase:
            if b2 = = j:
                b3 = string.ascii_uppercase.find(b2)
                if b3 + b10[a1] > 25:
                    b3 -= 26
                b4 = string.ascii_uppercase[b3+b10[a1]]
                b1 += b4
                a1 += 1
    return b1
def fonk2(b1, b10):
    b5 = []
    for b2 in range(len(b10)):
        b5.append(26 - b10[b2])
    b6 = fonk1(b1, b5)
    return b6
def fonk3():
    print("Welcome to the One Time Pad Cipher.\n")
    b7 = "Thanks for taking a look at my one time pad cipher!"
    b8 = string.punctuation + string.whitespace + string.digits
    b9 = str.maketrans({key: None for key in b8})
    b7 = b7.translate(b9)
    b10 = []
    for b2 in range(len(b7)):
        b10.append(secrets.randbelow(27))
    print("Shifting the input by this list:", b10)
    b1 = fonk1(b7.upper(), b10)
    print("\nYour encrypted b7 is:\n", b1, b11 = "")
    b6 = fonk2(b1, b10)
    print("Your decrypted b7 is:\n", b6, b11 = "")
if b12 = = "__main__":
    fonk3()