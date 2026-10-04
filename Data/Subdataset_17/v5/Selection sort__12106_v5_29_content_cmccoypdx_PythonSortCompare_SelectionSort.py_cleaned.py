
def selection_sort(input_list):
    unsorted_list = input_list[:]
    sorted_list = []
    while unsorted_list:
        smallest = unsorted_list[0]
        for element in unsorted_list:
            if element < smallest:
                smallest = element
        sorted_list.append(smallest)
        unsorted_list.remove(smallest)
    return sorted_list
if __name__ == "__main__":
    sample_list = [34, 23, 12, 45, 9, 1, 24]
    print("Original list:", sample_list)
    sorted_sample_list = selection_sort(sample_list)
    print("Sorted list:", sorted_sample_list)