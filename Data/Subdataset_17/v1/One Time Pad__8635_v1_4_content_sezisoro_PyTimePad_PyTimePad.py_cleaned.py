import sys
import argparse
import string
def shift(decrypt):
    def shift_char(char_shift_pair):
        char, shift = char_shift_pair
        shift = -int(shift) if decrypt else int(shift)
        if char in string.ascii_letters:
            base = ord('A') if char.isupper() else ord('a')
            shifted_index = (ord(char) - base + shift) % 26
            return chr(base + shifted_index)
        elif char in string.digits:
            base = ord('0')
            shifted_index = (ord(char) - base + shift) % 10
            return chr(base + shifted_index)
        else:
            return char
    return shift_char
def main():
    parser = argparse.ArgumentParser(description="Shift Cipher Encryption/Decryption")
    parser.add_argument("-d", "--decrypt", help="set the operation to decryption rather than encryption", action="store_true")
    parser.add_argument("k", type=int, help="conversion key")
    args = parser.parse_args()
    msg = list(input("Enter the message: "))
    key = list(str(args.k))
    if len(msg) > len(key):
        parser.error("Error: message length greater than key length.")
    pre = zip(msg, key)
    pst = map(shift(args.decrypt), pre)
    print(''.join(pst))
if __name__ == "__main__":
    main()