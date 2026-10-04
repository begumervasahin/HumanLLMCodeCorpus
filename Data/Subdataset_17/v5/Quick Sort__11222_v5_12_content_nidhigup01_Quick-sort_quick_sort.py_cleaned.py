import datetime
import statistics
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    first, middle, last = arr[0], arr[len(arr)
    pivot = statistics.median([first, middle, last])
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
if __name__ == "__main__":
    test_array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    start_time = datetime.datetime.now()
    sorted_array = quick_sort(test_array)
    end_time = datetime.datetime.now()
    print("Sorted array:", sorted_array)
    print("Time taken:", end_time - start_time)