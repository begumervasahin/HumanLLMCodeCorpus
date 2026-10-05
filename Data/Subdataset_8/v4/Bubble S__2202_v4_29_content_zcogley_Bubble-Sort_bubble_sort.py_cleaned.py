def bubble_sort(lst):
    new_list = lst[:]
    is_sorted = False
    while not is_sorted:
        idx = 0
        n_swaps = 0
        lst_range = len(new_list) if len(new_list) % 2 == 0 else len(new_list) - 1
        while idx < lst_range:
            a = new_list[idx]
            b = new_list[idx + 1]
            if a > b:
                new_list[idx] = b
                new_list[idx + 1] = a
                n_swaps += 1
            idx += 1
        if n_swaps == 0:
            is_sorted = True
    return new_list