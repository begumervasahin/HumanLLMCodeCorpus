def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high)
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def run_test_cases():
    test_list = [1, 3, 9, 11, 15, 19, 29]
    test_cases = [
        (25, "Index of {0} in the list: {1}"),
        (15, "Index of {0} in the list: {1}")
    ]
    for value, message in test_cases:
        result = binary_search(test_list, value)
        print(message.format(value, result))
if __name__ == "__main__":
    run_test_cases()