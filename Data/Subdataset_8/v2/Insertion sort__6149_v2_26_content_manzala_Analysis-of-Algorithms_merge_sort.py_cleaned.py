import timeit
import random
def array_copy(src, src_pos, dest, dest_pos, length):
    for i in range(length):
        dest[i + dest_pos] = src[i + src_pos]
def split_sort(array):
    if len(array) <= 1:
        return array
    left = array[0:len(array)
    right = array[len(array)
    split_sort(left)
    split_sort(right)
    merge_sort(left, right, array)
    return array
def merge_sort(left, right, array):
    rcount = 0
    lcount = 0
    merge_count = 0
    while lcount < len(left) and rcount < len(right):
        if left[lcount] > right[rcount]:
            array[merge_count] = right[rcount]
            rcount += 1
        else:
            array[merge_count] = left[lcount]
            lcount += 1
        merge_count += 1
    array_copy(left, lcount, array, merge_count, len(left) - lcount)
    array_copy(right, rcount, array, merge_count, len(right) - rcount)
numbers = [7, 4, 8, 3, 1, 12, 9, 14]
for x in range(0, 5000):
    rand = random.randint(1, 99999)
    numbers.append(rand)
start_time = timeit.default_timer()
split_sort(numbers)
elapsed_time = timeit.default_timer() - start_time
print("Merge Sort: " + str(elapsed_time))
print(numbers)