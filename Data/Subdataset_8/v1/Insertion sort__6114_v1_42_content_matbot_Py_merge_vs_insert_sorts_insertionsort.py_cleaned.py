def insertion_sort(array):
    for i in range(1, len(array)):
        index = i - 1
        value = array[i]
        while index >= 0 and array[index] > value:
            array[index + 1] = array[index]
            index -= 1
        array[index + 1] = value
    return array
if __name__ == "__main__":
    number_lists = []
    with open("data.txt", "r") as input_file:
        for line in input_file:
            data_list = list(map(int, line.strip().split()[1:]))
            number_lists.append(data_list)
    for number_list in number_lists:
        insertion_sort(number_list)
    with open("insertionsort.txt", "w") as output_file:
        for number_list in number_lists:
            output_file.write(" ".join(map(str, number_list)) + "\n")