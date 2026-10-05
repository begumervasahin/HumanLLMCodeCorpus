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
numbers_list = read_numbers(READ_FILE)
list_insertion_sort = numbers_list.copy()
start_time_bubble_sort = time.time()
sorted_bubble_sort = sort_numbers.bubble_sort(numbers_list)
end_time_bubble_sort = time.time()
running_time_bubble_sort = end_time_bubble_sort - start_time_bubble_sort
start_time_insertion_sort = time.time()
sort_numbers.insertion_sort(list_insertion_sort)
end_time_insertion_sort = time.time()
running_time_insertion_sort = end_time_insertion_sort - start_time_insertion_sort
write_sorted_list(WRITE_B_FILE, sorted_bubble_sort, running_time_bubble_sort)
write_sorted_list(WRITE_I_FILE, list_insertion_sort, running_time_insertion_sort)