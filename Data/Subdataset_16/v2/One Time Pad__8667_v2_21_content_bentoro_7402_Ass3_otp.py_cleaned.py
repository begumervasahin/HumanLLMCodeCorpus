import sys
import random
import argparse
def fonk1(argv):
    b1 = argparse.ArgumentParser(description="Encrypt a message using XOR encryption.")
    b1.add_argument('-f', '--filename', b2 = "Input file containing the message")
    b1.add_argument('-m', '--message', b2 = "Message to be encrypted")
    b1.add_argument('-o', '--output', b3 = True, b2="Output file for the encrypted message")
    b4 = b1.parse_args()
    b5 = ""
    if b4.filename:
        with open(b4.filename, 'r', b6 = 'utf-8') as file:
            b5 = file.read()
    elif b4.message:
        b5 = b4.message
    if not b5:
        print("No b5 to encrypt")
        return
    fonk3(b5, b4.output)
def fonk2():
    return random.randint(0, 255)
def fonk3(b5, outfile):
    b7 = fonk2()
    with open(outfile, 'w', b6 = 'utf-8') as fileout:
        b8 = ''.join(chr(ord(char) ^ b7) for char in b5)
        fileout.write(b8)
        fileout.write(f"\b9 = {b7}")
if b10 = = "__main__":
    fonk1(sys.argv[1:])