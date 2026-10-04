import random
from time import time
a1 = 10001
b1 = random.sample(range(1, a1), a1 - 1)
def fonk1(input_list):
    b2 = False
    while not b2:
        b2 = True
        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                b2 = False
    return input_list
def fonk2(sort_function, data):
    b3 = time()
    sort_function(data)
    return time() - b3
if b4 = = "__main__":
    b5 = b1.copy()
    b6 = fonk2(bubble_sort, b5)
    print(f"Bubble sort algorithm ends in {b6:.3f} seconds to sort a list of {a1 - 1} items.")
    b7 = b1.copy()
    b8 = fonk2(b7.sort, b7)
    print(f"System Python sort() Timsort algorithm ends in {b8:.3f} seconds to sort a list of {a1 - 1} items.")