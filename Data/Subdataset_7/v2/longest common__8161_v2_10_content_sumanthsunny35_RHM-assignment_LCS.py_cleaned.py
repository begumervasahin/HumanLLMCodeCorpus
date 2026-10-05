import re
def fonk1(sequence):
    return re.match("^[ATCG ]*$", sequence)
def fonk2(X, Y):
    b1 = len(X)
    b2 = len(Y)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for b6 in range(1, b1 + 1):
        for b7 in range(1, b2 + 1):
            if X[b6 - 1] == Y[b7 - 1]:
                b3[b6][b7] = b3[b6 - 1][b7 - 1] + 1
            else:
                b3[b6][b7] = max(b3[b6 - 1][b7], b3[b6][b7 - 1])
    b4 = b3[b1][b2]
    b5 = [""] * (b4 + 1)
    b5[b4] = "\0"
    b6 = b1
    b7 = b2
    while b6 > 0 and b7 > 0:
        if X[b6 - 1] == Y[b7 - 1]:
            b5[b4 - 1] = X[b6 - 1]
            b6 -= 1
            b7 -= 1
            b4 -= 1
        elif b3[b6 - 1][b7] > b3[b6][b7 - 1]:
            b6 -= 1
        else:
            b7 -= 1
    b8 = "".join(b5).replace("\0", "")
    return b8, len(b8)
def fonk3():
    b9 = input("Enter the First Sequence\b2").upper()
    b10 = input("\nEnter the Querying Sequence\b2").upper()
    if fonk1(b9) and fonk1(b10) and len(b9) >= len(b10):
        lcs_result, b11 = fonk2(b9, b10)
        print(f"\nLongest Common Subsequence of the given two DNA sequences is {lcs_result} and its b11 is: {b11}")
    elif len(b9) < len(b10):
        print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain only 'A', 'T', 'C', 'G', or space characters")
if b12 = = "__main__":
    fonk3()