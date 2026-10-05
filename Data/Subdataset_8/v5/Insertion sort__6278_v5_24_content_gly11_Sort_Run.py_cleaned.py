import time
import sort_numbers
with open("NUM.txt", "r") as file:
    numbers_str = file.read()
numbers_list = list(map(int, numbers_str.split()))
list_insertion_sort = numbers_list.copy()
start_time_bubble = time.time()
sort_numbers.bubble_sort(numbers_list)
end_time_bubble = time.time()
running_time_bubble = end_time_bubble - start_time_bubble
start_time_insertion = time.time()
sort_numbers.insertion_sort(list_insertion_sort)
end_time_insertion = time.time()
running_time_insertion = end_time_insertion - start_time_insertion
with open("BUBBLE_SORTED.txt", "w") as file_bubble:
    file_bubble.write(' '.join(map(str, numbers_list)) + '\n')
    file_bubble.write(f"Running time for Bubble Sort: {running_time_bubble} seconds\n")
with open("INSERTION_SORTED.txt", "w") as file_insertion:
    file_insertion.write(' '.join(map(str, list_insertion_sort)) + '\n')
    file_insertion.write(f"Running time for Insertion Sort: {running_time_insertion} seconds\n")