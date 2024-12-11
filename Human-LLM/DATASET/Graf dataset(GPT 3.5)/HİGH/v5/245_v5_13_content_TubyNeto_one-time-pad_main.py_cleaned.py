import string
import random
def fonk1(plain_letter, key_letter):
    b1 = string.ascii_lowercase
    b2 = b1.index(plain_letter.lower()) + 1
    b3 = b1.index(key_letter.lower()) + 1
    b4 = (b2 + b3) % 26
    return b1[b4 - 1]
def fonk2(cipher_letter, key_letter):
    b1 = string.ascii_lowercase
    b4 = b1.index(cipher_letter.lower()) + 1
    b3 = b1.index(key_letter.lower()) + 1
    b2 = (b4 - b3) % 26
    return b1[b2 - 1]
def fonk3(b6, b9):
    b5 = ''
    for i in range(len(b6)):
        b5 += fonk2(b6[i], b9[i % len(b9)])
    return b5
def fonk4(b5, b9):
    b6 = ''
    for i in range(len(b5)):
        b6 += fonk1(b5[i], b9[i % len(b9)])
    return b6
def fonk5(text_length):
    b7 = string.ascii_lowercase
    return ''.join(random.choice(b7) for _ in range(text_length))
def fonk6():
    while True:
        print("Menu:")
        print("1 - Encrypt")
        print("2 - Decrypt")
        print("3 - Quit")
        b8 = input("Select an option: ")
        if b8 = = '1':
            b5 = input("Enter the Plain Text: ")
            b9 = fonk5(len(b5))
            print('Cipher Text:', fonk4(b5, b9))
        elif b8 = = '2':
            b6 = input("Enter the Cipher Text: ")
            b9 = input("Enter the Key: ")
            print('Plain Text:', fonk3(b6, b9))
        elif b8 = = '3':
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
if b10 = = "__main__":
    fonk6()