
def fonk1(array):
    for i in range(1, len(array)):
        b1 = array[i]
        b2 = i - 1
        while b2 >= 0 and array[b2] > b1:
            array[b2 + 1] = array[b2]
            b2 -= 1
        array[b2 + 1] = b1
def fonk2(filename):
    b3 = []
    with open(filename, "r") as file:
        for line in file:
            b4 = list(map(int, line.split()[1:]))
            b3.append(b4)
    return b3
def fonk3(filename, sorted_list):
    with open(filename, "w") as file:
        for sorted_numbers in sorted_list:
            file.write(" ".join(map(str, sorted_numbers)) + "\n")
if b5 = = "__main__":
    b6 = fonk2("data.txt")
    for data in b6:
        fonk1(data)
    fonk3("insertionsort.txt", b6)