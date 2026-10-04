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
    return b2
def fonk3(X, Y, b2):
    m, b1 = len(X), len(Y)
    b3 = b2[m][b1]
    b4 = [""] * b3
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
    return "".join(b4)
def fonk4(X, Y):
    b2 = fonk2(X, Y)
    b6 = fonk3(X, Y, b2)
    print(f"\b1\nLCS of {X} and {Y} is {b6} \nand length of it is: {len(b6)}")
def fonk5():
    b7 = input("Enter the First Sequence\b1").upper()
    b8 = input("\nEnter the Querying Sequence\b1").upper()
    if fonk1(b7) and fonk1(b8):
        if len(b7) >= len(b8):
            fonk4(b7, b8)
        else:
            print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain 'A', 'T', 'C', 'G', ' ' only")
if b9 = = "__main__":
    fonk5()