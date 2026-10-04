
def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_value = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current_value:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current_value
def read_data(file_path):
    with open(file_path, "r") as file:
        return [list(map(int, line.split()[1:])) for line in file]
def write_data(file_path, sorted_lists):
    with open(file_path, "w") as file:
        for lst in sorted_lists:
            file.write(" ".join(map(str, lst)) + "\n")
def main(input_file, output_file):
    unsorted_lists = read_data(input_file)
    for lst in unsorted_lists:
        insertion_sort(lst)
    write_data(output_file, unsorted_lists)
if __name__ == "__main__":
    main("data.txt", "insertionsort.txt")