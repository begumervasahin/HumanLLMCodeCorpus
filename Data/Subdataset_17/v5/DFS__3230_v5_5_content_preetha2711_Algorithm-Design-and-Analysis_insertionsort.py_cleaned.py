def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        position = i
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1
        array[position] = current_value
def main():
    array_to_sort = [12, 11, 4, 3, 1, 1, 6, 7]
    insertion_sort(array_to_sort)
    print("Sorted array:", array_to_sort)
if __name__ == "__main__":
    main()