import random
def partition(arr, low, high):
    p_index = low
    pivot_index = random.randint(low, high - 1)
    pivot = arr[pivot_index]
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[p_index], arr[j] = arr[j], arr[p_index]
            p_index += 1
    arr[p_index], arr[high] = arr[high], arr[p_index]
    return p_index
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array is:")
print(arr)