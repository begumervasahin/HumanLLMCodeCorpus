import time
import sort_numbers
with open("NUM.txt", "r") as file:
    b1 = file.read()
b2 = list(map(int, b1.split()))
b3 = b2.copy()
b4 = time.time()
sort_numbers.bubble_sort(b2)
b5 = time.time()
b6 = b5 - b4
b7 = time.time()
sort_numbers.insertion_sort(b3)
b8 = time.time()
b9 = b8 - b7
with open("BUBBLE_SORTED.txt", "w") as file_bubble:
    file_bubble.write(' '.join(map(str, b2)) + '\n')
    file_bubble.write(f"Running time: {b6} seconds")
with open("INSERTION_SORTED.txt", "w") as file_insertion:
    file_insertion.write(' '.join(map(str, b3)) + '\n')
    file_insertion.write(f"Running time: {b9} seconds")