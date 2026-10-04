import math
def read_data_from_file(file_path):
    nums = []
    with open(file_path, "r") as file:
        for line in file:
            nums.append([int(num) for num in line.split()[1:]])
    return nums
def stooge_sort(array, start, end):
    if end - start + 1 == 2:
        if array[start] > array[end]:
            array[start], array[end] = array[end], array[start]
    elif end - start + 1 > 2:
        m = (end - start + 1)
        stooge_sort(array, start, end - m)
        stooge_sort(array, start + m, end)
        stooge_sort(array, start, end - m)
def write_data_to_file(file_path, data):
    with open(file_path, "w") as file:
        for line in data:
            file.write(" ".join(map(str, line)) + "\n")
def main():
    nums = read_data_from_file("data.txt")
    print("Merge Sort")
    print("The unsorted arrays are:")
    for array in nums:
        print(array)
    for array in nums:
        stooge_sort(array, 0, len(array) - 1)
    print("The sorted arrays are:")
    for array in nums:
        print(array)
    write_data_to_file("stooge.out", nums)
if __name__ == "__main__":
    main()