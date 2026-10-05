def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    equal = [x for x in lista if x == pivot]
    less = [x for x in lista if x < pivot]
    greater = [x for x in lista if x > pivot]
    return quicksort(less) + equal + quicksort(greater)
def selection_sort(v):
    sorted_list = []
    while v:
        min_value = min(v)
        sorted_list.append(min_value)
        v.remove(min_value)
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
def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        middle = len(v)
        left = mergesort(v[:middle])
        right = mergesort(v[middle:])
        return merge(left, right)