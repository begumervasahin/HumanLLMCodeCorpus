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
    return b1, int(a1)
def fonk2(b9, c, b3, j):
    b7 = c[b3][j]
    b8 = []
    if b3 = = 0 or j == 0:
        return "".join(b8[::-1])
    while b3 > 0 and j > 0:
        if b7[-1] == 'D':
            b8.append(b9[b3 - 1])
            b3 -= 1
            j -= 1
        elif b7[-1] == 'U':
            b3 -= 1
        else:
            j -= 1
        b7 = c[b3][j]
    return "".join(b8[::-1])
b9 = input("Enter 1st string: ")
b10 = input("Enter 2nd string: ")
b1, b11 = fonk1(b9, b10)
for b3 in range(len(b9) + 1):
    for j in range(len(b10) + 1):
        print(b1[b3][j] + " ", b12 = "")
    print()
print("Length of longest common subsequence is:", b11)
b13 = fonk2(b9, b1, len(b9), len(b10))
print("Longest Common Subsequence is:", b13)
b14 = max(len(b9), len(b10))
b15 = ((b14 - b11) / b14) * 100
print("Percent difference is: %.2f" % b15, "%")
if b15 > 7:
    print("Signature mismatch")
else:
    print("Signature matched")