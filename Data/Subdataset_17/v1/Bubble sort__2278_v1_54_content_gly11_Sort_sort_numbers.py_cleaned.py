vdef insertion_sort(lists):
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
    for i in range(count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:")
    print(sample_list)
    sorted_list_insertion = insertion_sort(sample_list.copy())
    print("\nSorted list using insertion sort:")
    print(sorted_list_insertion)
    sorted_list_bubble = bubble_sort(sample_list.copy())
    print("\nSorted list using bubble sort:")
    print(sorted_list_bubble)