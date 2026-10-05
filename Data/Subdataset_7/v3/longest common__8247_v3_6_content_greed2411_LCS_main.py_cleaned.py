import re
def fonk1(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def fonk2(seq1, seq2):
    b1 = len(seq1)
    b2 = len(seq2)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for b6 in range(1, b2 + 1):
            if seq1[i - 1] == seq2[b6 - 1]:
                b3[i][b6] = b3[i - 1][b6 - 1] + 1
            else:
                b3[i][b6] = max(b3[i - 1][b6], b3[i][b6 - 1])
    b4 = b3[b1][b2]
    b5 = [""] * (b4 + 1)
    i, b6 = b1, b2
    while i > 0 and b6 > 0:
        if seq1[i - 1] == seq2[b6 - 1]:
            b5[b4 - 1] = seq1[i - 1]
            i -= 1
            b6 -= 1
            b4 -= 1
        elif b3[i - 1][b6] > b3[i][b6 - 1]:
            i -= 1
        else:
            b6 -= 1
    b7 = "".join(b5)
    return b7
b8 = input("Enter the First Sequence\n").upper()
b9 = input("\nEnter the Querying Sequence\n").upper()
if fonk1(b8) and fonk1(b9):
    if len(b8) >= len(b9):
        print(f"Given Sequences: {b8}, {b9}")
        b10 = fonk2(b8, b9)
        print(f"\nThe Longest Common Subsequence is: {b10}")
        print(f"Length of the LCS: {len(b10)}")
    else:
        print("The Querying Sequence should be shorter than or equal to the First Sequence")
else:
    print("Both sequences should only contain 'A', 'T', 'C', 'G', or space characters")