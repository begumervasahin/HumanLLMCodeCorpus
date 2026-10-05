from random import randrange
def fonk1(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def fonk2(left, right):
    b1 = []
    while left and right:
        b1.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return b1 + left + right
def fonk3(arr):
    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                fonk1(arr, i, i + 1)
def fonk4(arr):
    if len(arr) <= 1:
        return arr
    b2 = len(arr)
    b3 = arr[:b2]
    b4 = arr[b2:]
    b5 = fonk4(b3)
    b6 = fonk4(b4)
    return fonk2(b5, b6)
def fonk5(arr, b7 = 0, b8=None):
    if b8 is None:
        b8 = len(arr) - 1
    if b7 >= b8:
        return arr
    b9 = randrange(b7, b8 + 1)
    b10 = arr[b9]
    arr[b8], arr[b9] = arr[b9], arr[b8]
    b11 = b7
    for i in range(b7, b8):
        if arr[i] < b10:
            fonk1(arr, i, b11)
            b11 += 1
    fonk1(arr, b8, b11)
    fonk5(arr, b7, b11 - 1)
    fonk5(arr, b11 + 1, b8)
    return arr