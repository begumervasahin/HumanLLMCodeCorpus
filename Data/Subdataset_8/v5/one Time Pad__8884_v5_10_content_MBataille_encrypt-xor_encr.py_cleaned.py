import os
import argparse
def generate_random_string(length):
    return ''.join(chr(65 + ord(os.urandom(1)) % 26) for _ in range(length))
def string_xor(a, b):
    return ''.join(chr(64 + (ord(char_a) ^ ord(char_b))) for char_a, char_b in zip(a, b))
def clean_message(message):
    return message.upper().replace(" ", "A").replace(".", "B").replace(",", "C").replace("'", "D")
def unclean_message(message):
    return message.replace("A", " ").replace("B", ".").replace("C", ",").replace("D", "'")
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