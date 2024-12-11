
def fonk1(array):
    for i in range(1, len(array)):
        b1 = array[i]
        b2 = i - 1
        while b2 >= 0 and array[b2] > b1:
            array[b2 + 1] = array[b2]
            b2 -= 1
        array[b2 + 1] = b1
    return array
if b3 = = "__main__":
    b4 = []
    with open("data.txt", "r") as input_file:
        for line in input_file:
            b5 = list(map(int, line.split()[1:]))
            b4.append(b5)
    for array in b4:
        fonk1(array)
    with open("insertionsort.txt", "w") as output_file:
        for array in b4:
            output_file.write(" ".join(map(str, array)) + "\n")