def fonk1(arr):
    for i in range(1, len(arr)):
        b1 = arr[i]
        b2 = i - 1
        while b2 >= 0 and arr[b2] > b1:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1
    return arr
def fonk2(arr):
    b3 = len(arr)
    for i in range(b3):
        for b2 in range(0, b3-i-1):
            if arr[b2] > arr[b2+1]:
                arr[b2], arr[b2+1] = arr[b2+1], arr[b2]
    return arr
b4 = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", b4)
b5 = fonk1(b4.copy())
print("Sorted list (Insertion Sort):", b5)
b6 = fonk2(b4.copy())
print("Sorted list (Bubble Sort):", b6)