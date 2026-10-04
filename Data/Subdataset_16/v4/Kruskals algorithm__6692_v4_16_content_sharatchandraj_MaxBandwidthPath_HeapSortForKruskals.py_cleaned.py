def fonk1(arr, b4, i):
    b1 = i
    b2 = 2 * i + 1
    b3 = 2 * i + 2
    if b2 < b4 and arr[i] > arr[b2]:
        b1 = b2
    if b3 < b4 and arr[b1] > arr[b3]:
        b1 = b3
    if b1 != i:
        arr[i], arr[b1] = arr[b1], arr[i]
        fonk1(arr, b4, b1)
def fonk2(arr):
    b4 = len(arr)
    for i in range(b4
        fonk1(arr, b4, i)
    for i in range(b4 - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        fonk1(arr, i, 0)
