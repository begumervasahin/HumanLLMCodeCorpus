def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if arr[j] < arr[b2]:
                b2 = j
        arr[i], arr[b2] = arr[b2], arr[i]
    return arr
b3 = [5, 3, 2, 10, 45, 3, 1]
b4 = fonk1(b3)
print("Sorted array:", b4)