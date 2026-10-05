
my_list = [0, 2, 100, 0, 120, 11]
for i in range(len(my_list) - 1):
    max_val = my_list[i]
    max_index = i
    for j in range(i + 1, len(my_list)):
        if my_list[j] > max_val:
            max_val = my_list[j]
            max_index = j
    if max_index != i:
        temp = my_list[i]
        my_list[i] = max_val
        my_list[max_index] = temp
print(my_list)