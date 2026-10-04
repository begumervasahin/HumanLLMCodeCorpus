list1 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
def insertion_sort(lst):
    for i in range(1, len(lst)):
        element = lst[i]
        j = i
        while j > 0 and lst[j-1] > element:
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = element
    return lst
def bubble_sort(lst):
    permutation = True
    passage = 0
    while permutation:
        permutation = False
        passage += 1
        for i in range(len(lst) - passage):
            if lst[i] > lst[i + 1]:
                permutation = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst
def shaker_sort(lst):
    permutation, way, element = True, 1, 0
    start, end = 0, len(lst) - 2
    while permutation:
        permutation = False
        while (element < end and way == 1) or (element > start and way == -1):
            if lst[element] > lst[element + 1]:
                permutation = True
                lst[element], lst[element + 1] = lst[element + 1], lst[element]
            element += way
        if way == 1:
            end -= 1
        else:
            start += 1
        way = -way
    return lst
def gnome_sort(lst):
    i_b, i_i, size = 1, 2, len(lst)
    while i_b < size:
        if lst[i_b - 1] <= lst[i_b]:
            i_b, i_i = i_i, i_i + 1
        else:
            lst[i_b - 1], lst[i_b] = lst[i_b], lst[i_b - 1]
            i_b -= 1
            if i_b == 0:
                i_b, i_i = i_i, i_i + 1
    return lst
def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result
def merge_sort(x):
    if len(x) <= 1:
        return x
    middle = len(x)
    left = x[:middle]
    right = x[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))
def selection_sort(lst):
    nb = len(lst)
    for i in range(nb):
        min_index = i
        for j in range(i + 1, nb):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
list1_copy = list1[:]
print("Insertion Sort:", insertion_sort(list1_copy[:]))
print("Bubble Sort:", bubble_sort(list1_copy[:]))
print("Shaker Sort:", shaker_sort(list1_copy[:]))
print("Gnome Sort:", gnome_sort(list1_copy[:]))
print("Merge Sort:", merge_sort(list1_copy[:]))
print("Selection Sort:", selection_sort(list1_copy[:]))