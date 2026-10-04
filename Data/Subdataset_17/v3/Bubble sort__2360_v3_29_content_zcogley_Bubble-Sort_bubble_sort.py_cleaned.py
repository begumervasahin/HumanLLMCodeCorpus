def bubble_sort(lst):
    sorted_list = lst[:]
    n = len(sorted_list)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for idx in range(n - 1):
            if sorted_list[idx] > sorted_list[idx + 1]:
                sorted_list[idx], sorted_list[idx + 1] = sorted_list[idx + 1], sorted_list[idx]
                is_sorted = False
    return sorted_list
if __name__ == "__main__":
    lst = [64, 25, 12, 22, 11]
    sorted_lst = bubble_sort(lst)
    print("Sorted list:", sorted_lst)