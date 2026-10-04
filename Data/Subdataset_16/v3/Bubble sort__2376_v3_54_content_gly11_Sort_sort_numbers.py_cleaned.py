def fonk1(arr):
    for j in range(1, len(arr)):
        b1 = arr[j]
        b2 = j - 1
        while b2 >= 0 and arr[b2] > b1:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1
    return arr
def fonk2(arr):
    b3 = len(arr)
    for b2 in range(b3):
        for j in range(0, b3 - b2 - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
if b4 = = "__main__":
    b5 = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:")
    print(b5)
    b6 = fonk1(b5.copy())
    print("\nSorted list using insertion sort:")
    print(b6)
    b7 = fonk2(b5.copy())
    print("\nSorted list using bubble sort:")
    print(b7)