import timeit
import random
numbers = [7, 4, 8, 3, 1, 12, 9, 14]
def arrayCopy(src, srcPos, dest, destPos, length):
    for i in range(length):
        dest[i + destPos] = src[i + srcPos]
def split_Sort(array):
    if len(array) <= 1:
        return array
    left = array[0:(len(array) / 2)]
    right = array[(len(array) / 2):len(array)]
    split_Sort(left)
    split_Sort(right)
    merge_Sort(left,right,array)
    return array
def merge_Sort(left,right,array):
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
    arrayCopy(left,lcount,array,merge_count, len(left)-lcount)
    arrayCopy(right,rcount, array, merge_count, len(right) - rcount)
numbers = [7,4,3,8,1,12,9,14]
for x in range(0,5000):
    rand = random.randint(1,99999)
    numbers.append(rand)
start_time = timeit.default_timer()
split_Sort(numbers)
elapsed_time2 = timeit.default_timer() - start_time
print("Merge Sort: " + str(elapsed_time2))
print(numbers)