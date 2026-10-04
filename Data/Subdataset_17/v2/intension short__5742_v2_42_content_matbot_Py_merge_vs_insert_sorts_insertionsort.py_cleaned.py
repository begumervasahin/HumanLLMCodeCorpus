
def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        position = i - 1
        while position >= 0 and array[position] > current_value:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = current_value
def read_data_from_file(filename):
    all_lists = []
    with open(filename, "r") as file:
        for line in file:
            numbers = list(map(int, line.split()[1:]))
            all_lists.append(numbers)
    return all_lists
def write_data_to_file(filename, data):
    with open(filename, "w") as file:
        for number_list in data:
            file.write(" ".join(map(str, number_list)) + "\n")
def main():
    unsorted_data = read_data_from_file("data.txt")
    for sublist in unsorted_data:
        insertion_sort(sublist)
    write_data_to_file("insertionsort.txt", unsorted_data)
if __name__ == "__main__":
    main()