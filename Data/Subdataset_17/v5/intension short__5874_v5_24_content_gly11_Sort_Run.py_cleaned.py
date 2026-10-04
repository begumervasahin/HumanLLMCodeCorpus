import time
import sort_numbers
def read_numbers_from_file(filename):
    with open(filename, "r") as file:
        return list(map(int, file.read().split()))
def write_sorted_numbers_to_file(filename, sorted_list, running_time):
    with open(filename, "w") as file:
        file.write(" ".join(map(str, sorted_list)) + "\n")
        file.write(f"Running time: {running_time:.6f} Seconds\n")
def measure_sorting_time(sort_function, data):
    start_time = time.process_time()
    sort_function(data)
    end_time = time.process_time()
    return end_time - start_time
def main():
    number_list = read_numbers_from_file("NUM.txt")
    bubble_list = number_list[:]
    insertion_list = number_list[:]
    bubble_sort_time = measure_sorting_time(sort_numbers.bubble_sort, bubble_list)
    insertion_sort_time = measure_sorting_time(sort_numbers.insertion_sort, insertion_list)
    write_sorted_numbers_to_file("BUBBLE_SORTED.txt", bubble_list, bubble_sort_time)
    write_sorted_numbers_to_file("INSERTION_SORTED.txt", insertion_list, insertion_sort_time)
if __name__ == "__main__":
    main()