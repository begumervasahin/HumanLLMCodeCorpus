import sys
import random
import argparse
def fonk1(argv):
    b1 = argparse.ArgumentParser(description="Encrypt a message using XOR encryption.")
    b1.add_argument('-f', '--file', b2 = "store", dest="filename", help="Input file name")
    b1.add_argument('-m', '--message', b2 = "store", dest="message", help="Message to encrypt")
    b1.add_argument('-o', '--output', b2 = "store", dest="output", required=True, help="Output file name")
    b3 = b1.parse_args()
    if b3.filename:
        with open(b3.filename, 'r') as file:
            b4 = file.read()
    elif b3.message:
        b4 = b3.message
    else:
        raise ValueError("Either an input file or a message must be provided.")
    fonk3(b4, b3.output)
def fonk2():
    return random.randint(0, 255)
def fonk3(b4, output_filename):
    b5 = fonk2()
    b6 = ''.join(chr(ord(char) ^ b5) for char in b4)
    with open(output_filename, 'w') as fileout:
        fileout.write(b6)
if b7 = = "__main__":
    fonk1(sys.argv[1:])