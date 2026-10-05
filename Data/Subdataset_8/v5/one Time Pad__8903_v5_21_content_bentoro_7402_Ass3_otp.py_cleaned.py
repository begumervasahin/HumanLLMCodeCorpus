import sys
import random
import argparse
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", dest="filename")
    parser.add_argument('-m', action="store", dest="message")
    parser.add_argument('-o', action="store", dest="output", required=True)
    args = parser.parse_args()
    content = ""
    if args.filename:
        with open(args.filename) as file:
            content = file.read()
    elif args.message:
        content = args.message
    xormessage(content, args.output)
def generate_random_key():
    return random.randint(0, 255)
def xormessage(content, outfile):
    key = generate_random_key()
    with open(outfile, 'w') as fileout:
        for char in content:
            encrypt = ord(char) ^ key
            fileout.write(chr(encrypt))
        fileout.write(" ")
if __name__ == "__main__":
    main(sys.argv[1:])