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
def fonk3():
    b2 = [5, 3, 6, 2, 10]
    print("Unsorted list:", b2)
    b3 = fonk2(b2.copy())
    print("Sorted list:", b3)
if b4 = = "__main__":
    fonk3()