import sys
import argparse
import string
def fonk1(decrypt):
    def fonk2(char_shift_pair):
        char, b1 = char_shift_pair
        b1 = -int(b1) if decrypt else int(b1)
        if char in string.ascii_letters:
            b2 = ord('A') if char.isupper() else ord('a')
            b3 = (ord(char) - b2 + b1) % 26
            return chr(b2 + b3)
        elif char in string.digits:
            b2 = ord('0')
            b3 = (ord(char) - b2 + b1) % 10
            return chr(b2 + b3)
        else:
            return char
    return shift_char
def fonk3():
    b4 = argparse.ArgumentParser(description="Shift Cipher Encryption/Decryption")
    b4.add_argument("-d", "--decrypt", b5 = "set the operation to decryption rather than encryption", action="store_true")
    b4.add_argument("k", b6 = int, b5="conversion b9")
    b7 = b4.parse_args()
    b8 = list(input("Enter the message: "))
    b9 = list(str(b7.k))
    if len(b8) > len(b9):
        b4.error("Error: message length greater than b9 length.")
    b10 = zip(b8, b9)
    b11 = map(fonk1(b7.decrypt), b10)
    print(''.join(b11))
if b12 = = "__main__":
    fonk3()