from random import randrange
def fonk1(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def fonk2(left, right):
    b1 = []
    while left and right:
        if left[0] < right[0]:
            b1.append(left.pop(0))
        else:
            b1.append(right.pop(0))
    b1.extend(left)
    b1.extend(right)
    return b1
def fonk3(arr):
    b2 = len(arr)
    for _ in range(b2):
        for i in range(b2 - 1):
            if arr[i] > arr[i + 1]:
                fonk1(arr, i, i + 1)
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
        return
    b8 = randrange(start, end + 1)
    b9 = arr[b8]
    fonk1(arr, b8, end)
    b10 = start
    for i in range(start, end):
        if arr[i] < b9:
            fonk1(arr, i, b10)
            b10 += 1
    fonk1(arr, b10, end)
    fonk5(arr, start, b10 - 1)
    fonk5(arr, b10 + 1, end)
if b11 = = "__main__":
    b12 = [randrange(1, 100) for _ in range(10)]
    print("Original b12:", b12)
    b13 = b12.copy()
    fonk3(b13)
    print("Bubble Sorted b12:", b13)
    b13 = fonk4(b12.copy())
    print("Merge Sorted b12:", b13)
    b13 = b12.copy()
    fonk5(b13, 0, len(b13) - 1)
    print("Quick Sorted b12:", b13)