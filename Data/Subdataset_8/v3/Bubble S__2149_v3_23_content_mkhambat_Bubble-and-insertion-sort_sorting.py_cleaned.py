import random
import pickle
import time
import matplotlib.pyplot as plt
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
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
def generate_input_data():
    data = random.sample(range(1, 300000), 200000)
    with open("data.txt", 'wb') as file:
        pickle.dump(data, file)
def load_input_data():
    with open("data.txt", 'rb') as file:
        return pickle.load(file)
def measure_sorting_time(data, sorting_func):
    total_time = 0.0
    for _ in range(10):
        arr = random.sample(data, len(data))
        start_time = time.time()
        sorting_func(arr)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / 10
def process_data():
    data = load_input_data()
    avg_time_bubble_sort = []
    avg_time_insertion_sort = []
    input_sizes = []
    increment = 2000
    for _ in range(25):
        avg_time_bubble_sort.append(measure_sorting_time(data[:increment], bubble_sort))
        avg_time_insertion_sort.append(measure_sorting_time(data[:increment], insertion_sort))
        input_sizes.append(increment)
        increment += 2000
    plot_results(input_sizes, avg_time_bubble_sort, avg_time_insertion_sort)
def plot_results(input_sizes, bubble_sort_times, insertion_sort_times):
    plt.plot(input_sizes, bubble_sort_times, 'r--', label='Bubble Sort')
    plt.plot(input_sizes, insertion_sort_times, 'b--', label='Insertion Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Bubble Sort vs Insertion Sort')
    plt.legend()
    plt.grid(True)
    plt.show()
def main():
    generate_input_data()
    process_data()
if __name__ == "__main__":
    main()