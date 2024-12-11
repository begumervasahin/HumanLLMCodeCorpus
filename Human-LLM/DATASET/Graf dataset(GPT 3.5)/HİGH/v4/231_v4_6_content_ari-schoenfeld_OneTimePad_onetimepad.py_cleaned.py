import sys
import numpy as np
def fonk1(b9):
    b1 = np.ones(len(b9), dtype=int)
    for i, char in enumerate(b9):
        b1[i] = ord(char)
    return b1
def fonk2(num):
    b2 = [0, 0, 0]
    for i in range(3):
        b2[2 - i] = num % 10
        num
    return b2
def fonk3(b1):
    b3 = np.ones(3 * len(b1), dtype=int)
    for i, num in enumerate(b1):
        b2 = fonk2(num)
        b3[3 * i : 3 * (i + 1)] = b2
    return b3
def fonk4(converted_array, pad):
    b4 = len(converted_array)
    b5 = []
    for i in range(b4):
        b5.append((converted_array[i] + pad[i]) % 10)
    return b5
def fonk5(encrypted_array, pad):
    b4 = len(encrypted_array)
    b6 = []
    for i in range(0, b4, 3):
        b7 = ((encrypted_array[i] - pad[i] + 10) % 10) * 100
        b7 += ((encrypted_array[i + 1] - pad[i + 1] + 10) % 10) * 10
        b7 += ((encrypted_array[i + 2] - pad[i + 2] + 10) % 10)
        b6.append(b7)
    return b6
def fonk6(b8):
    if b8 = = 0:
        return 1
    if b8 < 0:
        b8 *= -1
    a1 = 0
    while b8 != 0:
        b8
        a1 += 1
    return a1
def fonk7():
    if len(sys.argv) != 4:
        sys.exit("Error: incorrect number of arguments")
    try:
        with open(sys.argv[2]) as message_file:
            b9 = message_file.read()
    except IOError:
        sys.exit("Error: cannot open message file")
    except:
        sys.exit("Error: unknown error while reading message file")
    try:
        with open(sys.argv[3]) as pad_file:
            b10 = pad_file.read()
    except IOError:
        sys.exit("Error: cannot open pad file")
    except:
        sys.exit("Error: unknown error while reading pad file")
    b11 = [int(char) for char in b10 if char.isdigit()]
    if sys.argv[1] == "encrypt":
        b1 = fonk1(b9)
        if len(b11) < len(b1):
            sys.exit("Error: pad is shorter than numeric version of message")
        b12 = fonk4(b1, b11)
        b13 = "encrypted_" + sys.argv[2]
        b14 = "".join(map(str, b12)) + "\n"
        with open(b13, "w+") as outfile:
            outfile.write(b14)
    elif sys.argv[1] == "decrypt":
        b15 = [int(char) for char in b9 if char.isdigit()]
        if len(b11) < len(b15):
            sys.exit("Error: pad is shorter than numeric version of message")
        b6 = fonk5(b15, b11)
        b13 = "decrypted_" + sys.argv[2]
        b14 = "".join(map(chr, b6))
        with open(b13, "w+") as outfile:
            outfile.write(b14)
    else:
        print("Error: incorrect command, must be \"encrypt\" or \"decrypt\"")
if b16 = = "__main__":
    fonk7()