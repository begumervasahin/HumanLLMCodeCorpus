def fonk1(a):
    for b4 in range(len(a)):
        for x in range(0, len(a) - 1):
            if a[x] > a[x + 1]:
                a[x + 1], a[x] = a[x], a[x + 1]
    return a
def fonk2(a):
    if len(a) > 1:
        b1 = len(a)
        b2 = a[:b1]
        b3 = a[b1:]
        fonk2(b2)
        fonk2(b3)
        b4 = j = k = 0
        print('Left:', b2, 'Right:', b3)
        while b4 < len(b2) and j < len(b3):
            if b2[b4] < b3[j]:
                a[k] = b2[b4]
                b4 += 1
            else:
                a[k] = b3[j]
                j += 1
            k += 1
        while b4 < len(b2):
            a[k] = b2[b4]
            b4 += 1
            k += 1
        while j < len(b3):
            a[k] = b3[j]
            j += 1
            k += 1
        print('Merged:', a)
if b5 = = "__main__":
    b6 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array for bubble sort:", b6)
    b7 = fonk1(b6[:])
    print("Sorted array with bubble sort:", b7)
    b8 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array for merge sort:", b8)
    fonk2(b8)
    print("Sorted array with merge sort:", b8)