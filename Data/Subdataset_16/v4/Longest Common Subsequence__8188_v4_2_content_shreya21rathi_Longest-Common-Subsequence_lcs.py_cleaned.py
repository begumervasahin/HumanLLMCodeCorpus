def fonk1(b10, b11):
    b1 = []
    a1 = 0
    for b3 in range(len(b10) + 1):
        b2 = []
        for j in range(len(b11) + 1):
            if b3 = = 0 or j == 0:
                b2.append('0H')
            else:
                if b10[b3 - 1] != b11[j - 1]:
                    b4 = b1[b3 - 1][j]
                    b5 = b2[j - 1]
                    if int(b4[:-1]) >= int(b5[:-1]):
                        b2.append(f'{b4[:-1]}U')
                    else:
                        b2.append(f'{b5[:-1]}S')
                else:
                    b6 = b1[b3 - 1][j - 1]
                    b7 = int(b6[:-1]) + 1
                    b2.append(f'{b7}D')
                    if a1 < b7:
                        a1 = b7
        b1.append(b2)
    return b1, a1
def fonk2(b10, c, b3, j):
    b8 = []
    while b3 > 0 and j > 0:
        b9 = c[b3][j]
        if b9[-1] == 'D':
            b8.append(b10[b3 - 1])
            b3 -= 1
            j -= 1
        elif b9[-1] == 'U':
            b3 -= 1
        else:
            j -= 1
    return ''.join(reversed(b8))
b10 = input("Enter 1st string: ")
b11 = input("Enter 2nd string: ")
b1, b12 = fonk1(b10, b11)
for b2 in b1:
    print(" ".join(b2))
print(f"Length of longest common subsequence is: {b12}")
b8 = fonk2(b10, b1, len(b10), len(b11))
print(f"Longest common subsequence is: {b8}")
b13 = max(len(b10), len(b11))
b14 = ((b13 - b12) / b13) * 100
print(f"Percent difference is: {b14:.2f}%")
if b14 > 7:
    print("Signature mismatch")
else:
    print("Signature matched")