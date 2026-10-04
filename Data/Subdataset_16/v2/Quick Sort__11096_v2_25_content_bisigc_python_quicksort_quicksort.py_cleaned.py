def fonk1(arr, left, right):
    if left < right:
        b1 = arr[left]
        b2 = left
        for i in range(left + 1, right):
            if arr[i] < b1:
                b2 += 1
                arr[b2], arr[i] = arr[i], arr[b2]
        arr[left], arr[b2] = arr[b2], arr[left]
        fonk1(arr, left, b2)
        fonk1(arr, b2 + 1, right)
def fonk2():
    b3 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print("Original b3:", b3)
    fonk1(b3, 0, len(b3))
    print("Sorted b3:", b3)
if b4 = = "__main__":
    fonk2()