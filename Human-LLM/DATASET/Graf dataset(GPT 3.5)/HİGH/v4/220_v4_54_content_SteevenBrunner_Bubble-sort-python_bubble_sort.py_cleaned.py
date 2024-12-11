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
b3 = b1[:]
b4 = time()
fonk1(b3)
print(f"bubble sort algorithm ends in {time() - b4} seconds to sort a list of {a1 - 1} items.")
b3 = b1[:]
b4 = time()
b3.sort()
print(f"system python sort() Timsort algorithm ends in {time() - b4} seconds to sort a list of {a1 - 1} items.")