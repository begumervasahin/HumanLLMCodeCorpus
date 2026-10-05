def partition(arr, left, right):
    if left >= right:
        return right
    pivot = arr[right]
    split_index = left
    for i in range(left, right + 1):
        if arr[i] <= pivot:
            if i != split_index:
                arr[i], arr[split_index] = arr[split_index], arr[i]
            split_index += 1
    return split_index - 1
def quicksort(arr, left, right):
    if right != left:
        split_index = partition(arr, left, right)
        if split_index >= left + 1:
            quicksort(arr, left, split_index - 1)
        if split_index <= right - 1:
            quicksort(arr, split_index + 1, right)
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)