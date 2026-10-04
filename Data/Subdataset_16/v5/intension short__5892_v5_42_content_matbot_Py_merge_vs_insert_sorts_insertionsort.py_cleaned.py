
def fonk1(lst):
    for i in range(1, len(lst)):
        b1 = lst[i]
        b2 = i - 1
        while b2 >= 0 and lst[b2] > b1:
            lst[b2 + 1] = lst[b2]
            b2 -= 1
        lst[b2 + 1] = b1
def fonk2(file_path):
    with open(file_path, "r") as file:
        return [list(map(int, line.split()[1:])) for line in file]
def fonk3(file_path, sorted_lists):
    with open(file_path, "w") as file:
        for lst in sorted_lists:
            file.write(" ".join(map(str, lst)) + "\n")
def fonk4(input_file, output_file):
    b3 = fonk2(input_file)
    for lst in b3:
        fonk1(lst)
    fonk3(output_file, b3)
if b4 = = "__main__":
    fonk4("data.txt", "insertionsort.txt")