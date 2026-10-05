import time
def bubble_sort(array):
    start_time = time.time()
    swapped = False
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array
try:
    l = input("Enter space-separated numbers: ").split()
    l = [int(x) for x in l]
    sorted_list = bubble_sort(l)
    print("Sorted list:", sorted_list)
except ValueError:
    print("Invalid input. Please enter space-separated numbers.")