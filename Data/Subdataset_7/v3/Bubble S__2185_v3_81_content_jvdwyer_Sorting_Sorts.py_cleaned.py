from random import randrange
def fonk1(b12, index_1, index_2):
    b12[index_1], b12[index_2] = b12[index_2], b12[index_1]
def fonk2(left, right):
    b1 = []
    while left and right:
        if left[0] < right[0]:
            b1.append(left.pop(0))
        else:
            b1.append(right.pop(0))
    return b1 + left + right
def fonk3(b12):
    for _ in b12:
        for i in range(len(b12) - 1):
            if b12[i] > b12[i + 1]:
                fonk1(b12, i, i + 1)
def fonk4(b12):
    if len(b12) <= 1:
        return b12
    b2 = len(b12)
    b3 = b12[:b2]
    b4 = b12[b2:]
    b5 = fonk4(b3)
    b6 = fonk4(b4)
    return fonk2(b5, b6)
def fonk5(b12, b7 = 0, b8=None):
    if b8 is None:
        b8 = len(b12) - 1
    if b7 >= b8:
        return b12
    b9 = randrange(b7, b8 + 1)
    b10 = b12[b9]
    b12[b8], b12[b9] = b12[b9], b12[b8]
    b11 = b7
    for i in range(b7, b8):
        if b12[i] < b10:
            fonk1(b12, i, b11)
            b11 += 1
    fonk1(b12, b8, b11)
    fonk5(b12, b7, b11 - 1)
    fonk5(b12, b11 + 1, b8)
    return b12
b12 = [7, 2, 5, 1, 8, 6, 3, 4]
print("Original array:", b12)
b13 = b12.copy()
fonk3(b13)
print("Bubble sort:", b13)
b13 = b12.copy()
b13 = fonk4(b13)
print("Merge sort:", b13)
b13 = b12.copy()
b13 = fonk5(b13)
print("Quick sort:", b13)