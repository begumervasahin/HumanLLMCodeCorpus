def partition(array, left, right):
    pivot = array[right]
    print(f"Pivot selected: {pivot}")
    split_index = left
    for current_index in range(left, right + 1):
        print(f"Inspecting element at index {current_index}: {array[current_index]}")
        if array[current_index] <= pivot:
            if current_index != split_index:
                array[current_index], array[split_index] = array[split_index], array[current_index]
            split_index += 1
    return split_index - 1
def quicksort(array, left, right):
    if left < right:
        split_index = partition(array, left, right)
        print(f"Array after partitioning at index {split_index}: {array}")
        quicksort(array, left, split_index - 1)
        quicksort(array, split_index + 1, right)
if __name__ == "__main__":
    array = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", array)
    quicksort(array, 0, len(array) - 1)
    print("Sorted array:", array)