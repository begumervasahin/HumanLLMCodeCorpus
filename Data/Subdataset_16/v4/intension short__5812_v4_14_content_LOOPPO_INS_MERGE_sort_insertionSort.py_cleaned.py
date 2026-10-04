def fonk1(arr):
    for i in range(1, len(arr)):
        b1 = arr[i]
        b2 = i - 1
        while b2 >= 0 and arr[b2] > b1:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1