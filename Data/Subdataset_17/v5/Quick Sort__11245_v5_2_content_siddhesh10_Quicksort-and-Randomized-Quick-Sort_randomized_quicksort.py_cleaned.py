import random
def partition(arr, low, high):
    pivot_index = random.randint(low, high - 1)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    partition_index = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[partition_index], arr[j] = arr[j], arr[partition_index]
            partition_index += 1
    arr[partition_index], arr[high] = arr[high], arr[partition_index]
    return partition_index
def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array is:")
    print(arr)