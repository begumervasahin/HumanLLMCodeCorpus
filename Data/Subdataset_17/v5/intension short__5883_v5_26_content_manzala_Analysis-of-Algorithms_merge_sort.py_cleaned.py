import timeit
import random
def array_copy(src, src_pos, dest, dest_pos, length):
    for i in range(length):
        dest[i + dest_pos] = src[i + src_pos]
def split_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)
    left_half = split_sort(array[:mid])
    right_half = split_sort(array[mid:])
    return merge_sort(left_half, right_half)
def merge_sort(left, right):
    merged = []
    l_index, r_index = 0, 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            merged.append(left[l_index])
            l_index += 1
        else:
            merged.append(right[r_index])
            r_index += 1
    merged.extend(left[l_index:])
    merged.extend(right[r_index:])
    return merged
def generate_random_numbers(size, lower_bound=1, upper_bound=99999):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]
numbers = [7, 4, 3, 8, 1, 12, 9, 14] + generate_random_numbers(5000)
start_time = timeit.default_timer()
sorted_numbers = split_sort(numbers)
elapsed_time = timeit.default_timer() - start_time
print(f"Merge Sort: {elapsed_time:.6f} seconds")
print(sorted_numbers)