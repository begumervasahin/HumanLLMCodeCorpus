import time
def fonk1(array):
    b1 = time.time()
    b2 = False
    if len(array) == 0:
        return []
    while not b2:
        b2 = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                b2 = False
    return array
try:
    b3 = input("Enter a list of integers separated by spaces: ")
    b4 = [int(x) for x in b3.split()]
    b5 = fonk1(b4)
    print("Sorted list:", b5)
except ValueError:
    print("Invalid input. Please enter a list of integers separated by spaces.")