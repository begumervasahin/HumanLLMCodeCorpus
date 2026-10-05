from random import randrange
def fonk1(b13, index_1, index_2):
    b1 = b13[index_1]
    b13[index_1] = b13[index_2]
    b13[index_2] = b1
def fonk2(left, right):
    b2 = []
    while left and right:
        if left[0] < right[0]:
            b2.append(left.pop(0))
        else:
            b2.append(right.pop(0))
    if left:
        b2 += left
    if right:
        b2 += right
    return b2
def fonk3(b13):
    for _ in b13:
        for i in range(len(b13) - 1):
            if b13[i] > b13[i + 1]:
                fonk1(b13, i, i + 1)
def fonk4(b13):
    if len(b13) <= 1:
        return b13
    b3 = len(b13)
    b4 = b13[:b3]
    b5 = b13[b3:]
    b6 = fonk4(b4)
    b7 = fonk4(b5)
    return fonk2(b6, b7)
def fonk5(b13, b8 = 0, b9=None):
    if b9 is None:
        b9 = len(b13) - 1
    if b8 >= b9:
        return b13
    b10 = randrange(b8, b9 + 1)
    b11 = b13[b10]
    b13[b9], b13[b10] = b13[b10], b13[b9]
    b12 = b8
    for i in range(b8, b9):
        if b13[i] < b11:
            b13[i], b13[b12] = b13[b12], b13[i]
            b12 += 1
    b13[b9], b13[b12] = b13[b12], b13[b9]
    fonk5(b13, b8, b12 - 1)
    fonk5(b13, b12 + 1, b9)
    return b13
b13 = [7, 2, 5, 1, 8, 6, 3, 4]
print("Original array:", b13)
b14 = b13.copy()
fonk3(b14)
print("Bubble sort:", b14)
b14 = b13.copy()
b14 = fonk4(b14)
print("Merge sort:", b14)
b14 = b13.copy()
b14 = fonk5(b14)
print("Quick sort:", b14)