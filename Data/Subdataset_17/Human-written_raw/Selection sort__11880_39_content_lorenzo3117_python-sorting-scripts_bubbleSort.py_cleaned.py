def bubbleSort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return "\nBubble Sort:\nComparisons: " + str(comparisons) + "\nSwaps: " + str(swaps)