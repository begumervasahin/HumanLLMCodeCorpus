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
b5 = fonk1(b1)
b6 = b5.copy()
b7 = time.clock()
b8 = sort_numbers.bubble_sort(b5)
b9 = time.clock()
b10 = b9 - b7
b11 = time.clock()
sort_numbers.insertion_sort(b6)
b12 = time.clock()
b13 = b12 - b11
fonk2(b2, b8, b10)
fonk2(b3, b6, b13)