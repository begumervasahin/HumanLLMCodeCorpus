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
    for i in range(0, count):
        for j in range(i + 1, count):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", my_list)
sorted_list_insertion = insertion_sort(my_list.copy())
print("Sorted list (Insertion Sort):", sorted_list_insertion)
sorted_list_bubble = bubble_sort(my_list.copy())
print("Sorted list (Bubble Sort):", sorted_list_bubble)