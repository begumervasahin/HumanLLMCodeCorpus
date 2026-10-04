import sys
import random
import argparse
def fonk1(argv):
    b1 = argparse.ArgumentParser()
    b1.add_argument('-f', b2 = "store", dest="filename", help="Input file name")
    b1.add_argument('-m', b2 = "store", dest="message", help="Message to encrypt")
    b1.add_argument('-o', b2 = "store", dest="output", required=True, help="Output file name")
    b3 = b1.parse_args()
    b4 = ""
    if b3.filename:
        with open(b3.filename, 'r') as file:
            b4 = file.read()
    elif b3.message:
        with open('input.txt', 'w') as file:
            file.write(b3.message)
        with open('input.txt', 'r') as file:
            b4 = file.read()
    b5 = b3.output
    fonk3(b4, b5)
def fonk2():
    return random.randint(0, 255)
def fonk3(b4, b5):
    b6 = fonk2()
    with open(b5, 'w') as fileout:
        for char in b4:
            b7 = chr(ord(char) ^ b6)
            fileout.write(b7)
if b8 = = "__main__":
    fonk1(sys.argv[1:])