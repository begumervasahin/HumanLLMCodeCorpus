import timeit
import random
def array_copy(src, src_pos, dest, dest_pos, length):
    for i in range(length):
        dest[i + dest_pos] = src[i + src_pos]
def split_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)
    left = array[:mid]
    right = array[mid:]
    split_sort(left)
    split_sort(right)
    merge_sort(left, right, array)
    return array
def merge_sort(left, right, array):
    left_index, right_index, merged_index = 0, 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            array[merged_index] = left[left_index]
            left_index += 1
        else:
            array[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1
    array_copy(left, left_index, array, merged_index, len(left) - left_index)
    array_copy(right, right_index, array, merged_index, len(right) - right_index)
numbers = [7, 4, 3, 8, 1, 12, 9, 14]
for _ in range(5000):
    rand = random.randint(1, 99999)
    numbers.append(rand)
start_time = timeit.default_timer()
split_sort(numbers)
elapsed_time = timeit.default_timer() - start_time
print("Merge Sort Time: {:.6f} seconds".format(elapsed_time))
print(numbers)