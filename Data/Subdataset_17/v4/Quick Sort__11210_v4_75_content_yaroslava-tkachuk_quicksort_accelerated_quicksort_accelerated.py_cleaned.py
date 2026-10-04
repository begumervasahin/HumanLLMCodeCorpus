import random
def insert_sort(lst):
    if not isinstance(lst, list):
        raise TypeError('The function argument must be a list containing numbers.')
    n = len(lst)
    if n < 2:
        return lst
    for i in range(1, n):
        el = lst[i]
        j = i - 1
        try:
            while j >= 0 and lst[j] > el:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = el
        except TypeError:
            print('The list must contain numbers.')
            return None
    return lst
def choose_pivot(lst, l, h, pi):
    pivots = {'first': l, 'last': h, 'middle': (l + h)
    if pi not in pivots:
        raise ValueError("Pivot options: 'first', 'last', 'middle', 'random'.")
    pivot_index = pivots[pi]
    pivot = lst[pivot_index]
    lst[pivot_index], lst[h] = lst[h], lst[pivot_index]
    return pivot, lst
def partition(lst, l, h, pi):
    pivot, lst = choose_pivot(lst, l, h, pi)
    i = l - 1
    for j in range(l, h):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[h] = lst[h], lst[i + 1]
    return i + 1
def quick_sort_rec(lst, l, h, pi, use_insertion_sort=False, threshold=10):
    if not isinstance(lst, list):
        raise TypeError('The function argument must be a list containing numbers.')
    if len(lst) < 2:
        return lst
    if l < h:
        if use_insertion_sort and (h - l) < threshold:
            lst[l:h + 1] = insert_sort(lst[l:h + 1])
        else:
            try:
                pivot_index = partition(lst, l, h, pi)
            except ValueError as e:
                print(e)
                return None
            if use_insertion_sort and (pivot_index - l) < threshold:
                lst[l:pivot_index] = insert_sort(lst[l:pivot_index])
            else:
                quick_sort_rec(lst, l, pivot_index - 1, pi, use_insertion_sort, threshold)
            if use_insertion_sort and (h - pivot_index) < threshold:
                lst[pivot_index + 1:h + 1] = insert_sort(lst[pivot_index + 1:h + 1])
            else:
                quick_sort_rec(lst, pivot_index + 1, h, pi, use_insertion_sort, threshold)
    return lst