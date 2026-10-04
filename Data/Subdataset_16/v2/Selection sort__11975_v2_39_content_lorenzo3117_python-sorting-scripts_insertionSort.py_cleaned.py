def fonk1(array):
    a1 = 0
    a2 = 0
    for i in range(1, len(array)):
        b1 = array[i]
        b2 = i
        a2 += 1
        while b2 > 0 and b1 < array[b2 - 1]:
            array[b2] = array[b2 - 1]
            b2 -= 1
            a2 += 1
            a1 += 1
        array[b2] = b1
    return a2, a1
def fonk2():
    b3 = [12, 11, 13, 5, 6]
    print("Array before sorting:")
    print(b3)
    comparisons, b4 = fonk1(b3)
    print("Sorted array is:")
    print(b3)
    print(f"\nINSERTION SORT:\nComparisons: {comparisons}\nSwaps: {b4}")
if b5 = = "__main__":
    fonk2()