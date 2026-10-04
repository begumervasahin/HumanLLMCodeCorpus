
a1 = 0
def fonk1(arr, b4, i):
    global a1
    a2 = 0
    b1 = i
    b2 = 2 * i + 1
    b3 = 2 * i + 2
    if b2 < b4:
        a2 += 1
        if arr[i] < arr[b2]:
            b1 = b2
    if b3 < b4:
        a2 += 1
        if arr[b1] < arr[b3]:
            b1 = b3
    if b1 != i:
        arr[i], arr[b1] = arr[b1], arr[i]
        a1 += 1
        a2 += fonk1(arr, b4, b1)
    return a2
def fonk2(arr):
    global a1
    a1 = 0
    b4 = len(arr)
    a3 = 0
    for i in range(b4
        a3 += fonk1(arr, b4, i)
    for i in range(b4 - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        a1 += 1
        a3 += fonk1(arr, i, 0)
    return f"HEAP SORT:\nComparisons: {a3}\nSwaps: {a1}"
if b5 = = "__main__":
    b6 = [12, 11, 13, 5, 6, 7]
    print("Original b6:", b6)
    b7 = fonk2(b6)
    print(b7)
    print("Sorted b6:", b6)