import string
def fonk1(b6, b7):
    b1 = ""
    a1 = 0
    for char in b6:
        if char.isalpha():
            b2 = (string.ascii_uppercase.index(char) + b7[a1]) % 26
            b3 = string.ascii_uppercase[b2]
            b1 += b3
            a1 = (a1 + 1) % len(b7)
        else:
            b1 += char
    return b1
def fonk2(b1, b7):
    b4 = [(26 - s) % 26 for s in b7]
    return fonk1(b1, b4)
def fonk3():
    print("Welcome to the Polyalphabetic Cipher.\n")
    b5 = "encrypt"
    b6 = "Thanks for taking a look at my polyalphabetic cipher!"
    b5 = ''.join(char.upper() for char in b5 if char.isalpha())
    b6 = ''.join(char.upper() for char in b6 if char.isalpha())
    b7 = [(ord(char) - ord('A') + 1) for char in b5]
    print("Shifting the input by this list:", b7)
    print("Message to be encrypted:\n", b6)
    b1 = fonk1(b6, b7)
    print("\nYour encrypted b6 is:\n", b1)
    b8 = fonk2(b1, b7)
    print("Your decrypted b6 is:\n", b8)
if b9 = = "__main__":
    fonk3()