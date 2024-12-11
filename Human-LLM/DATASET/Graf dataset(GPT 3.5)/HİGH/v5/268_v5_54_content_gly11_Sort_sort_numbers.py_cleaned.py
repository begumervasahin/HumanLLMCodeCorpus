def fonk1(arr):
    b1 = len(arr)
    for i in range(1, b1):
        b2 = arr[i]
        b3 = i - 1
        while b3 >= 0 and arr[b3] > b2:
            arr[b3 + 1] = arr[b3]
            b3 -= 1
        arr[b3 + 1] = b2
    return arr
def fonk2(arr):
    b1 = len(arr)
    for i in range(b1):
        for b3 in range(0, b1 - i - 1):
            if arr[b3] > arr[b3 + 1]:
                arr[b3], arr[b3 + 1] = arr[b3 + 1], arr[b3]
    return arr