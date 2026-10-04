def stooge_sort(arr, start, end):
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if end - start + 1 > 2:
        third = (end - start + 1)
        stooge_sort(arr, start, end - third)
        stooge_sort(arr, start + third, end)
        stooge_sort(arr, start, end - third)
def read_input_file(file_path):
    arrays = []
    with open(file_path, "r") as file:
        for line in file:
            numbers = list(map(int, line.split()))
            arrays.append(numbers[1:])
    return arrays
def write_output_file(file_path, sorted_arrays):
    with open(file_path, "w") as file:
        for array in sorted_arrays:
            file.write(" ".join(map(str, array)) + "\n")
def display_arrays(title, arrays):
    print(f"{title}:")
    for array in arrays:
        print(array)
def main():
    input_file = "data.txt"
    output_file = "stooge.out"
    arrays = read_input_file(input_file)
    display_arrays("The unsorted arrays are", arrays)
    for array in arrays:
        stooge_sort(array, 0, len(array) - 1)
    display_arrays("The sorted arrays are", arrays)
    write_output_file(output_file, arrays)
if __name__ == "__main__":
    main()