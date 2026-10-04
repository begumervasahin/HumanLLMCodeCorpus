import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
sorting_times = []
operation_counts = []
average_times = np.zeros(5)
def insertion_sort(numbers):
    operations = 1
    for i in range(1, len(numbers)):
        current_value = numbers[i]
        position = i
        swap_occurred = False
        while position > 0 and numbers[position - 1] > current_value:
            numbers[position] = numbers[position - 1]
            position -= 1
            operations += 1
            swap_occurred = True
        if not swap_occurred:
            operations += 1
        numbers[position] = current_value
    operation_counts.append(operations)
def measure_sorting_times():
    global sorting_times
    sorting_times.clear()
    for filename in cds.fileNames:
        data = []
        with open(filename, "r") as file:
            data = [int(line.strip()) for line in file]
        start_time = time.time()
        insertion_sort(data)
        end_time = time.time()
        sorting_times.append(end_time - start_time)
    cds.generateAverageValues(sorting_times, average_times)
def generate_cases():
    best_case = []
    average_case = []
    worst_case = []
    for i in range(len(operation_counts)):
        if i % 9 == 0:
            best_case.append(operation_counts[i])
        elif i % 9 == 4:
            worst_case.append(operation_counts[i])
        elif i % 9 in [1, 2, 3]:
            average_case.append(operation_counts[i])
    averaged_case = [
        (average_case[i] + average_case[i+1] + average_case[i+2]) / 3
        for i in range(0, len(average_case), 3)
    ]
    input_sizes = [200, 400, 600, 800, 1000]
    plt.plot(input_sizes, best_case, '-ro', label="Best Case")
    plt.plot(input_sizes, averaged_case, '-bo', label="Average Case")
    plt.plot(input_sizes, worst_case, '-go', label="Worst Case")
    plt.xlabel("Input Size")
    plt.ylabel("Operation Count")
    plt.title("Insertion Sort - Best, Average, and Worst Case Scenarios")
    plt.legend()
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    measure_sorting_times()
    generate_cases()