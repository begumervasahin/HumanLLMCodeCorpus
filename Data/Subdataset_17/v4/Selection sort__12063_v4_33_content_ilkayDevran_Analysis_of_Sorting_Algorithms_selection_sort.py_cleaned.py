def selection_sort(alist):
    for j in range(len(alist) - 1):
        smallest_index = j
        for i in range(j + 1, len(alist)):
            if alist[i] < alist[smallest_index]:
                smallest_index = i
        alist[j], alist[smallest_index] = alist[smallest_index], alist[j]