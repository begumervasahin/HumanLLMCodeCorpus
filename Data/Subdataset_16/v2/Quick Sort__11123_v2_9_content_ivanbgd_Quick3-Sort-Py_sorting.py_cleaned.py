import random
def fonk1(b8, left, right):
    b1 = b8[left]
    b2 = left
    b3 = left
    for i in range(left + 1, right + 1):
        if b8[i] < b1:
            b2 += 1
            b8[i], b8[b2] = b8[b2], b8[i]
            b8[b2], b8[b3] = b8[b3], b8[b2]
            b3 += 1
        elif b8[i] == b1:
            b3 += 1
            b8[i], b8[b3] = b8[b3], b8[i]
    if b2 > left:
        b8[left], b8[b2 - 1] = b8[b2 - 1], b8[left]
    else:
        b8[left], b8[b2] = b8[b2], b8[left]
    return b2, b3
def fonk2(b8, left, right):
    if left >= right:
        return
    b4 = random.randint(left, right)
    b8[left], b8[b4] = b8[b4], b8[left]
    m1, b5 = fonk1(b8, left, right)
    fonk2(b8, left, m1 - 1)
    fonk2(b8, b5 + 1, right)
def fonk3():
    b6 = "5\n2 3 9 2 2"
    b6 = list(map(int, b6.split()))
    b7 = b6[0]
    b8 = b6[1:]
    fonk2(b8, 0, b7 - 1)
    print("Sorted array:", b8)
if b9 = = '__main__':
    fonk3()