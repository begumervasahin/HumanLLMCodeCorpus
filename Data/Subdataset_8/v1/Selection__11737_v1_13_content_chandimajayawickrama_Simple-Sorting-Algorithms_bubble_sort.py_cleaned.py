import time
def bubble_sort(array):
    start_time = time.time()
    swapped = False
    if len(array) == 0:
        return []
    while not swapped:
        swapped = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = False
    return array
try:
    l = input("Enter a list of integers separated by spaces: ").split(' ')
    l = [int(x) for x in l]
    sorted_list = bubble_sort(l)
    print("Sorted list:", sorted_list)
except ValueError:
    print("[]")