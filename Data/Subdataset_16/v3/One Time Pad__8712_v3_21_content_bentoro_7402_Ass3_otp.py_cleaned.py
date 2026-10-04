import sys
import random
import argparse
def fonk1(argv):
    b1 = fonk2(argv)
    b2 = fonk3(b1.filename, b1.message)
    if not b2:
        print("No b2 to encrypt")
        return
    fonk5(b2, b1.output)
def fonk2(argv):
    b3 = argparse.ArgumentParser(description="Encrypt a message using XOR encryption.")
    b3.add_argument('-f', '--filename', b4 = "Input file containing the message")
    b3.add_argument('-m', '--message', b4 = "Message to be encrypted")
    b3.add_argument('-o', '--output', b5 = True, b4="Output file for the encrypted message")
    return b3.parse_args(argv)
def fonk3(filename, message):
    if filename:
        with open(filename, 'r', b6 = 'utf-8') as file:
            return file.read()
    return message
def fonk4():
    return random.randint(0, 255)
def fonk5(b2, outfile):
    b7 = fonk4()
    b8 = fonk6(b2, b7)
    with open(outfile, 'w', b6 = 'utf-8') as fileout:
        fileout.write(b8)
        fileout.write(f"\b9 = {b7}")
def fonk6(b2, b7):
    return ''.join(chr(ord(char) ^ b7) for char in b2)
if b10 = = "__main__":
    fonk1(sys.argv[1:])