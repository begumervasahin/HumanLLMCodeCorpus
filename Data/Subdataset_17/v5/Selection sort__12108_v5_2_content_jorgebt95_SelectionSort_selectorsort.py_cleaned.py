def selection_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        min_position = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_position]:
                min_position = j
        numbers[i], numbers[min_position] = numbers[min_position], numbers[i]
def test_selection_sort():
    test_numbers = [5, 6, 4, 3, 7, 8]
    selection_sort(test_numbers)
    assert test_numbers == [3, 4, 5, 6, 7, 8], f"Test failed: {test_numbers}"
    print("Test passed!")
if __name__ == "__main__":
    numbers = [5, 6, 4, 3, 7, 8]
    print("Original list:", numbers)
    selection_sort(numbers)
    print("Sorted list:", numbers)
    test_selection_sort()