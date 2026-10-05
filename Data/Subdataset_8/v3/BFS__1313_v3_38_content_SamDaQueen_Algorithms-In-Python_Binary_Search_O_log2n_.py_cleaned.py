def binary_search(input_array, value):
    upper_bound = len(input_array) - 1
    lower_bound = 0
    while lower_bound <= upper_bound:
        mid = (upper_bound + lower_bound)
        if input_array[mid] == value:
            return mid
        elif value < input_array[mid]:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return -1
test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
