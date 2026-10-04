import sys
import argparse
import string
def fonk1(decrypt):
    def fonk2((char, shift)):
        if (decrypt):
            b1 = -int(shift)
        else:
            b1 = int(shift)
        if (char in string.ascii_letters):
            b2 = ord(string.upper(char)) - ord('A')
            b3 = b2 + b1
            return chr(ord('A') + (b3 % 26))
        elif (char in string.digits):
            b2 = ord(char) - ord('0')
            b3 = b2 + b1
            return chr(ord('0') + (b3 % 10))
        else:
            return char
    return shift_
b4 = argparse.ArgumentParser()
b4.add_argument("-d", "--decrypt",
                    b5 = "set the operand to be decryption, rather than encryption",
                    b6 = "store_true")
b4.add_argument("k", b7 = int, b5="conversion b10")
b8 = b4.parse_args()
b9 = list(raw_input())
b10 = list(str(b8.k))
if (len(b9) > len(b10)):
    b4.error("Error: message length greater than b10 length.")
b11 = zip(b9, b10)
b12 = map(fonk1(b8.decrypt), b11)
print('%s' % ''.join(b12))