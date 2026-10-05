def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
def main():
    array = [25, 66, 1, 4, 77, 55, 13, 5, 3]
    bubble_sort(array)
    for element in array:
        print(element)
if __name__ == "__main__":
    main()