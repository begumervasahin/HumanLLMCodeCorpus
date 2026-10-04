def fonk1(array):
    a1 = 0
    a2 = 0
    for f in range(len(array)):
        b1 = array[f]
        b2 = f
        a2 += 1
        while b2 > 0 and b1 < array[b2-1]:
            array[b2] = array[b2-1]
            b2 -= 1
            a2 += 1
            a1 += 1
        array[b2] = b1
    return "INSERTION SORT:\nComparisons: " + str(a2) + "\nSwaps: " + str(a1)