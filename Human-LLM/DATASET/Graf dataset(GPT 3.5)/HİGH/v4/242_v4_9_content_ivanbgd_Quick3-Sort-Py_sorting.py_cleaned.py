import sys
import random
def fonk1(b9, l, r):
    b1 = b9[l]
    j, b2 = l, l
    for i in range(l + 1, r + 1):
        if b9[i] < b1:
            b2 += 1
            b9[i], b9[b2] = b9[b2], b9[i]
            b9[j], b9[b2] = b9[b2], b9[j]
            j += 1
        elif b9[i] == b1:
            b2 += 1
            b9[i], b9[b2] = b9[b2], b9[i]
    if j > l:
        b9[l], b9[j - 1] = b9[j - 1], b9[l]
    else:
        b9[l], b9[j] = b9[j], b9[l]
    return j, b2
def fonk2(b9, l, r):
    if l >= r:
        return
    b3 = random.randint(l, r)
    b9[l], b9[b3] = b9[b3], b9[l]
    m1, b4 = fonk1(b9, l, r)
    fonk2(b9, l, m1 - 1)
    fonk2(b9, b4 + 1, r)
if b5 = = '__main__':
    b6 = "5\n2 3 9 2 2"
    b7 = list(map(int, b6.split()))
    b8 = b7[0]
    b9 = b7[1:]
    fonk2(b9, 0, b8 - 1)
    for b1 in b9:
        print(b1, b10 = " ")
    print()