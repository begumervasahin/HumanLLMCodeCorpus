import math
def fonk1(file_path):
    b1 = []
    with open(file_path, "r") as file:
        for line in file:
            b2 = [int(num) for num in line.split()[1:]]
            b1.append(b2)
    return b1
def fonk2(array, start, end):
    if start >= end:
        return
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
    if end - start + 1 > 2:
        b3 = (end - start + 1)
        fonk2(array, start, end - b3)
        fonk2(array, start + b3, end)
        fonk2(array, start, end - b3)
def fonk3(file_path, b1):
    with open(file_path, "w") as file:
        for line in b1:
            file.write(" ".join(map(str, line)) + "\n")
def fonk4():
    b1 = fonk1("b1.txt")
    print("Merge Sort")
    print("The unsorted arrays are:")
    for array in b1:
        print(array)
    for array in b1:
        fonk2(array, 0, len(array) - 1)
    print("The sorted arrays are:")
    for array in b1:
        print(array)
    fonk3("stooge.out", b1)
if b4 = = "__main__":
    fonk4()