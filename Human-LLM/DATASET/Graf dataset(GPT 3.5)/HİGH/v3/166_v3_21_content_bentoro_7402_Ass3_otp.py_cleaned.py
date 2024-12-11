import sys
import random
import argparse
def fonk1(argv):
    b1 = argparse.ArgumentParser()
    b1.add_argument('-f', b2 = "store", dest="filename")
    b1.add_argument('-m', b2 = "store", dest="message")
    b1.add_argument('-o', b2 = "store", dest="output", required=True)
    b3 = b1.parse_args(argv)
    b4 = fonk2(b3.filename, b3.message)
    fonk4(b4, b3.output)
def fonk2(filename, message):
    if filename:
        with open(filename, 'r') as file:
            return file.read()
    elif message:
        return message
    return ""
def fonk3():
    return random.randint(0, 255)
def fonk4(b4, outfile):
    b5 = fonk3()
    with open(outfile, 'w') as fileout:
        for char in b4:
            b6 = ord(char) ^ b5
            fileout.write(chr(b6)))
if b7 = = "__main__":
    fonk1(sys.argv[1:])