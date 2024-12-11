import random
b1 = [random.randrange(100) for i in range(10)]
def fonk1(array) -> bool:
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return True
    return False
def fonk2(array):
    for i in range(1, len(array)):
        b2 = array[i]
        b3 = i - 1
        while b3 >= 0 and b2 < array[b3]:
            array[b3 + 1] = array[b3]
            b3 -= 1
        array[b3 + 1] = b2
    return array
print("Original array:")
print(b1)
print("Sorted array:")
b4 = fonk2(b1)
print(b4)
if fonk1(b4):
    print("Array is not sorted.")
else:
    print("Array is sorted.")