list1 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
def insertion_sort(lst):
    for i in range(1, len(lst)):
        element = lst[i]
        j = i
        while j > 0 and lst[j - 1] > element:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = element
    return lst
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst
def shaker_sort(lst):
    n = len(lst)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end, start, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                swapped = True
        start += 1
    return lst
def gnome_sort(lst):
    i = 0
    while i < len(lst):
        if i == 0 or lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
list1_copy = list1[:]
print("Original List:", list1_copy)
print("Insertion Sort:", insertion_sort(list1_copy[:]))
print("Bubble Sort:", bubble_sort(list1_copy[:]))
print("Shaker Sort:", shaker_sort(list1_copy[:]))
print("Gnome Sort:", gnome_sort(list1_copy[:]))
print("Merge Sort:", merge_sort(list1_copy[:]))
print("Selection Sort:", selection_sort(list1_copy[:]))