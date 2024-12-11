import string
def fonk1(b7, b6):
    b1 = ""
    b2 = [string.ascii_uppercase.find(char) + 1 for char in b6.upper()]
    a1 = 0
    for char in b7:
        if char in string.ascii_uppercase:
            b3 = string.ascii_uppercase.find(char)
            b4 = (b3 + b2[a1]) % 26
            b1 += string.ascii_uppercase[b4]
            a1 = (a1 + 1) % len(b2)
        else:
            b1 += char
    return b1
def fonk2(b1, b6):
    b5 = ""
    b2 = [(26 - string.ascii_uppercase.find(char)) % 26 for char in b6.upper()]
    a1 = 0
    for char in b1:
        if char in string.ascii_uppercase:
            b3 = string.ascii_uppercase.find(char)
            b4 = (b3 + b2[a1]) % 26
            b5 += string.ascii_uppercase[b4]
            a1 = (a1 + 1) % len(b2)
        else:
            b5 += char
    return b5
def fonk3():
    print("Welcome to the Polyalphabetic Cipher.\n")
    b6 = "encrypt"
    b7 = "Thanks for taking a look at my polyalphabetic cipher!"
    b6 = b6.translate(str.maketrans('', '', string.punctuation + string.whitespace))
    b7 = b7.translate(str.maketrans('', '', string.punctuation))
    print("Shifting the input by this word:", b6)
    print("Message to be encrypted:\n", b7, b8 = "")
    b1 = fonk1(b7.upper(), b6)
    print("\nYour encrypted b7 is:\n", b1, b8 = "")
    b5 = fonk2(b1, b6)
    print("Your decrypted b7 is:\n", b5, b8 = "")
if b9 = = "__main__":
    fonk3()