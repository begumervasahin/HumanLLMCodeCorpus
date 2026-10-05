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
                    b7 = int(b6[:-1]) + 1
                    b2.append('{0}D'.format(str(b7)))
                    if a1 < b7:
                        a1 = b7
        b1.append(b2)
    return b1, a1
def fonk2(b9, lcs_matrix, b3, j, b12):
    if b3 = = 0 or j == 0:
        print("".join(b12[::-1]))
        return
    b8 = lcs_matrix[b3][j][-1]
    if b8 = = 'D':
        b12.append(b9[b3 - 1])
        fonk2(b9, lcs_matrix, b3 - 1, j - 1, b12)
    elif b8 = = 'U':
        fonk2(b9, lcs_matrix, b3 - 1, j, b12)
    else:
        fonk2(b9, lcs_matrix, b3, j - 1, b12)
def fonk3():
    b9 = input("Enter 1st string:")
    b10 = input("Enter 2nd string:")
    lcs_matrix, b7 = fonk1(b9, b10)
    for b3 in range(len(b9) + 1):
        for j in range(len(b10) + 1):
            print(lcs_matrix[b3][j] + " ", b11 = "")
        print()
    print("Length of the longest common subsequence is:", b7)
    b12 = []
    fonk2(b9, lcs_matrix, len(b9), len(b10), b12)
    a1 = max(len(b9), len(b10))
    b13 = ((a1 - b7) / a1) * 100
    print("Percent difference is: %.2f%%" % b13)
    if b13 > 7:
        print("Signature mismatch")
    else:
        print("Signature matched")
if b14 = = "__main__":
    fonk3()