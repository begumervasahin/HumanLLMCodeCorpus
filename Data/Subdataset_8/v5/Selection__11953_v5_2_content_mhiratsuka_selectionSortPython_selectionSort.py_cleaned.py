
my_list = [0, 2, 100, 0, 120, 11]
for i in range(len(my_list) - 1):
    max_val = max(my_list[i:])
    max_index = my_list.index(max_val, i)
    if max_index != i:
        my_list[i], my_list[max_index] = max_val, my_list[i]
print(my_list)