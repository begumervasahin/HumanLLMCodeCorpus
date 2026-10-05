def fonk1(b5,b6):
    b1 = len(b5)
    b2 = len(b6)
    b3 = [[None]*(b2+1) for b4 in range(b1+1)]
    for b4 in range(b1+1):
        for j in range(b2+1):
            if b4 = = 0 or j == 0:
                b3[b4][j]=0
            elif b5[b4-1] == b6[j-1]:
                b3[b4][j] = b3[b4-1][j-1]+1
            else:
                b3[b4][j] = max(b3[b4-1][j],b3[b4][j-1])
    return b3[b1][b2]
b5 = input("First string : ")
b6 = input("Second string: ")
print("The length of LCS is : ",fonk1(b5,b6))