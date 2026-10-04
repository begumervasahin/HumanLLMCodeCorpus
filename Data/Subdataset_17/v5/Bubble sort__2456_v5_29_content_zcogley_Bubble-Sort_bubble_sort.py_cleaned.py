def bubble_sort(lst):
    sorted_list = lst[:]
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for idx in range(len(sorted_list) - 1):
            if sorted_list[idx] > sorted_list[idx + 1]:
                sorted_list[idx], sorted_list[idx + 1] = sorted_list[idx + 1], sorted_list[idx]
                is_sorted = False
    return sorted_list