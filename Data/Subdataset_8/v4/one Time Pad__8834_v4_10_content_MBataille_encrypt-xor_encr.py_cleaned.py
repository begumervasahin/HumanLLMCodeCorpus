import os
import argparse
def generate_random_string(length):
    random_string = ""
    for i in range(length):
        random_string += chr(65 + ord(os.urandom(1)) % 26)
    return random_string
def string_xor(a, b):
    result = ""
    for i in range(len(a)):
        result += chr(64 + (ord(a[i]) ^ ord(b[i])))
    return result
def clean_message(message):
    return message.upper().replace(" ", "a").replace(".", "b").replace(",", "c").replace("'", "d")
def unclean_message(message):
    return message.replace("a", " ").replace("b", ".").replace("c", ",").replace("d", "'")
parser = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad')
parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt data (default is to encrypt)')
args = parser.parse_args()
if args.decrypt:
    key = raw_input("Enter the key: ")
    coded = raw_input("Enter the coded stuff: ")
    print unclean_message(string_xor(key, coded))
else:
    decoded = clean_message(raw_input("Enter the message: "))
    key = generate_random_string(len(decoded))
    print "Generated key:", key
    print "Encoded message:", string_xor(decoded, key)