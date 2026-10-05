import string
def fonk1(b8, b9):
    b1 = ''
    for char in b8:
        if char.isalpha():
            b2 = (ord(char.lower()) - ord('a') + int(b9)) % 26
            b3 = chr((b2 + ord('a')))
        else:
            b3 = char
        b1 += b3
    return b1
def fonk2(b10, b9):
    b4 = ''
    for char in b10:
        if char.isalpha():
            b2 = (ord(char.lower()) - ord('a') - int(b9)) % 26
            b5 = chr((b2 + ord('a')))
        else:
            b5 = char
        b4 += b5
    return b4
def fonk3(b8, b9):
    b6 = len(b9)
    b1 = ''
    for i, char in enumerate(b8):
        if char.isalpha():
            b2 = (ord(b9[i % b6].lower()) - ord('a'))
            b3 = chr(((ord(char.lower()) - ord('a') + b2) % 26) + ord('a'))
        else:
            b3 = char
        b1 += b3
    return b1
def fonk4(b10, b9):
    b6 = len(b9)
    b4 = ''
    for i, char in enumerate(b10):
        if char.isalpha():
            b2 = (ord(b9[i % b6].lower()) - ord('a'))
            b5 = chr(((ord(char.lower()) - ord('a') - b2) % 26) + ord('a'))
        else:
            b5 = char
        b4 += b5
    return b4
def fonk5():
    print("Choose an option:")
    print("1. Caesar Cipher Encryption")
    print("2. Caesar Cipher Decryption")
    print("3. Vigenere Cipher Encryption")
    print("4. Vigenere Cipher Decryption")
    print("5. Exit")
    while True:
        b7 = input("Enter your b7: ")
        if b7 = = "1":
            b8 = input("Enter the b8: ")
            b9 = input("Enter the b9: ")
            print("Encrypted text:", fonk1(b8, b9))
        elif b7 = = "2":
            b10 = input("Enter the b10: ")
            b9 = input("Enter the b9: ")
            print("Decrypted text:", fonk2(b10, b9))
        elif b7 = = "3":
            b8 = input("Enter the b8: ")
            b9 = input("Enter the b9: ")
            print("Encrypted text:", fonk3(b8, b9))
        elif b7 = = "4":
            b10 = input("Enter the b10: ")
            b9 = input("Enter the b9: ")
            print("Decrypted text:", fonk4(b10, b9))
        elif b7 = = "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid b7. Please choose again.")
if b11 = = "__main__":
    fonk5()