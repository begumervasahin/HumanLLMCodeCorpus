import time
import random
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr
if __name__ == '__main__':
    length = int(input('How many values should be generated? '))
    min_val = 0
    max_val = 100
    ascending = list(range(1, length + 1))
    descending = list(range(length, 0, -1))
    random_array = [random.randint(min_val, max_val) for _ in range(length)]
    arrays = [ascending, descending, random_array]
    average_times = []
    for arr in arrays:
        times = []
        for _ in range(5):
            temp_arr = arr.copy()
            start_time = time.perf_counter()
            if arr == ascending or arr == descending:
                selection_sort(temp_arr)
            else:
                insertion_sort(temp_arr)
            end_time = time.perf_counter()
            times.append(end_time - start_time)
        average_times.append(sum(times) / 5)
    labels = ["Increasing Selection", "Decreasing Selection", "Random Selection"]
    for label, avg_time in zip(labels, average_times):
        print(f'{length}-Val {label}: {avg_time:.20f}')