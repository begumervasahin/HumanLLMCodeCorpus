def selection_sort(input_list):
    unsorted_list = list(input_list)
    sorted_list = []
    while unsorted_list:
        smallest = unsorted_list[0]
        for item in unsorted_list:
            if item < smallest:
                smallest = item
        sorted_list.append(smallest)
        unsorted_list.remove(smallest)
    return sorted_list
if __name__ == "__main__":
    example_list = [64, 25, 12, 22, 11]
    sorted_list = selection_sort(example_list)
    print("Original list:", example_list)
    print("Sorted list:", sorted_list)