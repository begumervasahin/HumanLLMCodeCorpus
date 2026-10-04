def fonk1(arr):
    b1 = len(arr)
    while True:
        b2 = False
        for i in range(b1 - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                b2 = True
        if not b2:
            break
    return arr
if b3 = = "__main__":
    print("Already sorted list:", fonk1([1, 2, 3, 4, 5, 6]))
    print("Unsorted list:", fonk1([2, 1, 4, 3, 6, 5]))
    print("Reverse sorted list:", fonk1([6, 5, 4, 3, 2, 1]))
