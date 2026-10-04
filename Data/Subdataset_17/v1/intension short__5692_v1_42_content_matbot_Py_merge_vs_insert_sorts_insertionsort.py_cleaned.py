
def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        index = i - 1
        while index >= 0 and array[index] > value:
            array[index + 1] = array[index]
            index -= 1
        array[index + 1] = value
def read_data_from_file(filename):
    number_list = []
    with open(filename, "r") as file:
        for line in file:
            numbers = list(map(int, line.split()[1:]))
            number_list.append(numbers)
    return number_list
def write_data_to_file(filename, sorted_list):
    with open(filename, "w") as file:
        for sorted_numbers in sorted_list:
            file.write(" ".join(map(str, sorted_numbers)) + "\n")
if __name__ == "__main__":
    unsorted_data = read_data_from_file("data.txt")
    for data in unsorted_data:
        insertion_sort(data)
    write_data_to_file("insertionsort.txt", unsorted_data)