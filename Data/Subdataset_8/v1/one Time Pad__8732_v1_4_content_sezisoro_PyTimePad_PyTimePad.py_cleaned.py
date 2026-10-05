import sys
import argparse
import string
def shift(decrypt):
    def shift_(char, shift):
        if decrypt:
            s_i = -int(shift)
        else:
            s_i = int(shift)
        if char in string.ascii_letters:
            c_i = ord(char.upper()) - ord('A')
            p_i = c_i + s_i
            return chr(ord('A') + (p_i % 26))
        elif char in string.digits:
            c_i = ord(char) - ord('0')
            p_i = c_i + s_i
            return chr(ord('0') + (p_i % 10))
        else:
            return char
    return shift_
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decrypt",
                    help="set the operand to be decryption, rather than encryption",
                    action="store_true")
parser.add_argument("k", type=int, help="conversion key")
args = parser.parse_args()
msg = list(input("Enter message: "))
key = list(str(args.k))
if len(msg) > len(key):
    parser.error("Error: message length greater than key length.")
pre = zip(msg, key)
pst = map(shift(args.decrypt), pre)
print('%s' % ''.join(pst))