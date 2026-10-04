import sys
import random
import argparse
def fonk1(argv):
    b1 = ""
    b2 = argparse.ArgumentParser()
    b2.add_argument('-f', b3 = "store", dest="filename", help="Input file containing the message")
    b2.add_argument('-m', b3 = "store", dest="message", help="Message to be encrypted")
    b2.add_argument('-o', b3 = "store", dest="output", required=True, help="Output file for the encrypted message")
    b4 = b2.parse_args()
    if b4.filename:
        with open(b4.filename, 'r') as file:
            b1 = file.read()
    elif b4.message:
        b1 = b4.message
    if not b1:
        print("No b1 to encrypt")
        return
    fonk3(b1, b4.output)
def fonk2():
    return int(random.random() * 255.0)
def fonk3(b1, outfile):
    b5 = fonk2()
    with open(outfile, 'w', b6 = 'utf-8') as fileout:
        for char in b1:
            b7 = ord(char) ^ b5
            fileout.write(chr(b7))
        fileout.write(f"\b8 = {b5}")
if b9 = = "__main__":
    fonk1(sys.argv[1:])