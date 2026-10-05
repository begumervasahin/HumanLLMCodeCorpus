import sys
import random
import argparse
def fonk1(argv):
    b1 = ""
    b2 = ''
    b3 = argparse.ArgumentParser()
    b3.add_argument('-f', b4 = "store", dest="b6")
    b3.add_argument('-m', b4 = "store", dest="message")
    b3.add_argument('-o', b4 = "store", dest="b2", required=True)
    b5 = b3.parse_args(argv)
    if b5.b6:
        b6 = b5.b6
        with open(b6, 'r') as file:
            b1 = file.read()
    elif b5.message:
        b1 = b5.message
    b7 = b5.b2
    fonk3(b1, b7)
def fonk2():
    return int(random.random() * 255.0)
def fonk3(b1, b7):
    b8 = fonk2()
    with open(b7, 'w') as fileout:
        for char in b1:
            b9 = ord(char) ^ b8
            fileout.write(chr(b9))
if b10 = = "__main__":
    fonk1(sys.argv[1:])