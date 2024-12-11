import random
def fonk1(b9, left, right):
    b1 = b9[left]
    j, b2 = left, left
    for i in range(left + 1, right + 1):
        if b9[i] < b1:
            b2 += 1
            b9[i], b9[b2] = b9[b2], b9[i]
            b9[j], b9[b2] = b9[b2], b9[j]
            j += 1
        elif b9[i] == b1:
            b2 += 1
            b9[i], b9[b2] = b9[b2], b9[i]
    if j > left:
        b9[left], b9[j - 1] = b9[j - 1], b9[left]
    else:
        b9[left], b9[j] = b9[j], b9[left]
    return j, b2
def fonk2(b9, left, right):
    if left >= right:
        return
    b3 = random.randint(left, right)
    b9[left], b9[b3] = b9[b3], b9[left]
    m1, b4 = fonk1(b9, left, right)
    fonk2(b9, left, m1 - 1)
    fonk2(b9, b4 + 1, right)
if b5 = = '__main__':
    b6 = "5\n2 3 9 2 2"
    b7 = list(map(int, b6.split()))
    b8 = b7[0]
    b9 = b7[1:]
    fonk2(b9, 0, b8 - 1)
    for element in b9:
        print(element, b10 = ' ')
    print()
    print(b9)