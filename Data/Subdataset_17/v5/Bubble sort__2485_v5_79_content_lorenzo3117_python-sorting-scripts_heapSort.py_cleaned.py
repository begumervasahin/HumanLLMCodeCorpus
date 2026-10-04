
swaps = 0
def heapify(arr, n, i):
    global swaps
    comparisons = 0
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
        comparisons += 1
    if right < n and arr[largest] < arr[right]:
        largest = right
        comparisons += 1
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swaps += 1
        comparisons += heapify(arr, n, largest)
    return comparisons
def heap_sort(arr):
    global swaps
    swaps = 0
    n = len(arr)
    total_comparisons = 0
    for i in range(n
        total_comparisons += heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swaps += 1
        total_comparisons += heapify(arr, i, 0)
    return f"HEAP SORT:\nComparisons: {total_comparisons}\nSwaps: {swaps}"
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    result = heap_sort(arr)
    print(result)
    print(f"Sorted array: {arr}")