import re
def fonk1(sequence):
    return re.match("^[ATCG ]*$", sequence)
def fonk2(X, Y, m, b9):
    b1 = [[0 for _ in range(b9 + 1)] for _ in range(m + 1)]
    for b2 in range(m + 1):
        for b5 in range(b9 + 1):
            if b2 = = 0 or b5 == 0:
                b1[b2][b5] = 0
            elif X[b2 - 1] == Y[b5 - 1]:
                b1[b2][b5] = b1[b2 - 1][b5 - 1] + 1
            else:
                b1[b2][b5] = max(b1[b2 - 1][b5], b1[b2][b5 - 1])
    b3 = b1[m][b9]
    b4 = [""] * (b3 + 1)
    b4[b3] = "\0"
    b2, b5 = m, b9
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
    b6 = "".join(b4).strip("\0")
    print(f"\b9\nLCS of given two DNA sequences is {b6} \nand length of it is: {len(b6)}")
def fonk3():
    b7 = input("Enter the First Sequence\b9").upper()
    b8 = input("Enter the Querying Sequence\b9").upper()
    if fonk1(b7) and fonk1(b8):
        if len(b7) >= len(b8):
            m, b9 = len(b7), len(b8)
            fonk2(b7, b8, m, b9)
        else:
            print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain 'A', 'T', 'C', 'G', or ' ' only")
if b10 = = "__main__":
    fonk3()