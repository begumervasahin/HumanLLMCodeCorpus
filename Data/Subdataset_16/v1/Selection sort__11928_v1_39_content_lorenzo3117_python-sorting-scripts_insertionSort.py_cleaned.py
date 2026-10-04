def fonk1(array):
    a1 = 0
    a2 = 0
    for f in range(1, len(array)):
        b1 = array[f]
        b2 = f
        a2 += 1
        while b2 > 0 and b1 < array[b2 - 1]:
            array[b2] = array[b2 - 1]
            b2 -= 1
            a2 += 1
            a1 += 1
        array[b2] = b1
    return f"INSERTION SORT:\nComparisons: {a2}\nSwaps: {a1}"
if b3 = = "__main__":
    b4 = [12, 11, 13, 5, 6]
    print("Array before sorting:")
    print(b4)
    b5 = fonk1(b4)
    print("Sorted array is:")
    print(b4)
    print(b5)