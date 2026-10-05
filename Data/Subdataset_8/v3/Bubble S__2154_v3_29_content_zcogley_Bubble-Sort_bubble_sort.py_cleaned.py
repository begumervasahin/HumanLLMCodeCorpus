def bubble_sort(lst):
    new_list = lst[:]
    is_sorted = False
    while not is_sorted:
        n_swaps = 0
        for i in range(len(new_list) - 1):
            if new_list[i] > new_list[i + 1]:
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
                n_swaps += 1
        if n_swaps == 0:
            is_sorted = True
    return new_list
def main():
    lst = [4, 2, 7, 1, 9, 5, 3]
    sorted_lst = bubble_sort(lst)
    print("Original list:", lst)
    print("Sorted list:", sorted_lst)
if __name__ == "__main__":
    main()