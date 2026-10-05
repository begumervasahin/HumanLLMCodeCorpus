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
        with open('input.txt', 'w+') as file:
            file.write(args.message)
        with open('input.txt', 'r') as file:
            content = file.read()
    xormessage(content, args.output)
def generaterandom():
    return int(random.random() * 255.0)
def xormessage(content, outfile):
    key = generaterandom()
    with open(outfile, 'w') as fileout:
        for char in content:
            encrypt = ord(char) ^ key
            fileout.write(chr(encrypt))
        fileout.write(" ")
if __name__ == "__main__":
    main(sys.argv[1:])