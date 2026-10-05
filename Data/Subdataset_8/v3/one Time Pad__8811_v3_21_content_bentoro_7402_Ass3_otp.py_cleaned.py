import sys
import random
import argparse
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", dest="filename")
    parser.add_argument('-m', action="store", dest="message")
    parser.add_argument('-o', action="store", dest="output", required=True)
    args = parser.parse_args(argv)
    content = read_content(args.filename, args.message)
    xormessage(content, args.output)
def read_content(filename, message):
    if filename:
        with open(filename, 'r') as file:
            return file.read()
    elif message:
        return message
    return ""
def generate_random():
    return random.randint(0, 255)
def xormessage(content, outfile):
    key = generate_random()
    with open(outfile, 'w') as fileout:
        for char in content:
            encrypt = ord(char) ^ key
            fileout.write(chr(encrypt)))
if __name__ == "__main__":
    main(sys.argv[1:])