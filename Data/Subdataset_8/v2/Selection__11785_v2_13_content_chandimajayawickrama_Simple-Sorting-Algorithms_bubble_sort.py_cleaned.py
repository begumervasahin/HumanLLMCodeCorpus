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
    user_input = input("Enter a list of integers separated by spaces: ")
    user_list = [int(x) for x in user_input.split()]
    sorted_list = bubble_sort(user_list)
    print("Sorted list:", sorted_list)
except ValueError:
    print("Invalid input. Please enter a list of integers separated by spaces.")