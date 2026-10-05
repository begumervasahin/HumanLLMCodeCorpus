import sys
import argparse
import string
def shift_character(char, shift, decrypt):
    if decrypt:
        shift = -shift
    if char in string.ascii_letters:
        char_index = ord(char.upper()) - ord('A')
        shifted_index = (char_index + shift) % 26
        return chr(ord('A') + shifted_index)
    elif char in string.digits:
        char_index = ord(char) - ord('0')
        shifted_index = (char_index + shift) % 10
        return chr(ord('0') + shifted_index)
    else:
        return char
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--decrypt",
                        help="set the operand to be decryption, rather than encryption",
                        action="store_true")
    parser.add_argument("k", type=int, help="conversion key")
    args = parser.parse_args()
    message = input("Enter message: ")
    key = str(args.k)
    if len(message) > len(key):
        parser.error("Error: message length greater than key length.")
    shifted_message = ''.join(shift_character(char, int(key), args.decrypt) for char in message)
    print(shifted_message)