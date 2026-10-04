import time
import sort_numbers
with open("NUM.txt", "r") as file:
    document = file.read()
number_list = list(map(int, document.split()))
bubble_list = number_list[:]
insertion_list = number_list[:]
start_time_bubble = time.process_time()
sort_numbers.bubble_sort(bubble_list)
end_time_bubble = time.process_time()
bubble_sort_time = end_time_bubble - start_time_bubble
start_time_insertion = time.process_time()
sort_numbers.insertion_sort(insertion_list)
end_time_insertion = time.process_time()
insertion_sort_time = end_time_insertion - start_time_insertion
with open("BUBBLE_SORTED.txt", "w") as bubble_file:
    bubble_file.write(" ".join(map(str, bubble_list)) + "\n")
    bubble_file.write(f"Running time: {bubble_sort_time} Seconds\n")
with open("INSERTION_SORTED.txt", "w") as insertion_file:
    insertion_file.write(" ".join(map(str, insertion_list)) + "\n")
    insertion_file.write(f"Running time: {insertion_sort_time} Seconds\n")