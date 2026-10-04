def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high)
        mid_value = input_array[mid]
        if mid_value == value:
            return mid
        elif mid_value < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
if __name__ == "__main__":
    test_list = [1, 3, 9, 11, 15, 19, 29]
    test_val1 = 25
    test_val2 = 15
    result1 = binary_search(test_list, test_val1)
    result2 = binary_search(test_list, test_val2)
    print(f"Index of {test_val1}: {result1 if result1 != -1 else 'not found'}")
    print(f"Index of {test_val2}: {result2 if result2 != -1 else 'not found'}")