import random
from time import time
a1 = 10001
b1 = random.sample(range(1, a1), a1 - 1)
def fonk1(input_list):
    b2 = len(input_list)
    for i in range(b2):
        b3 = False
        for j in range(0, b2 - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                b3 = True
        if not b3:
            break
    return input_list
def fonk2(sort_function, data):
    b4 = time()
    sort_function(data)
    return time() - b4
if b5 = = "__main__":
    b6 = b1.copy()
    b7 = fonk2(bubble_sort, b6)
    print(f"Bubble sort algorithm ends in {b7:.3f} seconds to sort a list of {a1 - 1} items.")
    b8 = b1.copy()
    b9 = fonk2(b8.sort, b8)
    print(f"System Python sort() Timsort algorithm ends in {b9:.3f} seconds to sort a list of {a1 - 1} items.")