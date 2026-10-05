import random
def partition(arr, low, high):
    pivot_index = random.randint(low, high - 1)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high - 1] = arr[high - 1], arr[pivot_index]
    p_index = low
    for j in range(low, high - 1):
        if arr[j] <= pivot:
            arr[p_index], arr[j] = arr[j], arr[p_index]
            p_index += 1
    arr[p_index], arr[high - 1] = arr[high - 1], arr[p_index]
    return p_index
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n)
print("Sorted array is:")
print(arr)