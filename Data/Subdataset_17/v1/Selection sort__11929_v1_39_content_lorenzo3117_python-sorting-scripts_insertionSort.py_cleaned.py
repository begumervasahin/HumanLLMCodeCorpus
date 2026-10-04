def insertion_sort(array):
    swaps_made = 0
    checks_made = 0
    for f in range(1, len(array)):
        value = array[f]
        value_index = f
        checks_made += 1
        while value_index > 0 and value < array[value_index - 1]:
            array[value_index] = array[value_index - 1]
            value_index -= 1
            checks_made += 1
            swaps_made += 1
        array[value_index] = value
    return f"INSERTION SORT:\nComparisons: {checks_made}\nSwaps: {swaps_made}"
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Array before sorting:")
    print(arr)
    result = insertion_sort(arr)
    print("Sorted array is:")
    print(arr)
    print(result)