def bubble_sort(lst):
    new_list = lst[:]
    is_sorted = False
    while not is_sorted:
        idx = 0
        nswaps = 0
        lst_range = len(new_list) if len(new_list) % 2 == 0 else len(new_list) - 1
        while idx < lst_range - 1:
            if new_list[idx] > new_list[idx + 1]:
                new_list[idx], new_list[idx + 1] = new_list[idx + 1], new_list[idx]
                nswaps += 1
            idx += 1
        if nswaps == 0:
            is_sorted = True
    return new_list
if __name__ == "__main__":
    lst = [64, 25, 12, 22, 11]
    sorted_lst = bubble_sort(lst)
    print("Sorted list:", sorted_lst)