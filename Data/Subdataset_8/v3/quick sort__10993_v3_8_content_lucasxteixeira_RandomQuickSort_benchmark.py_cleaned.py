import timeit
import random
def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def random_quick_sort(arr, low, high):
    if low < high:
        partition_index = random_partition(arr, low, high)
        random_quick_sort(arr, low, partition_index - 1)
        random_quick_sort(arr, partition_index + 1, high)
def random_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[high], arr[random_index] = arr[random_index], arr[high]
    return partition(arr, low, high)
def median_random_quick_sort(arr, low, high):
    if low < high:
        partition_index = median_random_partition(arr, low, high)
        median_random_quick_sort(arr, low, partition_index - 1)
        median_random_quick_sort(arr, partition_index + 1, high)
def median_random_partition(arr, low, high):
    median_index = get_median_index(arr, low, high)
    arr[high], arr[median_index] = arr[median_index], arr[high]
    return partition(arr, low, high)
def get_median_index(arr, low, high):
    mid = (low + high)
    if arr[low] <= arr[mid] <= arr[high] or arr[high] <= arr[mid] <= arr[low]:
        return mid
    elif arr[mid] <= arr[low] <= arr[high] or arr[high] <= arr[low] <= arr[mid]:
        return low
    else:
        return high
if __name__ == "__main__":
    algorithms = {
        "Quick Sort": quick_sort,
        "Random Quick Sort": random_quick_sort,
        "Median Random Quick Sort": median_random_quick_sort
    }
    sizes = [1000, 10000, 100000]
    for name, algorithm in algorithms.items():
        print(name)
        for size in sizes:
            s = [random.random() for _ in range(size)]
            print(f"{size} elements:")
            print(min(timeit.Timer('a=s[:]; algorithm(a, 0, len(a) - 1)', globals=globals()).repeat(10, 100)))