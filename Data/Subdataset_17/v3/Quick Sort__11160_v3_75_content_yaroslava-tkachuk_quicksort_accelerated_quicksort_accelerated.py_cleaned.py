import random
def insert_sort(lst):
    if not isinstance(lst, list):
        raise TypeError('The function argument must be a list containing numbers.')
    n = len(lst)
    if n < 2:
        return lst
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
def choose_pivot(lst, low, high, pivot_type):
    pivot_indices = {
        'first': low,
        'last': high,
        'middle': (low + high)
        'random': random.randint(low, high)
    }
    if pivot_type not in pivot_indices:
        raise ValueError('Pivot options: first, last, middle, random.')
    pivot_index = pivot_indices[pivot_type]
    lst[pivot_index], lst[high] = lst[high], lst[pivot_index]
    return lst[high], lst
def partition(lst, low, high, pivot_type):
    pivot, lst = choose_pivot(lst, low, high, pivot_type)
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1
def quick_sort_rec(lst, low, high, pivot_type, modified=False, threshold=10):
    if not isinstance(lst, list):
        raise TypeError('The function argument must be a list containing numbers.')
    if len(lst) < 2:
        return lst
    if low < high:
        if modified and (high - low) < threshold:
            lst[low:high + 1] = insert_sort(lst[low:high + 1])
        else:
            pivot_index = partition(lst, low, high, pivot_type)
            quick_sort_rec(lst, low, pivot_index - 1, pivot_type, modified, threshold)
            quick_sort_rec(lst, pivot_index + 1, high, pivot_type, modified, threshold)
    return lst
if __name__ == "__main__":
    sample_list = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = quick_sort_rec(sample_list, 0, len(sample_list) - 1, 'middle', modified=True, threshold=10)
    print(sorted_list)