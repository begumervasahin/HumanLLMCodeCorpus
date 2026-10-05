import random
def partition3(array, left, right):
    pivot = array[left]
    j, equal = left, left
    for i in range(left + 1, right + 1):
        if array[i] < pivot:
            equal += 1
            array[i], array[equal] = array[equal], array[i]
            array[j], array[equal] = array[equal], array[j]
            j += 1
        elif array[i] == pivot:
            equal += 1
            array[i], array[equal] = array[equal], array[i]
    if j > left:
        array[left], array[j - 1] = array[j - 1], array[left]
    else:
        array[left], array[j] = array[j], array[left]
    return j, equal
def randomized_quick_sort3(array, left, right):
    if left >= right:
        return
    pivot_index = random.randint(left, right)
    array[left], array[pivot_index] = array[pivot_index], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort3(array, left, m1 - 1)
    randomized_quick_sort3(array, m2 + 1, right)
if __name__ == '__main__':
    input_str = "5\n2 3 9 2 2"
    input_list = list(map(int, input_str.split()))
    n = input_list[0]
    array = input_list[1:]
    randomized_quick_sort3(array, 0, n - 1)
    print(' '.join(map(str, array)))
    print(array)