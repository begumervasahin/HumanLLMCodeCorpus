import random
from time import time
a1 = 10001
b1 = random.sample(range(1, a1), a1 - 1)
def fonk1(input_list):
    b2 = len(input_list)
    for i in range(b2):
        b3 = True
        for j in range(0, b2 - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                b3 = False
        if b3:
            break
    return input_list
def fonk2(sort_func, data, sort_name):
    b4 = data[:]
    b5 = time()
    sort_func(b4)
    b6 = time() - b5
    print(f"{sort_name} algorithm ends in {b6:.4f} seconds to sort a list of {len(data)} items.")
    return b6
b7 = fonk2(bubble_sort, b1, "Bubble sort")
b8 = fonk2(sorted, b1, "System Python sort() (Timsort)")