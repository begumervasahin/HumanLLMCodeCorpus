from sys import argv
from os.path import isfile
a1 = 0
a2 = 0
a3 = 1
def fonk1(b1 = None, code=1):
    if b1:
        print(f"Error: {b1}")
    else:
        print("Error: An undefined error occurred!")
    exit(code)
def fonk2(b16):
    try:
        with open(b16, "r") as file:
            b2 = file.read()
    except IOError:
        fonk1(f"Error! Could not open {b16}")
    b3 = b2.strip().split("\n\n")
    if not b3:
        fonk1("Could not find any b3!")
    if b3[0][0] != '>':
        b3 = b3[1:]
    return [fonk3(seq) for seq in b3 if seq]
def fonk3(sequence):
    b4 = sequence.find('\n')
    b5 = sequence[1:b4]
    b6 = sequence[b4 + 1:].replace("\n", "")
    return b5, b6
def fonk4(seq1, seq2):
    len1, b7 = len(seq1), len(seq2)
    b8 = [[""] * (b7 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, b7 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                b8[i][j] = b8[i - 1][j - 1] + seq1[i - 1]
            else:
                b8[i][j] = max(b8[i - 1][j], b8[i][j - 1], b9 = len)
    b10 = b8[len1][b7]
    return len(b10), b10
def fonk5(sequence_dict):
    a4 = 0
    b11 = None
    for b9, seq_object in sequence_dict.items():
        b12 = seq_object[a1]
        if b12 > a4:
            b11 = (b9, seq_object)
            a4 = b12
    return b11
def fonk6(group_name, sequence, b13):
    if group_name not in b13:
        b13[group_name] = []
    b13[group_name].append(sequence)
def fonk7(b3):
    b13 = {}
    for seq in b3:
        max_seq_name, b14 = fonk5(b3[seq])
        b15 = (seq, b14[a1], b14[a3])
        fonk6(max_seq_name, b15, b13)
    return b13
def fonk8(args):
    if len(args) < 2:
        return input("Please enter the b16 containing protein b3: ")
    else:
        b16 = args[1]
    if not isfile(b16):
        fonk1(f"Could not find file '{b16}'")
    return b16
def fonk9(b3):
    b17 = {b5: {} for b5, _ in b3}
    b18 = len(b3)
    for idx, (first_name, first_seq) in enumerate(b3):
        print(f"[{idx + 1}/{b18}] {first_name}...")
        for second_name, second_seq in b3[idx:]:
            if first_name != second_name:
                b12, b19 = fonk4(first_seq, second_seq)
                b17[first_name][second_name] = (b12, b19)
                b17[second_name][first_name] = (b12, b19)
                print(f"   {second_name}... LCS Length: {b12}")
        print()
    return b17
def fonk10(grouped_item, b20 = 2, offset=20):
    b21 = " " * b20
    b22 = f"Name: {grouped_item[a2]}"
    b23 = " " * max(offset - len(b22), 0)
    print(f"{b21} {b22}{b23} Length of LCS: {grouped_item[1]}")
def fonk11(args):
    b16 = fonk8(args)
    b3 = fonk2(b16)
    b17 = fonk9(b3)
    b24 = fonk7(b17)
    for group, items in b24.items():
        print(f"Group {group}:")
        for item in items:
            fonk10(item)
if b25 = = "__main__":
    fonk11(argv)