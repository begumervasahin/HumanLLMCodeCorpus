import random
import sys
def fonk1(b6):
    b1 = ord(b6)
    b2 = random.randint(0, 255)
    b3 = b1 ^ b2
    return b2, b3
def fonk2(b9, b3):
    b4 = ord(b9)
    b5 = ord(b3)
    return b4 ^ b5
def fonk3(b12, b13, b14):
    with open(b12, "rb") as infile, open(b13, 'wb') as key_out, open(b14, 'wb') as encrypted_out:
        b6 = infile.read(1)
        while b6:
            b2, b7 = fonk1(b6)
            key_out.write(b2.to_bytes(1, b8 = "big", signed=False))
            encrypted_out.write(b7.to_bytes(1, b8 = "big", signed=False))
            b6 = infile.read(1)
def fonk4(b13, b14, b15):
    with open(b13, "rb") as key_in, open(b14, "rb") as encrypted_in, open(b15, 'wb') as outfile:
        b9 = key_in.read(1)
        b3 = encrypted_in.read(1)
        while b9 and b3:
            b10 = fonk2(b9, b3)
            outfile.write(b10.to_bytes(1, b8 = "big", signed=False))
            b9 = key_in.read(1)
            b3 = encrypted_in.read(1)
if b11 = = "__main__":
    print("Starting script...")
    if len(sys.argv) == 2:
        b12 = sys.argv[1]
        fonk3(b12, b12 + ".b2", b12 + ".enc")
    elif len(sys.argv) == 3:
        b13 = sys.argv[1]
        b14 = sys.argv[2]
        b15 = b13[:-4]
        fonk4(b13, b14, b15)
    else:
        print("Argument parsing error. Usage:")
        print("  To encrypt: python script.py b12")
        print("  To decrypt: python script.py b13 b14")
    print("Script finished.")