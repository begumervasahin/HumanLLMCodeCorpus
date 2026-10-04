def insertion_sort(lst):
    length = len(lst)
    for j in range(1, length):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = key
    return lst
def bubble_sort(lst):
    count = len(lst)
    for i in range(count):
        for j in range(0, count - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", unsorted_list)
    print("Sorted list using insertion sort:", insertion_sort(unsorted_list.copy()))
    print("Sorted list using bubble sort:", bubble_sort(unsorted_list.copy()))