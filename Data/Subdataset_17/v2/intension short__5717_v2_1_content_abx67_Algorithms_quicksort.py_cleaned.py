def partition(array, left, right):
    pivot = array[right]
    print(f"Pivot: {pivot}")
    split_index = left
    for i in range(left, right + 1):
        print(f"Inspecting element at index {i}: {array[i]}")
        if array[i] <= pivot:
            if i != split_index:
                array[i], array[split_index] = array[split_index], array[i]
            split_index += 1
    return split_index - 1
def quicksort(array, left, right):
    if left < right:
        split_index = partition(array, left, right)
        print(f"Split at index {split_index}: {array}")
        quicksort(array, left, split_index - 1)
        quicksort(array, split_index + 1, right)
if __name__ == "__main__":
    array = [3, 6, 8, 10, 1, 2, 1]
    quicksort(array, 0, len(array) - 1)
    print("Sorted array:", array)