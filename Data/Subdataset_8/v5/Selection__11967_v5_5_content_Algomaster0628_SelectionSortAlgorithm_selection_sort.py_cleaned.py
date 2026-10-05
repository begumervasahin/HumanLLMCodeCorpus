def selection_sort(num_list):
    sorted_list = []
    while num_list:
        min_value = min(num_list)
        sorted_list.append(min_value)
        num_list.remove(min_value)
        print('\nStep', len(sorted_list))
        print('Unsorted list:', num_list)
        print('Sorted list:', sorted_list)
    print('\nFinish:', num_list)
    print('Sorted list:', sorted_list)
numbers = [2, 1, 5, 3, 4, 7, 6, 9, 8, 10]
selection_sort(numbers)