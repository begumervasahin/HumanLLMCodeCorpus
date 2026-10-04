def binary_search(input_array, value):
    up = len(input_array)
    down = 0
    mid = up
    c = up
    while (value != input_array[mid]) and (c >= 0):
        if value < input_array[mid]:
            up = mid
            mid = mid - (up - down)
        else:
            down = mid
            mid = mid + (up - down)
        c = c - 1
    if c < 0:
        return -1
    else:
        return mid
if __name__ == "__main__":
    test_list = [1, 3, 9, 11, 15, 19, 29]
    test_val1 = 25
    test_val2 = 15
    result1 = binary_search(test_list, test_val1)
    result2 = binary_search(test_list, test_val2)
    print(f"Index of {test_val1} in the list: {result1}")
    print(f"Index of {test_val2} in the list: {result2}")