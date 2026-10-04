import argparse
import string
def shift(decrypt):
    def shift_char(char, shift_amount):
        shift_value = -int(shift_amount) if decrypt else int(shift_amount)
        if char in string.ascii_letters:
            char_index = ord(char.upper()) - ord('A')
            shifted_index = (char_index + shift_value) % 26
            return chr(ord('A') + shifted_index)
        elif char in string.digits:
            char_index = ord(char) - ord('0')
            shifted_index = (char_index + shift_value) % 10
            return chr(ord('0') + shifted_index)
        else:
            return char
    return shift_char
def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using a shift cipher.")
    parser.add_argument("-d", "--decrypt", help="Set the operation to decryption (default is encryption)", action="store_true")
    parser.add_argument("key", type=int, help="The key used for the shift cipher.")
    args = parser.parse_args()
    message = input("Enter the message: ")
    key = str(args.key)
    if len(message) > len(key):
        parser.error("Error: Message length is greater than key length.")
    shift_func = shift(args.decrypt)
    result = ''.join(shift_func(char, k) for char, k in zip(message, key))
    print(f"Result: {result}")
if __name__ == "__main__":
    main()