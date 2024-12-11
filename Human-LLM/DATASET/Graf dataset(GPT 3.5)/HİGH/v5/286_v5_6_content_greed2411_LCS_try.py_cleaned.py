import re
def fonk1(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def fonk2(X, Y, m, n):
    b1 = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for b2 in range(m + 1):
        for b5 in range(n + 1):
            if b2 = = 0 or b5 == 0:
                b1[b2][b5] = 0
            elif X[b2 - 1] == Y[b5 - 1]:
                b1[b2][b5] = b1[b2 - 1][b5 - 1] + 1
            else:
                b1[b2][b5] = max(b1[b2 - 1][b5], b1[b2][b5 - 1])
    return b1
def fonk3(X, Y, m, n):
    b1 = fonk2(X, Y, m, n)
    b3 = b1[m][n]
    b4 = [""] * (b3 + 1)
    b4[b3] = "\0"
    b2, b5 = m, n
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
    return b6, len(b6) - 1
def fonk4():
    b7 = input("Enter the First Sequence\n").upper()
    b8 = input("\nEnter the Querying Sequence\n").upper()
    if fonk1(b7) and fonk1(b8) and len(b7) >= len(b8):
        print(f"Sequences: {b7}, {b8}")
        lcs_result, b9 = fonk3(b7, b8, len(b7), len(b8))
        print(f"\nLongest Common Subsequence: {lcs_result}\nLength: {b9}")
    elif not (len(b7) >= len(b8)):
        print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain 'A', 'T', 'C', 'G', ' ' only")
if b10 = = "__main__":
    fonk4()