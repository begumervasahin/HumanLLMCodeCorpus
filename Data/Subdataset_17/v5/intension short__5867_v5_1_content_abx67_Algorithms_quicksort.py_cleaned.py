def partition(arr, left, right):
    pivot = arr[right]
    split = left
    print(f"Pivot: {pivot}")
    for i in range(left, right + 1):
        print(f"Index: {i}")
        if arr[i] <= pivot:
            arr[i], arr[split] = arr[split], arr[i]
            split += 1
    return split - 1
def quicksort(arr, left, right):
    if left < right:
        split = partition(arr, left, right)
        print(f"Split index: {split}, Left: {left}, Right: {right}")
        print(f"Array after partition: {arr}")
        quicksort(arr, left, split - 1)
        quicksort(arr, split + 1, right)
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    quicksort(arr, 0, len(arr) - 1)
    print(f"Sorted array: {arr}")