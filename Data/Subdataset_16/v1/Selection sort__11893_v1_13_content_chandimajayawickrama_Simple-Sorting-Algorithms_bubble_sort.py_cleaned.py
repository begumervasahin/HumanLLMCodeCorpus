import time
def fonk1(array):
    b1 = time.time()
    b2 = len(array)
    if b2 = = 0:
        return array
    for i in range(b2):
        b3 = False
        for j in range(0, b2-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                b3 = True
        if not b3:
            break
    print("Sorting took {:.6f} seconds".format(time.time() - b1))
    return array
if b4 = = "__main__":
    try:
        b5 = input("Enter the numbers to be sorted, separated by spaces: ").split(' ')
        b5 = [int(x) for x in b5]
        b6 = fonk1(b5)
        print("Sorted list:", b6)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")