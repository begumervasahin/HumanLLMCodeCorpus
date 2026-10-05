import re
def fonk1(b6):
    return bool(re.match("^[ATCG ]*$", b6))
def fonk2(seq1, seq2):
    m, b1 = len(seq1), len(seq2)
    b2 = [[0] * (b1 + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for b5 in range(1, b1 + 1):
            if seq1[i - 1] == seq2[b5 - 1]:
                b2[i][b5] = b2[i - 1][b5 - 1] + 1
            else:
                b2[i][b5] = max(b2[i - 1][b5], b2[i][b5 - 1])
    return b2[m][b1]
def fonk3(seq1, seq2):
    m, b1 = len(seq1), len(seq2)
    b2 = [[0] * (b1 + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for b5 in range(1, b1 + 1):
            if seq1[i - 1] == seq2[b5 - 1]:
                b2[i][b5] = b2[i - 1][b5 - 1] + 1
            else:
                b2[i][b5] = max(b2[i - 1][b5], b2[i][b5 - 1])
    b3 = b2[m][b1]
    b4 = [""] * (b3 + 1)
    b4[b3] = "\0"
    i, b5 = m, b1
    while i > 0 and b5 > 0:
        if seq1[i - 1] == seq2[b5 - 1]:
            b4[b3 - 1] = seq1[i - 1]
            i -= 1
            b5 -= 1
            b3 -= 1
        elif b2[i - 1][b5] > b2[i][b5 - 1]:
            i -= 1
        else:
            b5 -= 1
    return "".join(b4).replace("\0", "")
def fonk4(prompt):
    while True:
        b6 = input(prompt).upper()
        if fonk1(b6):
            return b6
        print("Invalid input. Please enter a b6 containing only 'A', 'T', 'C', 'G', ' '.")
def fonk5():
    b7 = fonk4("Enter the First Sequence: ")
    b8 = fonk4("Enter the Querying Sequence: ")
    if len(b7) >= len(b8):
        print(f"\nSequences: {b7}, {b8}")
        b9 = fonk3(b7, b8)
        print(f"\nLongest Common Subsequence: {b9}\nLength: {len(b9)}")
    else:
        print("Querying Sequence should be smaller than First Sequence.")
if b10 = = "__main__":
    fonk5()