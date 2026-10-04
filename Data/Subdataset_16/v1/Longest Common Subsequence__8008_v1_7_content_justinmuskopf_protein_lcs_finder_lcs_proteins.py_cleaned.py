from sys import argv
from os.path import isfile
a1 = 0
a2 = 0
a3 = 1
def fonk1(b1 = None, code=1):
    if b1:
        print("Error: {}".format(b1))
    else:
        print("Error: An Undefined Error Occurred!")
    exit(code)
def fonk2(b25):
    try:
        with open(b25, "r") as f:
            b2 = f.read()
    except IOError:
        fonk1("Error! Could not open {}".format(b25))
    b3 = b2.strip().split("\n\n")
    if len(b3) == 0:
        fonk1("Could not find any b3!")
    if b3[0][0] != '>':
        b3 = b3[1:]
    b3 = [fonk4(b7) for b7 in b3 if b7 != '']
    return b3
def fonk3(sequence_1, sequence_2):
    b4 = len(sequence_1)
    b5 = len(sequence_2)
    b6 = [[""] * (b5 + 1) for _ in range(b4 + 1)]
    for b7 in range(b4 + 1):
        for j in range(b5 + 1):
            if b7 = = 0 or j == 0:
                continue
            b8 = sequence_1[b7 - 1]
            b9 = sequence_2[j - 1]
            if b8 = = b9:
                b6[b7][j] = b6[b7 - 1][j - 1] + b8
            else:
                b10 = b6[b7 - 1][j]
                b11 = len(b10)
                b12 = b6[b7][j - 1]
                b13 = len(b12)
                b6[b7][j] = b10 if b11 > b13 else b12
    b14 = b6[b4][b5]
    return len(b14), b14
def fonk4(b17):
    b15 = b17.find('\n')
    b16 = b17[1:b15]
    b17 = b17[b15 + 1:].replace("\n", "")
    return b16, b17
def fonk5(b17):
    a4 = 0
    b18 = None
    for key in b17:
        b19 = b17[key]
        b20 = b19[a1]
        if b20 > a4:
            b18 = (key, b19)
            a4 = b20
    return b18
def fonk6(b16, b23, b21):
    if b16 not in b21:
        b21[b16] = []
    b21[b16].append(b23)
def fonk7(b3):
    b21 = {}
    for b17 in b3:
        max_sequence_name, b22 = fonk5(b3[b17])
        b23 = (b17, b22[a1], b22[a3])
        fonk6(max_sequence_name, b23, b21)
    return b21
def fonk8(args):
    b24 = len(args)
    if b24 < 2:
        b25 = input("Please enter the b25 containing protein b3: ")
    else:
        b25 = args[1]
    if not isfile(b25):
        fonk1("Could not find file '{}'".format(b25))
    return b25
def fonk9(b3):
    b26 = {}
    for b16, _ in b3:
        b26[b16] = {}
    b27 = len(b3)
    for sequence_idx, first_sequence_data in enumerate(b3):
        b28 = first_sequence_data[a2]
        b29 = first_sequence_data[a3]
        print("[{}/{}] {}...".format(sequence_idx + 1, b27, b28))
        for second_name, second_sequence in b3[sequence_idx:]:
            if b28 = = second_name:
                continue
            b30 = fonk3(b29, second_sequence)
            b26[b28][second_name] = b30
            b26[second_name][b28] = b30
            print("   {}... LCS Length: {}".format(second_name, b30[a1]))
        print()
    return b26
def fonk10(item, b31 = 2, b34=20):
    b32 = " " * b31
    b33 = "Name: {}".format(item[a2])
    b34 = max(b34 - len(b33), 0) * " "
    b33 += b34
    print("{} {} Length of LCS: {}".format(b32, b33, item[1]))
def fonk11(args):
    b25 = fonk8(args)
    b3 = fonk2(b25)
    b35 = fonk9(b3)
    b36 = fonk7(b35)
    for group in b36:
        print("Group {}:".format(group))
        for grouped_item in b36[group]:
            fonk10(grouped_item)
if b37 = = "__main__":
    fonk11(argv)