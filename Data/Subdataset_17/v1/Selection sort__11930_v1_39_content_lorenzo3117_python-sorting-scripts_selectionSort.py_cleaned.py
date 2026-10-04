def selection_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return f"SELECTION SORT:\nComparisons: {comparisons}\nSwaps: {swaps}"
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Array before sorting:")
    print(arr)
    result = selection_sort(arr)
    print("Sorted array is:")
    print(arr)
    print(result)