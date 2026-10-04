import random
import pickle
import time
import matplotlib.pyplot as plt
time_list_bubble_sort = []
time_list_insertion_sort = []
avg_time_bubble_sort = []
avg_time_insertion_sort = []
def generate_and_store_array():
    array = random.sample(range(1, 300000), 200000)
    with open("data.txt", 'wb') as fp:
        pickle.dump(array, fp)
    return array
def load_array():
    with open("data.txt", 'rb') as fp:
        array = pickle.load(fp)
    return array
def measure_sorting_times(array):
    k = 2000
    for i in range(25):
        bubble_sort_times = []
        insertion_sort_times = []
        total_bubble_sort_time = 0.0
        total_insertion_sort_time = 0.0
        for _ in range(10):
            arr1 = random.sample(array, k)
            arr2 = random.sample(array, k)
            start_time = time.time()
            bubble_sort(arr1)
            bubble_sort_duration = time.time() - start_time
            bubble_sort_times.append(bubble_sort_duration)
            total_bubble_sort_time += bubble_sort_duration
            start_time = time.time()
            insertion_sort(arr2)
            insertion_sort_duration = time.time() - start_time
            insertion_sort_times.append(insertion_sort_duration)
            total_insertion_sort_time += insertion_sort_duration
        avg_time_bubble_sort.append(total_bubble_sort_time / 10)
        avg_time_insertion_sort.append(total_insertion_sort_time / 10)
        print(f"Average time for bubble sort with {k} elements: {avg_time_bubble_sort[-1]}")
        print(f"Average time for insertion sort with {k} elements: {avg_time_insertion_sort[-1]}")
        k += 2000
def plot_results():
    input_sizes = [2000 * i for i in range(1, 26)]
    plt.plot(input_sizes, avg_time_bubble_sort, 'r--', label='Bubble Sort')
    plt.plot(input_sizes, avg_time_insertion_sort, 'b--', label='Insertion Sort')
    plt.xlabel('Number of Elements')
    plt.ylabel('Average Time (seconds)')
    plt.legend()
    plt.show()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def insertion_sort(arr):
    n = len(arr)
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
def main():
    array = generate_and_store_array()
    measure_sorting_times(array)
    plot_results()
if __name__ == "__main__":
    main()