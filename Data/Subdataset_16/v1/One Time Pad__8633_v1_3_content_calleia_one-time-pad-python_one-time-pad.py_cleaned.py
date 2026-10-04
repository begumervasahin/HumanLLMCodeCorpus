import random
import sys
def fonk1(b1):
    b1 = ord(b1)
    b2 = []
    b2.append(random.randint(0, 255))
    b2.append(b1 ^ b2[0])
    return b2
def fonk2(byte0, b5):
    b2 = []
    b2.append(ord(byte0))
    b2.append(ord(b5))
    b3 = b2[0] ^ b2[1]
    return b3
def fonk3(input_file, output1, output2):
    with open(input_file, "rb") as f, open(output1, 'wb') as key1File, open(output2, 'wb') as key2File:
        b1 = f.read(1)
        while b1:
            b3 = fonk1(b1)
            key1File.write(b3[0].to_bytes(1, b4 = "big", signed=False))
            key2File.write(b3[1].to_bytes(1, b4 = "big", signed=False))
            b1 = f.read(1)
def fonk4(input1, input2, output_file):
    with open(input1, "rb") as f1, open(input2, "rb") as f2, open(output_file, 'wb') as output:
        b5 = f1.read(1)
        b6 = f2.read(1)
        while b5 and b6:
            output.write(fonk2(b5, b6).to_bytes(1, b4 = "big", signed=False))
            b5 = f1.read(1)
            b6 = f2.read(1)
if b7 = = "__main__":
    print("Starting script...")
    if len(sys.argv) == 2:
        fonk3(sys.argv[1], sys.argv[1] + ".0", sys.argv[1] + ".1")
    elif len(sys.argv) == 3:
        fonk4(sys.argv[1], sys.argv[2], sys.argv[1][:-2])
    else:
        print("Argument parsing error.")
    print("Script finished.")