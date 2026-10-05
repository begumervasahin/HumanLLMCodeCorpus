import re
def fonk1(s):
    return (re.match("^[ATCG ]*$",s))
def fonk2(X, Y, b7, b8):
    b1 = [[0 for x in range(b8+1)] for x in range(b7+1)]
    for b2 in range(b7+1):
        for b5 in range(b8+1):
            if b2 = = 0 or b5 == 0:
                b1[b2][b5] = 0
            elif X[b2-1] == Y[b5-1]:
                b1[b2][b5] = b1[b2-1][b5-1] + 1
            else:
                b1[b2][b5] = max(b1[b2-1][b5], b1[b2][b5-1])
    b3 = b1[b7][b8]
    b4 = [""] * (b3+1)
    b4[b3] = "\0"
    b2 = b7
    b5 = b8
    while b2 > 0 and b5 > 0:
        if X[b2-1] == Y[b5-1]:
            b4[b3-1] = X[b2-1]
            b2-=1
            b5-=1
            b3-=1
        elif b1[b2-1][b5] > b1[b2][b5-1]:
            b2-=1
        else:
            b5-=1
    print("\b8\nLCS of " + X + " and " + Y + " is " + "".join(b4) + " \nand length of it is : " + str(len("".join(b4))-1))
s1,b6 = input("Enter the First Sequence\b8").upper(),input("\nEnter the Querying Sequence\b8").upper()
if (fonk1(s1) and fonk1(b6)) and (len(s1)>=len(b6)):
    print((s1,b6))
    b7 = len(s1)
    b8 = len(b6)
    fonk2(s1,b6,b7,b8)
elif (not(len(s1)>=len(b6))):
    print("Querying Sequence should be smaller than First Sequence")
else:
    print("The Sequences should contain 'A','T','C','G',' ' only")