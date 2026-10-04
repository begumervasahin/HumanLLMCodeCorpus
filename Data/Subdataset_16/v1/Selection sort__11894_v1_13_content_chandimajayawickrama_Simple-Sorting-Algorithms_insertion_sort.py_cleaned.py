import time
import random
def fonk1(array):
    b1 = time.time()
    for i in range(1, len(array)):
        b2 = i
        while b2 > 0 and array[b2] < array[b2 - 1]:
            array[b2], array[b2 - 1] = array[b2 - 1], array[b2]
            b2 -= 1
    b3 = time.time()
    return array, b3 - b1
b4 = [random.randint(0, 100) for _ in range(10)]
print("Original list:", b4)
sorted_list, b5 = fonk1(b4)
print("Sorted list:", sorted_list)
print("Time taken to sort:", b5, "seconds")