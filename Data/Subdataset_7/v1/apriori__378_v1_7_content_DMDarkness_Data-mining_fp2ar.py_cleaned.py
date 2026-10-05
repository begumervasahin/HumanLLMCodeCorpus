
def fonk1(b6, b8, b9, L, temp, base):
    if L < 1:
        if b8.count(temp) == 0:
            temp.sort()
            b6.sort()
            b8.append(temp)
            b9.append(b6)
    else:
        for i in range(base, len(b6)):
            fonk1(b6[0:i] + b6[i+1:], b8, b9, L-1, temp + [b6[i]], i)
def fonk2(fi, N, minconf, minlift):
    b1 = []
    b2 = len(fi)
    b3 = {}
    for i in range(b2):
        b4 = fi[i][0:-1]
        b4.sort()
        b3[tuple(b4)] = fi[i][-1]
    for i in range(b2):
        b5 = int((len(fi[i]) - 1) / 2)
        b6 = fi[i][0:-1]
        b7 = fi[i][-1]
        b8 = []
        b9 = []
        for j in range(1, b5 + 1):
            fonk1(b6, b8, b9, j, [], 0)
        for j in range(len(b8)):
            if b8.count(b9[j]) != 0:
                b8[j] = [-1, -9]
                b9[j] = [-2, -5]
            b10 = b8[j]
            b11 = b9[j]
            b10.sort()
            b11.sort()
            if tuple(b10) in b3 and tuple(b11) in b3:
                b12 = b3[tuple(b10)]
                b13 = b3[tuple(b11)]
                if b7 * N / (b12 * b13) > minlift:
                    if b7 / b12 > minconf:
                        b14 = [b10, b11, b7, b7 / b12, b7 * N / (b12 * b13)]
                        b1.append(b14)
                    if b7 / b13 > minconf:
                        b14 = [b11, b10, b7, b7 / b13, b7 * N / (b12 * b13)]
                        b1.append(b14)
    return b1