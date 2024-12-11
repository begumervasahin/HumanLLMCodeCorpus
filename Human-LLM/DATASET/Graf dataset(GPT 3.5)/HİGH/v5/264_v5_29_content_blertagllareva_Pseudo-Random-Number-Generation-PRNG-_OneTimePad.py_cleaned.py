def fonk1(char):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    return b1.index(char.lower()) + 1
def fonk2(num):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    return b1[num - 1]
def fonk3(plain_text_char, key_char):
    b2 = fonk1(plain_text_char)
    b3 = fonk1(key_char)
    b4 = (b2 + b3 - 1) % 26 + 1
    return fonk2(b4)
def fonk4(cipher_text_char, key_char):
    b4 = fonk1(cipher_text_char)
    b3 = fonk1(key_char)
    b2 = (b4 - b3 - 1) % 26 + 1
    return fonk2(b2)
def fonk5(b6, b8):
    b5 = ""
    for p_char, k_char in zip(b6, b8):
        b5 += fonk3(p_char, k_char)
    return b5
def fonk6(b5, b8):
    b6 = ""
    for c_char, k_char in zip(b5, b8):
        b6 += fonk4(c_char, k_char)
    return b6
def fonk7():
    print("One-Time Pad Program. The b8 must be smaller or equal in length to the plain text. The plain text should not contain numbers.")
    print("\nOptions:\n1: Encode\n2: Decode\n3: Exit")
    while True:
        b7 = input(">>> ")
        if b7 = = "1":
            b6 = input("Plain text: ")
            b8 = input("Key: ")
            print("Cipher text:", fonk5(b6, b8))
        elif b7 = = "2":
            b5 = input("Cipher text: ")
            b8 = input("Key: ")
            print("Plain text:", fonk6(b5, b8))
        elif b7 = = "3":
            break
        else:
            print("Please choose 1, 2, or 3")
if b9 = = "__main__":
    fonk7()