def bubble_sort(lst):
    new_list = lst[:]
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for idx in range(len(new_list) - 1):
            if new_list[idx] > new_list[idx + 1]:
                new_list[idx], new_list[idx + 1] = new_list[idx + 1], new_list[idx]
                is_sorted = False
    return new_list