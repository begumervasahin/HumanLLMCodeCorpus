
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
def fonk3(filename, data):
    with open(filename, "w") as file:
        for number_list in data:
            file.write(" ".join(map(str, number_list)) + "\n")
def fonk4():
    b5 = fonk2("data.txt")
    for sublist in b5:
        fonk1(sublist)
    fonk3("insertionsort.txt", b5)
if b6 = = "__main__":
    fonk4()