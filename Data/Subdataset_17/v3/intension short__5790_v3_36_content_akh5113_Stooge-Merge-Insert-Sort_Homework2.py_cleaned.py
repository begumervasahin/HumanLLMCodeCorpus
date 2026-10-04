import math
def read_data_from_file(file_path):
    with open(file_path, "r") as file:
        return [[int(num) for num in line.split()[1:]] for line in file]
def stooge_sort(array, start, end):
    if start >= end:
        return
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
    if end - start + 1 > 2:
        third = (end - start + 1)
        stooge_sort(array, start, end - third)
        stooge_sort(array, start + third, end)
        stooge_sort(array, start, end - third)
def write_data_to_file(file_path, data):
    with open(file_path, "w") as file:
        for line in data:
            file.write(" ".join(map(str, line)) + "\n")
def print_arrays(title, arrays):
    print(title)
    for array in arrays:
        print(array)
def main():
    input_file = "data.txt"
    output_file = "stooge.out"
    data = read_data_from_file(input_file)
    print_arrays("Unsorted Arrays:", data)
    for array in data:
        stooge_sort(array, 0, len(array) - 1)
    print_arrays("Sorted Arrays:", data)
    write_data_to_file(output_file, data)
if __name__ == "__main__":
    main()