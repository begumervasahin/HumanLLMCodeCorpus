import sys
import numpy as np
def fonk1(b6):
    b1 = np.ones(len(b6))
    for i, char in enumerate(b6):
        b1[i] = ord(char)
    b1 = b1.astype(int)
    b2 = np.ones(3 * len(b1))
    for i, num in enumerate(b1):
        b2[3*i:3*(i+1)] = [int(d) for d in str(num).zfill(3)]
    b2 = b2.astype(int)
    return b2
def fonk2(converted_array, pad):
    b3 = [(converted_array[i] + pad[i]) % 10 for i in range(len(converted_array))]
    return b3
def fonk3(encrypted_array, pad):
    b4 = []
    for i in range(0, len(encrypted_array), 3):
        b5 = int("".join(str((encrypted_array[i+j] - pad[i+j] + 10) % 10) for j in range(3)))
        b4.append(b5)
    return b4
def fonk4():
    if len(sys.argv) != 4:
        sys.exit("Error: incorrect number of arguments")
    try:
        with open(sys.argv[2]) as message_file:
            b6 = message_file.read()
    except IOError:
        sys.exit("Error: cannot open message file")
    try:
        with open(sys.argv[3]) as pad_file:
            b7 = pad_file.read()
    except IOError:
        sys.exit("Error: cannot open pad file")
    b8 = [int(char) for char in b7 if char.isdigit()]
    if sys.argv[1] == "encrypt":
        b1 = fonk1(b6)
        if len(b8) < len(b1):
            sys.exit("Error: pad is shorter than numeric version of message")
        b9 = fonk2(b1, b8)
        b10 = "encrypted_" + sys.argv[2]
        b11 = "".join(map(str, b9)) + "\n"
        with open(b10, "w+") as outfile:
            outfile.write(b11)
    elif sys.argv[1] == "decrypt":
        b12 = [int(char) for char in b6 if char.isdigit()]
        if len(b8) < len(b12):
            sys.exit("Error: pad is shorter than numeric version of message")
        b4 = fonk3(b12, b8)
        b10 = "decrypted_" + sys.argv[2]
        b11 = "".join(map(chr, b4))
        with open(b10, "w+") as outfile:
            outfile.write(b11)
    else:
        print("Error: incorrect command, must be \"encrypt\" or \"decrypt\"")
if b13 = = "__main__":
    fonk4()