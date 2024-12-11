import re
def fonk1(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
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
    b4 = [''] * (b3 + 1)
    b4[b3] = '\0'
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
    print(f"\b1\nLCS of {X} and {Y} is {''.join(b4)}\nand its length is: {len(''.join(b4)) - 1}")
b6 = input("Enter the First Sequence\b1").upper()
b7 = input("\nEnter the Querying Sequence\b1").upper()
if fonk1(b6) and fonk1(b7) and len(b6) >= len(b7):
    print(b6, b7)
    fonk2(b6, b7)
elif len(b6) < len(b7):
    print("Querying Sequence should be smaller than First Sequence")
else:
    print("The Sequences should contain 'A', 'T', 'C', 'G', or space characters only")