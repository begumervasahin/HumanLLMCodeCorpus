from random import randrange
def fonk1(arr, index_1, index_2):
    b1 = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = b1
def fonk2(left, right):
    b2 = []
    while left and right:
        if left[0] < right[0]:
            b2.append(left.pop(0))
        else:
            b2.append(right.pop(0))
    b2 += left
    b2 += right
    return b2
def fonk3(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                fonk1(arr, i, i + 1)
    return arr
def fonk4(arr):
    if len(arr) <= 1:
        return arr
    b3 = len(arr)
    b4 = arr[:b3]
    b5 = arr[b3:]
    b6 = fonk4(b4)
    b7 = fonk4(b5)
    return fonk2(b6, b7)
def fonk5(arr, start, end):
    if start >= end:
        return arr
    b8 = randrange(start, end + 1)
    b9 = arr[b8]
    arr[end], arr[b8] = arr[b8], arr[end]
    b10 = start
    for i in range(start, end):
        if arr[i] < b9:
            arr[i], arr[b10] = arr[b10], arr[i]
            b10 += 1
    arr[end], arr[b10] = arr[b10], arr[end]
    fonk5(arr, start, b10 - 1)
    fonk5(arr, b10 + 1, end)
    return arr
if b11 = = '__main__':
    b12 = [randrange(1, 101) for _ in range(10)]
    print("Original b12:", b12)
    b13 = fonk3(b12.copy())
    print("Bubble Sorted b12:", b13)
    b14 = fonk4(b12.copy())
    print("Merge Sorted b12:", b14)
    b15 = fonk5(b12.copy(), 0, len(b12) - 1)
    print("Quick Sorted b12:", b15)