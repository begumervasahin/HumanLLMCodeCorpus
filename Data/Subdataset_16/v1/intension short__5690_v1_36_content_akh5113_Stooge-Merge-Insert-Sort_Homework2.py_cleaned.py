import math
def fonk1(file_path):
    b1 = []
    with open(file_path, "r") as file:
        for line in file:
            b1.append([int(num) for num in line.split()[b2:]])
    return b1
def fonk2(array, start, end):
    if end - start + b2 = = 2:
        if array[start] > array[end]:
            array[start], array[end] = array[end], array[start]
    elif end - start + b2 > 2:
        b3 = (end - start + b2)
        fonk2(array, start, end - b3)
        fonk2(array, start + b3, end)
        fonk2(array, start, end - b3)
def fonk3(file_path, data):
    with open(file_path, "w") as file:
        for line in data:
            file.write(" ".join(map(str, line)) + "\n")
def fonk4():
    b1 = fonk1("data.txt")
    print("Merge Sort")
    print("The unsorted arrays are:")
    for array in b1:
        print(array)
    for array in b1:
        fonk2(array, 0, len(array) - b2)
    print("The sorted arrays are:")
    for array in b1:
        print(array)
    fonk3("stooge.out", b1)
if b4 = = "__main__":
    fonk4()