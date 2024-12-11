
import string
def fonk1(b7, b8):
    b1 = ""
    a1 = 0
    for char in b7:
        if char in string.ascii_uppercase:
            b2 = string.ascii_uppercase.find(char)
            b3 = (b2 + b8[a1]) % 26
            b1 += string.ascii_uppercase[b3]
            a1 = (a1 + 1) % len(b8)
        elif char in string.digits:
            b1 += char
        elif char in string.whitespace:
            b1 += char
    return b1
def fonk2(b1, b8):
    b4 = ""
    b5 = [(26 - s) % 26 for s in b8]
    for char in b1:
        if char in string.ascii_uppercase:
            b2 = string.ascii_uppercase.find(char)
            b3 = (b2 + b5[0]) % 26
            b4 += string.ascii_uppercase[b3]
            b5.append(b5.pop(0))
        else:
            b4 += char
    return b4
def fonk3():
    print("Welcome to the Polyalphabetic Cipher.\n")
    b6 = "encrypt"
    b7 = "Thanks for taking a look at my polyalphabetic cipher!"
    b6 = b6.translate(str.maketrans('', '', string.punctuation + string.whitespace))
    b8 = [(string.ascii_uppercase.find(char) + 1) for char in b6.upper()]
    b7 = b7.translate(str.maketrans('', '', string.punctuation))
    print("Shifting the input by this list:", b8)
    print("Message to be encrypted:\n", b7, b9 = "")
    b1 = fonk1(b7.upper(), b8)
    print("\nYour encrypted b7 is:\n", b1, b9 = "")
    b4 = fonk2(b1, b8)
    print("Your decrypted b7 is:\n", b4, b9 = "")
fonk3()