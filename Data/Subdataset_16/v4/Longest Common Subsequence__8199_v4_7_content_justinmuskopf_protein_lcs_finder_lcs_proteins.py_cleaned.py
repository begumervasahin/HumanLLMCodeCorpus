
from sys import argv, exit
from os.path import isfile
a1 = 0
a2 = 0
a3 = 1
def fonk1(b1 = None, code=1):
    if b1:
        print(f"Error: {b1}")
    else:
        print("Error: An Undefined Error Occurred!")
    exit(code)
def fonk2(b14):
    try:
        with open(b14, "r") as f:
            b2 = f.read()
    except IOError:
        fonk1(f"Error! Could not open {b14}")
    b3 = b2.strip().split("\n\n")
    if not b3 or b3[0][0] != '>':
        fonk1("Could not find any b3!")
    return [fonk4(seq) for seq in b3 if seq]
def fonk3(seq1, seq2):
    len1, b4 = len(seq1), len(seq2)
    b5 = [[""] * (b4 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, b4 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                b5[i][j] = b5[i - 1][j - 1] + seq1[i - 1]
            else:
                b5[i][j] = max(b5[i - 1][j], b5[i][j - 1], b6 = len)
    b7 = b5[len1][b4]
    return len(b7), b7
def fonk4(b8):
    b9, b8 = b8.split('\n', 1)
    b9 = b9[1:]
    b8 = b8.replace("\n", "")
    return b9, b8
def fonk5(sequence_dict):
    a4 = 0
    b10 = None
    for b6, seq_data in sequence_dict.items():
        if seq_data[a1] > a4:
            a4 = seq_data[a1]
            b10 = (b6, seq_data)
    return b10
def fonk6(b9, b13, b11):
    if b9 not in b11:
        b11[b9] = []
    b11[b9].append(b13)
def fonk7(b3):
    b11 = {}
    for b8 in b3:
        max_sequence_name, b12 = fonk5(b3[b8])
        b13 = (b8, b12[a1], b12[a3])
        fonk6(max_sequence_name, b13, b11)
    return b11
def fonk8(args):
    if len(args) < 2:
        b14 = input("Please enter the b14 containing protein b3: ")
    else:
        b14 = args[1]
    if not isfile(b14):
        fonk1(f"Could not find file '{b14}'")
    return b14
def fonk9(b3):
    b15 = {b9: {} for b9, _ in b3}
    b16 = len(b3)
    for idx, (name1, seq1) in enumerate(b3):
        print(f"[{idx + 1}/{b16}] {name1}...")
        for name2, seq2 in b3[idx + 1:]:
            b17 = fonk3(seq1, seq2)
            b15[name1][name2] = b15[name2][name1] = b17
            print(f"   {name2}... LCS Length: {b17[a1]}")
        print()
    return b15
def fonk10(item, b18 = 2, b21=20):
    b19 = " " * b18
    b20 = f"Name: {item[a2]}"
    b21 = max(b21 - len(b20), 0) * " "
    print(f"{b19}{b20} {b21}Length of LCS: {item[1]}")
def fonk11(args):
    b14 = fonk8(args)
    b3 = fonk2(b14)
    b22 = fonk9(b3)
    b23 = fonk7(b22)
    for group in b23:
        print(f"Group {group}:")
        for grouped_item in b23[group]:
            fonk10(grouped_item)
if b24 = = "__main__":
    fonk11(argv)