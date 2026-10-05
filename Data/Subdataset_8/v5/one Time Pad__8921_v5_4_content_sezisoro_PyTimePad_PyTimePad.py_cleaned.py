import sys
import argparse
import string
def shift_character(char, shift, decrypt):
    if decrypt:
        shift *= -1
    if char in string.ascii_letters:
        char_base = ord('A') if char.isupper() else ord('a')
        shifted_char = chr((ord(char) - char_base + shift) % 26 + char_base)
    elif char in string.digits:
        shifted_char = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
    else:
        shifted_char = char
    return shifted_char
def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using a conversion key.")
    parser.add_argument("key", type=int, help="conversion key")
    parser.add_argument("-d", "--decrypt", action="store_true", help="perform decryption")
    args = parser.parse_args()
    message = input("Enter the message: ")
    key = str(args.key)
    if len(message) > len(key):
        parser.error("Error: message length cannot exceed key length.")
    shifted_chars = [shift_character(char, int(key[i % len(key)]), args.decrypt) for i, char in enumerate(message)]
    encrypted_message = ''.join(shifted_chars)
    print("Encrypted message:" if not args.decrypt else "Decrypted message:", encrypted_message)
if __name__ == "__main__":
    main()