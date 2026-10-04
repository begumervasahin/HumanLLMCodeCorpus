def fonk1(arr):
    for i in range(len(arr)):
        b1 = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[b1]:
                b1 = j
        arr[i], arr[b1] = arr[b1], arr[i]
    print("Sorted array:", arr)
b2 = [5, 3, 2, 10, 45, 3, 1]
fonk1(b2)