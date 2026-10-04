def fonk1(arr):
    b1 = len(arr)
    for i in range(b1 - 1):
        b2 = i
        for j in range(i + 1, b1):
            if arr[j] < arr[b2]:
                b2 = j
        if b2 != i:
            arr[i], arr[b2] = arr[b2], arr[i]
def fonk2():
    b3 = [12, 3, 43, 43, 9, 3, 2, 2, 43, 23, 53, 3, 3, 23, 23, 12, 53, 91, 1]
    print("Array before sorting:")
    print(b3)
    fonk1(b3)
    print("Array after sorting:")
    print(b3)
if b4 = = "__main__":
    fonk2()