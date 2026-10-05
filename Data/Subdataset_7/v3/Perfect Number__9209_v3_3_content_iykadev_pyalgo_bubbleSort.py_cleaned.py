def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        for j in range(0, b1 - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
b2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b2)
print(b2)
