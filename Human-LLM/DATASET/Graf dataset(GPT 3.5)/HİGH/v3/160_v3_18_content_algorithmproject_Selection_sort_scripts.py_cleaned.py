def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if arr[j] < arr[b2]:
                b2 = j
        if i != b2:
            arr[i], arr[b2] = arr[b2], arr[i]
    return arr
b3 = [6, 3, 1, 9, 2, 5, 8, 7, 4]
print(fonk1(b3))