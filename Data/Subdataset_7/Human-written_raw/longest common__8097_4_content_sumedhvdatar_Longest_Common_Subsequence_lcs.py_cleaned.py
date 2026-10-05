import numpy as np
def fonk1(b1,position_column):
    if b1 = = 1 and position_column == 1:
        return b10
    if b8[b1][position_column] == b8[b1][position_column-1]:
        fonk1(b1,position_column-1)
    elif b8[b1][position_column] == b8[b1-1][position_column]:
        fonk1(b1-1,position_column)
    else:
        b2 = b8[b1-1][position_column-1]
        if(b8[b1][position_column] == b2 + 1):
            b10.append(b8[0][position_column])
            fonk1(b1-1,position_column-1)
b3 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
b4 = " GTCGTTCGGAATGCCGTTGCTCTGTAAA"
b5 = []
for letter in b3:
    b5.append(letter)
b6 = len(b5)+2
b5 = []
for letter in b4:
    b5.append(letter)
b7 = len(b5)+2
print b7,b6
b8 = [[0 for x in range(b6)] for y in range(b7)]
a1 = 0
a2 = 0
b8[0][0] = "L"
b8[0][1] = "P"
a2 = 2
for letter in b3:
    b8[0][a2] = letter
    b8[1][a2] = int(0)
    a2 = a2 + 1
b8[1][0] = "P"
a1 = 2
for letter in b4:
    b8[a1][0] = letter
    b8[a1][1] = int(0)
    a1 = a1 + 1
a1 = 2
a2 = 2
for i in range(2,b7,1):
    for j in range(2,b6,1):
        if(b8[a1][0] == b8[0][a2]):
            b9 = b8[a1 -1][a2-1]
            b8[a1][a2] = b9 + 1
        else:
            b8[a1][a2] = max(b8[a1][a2-1],b8[a1-1][a2])
        a2 = a2 + 1
    a1 = a1 + 1
    a2 = 2
print "Printing the matrix"
print np.matrix(b8)
b10 = []
print "We are sending b7 "+str(b7)
print "We are sending b6 "+str(b6)
b11 = fonk1(b7-1,b6-1)
b12 = "".join(str(x) for x in b10)
print b12[::-1]