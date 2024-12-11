def fonk1(arr):
    if len(arr) <= 1:
        return
    b1 = len(arr)
    b2 = arr[:b1]
    b3 = arr[b1:]
    fonk1(b2)
    fonk1(b3)
    fonk2(b2, b3, arr)
def fonk2(b2, b3, arr):
    b4 = j = k = 0
    while b4 < len(b2) and j < len(b3):
        if b2[b4] < b3[j]:
            arr[k] = b2[b4]
            b4 += 1
        else:
            arr[k] = b3[j]
            j += 1
        k += 1
    while b4 < len(b2):
        arr[k] = b2[b4]
        b4 += 1
        k += 1
    while j < len(b3):
        arr[k] = b3[j]
        j += 1
        k += 1
b5 = int(input("How many elements do you want in this list: "))
b6 = [int(input("Enter element: ")) for _ in range(b5)]
fonk1(b6)
print("Sorted list:", b6)