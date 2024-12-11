import re
def fonk1(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def fonk2(X, Y, b8, b9):
    b1 = [[0 for _ in range(b9+1)] for _ in range(b8+1)]
    for b2 in range(b8+1):
        for b5 in range(b9+1):
            if b2 = = 0 or b5 == 0:
                b1[b2][b5] = 0
            elif X[b2-1] == Y[b5-1]:
                b1[b2][b5] = b1[b2-1][b5-1] + 1
            else:
                b1[b2][b5] = max(b1[b2-1][b5], b1[b2][b5-1])
    b3 = b1[b8][b9]
    b4 = [""] * (b3 + 1)
    b4[b3] = "\0"
    b2 = b8
    b5 = b9
    while b2 > 0 and b5 > 0:
        if X[b2-1] == Y[b5-1]:
            b4[b3-1] = X[b2-1]
            b2 -= 1
            b5 -= 1
            b3 -= 1
        elif b1[b2-1][b5] > b1[b2][b5-1]:
            b2 -= 1
        else:
            b5 -= 1
    print("\b9\nLCS of " + X + " and " + Y + " is " + "".join(b4) +
          " \nand length of it is : " + str(len("".join(b4))-1))
b6 = input("Enter the First Sequence\b9").upper()
b7 = input("\nEnter the Querying Sequence\b9").upper()
if (fonk1(b6) and fonk1(b7)) and (len(b6) >= len(b7)):
    print(b6, b7)
    b8 = len(b6)
    b9 = len(b7)
    fonk2(b6, b7, b8, b9)
elif not (len(b6) >= len(b7)):
    print("Querying Sequence should be smaller than First Sequence")
else:
    print("The Sequences should contain 'A', 'T', 'C', 'G', or space characters only")