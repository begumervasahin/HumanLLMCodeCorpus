def bubble_sort(lst):
    length = len(lst)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(lst)
print(lst)