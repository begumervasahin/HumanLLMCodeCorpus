import re
def fonk1(sequence):
    return re.match("^[ATCG ]*$", sequence)
def fonk2(X, Y):
    m, b1 = len(X), len(Y)
    b2 = [[0] * (b1 + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for b5 in range(1, b1 + 1):
            if X[i - 1] == Y[b5 - 1]:
                b2[i][b5] = b2[i - 1][b5 - 1] + 1
            else:
                b2[i][b5] = max(b2[i - 1][b5], b2[i][b5 - 1])
    b3 = b2[m][b1]
    b4 = [""] * (b3 + 1)
    b4[b3] = "\0"
    i, b5 = m, b1
    while i > 0 and b5 > 0:
        if X[i - 1] == Y[b5 - 1]:
            b4[b3 - 1] = X[i - 1]
            i -= 1
            b5 -= 1
            b3 -= 1
        elif b2[i - 1][b5] > b2[i][b5 - 1]:
            i -= 1
        else:
            b5 -= 1
    b6 = "".join(b4).replace("\0", "")
    return b6, len(b6)
def fonk3():
    b7 = input("Enter the First Sequence\b1").upper()
    b8 = input("\nEnter the Querying Sequence\b1").upper()
    if fonk1(b7) and fonk1(b8) and len(b7) >= len(b8):
        lcs_result, b9 = fonk2(b7, b8)
        print(f"\nLongest Common Subsequence of the given two DNA sequences is {lcs_result} and its b9 is: {b9}")
    elif len(b7) < len(b8):
        print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain only 'A', 'T', 'C', 'G', or space characters")
if b10 = = "__main__":
    fonk3()