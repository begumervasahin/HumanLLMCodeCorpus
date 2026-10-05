import random
def insertion_sort(arr):
    '''Insertion sort algorithm.'''
    if not isinstance(arr, list):
        raise TypeError('The function argument must be a list containing numbers.')
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def choose_pivot(arr, low, high, pivot_choice):
    '''Chooses the reference element and moves it to the last place in the list.'''
    pivots = {'first': low, 'last': high, 'middle': (low + high)
    pivot = arr[pivots[pivot_choice]]
    arr[pivots[pivot_choice]], arr[high] = arr[high], arr[pivots[pivot_choice]]
    return pivot, arr
def partition(arr, low, high, pivot_choice):
    '''Places the reference element in its correct position in the sorted list.'''
    pivot, arr = choose_pivot(arr, low, high, pivot_choice)
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort_recursive(arr, low, high, pivot_choice, modified=False, mod_length=10):
    '''Recursive version of the Quicksort algorithm.'''
    if not isinstance(arr, list):
        raise TypeError('The function argument must be a list containing numbers.')
    if len(arr) < 2:
        return arr
    if low < high:
        if modified and ((high - low) < mod_length):
            arr[low:high + 1] = insertion_sort(arr[low:high + 1])
        else:
            try:
                pivot_index = partition(arr, low, high, pivot_choice)
            except KeyError:
                print('Pivot options: first, last, middle, random.')
                return None
            if modified and ((pivot_index - low) < mod_length):
                arr[low:pivot_index] = insertion_sort(arr[low:pivot_index])
            else:
                quick_sort_recursive(arr, low, pivot_index - 1, pivot_choice, modified, mod_length)
            if modified and ((high - pivot_index) < mod_length):
                arr[pivot_index + 1:high + 1] = insertion_sort(arr[pivot_index + 1:high + 1])
            else:
                quick_sort_recursive(arr, pivot_index + 1, high, pivot_choice, modified, mod_length)
    return arr