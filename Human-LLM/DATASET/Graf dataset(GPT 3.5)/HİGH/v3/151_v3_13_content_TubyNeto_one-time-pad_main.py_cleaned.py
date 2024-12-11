import string
import random
def fonk1(b6, key_letter):
    b1 = string.ascii_lowercase
    b2 = b1.index(b6.lower()) + 1
    b3 = b1.index(key_letter.lower()) + 1
    b4 = (b2 + b3) % 26
    b5 = b1[b4 - 1]
    return b5
def fonk2(b5, key_letter):
    b1 = string.ascii_lowercase
    b4 = b1.index(b5.lower()) + 1
    b3 = b1.index(key_letter.lower()) + 1
    b2 = b4 - b3
    b6 = b1[b2 - 1]
    return b6
def fonk3(b8, b11):
    b7 = ''.join(fonk2(c, k) for c, k in zip(b8, b11))
    return b7
def fonk4(b7, b11):
    b8 = ''.join(fonk1(p, k) for p, k in zip(b7, b11))
    return b8
def fonk5(key_length):
    b9 = string.ascii_lowercase
    return ''.join(random.choice(b9) for _ in range(key_length))
def fonk6():
    while True:
        print("Menu:")
        print("1 - Encrypt")
        print("2 - Decrypt")
        print("3 - Quit")
        b10 = input()
        if b10 = = '1':
            b7 = input("Enter the Plain Text: ")
            b11 = fonk5(len(b7))
            print('Cipher Text:', fonk4(b7, b11))
        elif b10 = = '2':
            b8 = input("Enter the Cipher Text: ")
            b11 = fonk5(len(b8))
            print('Plain Text:', fonk3(b8, b11))
        elif b10 = = '3':
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
if b12 = = "__main__":
    fonk6()