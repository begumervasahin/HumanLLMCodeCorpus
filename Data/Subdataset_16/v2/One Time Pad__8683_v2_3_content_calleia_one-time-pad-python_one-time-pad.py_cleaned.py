import random
import sys
def fonk1(b1):
    b1 = ord(b1)
    b2 = random.randint(0, 255)
    b3 = b1 ^ b2
    return [b2, b3]
def fonk2(b6, b3):
    b2 = ord(b6)
    b4 = ord(b3)
    return b2 ^ b4
def fonk3(b9, b10, b11):
    with open(b9, "rb") as infile, open(b10, 'wb') as key_out, open(b11, 'wb') as encrypted_out:
        b1 = infile.read(1)
        while b1:
            b2, b4 = fonk1(b1)
            key_out.write(b2.to_bytes(1, b5 = "big", signed=False))
            encrypted_out.write(b4.to_bytes(1, b5 = "big", signed=False))
            b1 = infile.read(1)
def fonk4(b10, b11, b12):
    with open(b10, "rb") as key_in, open(b11, "rb") as encrypted_in, open(b12, 'wb') as outfile:
        b6 = key_in.read(1)
        b3 = encrypted_in.read(1)
        while b6 and b3:
            b7 = fonk2(b6, b3)
            outfile.write(b7.to_bytes(1, b5 = "big", signed=False))
            b6 = key_in.read(1)
            b3 = encrypted_in.read(1)
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