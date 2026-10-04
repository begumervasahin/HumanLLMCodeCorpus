import random
def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pindex = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[pindex], arr[j] = arr[j], arr[pindex]
            pindex += 1
    arr[pindex], arr[high] = arr[high], arr[pindex]
    return pindex
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
if __name__ == '__main__':
    sample_array = [10, 7, 8, 9, 1, 5]
    n = len(sample_array)
    quick_sort(sample_array, 0, n - 1)
    print("Sorted array is:")
    print(sample_array)