def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparisons, swaps
def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Array before sorting:")
    print(arr)
    comparisons, swaps = bubble_sort(arr)
    print("Sorted array is:")
    print(arr)
    print(f"\nBubble Sort:\nComparisons: {comparisons}\nSwaps: {swaps}")
if __name__ == "__main__":
    main()