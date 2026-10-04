import sys
import random
import argparse
def main(argv):
    parser = argparse.ArgumentParser(description="Encrypt a message using XOR encryption.")
    parser.add_argument('-f', '--filename', help="Input file containing the message")
    parser.add_argument('-m', '--message', help="Message to be encrypted")
    parser.add_argument('-o', '--output', required=True, help="Output file for the encrypted message")
    args = parser.parse_args()
    content = ""
    if args.filename:
        with open(args.filename, 'r', encoding='utf-8') as file:
            content = file.read()
    elif args.message:
        content = args.message
    if not content:
        print("No content to encrypt")
        return
    xor_message(content, args.output)
def generate_random_key():
    return random.randint(0, 255)
def xor_message(content, outfile):
    key = generate_random_key()
    with open(outfile, 'w', encoding='utf-8') as fileout:
        encrypted_content = ''.join(chr(ord(char) ^ key) for char in content)
        fileout.write(encrypted_content)
        fileout.write(f"\nKEY={key}")
if __name__ == "__main__":
    main(sys.argv[1:])