import sys
import random
import argparse
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", dest="filename", help="Input file name")
    parser.add_argument('-m', action="store", dest="message", help="Message to encrypt")
    parser.add_argument('-o', action="store", dest="output", required=True, help="Output file name")
    args = parser.parse_args()
    content = ""
    if args.filename:
        with open(args.filename, 'r') as file:
            content = file.read()
    elif args.message:
        with open('input.txt', 'w') as file:
            file.write(args.message)
        with open('input.txt', 'r') as file:
            content = file.read()
    outfile = args.output
    xormessage(content, outfile)
def generaterandom():
    return random.randint(0, 255)
def xormessage(content, outfile):
    key = generaterandom()
    with open(outfile, 'w') as fileout:
        for char in content:
            encrypted_char = chr(ord(char) ^ key)
            fileout.write(encrypted_char)
if __name__ == "__main__":
    main(sys.argv[1:])