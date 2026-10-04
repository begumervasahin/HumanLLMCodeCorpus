import time
import sort_numbers
def fonk1(filename):
    with open(filename, "r") as file:
        return list(map(int, file.read().split()))
def fonk2(filename, sorted_list, running_time):
    with open(filename, "w") as file:
        file.write(" ".join(map(str, sorted_list)) + "\n")
        file.write(f"Running time: {running_time:.6f} Seconds\n")
def fonk3(sort_function, data):
    b1 = time.process_time()
    sort_function(data)
    b2 = time.process_time()
    return b2 - b1
def fonk4():
    b3 = fonk1("NUM.txt")
    b4 = b3[:]
    b5 = b3[:]
    b6 = fonk3(sort_numbers.bubble_sort, b4)
    b7 = fonk3(sort_numbers.insertion_sort, b5)
    fonk2("BUBBLE_SORTED.txt", b4, b6)
    fonk2("INSERTION_SORTED.txt", b5, b7)
if b8 = = "__main__":
    fonk4()