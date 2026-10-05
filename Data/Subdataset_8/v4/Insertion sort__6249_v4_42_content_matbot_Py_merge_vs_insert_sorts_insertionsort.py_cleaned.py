
def insertion_sort(array):
    for i in range(1, len(array)):
        index = i - 1
        value = array[i]
        while index >= 0 and array[index] > value:
            array[index + 1] = array[index]
            index -= 1
        array[index + 1] = value
if __name__ == "__main__":
    number_lists = []
    with open("data.txt", "r") as input_file:
        for line in input_file:
            data_list = []
            data = line.split()
            data.pop(0)
            for number in data:
                data_list.append(int(number))
            number_lists.append(data_list)
    for x in number_lists:
        insertion_sort(x)
    with open("insertionsort.txt", "w+") as output_file:
        for x in number_lists:
            for y in x:
                output_file.write("%i " % y)
            output_file.write("\n")