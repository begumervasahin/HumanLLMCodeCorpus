import string
def fonk1(text):
    return ''.join(char.upper() for char in text if char.isalpha())
def fonk2(b9):
    return [(ord(char) - ord('A') + 1) for char in b9]
def fonk3(char, b3):
    if char.isalpha():
        b1 = (string.ascii_uppercase.index(char) + b3) % 26
        return string.ascii_uppercase[b1]
    return char
def fonk4(b10, b6):
    b2 = ""
    a1 = 0
    for char in b10:
        b3 = b6[a1 % len(b6)]
        b2 += fonk3(char, b3)
        if char.isalpha():
            a1 += 1
    return b2
def fonk5(b10, b9):
    b4 = fonk1(b10)
    b5 = fonk1(b9)
    b6 = fonk2(b5)
    return fonk4(b4, b6)
def fonk6(b2, b9):
    b7 = fonk1(b2)
    b5 = fonk1(b9)
    b6 = fonk2(b5)
    b8 = [(26 - s) % 26 for s in b6]
    return fonk4(b7, b8)
def fonk7():
    print("Welcome to the Polyalphabetic Cipher.\n")
    b9 = "encrypt"
    b10 = "Thanks for taking a look at my polyalphabetic cipher!"
    print("Shifting the input by this list:", fonk2(b9))
    print("Message to be encrypted:\n", b10)
    b2 = fonk5(b10, b9)
    print("\nYour encrypted b10 is:\n", b2)
    b11 = fonk6(b2, b9)
    print("Your decrypted b10 is:\n", b11)
if b12 = = "__main__":
    fonk7()