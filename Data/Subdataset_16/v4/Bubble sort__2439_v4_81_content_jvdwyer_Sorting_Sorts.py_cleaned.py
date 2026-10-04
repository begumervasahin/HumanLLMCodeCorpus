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
    b1 += left
    b1 += right
    return b1
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
def fonk5(arr, start, end):
    if start >= end:
        return arr
    b7 = randrange(start, end + 1)
    b8 = arr[b7]
    fonk1(arr, b7, end)
    b9 = start
    for i in range(start, end):
        if arr[i] < b8:
            fonk1(arr, i, b9)
            b9 += 1
    fonk1(arr, b9, end)
    fonk5(arr, start, b9 - 1)
    fonk5(arr, b9 + 1, end)
if b10 = = "__main__":
    b11 = [randrange(1, 100) for _ in range(10)]
    print("Original b11:", b11)
    b12 = b11.copy()
    fonk3(b12)
    print("Bubble Sorted b11:", b12)
    b12 = fonk4(b11.copy())
    print("Merge Sorted b11:", b12)
    b12 = b11.copy()
    fonk5(b12, 0, len(b12) - 1)
    print("Quick Sorted b11:", b12)