def insertion_sort(lists):
    length = len(lists)
    for j in range(1, length):
        key = lists[j]
        i = j - 1
        while i >= 0 and lists[i] > key:
            lists[i + 1] = lists[i]
            i -= 1
        lists[i + 1] = key
    return lists
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", my_list)
sorted_list_insertion = insertion_sort(my_list.copy())
print("Sorted list (Insertion Sort):", sorted_list_insertion)
sorted_list_bubble = bubble_sort(my_list.copy())
print("Sorted list (Bubble Sort):", sorted_list_bubble)