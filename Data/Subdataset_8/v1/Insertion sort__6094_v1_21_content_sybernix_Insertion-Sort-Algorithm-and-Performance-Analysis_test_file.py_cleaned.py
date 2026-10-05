def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def test_insertion_sort(number_list):
    print('Unsorted list:', number_list)
    sorted_list = insertion_sort(number_list)
    print('Sorted list:', sorted_list)
    is_sorted = all(sorted_list[i] <= sorted_list[i + 1] for i in range(len(sorted_list) - 1))
    if is_sorted:
        print("Answer is the correct sorted list")
    else:
        print('Answer is not the correct sorted list')
list1 = [20, 12, 8, 5, 7, 10, 14]
list2 = [20, -7, 10, 14]
list3 = []
list4 = [0, 0, 0]
big_list = [list1, list2, list3, list4]
for lst in big_list:
    test_insertion_sort(lst)