
def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
    return array
if __name__ == "__main__":
    number_lists = []
    with open("data.txt", "r") as input_file:
        for line in input_file:
            data_list = list(map(int, line.split()[1:]))
            number_lists.append(data_list)
    for array in number_lists:
        insertion_sort(array)
    with open("insertionsort.txt", "w") as output_file:
        for array in number_lists:
            output_file.write(" ".join(map(str, array)) + "\n")