import datetime
import statistics
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    items = [arr[0], arr[len(arr)
    pivot = statistics.median(items)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
start = datetime.datetime.now()
sorted_list = quick_sort(test)
finish = datetime.datetime.now()
print("Sorted list:", sorted_list)
print("Time taken:", finish - start)