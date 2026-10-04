from is_140422H import InsertionSort
def test_insertion_sort(number_list):
    print(f"Unsorted list: {number_list}")
    sorted_list = InsertionSort(number_list)
    print(f"Sorted list: {sorted_list}")
    is_sorted = all(sorted_list[i] <= sorted_list[i + 1] for i in range(len(sorted_list) - 1))
    elements_match = set(number_list) == set(sorted_list)
    if is_sorted and elements_match:
        print("The list is sorted correctly.")
    else:
        print("The list is not sorted correctly.")
    print()
if __name__ == "__main__":
    test_cases = [
        [20, 12, 8, 5, 7, 10, 14],
        [20, -7, 10, 14],
        [],
        [0, 0, 0]
    ]
    for test_case in test_cases:
        test_insertion_sort(test_case)