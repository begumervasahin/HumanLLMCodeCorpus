import time
def bubble_sort(array):
    start_time = time.time()
    n = len(array)
    if n == 0:
        return array
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    print("Sorting took {:.6f} seconds".format(time.time() - start_time))
    return array
if __name__ == "__main__":
    try:
        l = input("Enter the numbers to be sorted, separated by spaces: ").split(' ')
        l = [int(x) for x in l]
        sorted_list = bubble_sort(l)
        print("Sorted list:", sorted_list)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")