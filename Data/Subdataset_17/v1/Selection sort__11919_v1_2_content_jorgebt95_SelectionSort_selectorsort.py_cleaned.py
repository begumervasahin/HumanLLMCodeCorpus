def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_position = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_position]:
                min_position = j
        numbers[i], numbers[min_position] = numbers[min_position], numbers[i]
def test_selection_sort():
    numbers = [5, 6, 4, 3, 7, 8]
    selection_sort(numbers)
    assert numbers == [3, 4, 5, 6, 7, 8], f"Expected [3, 4, 5, 6, 7, 8] but got {numbers}"
    print("Test passed!")
if __name__ == "__main__":
    test_selection_sort()