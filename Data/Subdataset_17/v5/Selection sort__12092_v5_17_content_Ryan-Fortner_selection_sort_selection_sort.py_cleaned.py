def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
def main():
    my_arr = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    print("Original array:", my_arr)
    sorted_array = selection_sort(my_arr)
    print("Sorted array:", sorted_array)
if __name__ == "__main__":
    main()