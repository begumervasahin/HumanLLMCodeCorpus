def fonk1(arr, b3, b4):
    b1 = j = k = 0
    while b1 < len(b3) and j < len(b4):
        if b3[b1] < b4[j]:
            arr[k] = b3[b1]
            b1 += 1
        else:
            arr[k] = b4[j]
            j += 1
        k += 1
    while b1 < len(b3):
        arr[k] = b3[b1]
        b1 += 1
        k += 1
    while j < len(b4):
        arr[k] = b4[j]
        j += 1
        k += 1
    return arr
def fonk2(arr):
    if len(arr) > 1:
        b2 = len(arr)
        b3 = arr[:b2]
        b4 = arr[b2:]
        fonk2(b3)
        fonk2(b4)
        fonk1(arr, b3, b4)
if b5 = = "__main__":
    b6 = [38, 27, 43, 3, 9, 82, 10]
    print(f"Unsorted list: {b6}")
    fonk2(b6)
    print(f"Sorted list: {b6}")