import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def yes_no(question):
    while True:
        reply = input(question + " (y/n): ").strip().lower()
        if reply in ['y', 'yes']:
            return True
        elif reply in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")
def main():
    print("\nPYTHON SORTING SCRIPTS")
    print("----------------------\n")
    while True:
        while True:
            n = int(input("How many numbers (between 2 and 50,000; could take a couple minutes) do you want in the array? "))
            if 2 <= n <= 50000:
                break
            else:
                print("Invalid number, please try again.")
        array = random.sample(range(1, n + 1), n)
        if yes_no("Do you want to see the array?"):
            print(array)
        start_time = time.time()
        sorted_array = bubbleSort(array.copy())
        print("Bubble Sort Result:", sorted_array)
        print("Time elapsed: {:.2f} seconds\n".format(time.time() - start_time))
        start_time = time.time()
        sorted_array = selectionSort(array.copy())
        print("Selection Sort Result:", sorted_array)
        print("Time elapsed: {:.2f} seconds\n".format(time.time() - start_time))
        start_time = time.time()
        sorted_array = insertionSort(array.copy())
        print("Insertion Sort Result:", sorted_array)
        print("Time elapsed: {:.2f} seconds\n".format(time.time() - start_time))
        start_time = time.time()
        sorted_array = heapSort(array.copy())
        print("Heap Sort Result:", sorted_array)
        print("Time elapsed: {:.2f} seconds\n".format(time.time() - start_time))
        start_time = time.time()
        sorted_array = array.copy()
        quickSort(sorted_array)
        print("Quick Sort Result:", sorted_array)
        print("Time elapsed: {:.2f} seconds\n".format(time.time() - start_time))
        if not yes_no("Try again with another array?"):
            break
    input("Press any key to quit...")
if __name__ == '__main__':
    main()