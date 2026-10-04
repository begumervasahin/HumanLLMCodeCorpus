from is_140422H import InsertionSort
def test_insertion_sort(number_list):
    print(f"Unsorted list: {number_list}")
    sorted_list = InsertionSort(number_list)
    print(f"Sorted list: {sorted_list}")
    if is_list_sorted(sorted_list) and elements_match(number_list, sorted_list):
        print("The list is sorted correctly.")
    else:
        print("The list is not sorted correctly.")
    print()
def is_list_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
def elements_match(original, sorted_list):
    return set(original) == set(sorted_list)
if __name__ == "__main__":
    test_cases = [
        [20, 12, 8, 5, 7, 10, 14],
        [20, -7, 10, 14],
        [],
        [0, 0, 0]
    ]
    for test_case in test_cases:
        test_insertion_sort(test_case)