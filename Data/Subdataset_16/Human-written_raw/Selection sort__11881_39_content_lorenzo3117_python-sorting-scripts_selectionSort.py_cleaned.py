def fonk1(arr):
    a1 = 0
    a2 = 0
    for i in range(0, len(arr) - 1):
        b1 = i
        for j in range(i+1, len(arr)):
            a1 += 1
            if arr[j] < arr[b1]:
                b1 = j
        arr[i], arr[b1] = arr[b1], arr[i]
        a2 += 1
    return "SELECTION SORT:\nComparisons: " + str(a1) + "\nSwaps: " + str(a2)