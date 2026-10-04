import math
def read_data_from_file(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            numbers = [int(num) for num in line.split()[1:]]
            data.append(numbers)
    return data
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
def main():
    data = read_data_from_file("data.txt")
    print("Merge Sort")
    print("The unsorted arrays are:")
    for array in data:
        print(array)
    for array in data:
        stooge_sort(array, 0, len(array) - 1)
    print("The sorted arrays are:")
    for array in data:
        print(array)
    write_data_to_file("stooge.out", data)
if __name__ == "__main__":
    main()