import time
import random
def selection_sort(arr):
    for k in range(len(arr) - 1):
        min_index = k
        for n in range(k + 1, len(arr)):
            if arr[n] < arr[min_index]:
                min_index = n
        arr[k], arr[min_index] = arr[min_index], arr[k]
    return arr
def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = cur
    return arr
def generate_random_array(length, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(length)]
def measure_sorting_time(sort_function, arr):
    start = time.process_time()
    sort_function(arr)
    end = time.process_time()
    return end - start
def print_average_sorting_times(average_times, length):
    scenarios = [
        "Increasing Selection",
        "Decreasing Selection",
        "Random Selection",
        "Increasing Insertion",
        "Decreasing Insertion",
        "Random Insertion"
    ]
    for i, scenario in enumerate(scenarios):
        print(f"{length}-Val {scenario}: {average_times[i]:.20f}")
if __name__ == '__main__':
    length = int(input('How many values should be generated? '))
    arr_sel_inc = list(range(1, length + 1))
    arr_sel_dec = list(range(length, 0, -1))
    arr_sel_ran = generate_random_array(length)
    arr_ins_inc = arr_sel_inc.copy()
    arr_ins_dec = arr_sel_dec.copy()
    arr_ins_ran = arr_sel_ran.copy()
    sort_functions = [selection_sort, selection_sort, selection_sort, insertion_sort, insertion_sort, insertion_sort]
    array_arrays = [arr_sel_inc, arr_sel_dec, arr_sel_ran, arr_ins_inc, arr_ins_dec, arr_ins_ran]
    array_times = [[measure_sorting_time(sort_function, arr) for _ in range(5)] for sort_function, arr in zip(sort_functions, array_arrays)]
    average_times = [sum(times) / 5 for times in array_times]
    print_average_sorting_times(average_times, length)