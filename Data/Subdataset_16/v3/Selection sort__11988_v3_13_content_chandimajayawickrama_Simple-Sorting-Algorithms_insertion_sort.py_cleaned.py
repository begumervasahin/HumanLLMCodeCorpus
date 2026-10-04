import time
import random
def fonk1(array):
    b1 = time.time()
    for i in range(1, len(array)):
        b2 = array[i]
        b3 = i - 1
        while b3 >= 0 and b2 < array[b3]:
            array[b3 + 1] = array[b3]
            b3 -= 1
        array[b3 + 1] = b2
    b4 = time.time()
    b5 = b4 - b1
    return array, b5
def fonk2(size, b6 = 0, upper_bound=100):
    return [random.randint(b6, upper_bound) for _ in range(size)]
b7 = fonk2(10)
print("Original list:", b7)
sorted_list, b5 = fonk1(b7)
print("Sorted list:", sorted_list)
print("Time taken to sort:", b5, "seconds")