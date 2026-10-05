def read_arrays_from_file(file_name):
    arrays = []
    with open(file_name, "r") as file:
        for line in file:
            values = list(map(int, line.strip().split()[1:]))
            arrays.append(values)
    return arrays
def stooge_sort(array):
    def recursive_sort(arr, start, end):
        num_elms = end - start + 1
        if num_elms == 2:
            if arr[start] > arr[end]:
                arr[start], arr[end] = arr[end], arr[start]
        elif num_elms > 2:
            third = num_elms
            recursive_sort(arr, start, end - third)
            recursive_sort(arr, start + third, end)
            recursive_sort(arr, start, end - third)
    recursive_sort(array, 0, len(array) - 1)
def write_arrays_to_file(arrays, file_name):
    with open(file_name, "w") as file:
        for array in arrays:
            file.write(" ".join(map(str, array)) + "\n")
def main():
    file_name = "data.txt"
    arrays = read_arrays_from_file(file_name)
    print("Stooge Sort")
    print("The unsorted arrays are:")
    for array in arrays:
        print(array)
    for array in arrays:
        stooge_sort(array)
    print("The sorted arrays are:")
    for array in arrays:
        print(array)
    write_arrays_to_file(arrays, "stooge.out")
if __name__ == "__main__":
    main()