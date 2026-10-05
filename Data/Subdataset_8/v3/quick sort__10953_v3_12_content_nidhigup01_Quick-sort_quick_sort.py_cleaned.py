import datetime
import statistics
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = choose_pivot(arr)
    left, middle, right = partition(arr, pivot)
    return quick_sort(left) + middle + quick_sort(right)
def choose_pivot(arr):
    items = [arr[0], arr[len(arr)
    return statistics.median(items)
def partition(arr, pivot):
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left, middle, right
def test_quick_sort():
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    start_time = datetime.datetime.now()
    sorted_list = quick_sort(test)
    end_time = datetime.datetime.now()
    print("Sorted list:", sorted_list)
    print("Time taken:", end_time - start_time)
if __name__ == "__main__":
    test_quick_sort()