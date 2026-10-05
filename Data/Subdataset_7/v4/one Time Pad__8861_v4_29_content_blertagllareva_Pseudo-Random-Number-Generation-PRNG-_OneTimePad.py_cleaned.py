def fonk1(char):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    a1 = 1
    for b2 in b1:
        if b2 = = char:
            break
        else:
            a1 += 1
    return a1
def fonk2(a1):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    return b1[a1 - 1]
def fonk3(plain_text_char, key_char):
    b3 = (fonk1(plain_text_char) + fonk1(key_char)) % 26
    b4 = fonk2(b3)
    return b4
def fonk4(cipher_text_char, key_char):
    b5 = fonk1(cipher_text_char) - fonk1(key_char)
    b6 = fonk2(b5)
    return b6
def fonk5(b8, b11):
    b7 = ""
    for i in range(len(b8)):
        b7 += fonk3(b8[i], b11[i])
    return b7
def fonk6(b7, b11):
    b8 = ""
    for i in range(len(b7)):
        b8 += fonk4(b7[i], b11[i])
    return b8
def fonk7():
    b9 = True
    print("One-Time Pad Program. The b11 must be smaller or equal in length to the plain text. The plain text should not contain numbers.")
    print("\nOptions:\n1: Encode\n2: Decode\n3: Exit")
    while b9:
        b10 = input(">>> ")
        if b10 = = "1":
            b8 = input("Plain text: ")
            b11 = input("Key: ")
            print("Cipher text:", fonk5(b8, b11))
        elif b10 = = "2":
            b7 = input("Cipher text: ")
            b11 = input("Key: ")
            print("Plain text:", fonk6(b7, b11))
        elif b10 = = "3":
            b9 = False
        else:
            print("Please choose 1, 2, or 3")
if b12 = = "__main__":
    fonk7()