import sys
import numpy as np
def fonk1(b8):
    b1 = np.ones(len(b8))
    for i, char in enumerate(b8):
        b1[i] = ord(char)
    b1 = b1.astype(int)
    b2 = np.ones(3 * len(b1))
    for i, num in enumerate(b1):
        if fonk4(num) == 3:
            b2[3*i] = num
            b2[3*i + 1] = num
            b2[3*i + 2] = num % 10
        elif fonk4(num) == 2:
            b2[3*i] = 0
            b2[3*i + 1] = num
            b2[3*i + 2] = num % 10
        else:
            b2[3*i] = 0
            b2[3*i + 1] = 0
            b2[3*i + 2] = num % 10
    b2 = b2.astype(int)
    return b2
def fonk2(converted_array, pad):
    b3 = len(converted_array)
    b4 = [(converted_array[i] + pad[i]) % 10 for i in range(b3)]
    return b4
def fonk3(encrypted_array, pad):
    b3 = len(encrypted_array)
    b5 = []
    for i in range(0, b3, 3):
        b6 = ((encrypted_array[i] - pad[i] + 10) % 10) * 100
        b6 += ((encrypted_array[i + 1] - pad[i + 1] + 10) % 10) * 10
        b6 += ((encrypted_array[i + 2] - pad[i + 2] + 10) % 10)
        b5.append(b6)
    return b5
def fonk4(b7):
    if b7 = = 0:
        return 1
    if b7 < 0:
        b7 *= -1
    a1 = 0
    while b7 != 0:
        b7
        a1 += 1
    return a1
def fonk5():
    if len(sys.argv) != 4:
        sys.exit("Error: incorrect number of arguments")
    try:
        with open(sys.argv[2]) as message_file:
            b8 = message_file.read()
    except IOError:
        sys.exit("Error: cannot open message file")
    try:
        with open(sys.argv[3]) as pad_file:
            b9 = pad_file.read()
    except IOError:
        sys.exit("Error: cannot open pad file")
    b10 = [int(char) for char in b9 if char.isdigit()]
    if sys.argv[1] == "encrypt":
        b1 = fonk1(b8)
        if len(b10) < len(b1):
            sys.exit("Error: pad is shorter than numeric version of message")
        b11 = fonk2(b1, b10)
        b12 = "encrypted_" + sys.argv[2]
        b13 = "".join(map(str, b11)) + "\n"
        with open(b12, "w+") as outfile:
            outfile.write(b13)
    elif sys.argv[1] == "decrypt":
        b14 = [int(char) for char in b8 if char.isdigit()]
        if len(b10) < len(b14):
            sys.exit("Error: pad is shorter than numeric version of message")
        b5 = fonk3(b14, b10)
        b12 = "decrypted_" + sys.argv[2]
        b13 = "".join(map(chr, b5))
        with open(b12, "w+") as outfile:
            outfile.write(b13)
    else:
        print("Error: incorrect command, must be \"encrypt\" or \"decrypt\"")
if b15 = = "__main__":
    fonk5()