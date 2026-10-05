import time
import sort_numbers
b1 = "NUM.txt"
b2 = "BUBBLE_SORTED.txt"
b3 = "INSERTION_SORTED.txt"
def fonk1(filename):
    with open(filename, "r") as file:
        b4 = file.read()
    return list(map(int, b4.split()))
def fonk2(filename, sorted_list, running_time):
    with open(filename, "w") as file:
        file.write(' '.join(map(str, sorted_list)) + '\n')
        file.write(f"Running time: {running_time} Seconds")
def fonk3(sort_func, data):
    b5 = time.time()
    b6 = sort_func(data)
    b7 = time.time()
    return b6, b7 - b5
b8 = fonk1(b1)
sorted_bubble_sort, b9 = fonk3(sort_numbers.bubble_sort, b8)
b10 = b8.copy()
sorted_insertion_sort, b11 = fonk3(sort_numbers.insertion_sort, b10)
fonk2(b2, sorted_bubble_sort, b9)
fonk2(b3, sorted_insertion_sort, b11)