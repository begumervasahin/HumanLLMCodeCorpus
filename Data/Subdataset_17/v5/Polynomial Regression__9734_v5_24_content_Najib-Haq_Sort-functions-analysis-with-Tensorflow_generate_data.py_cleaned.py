import sorting_algos as s
import random
import time
import csv
import sys
INT_MAX = 10000000
MAX_ITERATION = 100000
sort_functions = [
    s.bubble_sort,
    s.selection_sort,
    s.insertion_sort,
    s.merge_sort,
    s.quick_sort,
    s.heap_sort
]
def generate_array(size):
    return [random.randint(0, INT_MAX) for _ in range(size)]
def measure_sort_times(array, is_sorted, sort_functions=sort_functions):
    times = []
    for sort_func in sort_functions:
        total_time = 0
        for _ in range(MAX_ITERATION
            test_array = array if is_sorted else array.copy()
            start_time = time.time()
            sort_func(test_array)
            total_time += (time.time() - start_time)
        avg_time = total_time / (MAX_ITERATION
        times.append(avg_time)
    fastest_index = times.index(min(times))
    times.append(fastest_index)
    return times
def generate_data(start_size, end_size):
    data = []
    for size in range(start_size, end_size + 1, 100):
        print(f"Generating data for array size {size}")
        for case in range(3):
            array = generate_array(size)
            case_data = [size]
            if case == 0:
                array.sort()
                case_data.extend([1, 0, 0])
                times = measure_sort_times(array, True)
            elif case == 1:
                case_data.extend([0, 1, 0])
                times = measure_sort_times(array, False)
            else:
                array.sort(reverse=True)
                case_data.extend([0, 0, 1])
                times = measure_sort_times(array, False)
            case_data.extend(times)
            data.append(case_data)
    return data
def write_data_to_csv(filename, data):
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
if __name__ == "__main__":
    random.seed(time.time())
    sys.setrecursionlimit(1000000)
    data = generate_data(1300, 4000)
    write_data_to_csv("data.csv", data)
    sys.setrecursionlimit(1000)