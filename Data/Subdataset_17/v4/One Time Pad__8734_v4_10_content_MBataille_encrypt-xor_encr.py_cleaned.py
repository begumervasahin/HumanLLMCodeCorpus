import os
import argparse
def generate_key(length):
    key = ""
    for _ in range(length):
        key += chr(65 + ord(os.urandom(1)) % 26)
    return key
def str_xor(a, b):
    result = ""
    for i in range(len(a)):
        result += chr(64 + (ord(a[i]) ^ ord(b[i])))
    return result
def clean_text(text):
    return text.upper().replace(" ", "a").replace(".", "b").replace(",", "c").replace("'", "d")
def unclean_text(text):
    return text.replace("a", " ").replace("b", ".").replace("c", ",").replace("d", "'")
def main():
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt data (default is to encrypt)')
    args = parser.parse_args()
    if args.decrypt:
        key = input("Key: ")
        coded = input("Coded text: ")
        print("Decrypted text:", unclean_text(str_xor(key, coded)))
    else:
        message = input("Message: ")
        cleaned_message = clean_text(message)
        key = generate_key(len(cleaned_message))
        coded_message = str_xor(cleaned_message, key)
        print("Key:", key)
        print("Encrypted text:", coded_message)
if __name__ == "__main__":
    main()