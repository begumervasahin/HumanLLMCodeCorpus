import random
def fonk1(b9, left, right):
    b1 = b9[left]
    b2 = left
    b3 = left
    for i in range(left + 1, right + 1):
        if b9[i] < b1:
            b2 += 1
            b9[i], b9[b2] = b9[b2], b9[i]
            b9[b2], b9[b3] = b9[b3], b9[b2]
            b3 += 1
        elif b9[i] == b1:
            b3 += 1
            b9[i], b9[b3] = b9[b3], b9[i]
    b9[left], b9[b2] = b9[b2], b9[left]
    return b2, b3
def fonk2(b9, left, right):
    if left >= right:
        return
    b4 = random.randint(left, right)
    b9[left], b9[b4] = b9[b4], b9[left]
    m1, b5 = fonk1(b9, left, right)
    fonk2(b9, left, m1 - 1)
    fonk2(b9, b5 + 1, right)
def fonk3():
    b6 = "5\n2 3 9 2 2"
    b7 = b6.split('\b8')
    b8 = int(b7[0])
    b9 = list(map(int, b7[1].split()))
    fonk2(b9, 0, b8 - 1)
    print("Sorted array:", b9)
if b10 = = '__main__':
    fonk3()