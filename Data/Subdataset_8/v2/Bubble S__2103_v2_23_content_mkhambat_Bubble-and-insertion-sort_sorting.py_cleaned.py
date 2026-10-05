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
def process_data():
    with open("data.txt", 'rb') as file:
        data = pickle.load(file)
    avg_time_bubble_sort = []
    avg_time_insertion_sort = []
    input_sizes = []
    increment = 2000
    for _ in range(25):
        total_time_bubble_sort = 0.0
        total_time_insertion_sort = 0.0
        for _ in range(10):
            arr1 = random.sample(data, increment)
            arr2 = random.sample(data, increment)
            start_time = time.time()
            bubble_sort(arr1)
            end_time = time.time()
            total_time_bubble_sort += end_time - start_time
            start_time = time.time()
            insertion_sort(arr2)
            end_time = time.time()
            total_time_insertion_sort += end_time - start_time
        avg_time_bubble_sort.append(total_time_bubble_sort / 10)
        avg_time_insertion_sort.append(total_time_insertion_sort / 10)
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