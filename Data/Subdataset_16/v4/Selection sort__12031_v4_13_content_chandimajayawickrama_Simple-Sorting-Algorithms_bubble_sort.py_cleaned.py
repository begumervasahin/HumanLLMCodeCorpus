import time
import random
def fonk1(array):
    b1 = time.time()
    b2 = len(array)
    if b2 = = 0:
        return []
    for i in range(b2):
        b3 = False
        for j in range(0, b2 - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                b3 = True
        if not b3:
            break
    b4 = time.time()
    print(f"Sorting completed in {b4 - b1:.5f} seconds")
    return array
def fonk2():
    try:
        b5 = input("Enter a list of integers separated by space: ").split()
        b5 = [int(x) for x in b5]
        b6 = fonk1(b5)
        print("Sorted list:", b6)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")
if b7 = = "__main__":
    fonk2()