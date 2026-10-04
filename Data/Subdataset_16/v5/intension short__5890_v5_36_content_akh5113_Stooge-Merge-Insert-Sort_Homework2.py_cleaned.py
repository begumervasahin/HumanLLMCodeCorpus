def fonk1(arr, start, end):
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if end - start + 1 > 2:
        b1 = (end - start + 1)
        fonk1(arr, start, end - b1)
        fonk1(arr, start + b1, end)
        fonk1(arr, start, end - b1)
def fonk2(file_path):
    b2 = []
    with open(file_path, "r") as file:
        for line in file:
            b3 = list(map(int, line.split()))
            b2.append(b3[1:])
    return b2
def fonk3(file_path, sorted_arrays):
    with open(file_path, "w") as file:
        for array in sorted_arrays:
            file.write(" ".join(map(str, array)) + "\n")
def fonk4(title, b2):
    print(f"{title}:")
    for array in b2:
        print(array)
def fonk5():
    b4 = "data.txt"
    b5 = "stooge.out"
    b2 = fonk2(b4)
    fonk4("The unsorted b2 are", b2)
    for array in b2:
        fonk1(array, 0, len(array) - 1)
    fonk4("The sorted b2 are", b2)
    fonk3(b5, b2)
if b6 = = "__main__":
    fonk5()