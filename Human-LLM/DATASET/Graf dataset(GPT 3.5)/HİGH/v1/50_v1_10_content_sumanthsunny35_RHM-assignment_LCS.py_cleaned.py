import re
def fonk1(s):
    return re.match("^[ATCG ]*$", s)
def fonk2(X, Y, m, n):
    b1 = [[0] * (n + 1) for _ in range(m + 1)]
    for b2 in range(m + 1):
        for b5 in range(n + 1):
            if b2 = = 0 or b5 == 0:
                b1[b2][b5] = 0
            elif X[b2 - 1] == Y[b5 - 1]:
                b1[b2][b5] = b1[b2 - 1][b5 - 1] + 1
            else:
                b1[b2][b5] = max(b1[b2 - 1][b5], b1[b2][b5 - 1])
    b3 = b1[m][n]
    b4 = [""] * (b3 + 1)
    b4[b3] = "\0"
    b2 = m
    b5 = n
    while b2 > 0 and b5 > 0:
        if X[b2 - 1] == Y[b5 - 1]:
            b4[b3 - 1] = X[b2 - 1]
            b2 -= 1
            b5 -= 1
            b3 -= 1
        elif b1[b2 - 1][b5] > b1[b2][b5 - 1]:
            b2 -= 1
        else:
            b5 -= 1
    b6 = "".join(b4).replace("\0", "")
    return b6, len(b6)
b7 = input("Enter the First Sequence\n").upper()
b8 = input("\nEnter the Querying Sequence\n").upper()
if fonk1(b7) and fonk1(b8) and len(b7) >= len(b8):
    lcs_result, b9 = fonk2(b7, b8, len(b7), len(b8))
    print(f"\nLCS of the given two DNA sequences is {lcs_result} and its b9 is: {b9}")
elif len(b7) < len(b8):
    print("Querying Sequence should be smaller than First Sequence")
else:
    print("The Sequences should contain only 'A', 'T', 'C', 'G', or space characters")