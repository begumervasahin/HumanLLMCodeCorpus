from is_140422H import InsertionSort
def test_insertion_sort(number_list):
    print('Unsorted list:', number_list)
    sorted_list = InsertionSort(number_list)
    print('Sorted list:', sorted_list)
    is_sorted = all(sorted_list[i] <= sorted_list[i + 1] for i in range(len(sorted_list) - 1))
    if is_sorted and set(number_list) == set(sorted_list):
        print("Answer is the correct sorted list.")
    else:
        print("Answer is not the correct sorted list.")
    print()
if __name__ == "__main__":
    list1 = [20, 12, 8, 5, 7, 10, 14]
    list2 = [20, -7, 10, 14]
    list3 = []
    list4 = [0, 0, 0]
    big_list = [list1, list2, list3, list4]
    for lis in big_list:
        test_insertion_sort(lis)