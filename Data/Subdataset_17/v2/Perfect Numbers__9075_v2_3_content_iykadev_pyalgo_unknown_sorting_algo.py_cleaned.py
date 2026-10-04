
unsorted_list = [6, 2, 7, 8, 3, 1, 10, 5, 4, 9]
sorted_list = []
while unsorted_list:
    min_value = unsorted_list[0]
    min_index = 0
    for i in range(len(unsorted_list)):
        if unsorted_list[i] < min_value:
            min_value = unsorted_list[i]
            min_index = i
    del unsorted_list[min_index]
    sorted_list.append(min_value)
print(sorted_list)