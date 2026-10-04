def fonk1(arr):
    b1 = len(arr)
    a1 = 0
    a2 = 0
    for i in range(b1):
        b2 = False
        for j in range(0, b1-i-1):
            a1 += 1
            if arr[j] > arr[j+1]:
                a2 += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                b2 = True
        if b2 = = False:
            break
    return "\nBubble Sort:\nComparisons: " + str(a1) + "\nSwaps: " + str(a2)