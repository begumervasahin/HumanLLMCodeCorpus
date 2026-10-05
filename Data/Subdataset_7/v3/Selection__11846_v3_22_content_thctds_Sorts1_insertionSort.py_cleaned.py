def fonk1(arr):
    for i in range(1, len(arr)):
        b1 = arr[i]
        b2 = i
        while b2 > 0 and arr[b2 - 1] > b1:
            arr[b2] = arr[b2 - 1]
            b2 = b2 - 1
        arr[b2] = b1
    return arr
if b3 = = "__main__":
    b4 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    b5 = fonk1(b4)
    print("Sorted array:", b5)