import re
def fonk1(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def fonk2(X, Y):
    m, b1 = len(X), len(Y)
    b2 = [[0 for _ in range(b1+1)] for _ in range(m+1)]
    for b3 in range(m+1):
        for b6 in range(b1+1):
            if b3 = = 0 or b6 == 0:
                b2[b3][b6] = 0
            elif X[b3-1] == Y[b6-1]:
                b2[b3][b6] = b2[b3-1][b6-1] + 1
            else:
                b2[b3][b6] = max(b2[b3-1][b6], b2[b3][b6-1])
    b4 = b2[m][b1]
    b5 = [""] * (b4 + 1)
    b5[b4] = "\0"
    b3, b6 = m, b1
    while b3 > 0 and b6 > 0:
        if X[b3-1] == Y[b6-1]:
            b5[b4-1] = X[b3-1]
            b3 -= 1
            b6 -= 1
            b4 -= 1
        elif b2[b3-1][b6] > b2[b3][b6-1]:
            b3 -= 1
        else:
            b6 -= 1
    b7 = "".join(b5).strip("\0")
    print(f"\b1\nLCS of {X} and {Y} is {b7} \nand length of it is: {len(b7)}")
b8 = input("Enter the First Sequence: ").upper()
b9 = input("Enter the Querying Sequence: ").upper()
if fonk1(b8) and fonk1(b9):
    if len(b8) >= len(b9):
        print(b8, b9)
        fonk2(b8, b9)
    else:
        print("Querying Sequence should be smaller than First Sequence")
else:
    print("The Sequences should contain 'A', 'T', 'C', 'G', ' ' only")