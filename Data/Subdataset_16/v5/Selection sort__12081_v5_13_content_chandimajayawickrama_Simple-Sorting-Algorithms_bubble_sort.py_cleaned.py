import time
def fonk1(array):
    b1 = time.time()
    b2 = len(array)
    if b2 = = 0:
        return array
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
    b5 = input("Enter a list of integers separated by space: ")
    return [int(x) for x in b5.split()]
def fonk3():
    try:
        b6 = fonk2()
        b7 = fonk1(b6)
        print("Sorted list:", b7)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")
if b8 = = "__main__":
    fonk3()