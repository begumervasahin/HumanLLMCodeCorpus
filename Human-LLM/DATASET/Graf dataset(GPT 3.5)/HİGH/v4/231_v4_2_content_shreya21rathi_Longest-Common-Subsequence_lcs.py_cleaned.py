def fonk1(b9, b10):
    b1 = []
    a1 = 0
    for b3 in range(len(b9) + 1):
        b2 = []
        for j in range(len(b10) + 1):
            if b3 = = 0 or j == 0:
                b2.append('0H')
            else:
                if b9[b3 - 1] != b10[j - 1]:
                    b4 = b1[b3 - 1][j]
                    b5 = b2[j - 1]
                    if int(b4[:-1]) >= int(b5[:-1]):
                        b2.append('{0}U'.format(b4[:-1]))
                    else:
                        b2.append('{0}S'.format(b5[:-1]))
                else:
                    b6 = b1[b3 - 1][j - 1]
                    b2.append('{0}D'.format(str(int(b6[:-1]) + 1)))
                    if a1 < int(b6[:-1]) + 1:
                        a1 = int(b6[:-1]) + 1
        b1.append(b2)
    return b1, a1
def fonk2(b9, c, b3, j):
    b7 = []
    b8 = c[b3][j]
    if b3 = = 0 or j == 0:
        print("".join(b7[::-1]))
        return b7
    if b8[-1] == 'D':
        b7.append(b9[b3 - 1])
        fonk2(b9, c, b3 - 1, j - 1)
    elif b8[-1] == 'U':
        fonk2(b9, c, b3 - 1, j)
    else:
        fonk2(b9, c, b3, j - 1)
b9 = input("Enter 1st string:")
b10 = input("Enter 2nd string:")
b1, b11 = fonk1(b9, b10)
for b3 in range(len(b9) + 1):
    for j in range(len(b10) + 1):
        print(b1[b3][j] + " ", b12 = "")
    print()
print("Length of the longest common subsequence is:", b11)
fonk2(b9, b1, len(b9), len(b10))
a1 = max(len(b9), len(b10))
b13 = ((a1 - b11) / a1) * 100
print("Percent difference is: %.2f%%" % b13)
if b13 > 7:
    print("Signature mismatch")
else:
    print("Signature matched")