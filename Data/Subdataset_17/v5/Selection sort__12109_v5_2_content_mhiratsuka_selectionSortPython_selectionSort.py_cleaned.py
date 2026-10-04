def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
def test_selection_sort_descending():
    test_numbers = [0, 2, 100, 0, 120, 11]
    sorted_numbers = selection_sort_descending(test_numbers[:])
    expected_result = [120, 100, 11, 2, 0, 0]
    assert sorted_numbers == expected_result, f"Test failed: {sorted_numbers}"
    print("Test passed!")
if __name__ == "__main__":
    numbers = [0, 2, 100, 0, 120, 11]
    print("Original list:", numbers)
    sorted_numbers = selection_sort_descending(numbers)
    print("Sorted list:", sorted_numbers)
    test_selection_sort_descending()