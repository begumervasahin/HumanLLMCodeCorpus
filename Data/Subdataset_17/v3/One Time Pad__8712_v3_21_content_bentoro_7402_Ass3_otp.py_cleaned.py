import sys
import random
import argparse
def main(argv):
    args = parse_arguments(argv)
    content = read_content(args.filename, args.message)
    if not content:
        print("No content to encrypt")
        return
    xor_encrypt_and_save(content, args.output)
def parse_arguments(argv):
    parser = argparse.ArgumentParser(description="Encrypt a message using XOR encryption.")
    parser.add_argument('-f', '--filename', help="Input file containing the message")
    parser.add_argument('-m', '--message', help="Message to be encrypted")
    parser.add_argument('-o', '--output', required=True, help="Output file for the encrypted message")
    return parser.parse_args(argv)
def read_content(filename, message):
    if filename:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    return message
def generate_random_key():
    return random.randint(0, 255)
def xor_encrypt_and_save(content, outfile):
    key = generate_random_key()
    encrypted_content = xor_encrypt(content, key)
    with open(outfile, 'w', encoding='utf-8') as fileout:
        fileout.write(encrypted_content)
        fileout.write(f"\nKEY={key}")
def xor_encrypt(content, key):
    return ''.join(chr(ord(char) ^ key) for char in content)
if __name__ == "__main__":
    main(sys.argv[1:])