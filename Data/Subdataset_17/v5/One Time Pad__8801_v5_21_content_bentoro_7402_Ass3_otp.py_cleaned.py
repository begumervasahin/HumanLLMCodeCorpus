import sys
import random
import argparse
def main(argv):
    parser = argparse.ArgumentParser(description="Encrypt a message using XOR encryption.")
    parser.add_argument('-f', '--file', action="store", dest="filename", help="Input file name")
    parser.add_argument('-m', '--message', action="store", dest="message", help="Message to encrypt")
    parser.add_argument('-o', '--output', action="store", dest="output", required=True, help="Output file name")
    args = parser.parse_args()
    if args.filename:
        with open(args.filename, 'r') as file:
            content = file.read()
    elif args.message:
        content = args.message
    else:
        raise ValueError("Either an input file or a message must be provided.")
    xor_encrypt(content, args.output)
def generate_random_key():
    return random.randint(0, 255)
def xor_encrypt(content, output_filename):
    key = generate_random_key()
    encrypted_content = ''.join(chr(ord(char) ^ key) for char in content)
    with open(output_filename, 'w') as fileout:
        fileout.write(encrypted_content)
if __name__ == "__main__":
    main(sys.argv[1:])