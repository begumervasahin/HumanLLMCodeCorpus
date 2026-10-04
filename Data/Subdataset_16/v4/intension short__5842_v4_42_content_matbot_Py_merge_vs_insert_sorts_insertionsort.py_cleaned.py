
def fonk1(array):
    for i in range(1, len(array)):
        b1 = array[i]
        b2 = i - 1
        while b2 >= 0 and array[b2] > b1:
            array[b2 + 1] = array[b2]
            b2 -= 1
        array[b2 + 1] = b1
def fonk2(file_path):
    b3 = []
    with open(file_path, "r") as file:
        for line in file:
            b4 = list(map(int, line.split()[1:]))
            b3.append(b4)
    return b3
def fonk3(file_path, sorted_lists):
    with open(file_path, "w") as file:
        for lst in sorted_lists:
            file.write(" ".join(map(str, lst)) + "\n")
if b5 = = "__main__":
    b6 = "data.txt"
    b7 = "insertionsort.txt"
    b8 = fonk2(b6)
    for lst in b8:
        fonk1(lst)
    fonk3(b7, b8)