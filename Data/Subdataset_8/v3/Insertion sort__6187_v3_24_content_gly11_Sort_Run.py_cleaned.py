import time
import sort_numbers
READ_FILE = "NUM.txt"
WRITE_B_FILE = "BUBBLE_SORTED.txt"
WRITE_I_FILE = "INSERTION_SORTED.txt"
def read_numbers(filename):
    with open(filename, "r") as file:
        numbers_str = file.read()
    return list(map(int, numbers_str.split()))
def write_sorted_list(filename, sorted_list, running_time):
    with open(filename, "w") as file:
        file.write(' '.join(map(str, sorted_list)) + '\n')
        file.write(f"Running time: {running_time} Seconds")
def measure_sorting_time(sort_func, data):
    start_time = time.time()
    sorted_data = sort_func(data)
    end_time = time.time()
    return sorted_data, end_time - start_time
numbers_list = read_numbers(READ_FILE)
sorted_bubble_sort, running_time_bubble_sort = measure_sorting_time(sort_numbers.bubble_sort, numbers_list)
list_insertion_sort = numbers_list.copy()
sorted_insertion_sort, running_time_insertion_sort = measure_sorting_time(sort_numbers.insertion_sort, list_insertion_sort)
write_sorted_list(WRITE_B_FILE, sorted_bubble_sort, running_time_bubble_sort)
write_sorted_list(WRITE_I_FILE, sorted_insertion_sort, running_time_insertion_sort)