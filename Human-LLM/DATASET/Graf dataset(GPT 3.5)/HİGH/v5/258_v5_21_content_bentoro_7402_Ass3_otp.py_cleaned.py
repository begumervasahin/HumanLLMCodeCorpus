import sys
import random
import argparse
def fonk1(argv):
    b1 = argparse.ArgumentParser()
    b1.add_argument('-f', b2 = "store", dest="filename")
    b1.add_argument('-m', b2 = "store", dest="message")
    b1.add_argument('-o', b2 = "store", dest="output", required=True)
    b3 = b1.parse_args()
    b4 = ""
    if b3.filename:
        with open(b3.filename) as file:
            b4 = file.read()
    elif b3.message:
        b4 = b3.message
    fonk3(b4, b3.output)
def fonk2():
    return random.randint(0, 255)
def fonk3(b4, outfile):
    b5 = fonk2()
    with open(outfile, 'w') as fileout:
        for char in b4:
            b6 = ord(char) ^ b5
            fileout.write(chr(b6))
        fileout.write(" ")
if b7 = = "__main__":
    fonk1(sys.argv[1:])