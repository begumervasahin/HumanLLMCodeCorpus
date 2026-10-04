import random
import sys
def fonk1(b1):
    b1 = ord(b1)
    b2 = random.randint(0, 255)
    b3 = b1 ^ b2
    return [b2, b3]
def fonk2(byte0, b5):
    b2 = ord(byte0)
    b3 = ord(b5)
    return b2 ^ b3
def fonk3(input_filename, key1_filename, key2_filename):
    with open(input_filename, "rb") as infile, \
         open(key1_filename, 'wb') as b10, \
         open(key2_filename, 'wb') as b11:
        b1 = infile.read(1)
        while b1:
            b2, b3 = fonk1(b1)
            b10.write(b2.to_bytes(1, b4 = "big", signed=False))
            b11.write(b3.to_bytes(1, b4 = "big", signed=False))
            b1 = infile.read(1)
def fonk4(key1_filename, key2_filename, output_filename):
    with open(key1_filename, "rb") as b10, \
         open(key2_filename, "rb") as b11, \
         open(output_filename, 'wb') as outfile:
        b5 = b10.read(1)
        b6 = b11.read(1)
        while b5 and b6:
            b7 = fonk2(b5, b6)
            outfile.write(b7.to_bytes(1, b4 = "big", signed=False))
            b5 = b10.read(1)
            b6 = b11.read(1)
if b8 = = "__main__":
    print("Starting script...")
    if len(sys.argv) == 2:
        b9 = sys.argv[1]
        fonk3(b9, b9 + ".0", b9 + ".1")
    elif len(sys.argv) == 3:
        b10 = sys.argv[1]
        b11 = sys.argv[2]
        b12 = b10[:-2]
        fonk4(b10, b11, b12)
    else:
        print("Argument parsing error.")
    print("Script finished.")