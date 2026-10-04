
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i - 1
        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = current_value
def read_data_from_file(filename):
    lists_of_numbers = []
    with open(filename, "r") as file:
        for line in file:
            numbers = [int(num) for num in line.split()[1:]]
            lists_of_numbers.append(numbers)
    return lists_of_numbers
def write_data_to_file(filename, data):
    with open(filename, "w") as file:
        for number_list in data:
            file.write(" ".join(map(str, number_list)) + "\n")
def main():
    unsorted_data = read_data_from_file("data.txt")
    for numbers in unsorted_data:
        insertion_sort(numbers)
    write_data_to_file("insertionsort.txt", unsorted_data)
if __name__ == "__main__":
    main()