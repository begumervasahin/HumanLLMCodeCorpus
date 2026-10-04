
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
def main():
    array = [25, 66, 1, 4, 77, 55, 13, 5, 3]
    print("Original array:", array)
    bubble_sort(array)
    print("Sorted array:")
    for element in array:
        print(element, end=" ")
if __name__ == "__main__":
    main()