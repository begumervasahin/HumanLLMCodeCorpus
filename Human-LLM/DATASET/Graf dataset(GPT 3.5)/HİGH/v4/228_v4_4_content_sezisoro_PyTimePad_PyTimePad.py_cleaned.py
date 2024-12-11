import sys
import argparse
import string
def fonk1(decrypt):
    def fonk2((char, shift)):
        if decrypt:
            b1 = -int(shift)
        else:
            b1 = int(shift)
        if char in string.ascii_letters:
            b2 = ord(char.upper()) - ord('A')
            b3 = b2 + b1
            return chr(ord('A') + (b3 % 26))
        elif char in string.digits:
            b2 = ord(char) - ord('0')
            b3 = b2 + b1
            return chr(ord('0') + (b3 % 10))
        else:
            return char
    return shift_
b4 = argparse.ArgumentParser()
b4.add_argument("-d", "--decrypt", b5 = "set the operand to be decryption, rather than encryption", action="store_true")
b4.add_argument("k", b6 = int, b5="conversion b9")
b7 = b4.parse_args()
b8 = list(input())
b9 = list(str(b7.k))
if len(b8) > len(b9):
    b4.error("Error: message length greater than b9 length.")
b10 = zip(b8, b9)
b11 = map(fonk1(b7.decrypt), b10)
print('%s' % ''.join(b11))