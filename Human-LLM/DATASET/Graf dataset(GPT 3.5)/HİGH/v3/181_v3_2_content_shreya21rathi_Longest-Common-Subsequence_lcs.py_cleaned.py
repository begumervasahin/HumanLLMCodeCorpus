def fonk1(b9, b10):
    b1 = [['0H' for _ in range(len(b10) + 1)] for _ in range(len(b9) + 1)]
    return b1
def fonk2(b9, b10):
    b1 = fonk1(b9, b10)
    a1 = 0
    for i in range(1, len(b9)+1):
        for b6 in range(1, len(b10)+1):
            if b9[i-1] != b10[b6-1]:
                b2 = b1[i-1][b6]
                b3 = b1[i][b6-1]
                if int(b2[:-1]) >= int(b3[:-1]):
                    b1[i][b6] = '{0}U'.format(b2[:-1])
                else:
                    b1[i][b6] = '{0}S'.format(b3[:-1])
            else:
                b4 = b1[i - 1][b6 - 1]
                b1[i][b6] = '{0}D'.format(str(int(b4[:-1]) + 1))
                if a1 < int(b4[:-1]) + 1:
                    a1 = int(b4[:-1]) + 1
    return b1, a1
def fonk3(b9, b1):
    b5 = []
    i, b6 = len(b9), len(b1[0]) - 1
    while i > 0 and b6 > 0:
        b7 = b1[i][b6]
        if b7[-1] == 'D':
            b5.append(b9[i-1])
            i -= 1
            b6 -= 1
        elif b7[-1] == 'U':
            i -= 1
        else:
            b6 -= 1
    return ''.join(b5[::-1])
def fonk4(b9, b10, b11):
    a1 = max(len(b9), len(b10))
    b8 = ((a1 - b11) / a1) * 100
    return b8
def fonk5(b1):
    for row in b1:
        print(' '.join(row))
def fonk6():
    b9 = input("Enter 1st string:")
    b10 = input("Enter 2nd string:")
    b1, b11 = fonk2(b9, b10)
    fonk5(b1)
    print("Length of the longest common subsequence is:", b11)
    b12 = fonk3(b9, b1)
    print("Longest common subsequence is:", b12)
    b8 = fonk4(b9, b10, b11)
    print("Percent difference is: %.2f%%" % b8)
    if b8 > 7:
        print("Signature mismatch")
    else:
        print("Signature matched")
if b13 = = "__main__":
    fonk6()