import os
import argparse
def generate_key(length):
    key = ""
    for _ in range(length):
        key += chr(65 + ord(os.urandom(1)) % 26)
    return key
def xor_strings(a, b):
    result = ""
    for i in range(len(a)):
        result += chr(64 + (ord(a[i]) ^ ord(b[i])))
    return result
def clean_message(message):
    return message.upper().replace(" ", "a").replace(".", "b").replace(",", "c").replace("'", "d")
def unclean_message(message):
    return message.replace("a", " ").replace("b", ".").replace("c", ",").replace("d", "'")
def main():
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad.')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt data (default is to encrypt)')
    args = parser.parse_args()
    if args.decrypt:
        key = input("Key: ")
        coded_message = input("Coded message: ")
        decrypted_message = unclean_message(xor_strings(key, coded_message))
        print("Decrypted message:", decrypted_message)
    else:
        message = input("Message: ")
        cleaned_message = clean_message(message)
        key = generate_key(len(cleaned_message))
        encrypted_message = xor_strings(cleaned_message, key)
        print("Key:", key)
        print("Encrypted message:", encrypted_message)
if __name__ == '__main__':
    main()