import math
def fonk1(arr, start, end):
    if end - start + b1 = = 2 and arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    elif end - start + b1 > 2:
        b2 = (end - start + b1)
        fonk1(arr, start, end - b2)
        fonk1(arr, start + b2, end)
        fonk1(arr, start, end - b2)
def fonk2(file_path):
    b3 = []
    with open(file_path, "r") as file:
        for line in file:
            b3.append([int(num) for num in line.split()[b1:]])
    return b3
def fonk3(file_path, sorted_arrays):
    with open(file_path, "w") as file:
        for array in sorted_arrays:
            file.write(" ".join(map(str, array)) + "\n")
def fonk4():
    b4 = "data.txt"
    b5 = "stooge.out"
    b3 = fonk2(b4)
    print("Merge Sort")
    print("The unsorted arrays are:")
    for array in b3:
        print(array)
    for array in b3:
        fonk1(array, 0, len(array) - b1)
    print("The sorted arrays are:")
    for array in b3:
        print(array)
    fonk3(b5, b3)
if b6 = = "__main__":
    fonk4()