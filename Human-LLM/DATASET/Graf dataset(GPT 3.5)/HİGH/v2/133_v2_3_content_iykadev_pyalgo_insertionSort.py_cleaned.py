def fonk1(arr):
    for i in range(1, len(arr)):
        b1 = arr[i]
        b2 = i
        while b2 > 0 and arr[b2 - 1] > b1:
            arr[b2] = arr[b2 - 1]
            b2 -= 1
        arr[b2] = b1
b3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b3)
print(b3)