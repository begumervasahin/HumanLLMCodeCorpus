import string
import secrets
def fonk1(b7, shift):
    b1 = ""
    a1 = 0
    for b2 in b7:
        for uppercase_letter in string.ascii_uppercase:
            if b2 = = uppercase_letter:
                b3 = string.ascii_uppercase.find(b2)
                if b3 + shift[a1] > 25:
                    b3 -= 26
                b4 = string.ascii_uppercase[b3 + shift[a1]]
                b1 += b4
                a1 += 1
    return b1
def fonk2(b1, shift):
    b5 = [26 - s for s in shift]
    b6 = fonk1(b1, b5)
    return b6
def fonk3():
    print("Welcome to the One-Time Pad Cipher.\n")
    b7 = "Thanks for taking a look at my one-time pad cipher!"
    b8 = string.punctuation + string.whitespace + string.digits
    b9 = str.maketrans({key: None for key in b8})
    b7 = b7.translate(b9)
    b10 = [secrets.randbelow(27) for _ in range(len(b7))]
    print("Shifting the input by this list:", b10)
    b11 = fonk1(b7.upper(), b10)
    print("\nYour encrypted b7 is:\n", b11, b12 = "")
    b13 = fonk2(b11, b10)
    print("Your decrypted b7 is:\n", b13, b12 = "")
if b14 = = "__main__":
    fonk3()