import time
def fonk1(array):
    b1 = time.time()
    b2 = False
    b3 = len(array)
    for i in range(b3):
        for j in range(0, b3-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                b2 = True
        if not b2:
            break
    return array
try:
    b4 = input("Enter space-separated numbers: ").split()
    b4 = [int(x) for x in b4]
    b5 = fonk1(b4)
    print("Sorted list:", b5)
except ValueError:
    print("Invalid input. Please enter space-separated numbers.")