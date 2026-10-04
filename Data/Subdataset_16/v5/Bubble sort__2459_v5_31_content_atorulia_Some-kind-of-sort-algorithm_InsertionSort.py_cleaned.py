import random
def fonk1(b1 = 10, upper_limit=100):
    return [random.randrange(upper_limit) for _ in range(b1)]
def fonk2(array) -> bool:
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))
def fonk3(array):
    for i in range(1, len(array)):
        b2 = array[i]
        b3 = i - 1
        while b3 >= 0 and array[b3] > b2:
            array[b3 + 1] = array[b3]
            b3 -= 1
        array[b3 + 1] = b2
    return array
b4 = fonk1()
print("Original array:", b4)
b5 = fonk3(b4)
print("Sorted array:", b5)
print("Is the array sorted?", fonk2(b5))