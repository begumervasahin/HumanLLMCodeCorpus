def binary_search(sorted_list, value, low=0, high=None):
    if high is None:
        high = len(sorted_list) - 1
    if low > high:
        return -1
    mid = (low + high)
    if sorted_list[mid] == value:
        return mid
    elif sorted_list[mid] > value:
        return binary_search(sorted_list, value, low, mid - 1)
    else:
        return binary_search(sorted_list, value, mid + 1, high)
def main():
    example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search_value_1 = 5
    search_value_2 = 11
    result_1 = binary_search(example_list, search_value_1)
    result_2 = binary_search(example_list, search_value_2)
    print(f"Index of {search_value_1} in the list: {result_1}")
    print(f"Index of {search_value_2} in the list: {result_2}")
if __name__ == "__main__":
    main()