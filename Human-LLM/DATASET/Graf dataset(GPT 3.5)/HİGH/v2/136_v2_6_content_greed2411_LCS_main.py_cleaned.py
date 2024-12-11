import re
def fonk1(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def fonk2(seq1, seq2, b9, b10):
    b1 = [[0 for _ in range(b10+1)] for _ in range(b9+1)]
    for b2 in range(b9+1):
        for b5 in range(b10+1):
            if b2 = = 0 or b5 == 0:
                b1[b2][b5] = 0
            elif seq1[b2-1] == seq2[b5-1]:
                b1[b2][b5] = b1[b2-1][b5-1] + 1
            else:
                b1[b2][b5] = max(b1[b2-1][b5], b1[b2][b5-1])
    b3 = b1[b9][b10]
    b4 = [""] * (b3+1)
    b4[b3] = "\0"
    b2 = b9
    b5 = b10
    while b2 > 0 and b5 > 0:
        if seq1[b2-1] == seq2[b5-1]:
            b4[b3-1] = seq1[b2-1]
            b2 -= 1
            b5 -= 1
            b3 -= 1
        elif b1[b2-1][b5] > b1[b2][b5-1]:
            b2 -= 1
        else:
            b5 -= 1
    b6 = "".join(b4)
    print("\n\nThe Longest Common Subsequence of " + seq1 + " and " + seq2 + " is " + b6 +
          " \nand its length is: " + str(len(b6)-1))
b7 = input("Enter the First Sequence\n").upper()
b8 = input("\nEnter the Querying Sequence\n").upper()
if (fonk1(b7) and fonk1(b8)) and (len(b7) >= len(b8)):
    print(b7, b8)
    b9 = len(b7)
    b10 = len(b8)
    fonk2(b7, b8, b9, b10)
elif not (len(b7) >= len(b8)):
    print("The Querying Sequence should be shorter than the First Sequence")
else:
    print("Both sequences should only contain 'A', 'T', 'C', 'G', or space characters")