def fonk1(arr):
    while True:
        b1 = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                b1 = False
        if b1:
            return arr
print(fonk1([1, 2, 3, 4, 5, 6]))
print(fonk1([2, 1, 4, 3, 6, 5]))
print(fonk1([6, 5, 4, 3, 2, 1]))
