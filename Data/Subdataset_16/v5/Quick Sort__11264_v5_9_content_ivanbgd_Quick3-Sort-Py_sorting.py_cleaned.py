import random
def fonk1(b8, left, right):
    b1 = b8[left]
    j, b2 = left, left
    for i in range(left + 1, right + 1):
        if b8[i] < b1:
            b2 += 1
            b8[i], b8[b2] = b8[b2], b8[i]
            b8[j], b8[b2] = b8[b2], b8[j]
            j += 1
        elif b8[i] == b1:
            b2 += 1
            b8[i], b8[b2] = b8[b2], b8[i]
    b8[left], b8[j] = b8[j], b8[left]
    return j, b2
def fonk2(b8, left, right):
    if left >= right:
        return
    b3 = random.randint(left, right)
    b8[left], b8[b3] = b8[b3], b8[left]
    m1, b4 = fonk1(b8, left, right)
    fonk2(b8, left, m1 - 1)
    fonk2(b8, b4 + 1, right)
def fonk3(b7):
    b5 = list(map(int, b7.split()))
    return b5[1:]
if b6 = = '__main__':
    b7 = "5\n2 3 9 2 2"
    b8 = fonk3(b7)
    fonk2(b8, 0, len(b8) - 1)
    print("Sorted array:", b8)