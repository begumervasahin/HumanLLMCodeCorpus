import time
import random
def bubble_sort(array):
    start_time = time.time()
    n = len(array)
    if n == 0:
        return []
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    print(f"Sorting completed in {end_time - start_time:.5f} seconds")
    return array
def main():
    try:
        input_list = input("Enter a list of integers separated by space: ").split()
        input_list = [int(x) for x in input_list]
        sorted_list = bubble_sort(input_list)
        print("Sorted list:", sorted_list)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")
if __name__ == "__main__":
    main()