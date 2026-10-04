
def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        j = i - 1
        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_value
def read_data(file_path):
    number_list = []
    with open(file_path, "r") as file:
        for line in file:
            numbers = list(map(int, line.split()[1:]))
            number_list.append(numbers)
    return number_list
def write_data(file_path, sorted_lists):
    with open(file_path, "w") as file:
        for lst in sorted_lists:
            file.write(" ".join(map(str, lst)) + "\n")
if __name__ == "__main__":
    input_file = "data.txt"
    output_file = "insertionsort.txt"
    unsorted_lists = read_data(input_file)
    for lst in unsorted_lists:
        insertion_sort(lst)
    write_data(output_file, unsorted_lists)