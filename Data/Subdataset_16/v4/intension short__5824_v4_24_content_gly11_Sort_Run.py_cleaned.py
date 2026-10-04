import time
import sort_numbers
with open("NUM.txt", "r") as file:
    b1 = file.read()
b2 = list(map(int, b1.split()))
b3 = b2[:]
b4 = b2[:]
b5 = time.process_time()
sort_numbers.bubble_sort(b3)
b6 = time.process_time()
b7 = b6 - b5
b8 = time.process_time()
sort_numbers.insertion_sort(b4)
b9 = time.process_time()
b10 = b9 - b8
with open("BUBBLE_SORTED.txt", "w") as bubble_file:
    bubble_file.write(" ".join(map(str, b3)) + "\n")
    bubble_file.write(f"Running time: {b7} Seconds\n")
with open("INSERTION_SORTED.txt", "w") as insertion_file:
    insertion_file.write(" ".join(map(str, b4)) + "\n")
    insertion_file.write(f"Running time: {b10} Seconds\n")