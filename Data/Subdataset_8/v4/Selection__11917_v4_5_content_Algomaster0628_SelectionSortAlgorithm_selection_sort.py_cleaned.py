def selection_sort(num_list):
    sorted_list = []
    while len(num_list) > 0:
        min_value = num_list[0]
        for number in num_list:
            if number < min_value:
                min_value = number
        print('\nStep ', len(sorted_list) + 1)
        print(num_list)
        print(sorted_list)
        sorted_list.append(min_value)
        num_list.remove(min_value)
    print('\nFinish:', num_list)
    print(sorted_list)
numbers = [2, 1, 5, 3, 4, 7, 6, 9, 8, 10]
selection_sort(numbers)