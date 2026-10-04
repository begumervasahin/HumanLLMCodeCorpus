import timeit
import random
def copy_array(src, src_start, dest, dest_start, length):
    for i in range(length):
        dest[dest_start + i] = src[src_start + i]
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)
    left_half = array[:mid]
    right_half = array[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(left_half, right_half, array)
    return array
def merge(left, right, merged):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1
    copy_array(left, i, merged, k, len(left) - i)
    copy_array(right, j, merged, k, len(right) - j)
def generate_random_numbers(size=5000, upper_limit=99999):
    initial_numbers = [7, 4, 3, 8, 1, 12, 9, 14]
    random_numbers = [random.randint(1, upper_limit) for _ in range(size)]
    return initial_numbers + random_numbers
def main():
    numbers = generate_random_numbers()
    start_time = timeit.default_timer()
    sorted_numbers = merge_sort(numbers)
    elapsed_time = timeit.default_timer() - start_time
    print(f"Merge Sort Time: {elapsed_time:.6f} seconds")
    print(sorted_numbers)
if __name__ == "__main__":
    main()