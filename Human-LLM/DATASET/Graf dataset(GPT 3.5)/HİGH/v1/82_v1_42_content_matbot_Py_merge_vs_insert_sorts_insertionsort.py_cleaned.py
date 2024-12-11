def fonk1(array):
    for i in range(1, len(array)):
        b1 = i - 1
        b2 = array[i]
        while b1 >= 0 and array[b1] > b2:
            array[b1 + 1] = array[b1]
            b1 -= 1
        array[b1 + 1] = b2
    return array
if b3 = = "__main__":
    b4 = []
    with open("data.txt", "r") as input_file:
        for line in input_file:
            b5 = list(map(int, line.strip().split()[1:]))
            b4.append(b5)
    for number_list in b4:
        fonk1(number_list)
    with open("insertionsort.txt", "w") as output_file:
        for number_list in b4:
            output_file.write(" ".join(map(str, number_list)) + "\n")