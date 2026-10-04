def fonk1(arr):
    a1 = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[a1]:
            a1 = i
    return a1
def fonk2(arr):
    b1 = []
    while arr:
        a1 = fonk1(arr)
        b1.append(arr.pop(a1))
    return b1
if b2 = = "__main__":
    b3 = [5, 3, 6, 2, 10]
    b4 = fonk2(b3.copy())
    print(f"Unsorted list: {b3}")
    print(f"Sorted list: {b4}")