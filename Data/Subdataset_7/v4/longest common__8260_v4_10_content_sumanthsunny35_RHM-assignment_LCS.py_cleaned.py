import re
def fonk1(sequence):
    return re.match("^[ATCG ]*$", sequence)
def fonk2(X, Y):
    b1 = len(X)
    b2 = len(Y)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for b6 in range(1, b2 + 1):
            if X[i - 1] == Y[b6 - 1]:
                b3[i][b6] = b3[i - 1][b6 - 1] + 1
            else:
                b3[i][b6] = max(b3[i - 1][b6], b3[i][b6 - 1])
    b4 = b3[b1][b2]
    b5 = [""] * (b4 + 1)
    b5[b4] = "\0"
    i, b6 = b1, b2
    while i > 0 and b6 > 0:
        if X[i - 1] == Y[b6 - 1]:
            b5[b4 - 1] = X[i - 1]
            i -= 1
            b6 -= 1
            b4 -= 1
        elif b3[i - 1][b6] > b3[i][b6 - 1]:
            i -= 1
        else:
            b6 -= 1
    b7 = "".join(b5).replace("\0", "")
    return b7, len(b7)
def fonk3():
    b8 = input("Enter the First DNA Sequence\b2").upper()
    b9 = input("\nEnter the Querying DNA Sequence\b2").upper()
    if fonk1(b8) and fonk1(b9) and len(b8) >= len(b9):
        lcs_result, b10 = fonk2(b8, b9)
        print(f"\nLongest Common Subsequence of the given two DNA sequences is '{lcs_result}' and its b10 is: {b10}")
    elif len(b8) < len(b9):
        print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain only 'A', 'T', 'C', 'G', or space characters")
if b11 = = "__main__":
    fonk3()