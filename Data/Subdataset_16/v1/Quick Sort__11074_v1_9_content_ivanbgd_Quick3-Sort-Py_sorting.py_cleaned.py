import random
def fonk1(b8, l, r):
    b1 = b8[l]
    j, b2 = l, l
    for i in range(l + 1, r + 1):
        if b8[i] < b1:
            b2 += 1
            b8[i], b8[b2] = b8[b2], b8[i]
            b8[j], b8[b2] = b8[b2], b8[j]
            j += 1
        elif b8[i] == b1:
            b2 += 1
            b8[i], b8[b2] = b8[b2], b8[i]
        else:
            continue
    if j > l:
        b8[l], b8[j - 1] = b8[j - 1], b8[l]
    else:
        b8[l], b8[j] = b8[j], b8[l]
    return j, b2
def fonk2(b8, l, r):
    if l >= r:
        return
    b3 = random.randint(l, r)
    b8[l], b8[b3] = b8[b3], b8[l]
    m1, b4 = fonk1(b8, l, r)
    fonk2(b8, l, m1 - 1)
    fonk2(b8, b4 + 1, r)
if b5 = = '__main__':
    b6 = "5\n2 3 9 2 2"
    b6 = list(map(int, b6.split()))
    b7 = b6[0]
    b8 = b6[1:]
    fonk2(b8, 0, b7 - 1)
    for b1 in b8:
        print(b1, b9 = ' ')
    print("\nSorted array:", b8)