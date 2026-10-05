def binary_search(input_array, value):
    upper_bound = len(input_array)
    lower_bound = 0
    mid = upper_bound
    count = upper_bound
    while (value != input_array[mid]) and (count >= 0):
        if value < input_array[mid]:
            upper_bound = mid
            mid = mid - (upper_bound - lower_bound)
        else:
            lower_bound = mid
            mid = mid + (upper_bound - lower_bound)
        count = count - 1
    if count < 0:
        return -1
    else:
        return mid
test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
