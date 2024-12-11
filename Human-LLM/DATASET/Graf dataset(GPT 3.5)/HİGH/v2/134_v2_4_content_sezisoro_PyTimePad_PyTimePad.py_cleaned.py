import sys
import argparse
import string
def fonk1(char, b1, decrypt):
    if decrypt:
        b1 = -b1
    if char in string.ascii_letters:
        b2 = ord(char.upper()) - ord('A')
        b3 = (b2 + b1) % 26
        return chr(ord('A') + b3)
    elif char in string.digits:
        b2 = ord(char) - ord('0')
        b3 = (b2 + b1) % 10
        return chr(ord('0') + b3)
    else:
        return char
if b4 = = "__main__":
    b5 = argparse.ArgumentParser()
    b5.add_argument("-d", "--decrypt",
                        b6 = "set the operand to be decryption, rather than encryption",
                        b7 = "store_true")
    b5.add_argument("k", b8 = int, b6="conversion b11")
    b9 = b5.parse_args()
    b10 = input("Enter b10: ")
    b11 = str(b9.k)
    if len(b10) > len(b11):
        b5.error("Error: b10 length greater than b11 length.")
    b12 = ''.join(fonk1(char, int(b11), b9.decrypt) for char in b10)
    print(b12)