import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def yesNo(question):
    reply = str(input(question + " (y/n): ")).lower().strip()
    if reply[0] == 'y':
        return True
    elif reply[0] == 'n':
        return False
    else:
        return yesNo("Please Enter (y/n) ")
def main():
    print("\nPYTHON SORTING SCRIPTS")
    print("----------------------\n")
    while True:
        ans = True
        while ans:
            n = int(input("How many numbers (between 2 and 50,000; could take a couple minutes) do you want in the array? "))
            if n > 50000 or n < 2:
                print("Can't use that number, please try again")
            else:
                ans = False
        array = random.sample(range(1, n+1), n)
        if yesNo("Do you want to see the array?"):
            print(array)
        start = time.time()
        sorted_array = bubbleSort(array.copy())
        print("Bubble Sort Result:", sorted_array)
        print("Time elapsed: ", str(time.time() - start) + "\n")
        start = time.time()
        sorted_array = selectionSort(array.copy())
        print("Selection Sort Result:", sorted_array)
        print("Time elapsed: ", str(time.time() - start) + "\n")
        start = time.time()
        sorted_array = insertionSort(array.copy())
        print("Insertion Sort Result:", sorted_array)
        print("Time elapsed: ", str(time.time() - start) + "\n")
        start = time.time()
        sorted_array = heapSort(array.copy())
        print("Heap Sort Result:", sorted_array)
        print("Time elapsed: ", str(time.time() - start) + "\n")
        start = time.time()
        sorted_array = array.copy()
        quickSort(sorted_array)
        print("Quick Sort Result:", sorted_array)
        print("Time elapsed: ", str(time.time() - start) + "\n")
        if not yesNo("Try again with another array?"):
            break
    input("Press any key to quit...")
if __name__ == '__main__':
    main()