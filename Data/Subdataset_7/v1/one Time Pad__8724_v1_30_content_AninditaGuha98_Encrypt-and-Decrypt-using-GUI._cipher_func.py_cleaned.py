import string
def fonk1(b9, b11):
    b1 = ''
    for b2 in b9:
        b2 = (ord(b2) + int(b11))
        if b2 - int(b11) == 32:
            b2 = 32
        elif b2 > ord('z'):
            b2 -= 26
        elif b2 < ord('a'):
            b2 += 26
        b2 = chr(b2)
        b1 += b2
    return b1
def fonk2(b7, b11):
    b3 = ''
    for b2 in b7:
        b2 = (ord(b2) - int(b11))
        if b2 + int(b11) == 32:
            b2 = 32
        elif b2 > ord('z'):
            b2 -= 26
        elif b2 < ord('a'):
            b2 += 26
        b2 = chr(b2)
        b3 += b2
    return b3
def fonk3(b9, b11):
    b4 = len(b11)
    b5 = [ord(i) for i in b11]
    b6 = [ord(i) for i in b9]
    b7 = ''
    for i in range(len(b6)):
        b2 = (b6[i] + b5[i % b4]) % 26
        b7 += chr(b2 + 65)
    return b7
def fonk4(b7, b11):
    b4 = len(b11)
    b5 = [ord(i) for i in b11]
    b8 = [ord(i) for i in b7]
    b9 = ''
    for i in range(len(b8)):
        b2 = (b8[i] - b5[i % b4]) % 26
        b9 += chr(b2 + 65)
    return b9
def fonk5():
    print("Choose an option:\n1. Caesar Cipher Encryption\n2. Caesar Cipher Decryption\n3. Vigenere Cipher Encryption\n4. Vigenere Cipher Decryption\n5. Exit")
    while True:
        b10 = input("Enter your b10: ")
        if b10 = = "1":
            b9 = input("Enter the b9: ")
            b11 = input("Enter the b11: ")
            print("Encrypted text:", fonk1(b9, b11))
        elif b10 = = "2":
            b7 = input("Enter the b7: ")
            b11 = input("Enter the b11: ")
            print("Decrypted text:", fonk2(b7, b11))
        elif b10 = = "3":
            b9 = input("Enter the b9: ")
            b11 = input("Enter the b11: ")
            print("Encrypted text:", fonk3(b9, b11))
        elif b10 = = "4":
            b7 = input("Enter the b7: ")
            b11 = input("Enter the b11: ")
            print("Decrypted text:", fonk4(b7, b11))
        elif b10 = = "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid b10. Please choose again.")
if b12 = = "__main__":
    fonk5()