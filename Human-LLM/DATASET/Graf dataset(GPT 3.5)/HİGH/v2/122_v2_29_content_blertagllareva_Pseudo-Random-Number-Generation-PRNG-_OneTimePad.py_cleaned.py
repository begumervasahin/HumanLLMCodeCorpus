def fonk1(char):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    a1 = 0
    for b2 in b1:
        a1 += 1
        if b2 = = char:
            break
    return a1
def fonk2(a1):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    return b1[a1 - 1]
def fonk3(b7, key_char):
    b3 = fonk1(b7)
    b4 = fonk1(key_char)
    b5 = (b3 + b4) % 26
    b6 = fonk2(b5)
    return b6
def fonk4(b6, key_char):
    b5 = fonk1(b6)
    b4 = fonk1(key_char)
    b3 = (b5 - b4) % 26
    b7 = fonk2(b3)
    return b7
def fonk5(b9, b11):
    b8 = ""
    for i in range(len(b9)):
        b8 += fonk3(b9[i], b11[i])
    return b8
def fonk6(b8, b11):
    b9 = ""
    for i in range(len(b8)):
        b9 += fonk4(b8[i], b11[i])
    return b9
def fonk7():
    print("OneTimePad Program. The b11 must be shorter or equal to the plain text. The plain text should not contain numbers.")
    print("\nOptions:\n1: Encoding\n2: Decoding\n3: Quit")
    while True:
        b10 = input(">>> ")
        if b10 = = "1":
            b9 = input("Plain text: ")
            b11 = input("Key: ")
            if len(b11) < len(b9):
                print("The b11 must be at least as long as the plain text.")
            else:
                print("Cipher text:", fonk5(b9, b11))
        elif b10 = = "2":
            b8 = input("Cipher text: ")
            b11 = input("Key: ")
            if len(b11) < len(b8):
                print("The b11 must be at least as long as the cipher text.")
            else:
                print("Plain text:", fonk6(b8, b11))
        elif b10 = = "3":
            break
        else:
            print("Please choose 1, 2, or 3.")
if b12 = = "__main__":
    fonk7()