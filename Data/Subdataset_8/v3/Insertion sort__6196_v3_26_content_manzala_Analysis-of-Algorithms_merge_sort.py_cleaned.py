import timeit
import random
def copy_array(src, src_pos, dest, dest_pos, length):
    for i in range(length):
        dest[i + dest_pos] = src[i + src_pos]
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)
    left = array[:mid]
    right = array[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, array)
    return array
def merge(left, right, array):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    copy_array(left, i, array, k, len(left) - i)
    copy_array(right, j, array, k, len(right) - j)
numbers = [7, 4, 8, 3, 1, 12, 9, 14]
for _ in range(5000):
    numbers.append(random.randint(1, 99999))
start_time = timeit.default_timer()
merge_sort(numbers)
elapsed_time = timeit.default_timer() - start_time
print("Merge Sort: " + str(elapsed_time))
print(numbers)