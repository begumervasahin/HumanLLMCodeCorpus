def fonk1(arr):
    b1 = len(arr)
    for b5 in range(b1):
        for j in range(0, b1 - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def fonk2(arr):
    if len(arr) > 1:
        b2 = len(arr)
        b3 = arr[:b2]
        b4 = arr[b2:]
        fonk2(b3)
        fonk2(b4)
        b5 = j = k = 0
        print("Left:", b3, "Right:", b4)
        while b5 < len(b3) and j < len(b4):
            if b3[b5] < b4[j]:
                arr[k] = b3[b5]
                b5 += 1
            else:
                arr[k] = b4[j]
                j += 1
            k += 1
        while b5 < len(b3):
            arr[k] = b3[b5]
            b5 += 1
            k += 1
        while j < len(b4):
            arr[k] = b4[j]
            j += 1
            k += 1
        print("Merged:", arr)
def fonk3():
    b6 = [34, 7, 23, 32, 5, 62]
    print("Original b6:", b6)
    b7 = fonk1(b6.copy())
    print("Bubble sorted b6:", b7)
    fonk2(b6)
    print("Merge sorted b6:", b6)
if b8 = = "__main__":
    fonk3()