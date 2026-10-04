def fonk1(arr, left, right):
    if left < right:
        b1 = fonk2(arr, left, right)
        fonk1(arr, left, b1)
        fonk1(arr, b1 + 1, right)
def fonk2(arr, left, right):
    b2 = arr[left]
    b3 = left
    for i in range(left + 1, right):
        if arr[i] < b2:
            b3 += 1
            arr[b3], arr[i] = arr[i], arr[b3]
    arr[left], arr[b3] = arr[b3], arr[left]
    return b3
def fonk3():
    b4 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print("Original b4:", b4)
    fonk1(b4, 0, len(b4))
    print("Sorted b4:", b4)
if b5 = = "__main__":
    fonk3()