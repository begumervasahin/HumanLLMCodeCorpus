def fonk1(arr):
    for pass_num in range(len(arr) - 1, 0, -1):
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
b1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b1)
print(b1)
