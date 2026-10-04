import time
def fonk1(array):
    b1 = time.time()
    b2 = len(array)
    if b2 = = 0:
        return array
    for i in range(b2):
        b3 = False
        for j in range(0, b2 - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                b3 = True
        if not b3:
            break
    print(f"Sorting took {time.time() - b1:.6f} seconds")
    return array
def fonk2():
    try:
        b4 = input("Enter the numbers to be sorted, separated by spaces: ")
        b5 = [int(x) for x in b4.split()]
        return b5
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")
        return []
def fonk3():
    b5 = fonk2()
    if b5:
        b6 = fonk1(b5)
        print("Sorted list:", b6)
if b7 = = "__main__":
    fonk3()