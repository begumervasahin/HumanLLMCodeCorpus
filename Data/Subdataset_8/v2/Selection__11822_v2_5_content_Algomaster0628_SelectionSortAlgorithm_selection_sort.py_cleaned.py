def selection_sort(num_list):
    sorted_list = []
    while num_list:
        min_value = min(num_list)
        sorted_list.append(min_value)
        num_list.remove(min_value)
        print_progress(sorted_list, num_list)
    print("\nSorted list:", sorted_list)
def print_progress(sorted_list, remaining_list):
    print("\nStep", len(sorted_list))
    print("Remaining:", remaining_list)
    print("Sorted:", sorted_list)
numbers = [2, 1, 5, 3, 4, 7, 6, 9, 8, 10]
selection_sort(numbers)