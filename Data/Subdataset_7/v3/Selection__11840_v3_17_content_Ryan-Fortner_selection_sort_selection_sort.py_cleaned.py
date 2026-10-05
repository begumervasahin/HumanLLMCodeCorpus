def fonk1(arr):
    for i in range(len(arr)):
        b1 = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[b1]:
                b1 = j
        arr[i], arr[b1] = arr[b1], arr[i]
    return arr
b2 = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(fonk1(b2))