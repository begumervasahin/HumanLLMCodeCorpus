def quicksort(alist):
    _quicksort_helper(alist, 0, len(alist) - 1)
def _quicksort_helper(alist, first, last):
    if first < last:
        split_point = _partition(alist, first, last)
        _quicksort_helper(alist, first, split_point - 1)
        _quicksort_helper(alist, split_point + 1, last)
def _partition(alist, first, last):
    pivot_value = alist[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark += 1
        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp
    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp
    return right_mark
alist = [57, 26, 93, 77, 33, 44, 50, 20]
quicksort(alist)
print(alist)