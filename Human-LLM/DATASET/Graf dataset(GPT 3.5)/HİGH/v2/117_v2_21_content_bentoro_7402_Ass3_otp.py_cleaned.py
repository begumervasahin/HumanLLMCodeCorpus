import sys
import random
import argparse
def fonk1(argv):
    b1 = argparse.ArgumentParser()
    b1.add_argument('-f', b2 = "store", dest="b5")
    b1.add_argument('-m', b2 = "store", dest="message")
    b1.add_argument('-o', b2 = "store", dest="output", required=True)
    b3 = b1.parse_args(argv)
    b4 = ""
    if b3.b5:
        b5 = b3.b5
        with open(b5, 'r') as file:
            b4 = file.read()
    elif b3.message:
        b4 = b3.message
    b6 = b3.output
    fonk3(b4, b6)
def fonk2():
    return random.randint(0, 255)
def fonk3(b4, b6):
    b7 = fonk2()
    with open(b6, 'w') as fileout:
        for char in b4:
            b8 = ord(char) ^ b7
            fileout.write(chr(b8))
if b9 = = "__main__":
    fonk1(sys.argv[1:])