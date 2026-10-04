
unsorted_list = [6, 2, 7, 8, 3, 1, 10, 5, 4, 9]
sorted_list = []
while unsorted_list:
    min_value = unsorted_list[0]
    min_index = 0
    for i, value in enumerate(unsorted_list):
        if value < min_value:
            min_value = value
            min_index = i
    sorted_list.append(unsorted_list.pop(min_index))
print(sorted_list)