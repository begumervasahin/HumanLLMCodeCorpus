def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    equals = [x for x in lst if x == pivot]
    less = [x for x in lst if x < pivot]
    greater = [x for x in lst if x > pivot]
    return quick_sort(less) + equals + quick_sort(greater)
def selection_sort(lst):
    sorted_list = []
    temp = lst[:]
    while temp:
        min_val = min(temp)
        sorted_list.append(min_val)
        temp.remove(min_val)
    return sorted_list
def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        middle = len(lst)
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])
        return merge(left, right)