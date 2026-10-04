def fonk1(arr, left, right):
    if left < right:
        b1 = fonk2(arr, left, right)
        fonk1(arr, left, b1 - 1)
        fonk1(arr, b1 + 1, right)
def fonk2(arr, left, right):
    b2 = arr[left]
    b3 = left + 1
    for i in range(left + 1, right + 1):
        if arr[i] < b2:
            arr[b3], arr[i] = arr[i], arr[b3]
            b3 += 1
    b3 -= 1
    arr[left], arr[b3] = arr[b3], arr[left]
    return b3
if b4 = = "__main__":
    b5 = [24, 3, 45, 29, 37, 12, 4]
    print("Original b5:", b5)
    fonk1(b5, 0, len(b5) - 1)
    print("Sorted b5:", b5)