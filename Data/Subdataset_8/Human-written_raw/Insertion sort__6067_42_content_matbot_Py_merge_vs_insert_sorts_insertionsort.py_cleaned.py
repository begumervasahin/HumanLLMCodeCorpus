
def insertionsort(array):
    for i in range(1, len(array)):
        index = i - 1
        value = array[i]
        while index >= 0 and array[index] > value:
            array[index + 1] = array[index]
            index -= 1
        array[index + 1] = value
if __name__ == "__main__":
    number_list = []
    with open("data.txt", "r") as ifile:
        for line in ifile:
            data_list = []
            data = line.split()
            data.pop(0)
            for number in data:
                data_list.append(int(number))
            number_list.append(data_list)
    for x in number_list:
        insertionsort(x)
    with open("insertionsort.txt", "w+") as ofile:
        for x in number_list:
            for y in x:
                ofile.write("%i " % y)
            ofile.write("\n")