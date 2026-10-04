b1 = [0, 9, 1, 4, 6, 7, b4, 1, 8, 7, 7, 4, 3, 5, 6, 1, 7, 8, 0, 3]
b2 = len(b1)
a1 = 0
b3 = b2
while b3 % b4 = = 0:
    b3
    a1 += 1
b5 = b4 ** a1
b6 = b2
print('Number of b7 = ', b6)
print('Interval b8 = ', b5)
print('List b2 = ', b2)
print(b1)
a2 = 1
for start in range(0, b2, b5):
    for k in range(a2 * b3 - 1):
        b9 = []
        print('b9 = ', b9, '\ng =', a2)
        a3 = 0
        a4 = 0
        for i in range(a2 * b3 - 1):
            for b10 in range(a2 * b3):
                if i >= a3:
                    if i < b10:
                        if b1[i] <= b1[b10]:
                            b9.append(b1[i])
                            a3 = b10
                            if b10 = = b3 - 1:
                                b9.append(b1[b10])
                            else:
                                break
                        else:
                            b9.append(b1[b10])
                            if b10 = = b3 - 1:
                                a4 += 1
                                b9.append(b1[i])
                                break
                else:
                    break
            if a4 > 0:
                break
        b1 = list(b9)
        print('b1 = ', b1, '\nb =', b9, '\nk =', k, '\ni =', i, '\nj =', b10, '\nh =', start, '\ng*b3-1 =', a2 * b3 - 1)
    a2 += 1
print('Final sorted list:', b1)