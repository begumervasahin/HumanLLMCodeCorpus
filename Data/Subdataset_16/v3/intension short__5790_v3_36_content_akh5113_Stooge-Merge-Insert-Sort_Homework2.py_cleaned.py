import math
def fonk1(file_path):
    with open(file_path, "r") as file:
        return [[int(num) for num in line.split()[1:]] for line in file]
def fonk2(array, start, end):
    if start >= end:
        return
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
    if end - start + 1 > 2:
        b1 = (end - start + 1)
        fonk2(array, start, end - b1)
        fonk2(array, start + b1, end)
        fonk2(array, start, end - b1)
def fonk3(file_path, b4):
    with open(file_path, "w") as file:
        for line in b4:
            file.write(" ".join(map(str, line)) + "\n")
def fonk4(title, arrays):
    print(title)
    for array in arrays:
        print(array)
def fonk5():
    b2 = "b4.txt"
    b3 = "stooge.out"
    b4 = fonk1(b2)
    fonk4("Unsorted Arrays:", b4)
    for array in b4:
        fonk2(array, 0, len(array) - 1)
    fonk4("Sorted Arrays:", b4)
    fonk3(b3, b4)
if b5 = = "__main__":
    fonk5()