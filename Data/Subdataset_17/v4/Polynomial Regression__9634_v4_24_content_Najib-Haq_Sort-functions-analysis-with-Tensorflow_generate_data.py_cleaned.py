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
def gen_array(size):
    return [random.randrange(0, INT_MAX) for _ in range(size)]
def get_time(arr, sorted_flag, func_list=sort_functions):
    ans_list = []
    for func in func_list:
        total_time = 0
        for _ in range(MAX_ITERATION
            copy_arr = arr.copy() if not sorted_flag else arr
            start_time = time.time()
            func(copy_arr)
            total_time += (time.time() - start_time)
        avg_time = total_time / (MAX_ITERATION
        ans_list.append(avg_time)
    ans_list.append(ans_list.index(min(ans_list)))
    return ans_list
def get_data(start_size, end_size):
    total_data = []
    for size in range(start_size, end_size + 1, 100):
        print(f"Generating data for array size {size}")
        for case in range(3):
            arr = gen_array(size)
            data = [size]
            if case == 0:
                sorted_flag = True
                data.extend([1, 0, 0])
                arr.sort()
            else:
                sorted_flag = False
                if case == 1:
                    data.extend([0, 1, 0])
                else:
                    data.extend([0, 0, 1])
                    arr.sort(reverse=True)
            data.extend(get_time(arr, sorted_flag))
            total_data.append(data)
    return total_data
def write_to_csv(filename, data):
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file, dialect=csv.excel)
        writer.writerows(data)
if __name__ == "__main__":
    random.seed(time.time())
    sys.setrecursionlimit(1000000)
    total_data = get_data(1300, 4000)
    write_to_csv("data.csv", total_data)
    sys.setrecursionlimit(1000)