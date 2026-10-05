import time
def fonk1(array):
    b1 = time.time()
    for i in range(1, len(array)):
        b2 = i
        while b2 > 0 and array[b2] < array[b2 - 1]:
            array[b2], array[b2 - 1] = array[b2 - 1], array[b2]
            b2 -= 1
    return array
try:
    b3 = input("Enter a list of integers separated by spaces: ")
    b4 = [int(x) for x in b3.split()]
    b5 = fonk1(b4)
    print("Sorted list:", b5)
except ValueError:
    print("Invalid input. Please enter a list of integers separated by spaces.")