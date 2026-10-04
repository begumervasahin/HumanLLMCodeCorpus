def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return f"SELECTION SORT:\nComparisons: {comparisons}\nSwaps: {swaps}"
def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:")
    print(arr)
    result = selection_sort(arr)
    print("Sorted array:")
    print(arr)
    print(result)
if __name__ == "__main__":
    main()