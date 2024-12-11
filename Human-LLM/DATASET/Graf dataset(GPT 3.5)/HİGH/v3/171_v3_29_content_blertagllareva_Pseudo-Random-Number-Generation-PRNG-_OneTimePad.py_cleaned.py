def fonk1(char):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    return b1.index(char) + 1
def fonk2(num):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    return b1[num - 1]
def fonk3(plain_char, key_char):
    b2 = fonk1(plain_char)
    b3 = fonk1(key_char)
    b4 = (b2 + b3 - 1) % 26 + 1
    return fonk2(b4)
def fonk4(cipher_char, key_char):
    b4 = fonk1(cipher_char)
    b3 = fonk1(key_char)
    b2 = (b4 - b3 - 1) % 26 + 1
    return fonk2(b2)
def fonk5(b6, b8):
    b5 = ""
    for plain_char, key_char in zip(b6, b8):
        b5 += fonk3(plain_char, key_char)
    return b5
def fonk6(b5, b8):
    b6 = ""
    for cipher_char, key_char in zip(b5, b8):
        b6 += fonk4(cipher_char, key_char)
    return b6
def fonk7():
    print("OneTimePad Program. The b8 must be shorter or equal to the plain text. The plain text should not contain numbers.")
    print("\nOptions:\n1: Encoding\n2: Decoding\n3: Quit")
    while True:
        b7 = input(">>> ")
        if b7 = = "1":
            b6 = input("Plain text: ")
            b8 = input("Key: ")
            if len(b8) < len(b6):
                print("The b8 must be at least as long as the plain text.")
            else:
                print("Cipher text:", fonk5(b6, b8))
        elif b7 = = "2":
            b5 = input("Cipher text: ")
            b8 = input("Key: ")
            if len(b8) < len(b5):
                print("The b8 must be at least as long as the cipher text.")
            else:
                print("Plain text:", fonk6(b5, b8))
        elif b7 = = "3":
            break
        else:
            print("Please choose 1, 2, or 3.")
if b9 = = "__main__":
    fonk7()