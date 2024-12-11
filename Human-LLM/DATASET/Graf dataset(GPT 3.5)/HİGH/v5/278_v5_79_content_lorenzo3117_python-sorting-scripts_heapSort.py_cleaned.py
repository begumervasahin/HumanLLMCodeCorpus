a1 = 0
def fonk1(arr, b4, i):
    global a1
    a2 = 0
    b1 = i
    b2 = 2 * i + 1
    b3 = 2 * i + 2
    if b2 < b4 and arr[b2] > arr[b1]:
        b1 = b2
    if b3 < b4 and arr[b3] > arr[b1]:
        b1 = b3
    if b1 != i:
        a2 += 1
        arr[i], arr[b1] = arr[b1], arr[i]
        a1 += 1
        a2 += fonk1(arr, b4, b1)
    return a2
def fonk2(arr):
    global a1
    b4 = len(arr)
    a2 = 0
    for i in range(b4, -1, -1):
        fonk1(arr, b4, i)
        a2 += fonk1(arr, i, 0)
    for i in range(b4-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        a1 += 1
        a2 += fonk1(arr, i, 0)
    return f"HEAP SORT:\nComparisons: {a2}\nSwaps: {a1}"