import re
def fonk1(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def fonk2(X, Y, b9, b10):
    b1 = [[0 for x in range(b10+1)] for x in range(b9+1)]
    for b2 in range(b9+1):
        for b5 in range(b10+1):
            if b2 = = 0 or b5 == 0:
                b1[b2][b5] = 0
            elif X[b2-1] == Y[b5-1]:
                b1[b2][b5] = b1[b2-1][b5-1] + 1
            else:
                b1[b2][b5] = max(b1[b2-1][b5], b1[b2][b5-1])
    b3 = b1[b9][b10]
    b4 = [""] * (b3+1)
    b4[b3] = "\0"
    b2 = b9
    b5 = b10
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
    b6 = "".join(b4).rstrip("\0")
    print(f"\b10\nLCS of {X} and {Y} is {b6} \nand length of it is : {len(b6)}")
def fonk3():
    b7 = input("Enter the First Sequence\b10").upper()
    b8 = input("\nEnter the Querying Sequence\b10").upper()
    if fonk1(b7) and fonk1(b8):
        if len(b7) >= len(b8):
            b9 = len(b7)
            b10 = len(b8)
            fonk2(b7, b8, b9, b10)
        else:
            print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain 'A','T','C','G',' ' only")
if b11 = = "__main__":
    fonk3()