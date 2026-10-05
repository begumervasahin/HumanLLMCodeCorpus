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
def clean_string(string):
    return string.upper().replace(" ", "a").replace(".", "b").replace(",", "c").replace("'", "d")
def unclean_string(string):
    return string.replace("a", " ").replace("b", ".").replace("c", ",").replace("d", "'")
parser = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad')
parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt data (default is to encrypt)')
args = parser.parse_args()
if args.decrypt:
    key = input("Key: ")
    coded = input("Coded message: ")
    print(unclean_string(str_xor(key, coded)))
else:
    decoded = clean_string(input("Message: "))
    key = generate_key(len(decoded))
    print("Key:", key)
    print("Encoded message:", str_xor(decoded, key))