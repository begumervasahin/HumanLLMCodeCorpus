def fonk1(b5):
    b1 = []
    with open(b5, "r") as file:
        for line in file:
            b2 = list(map(int, line.strip().split()[1:]))
            b1.append(b2)
    return b1
def fonk2(array):
    def fonk3(arr, start, end):
        b3 = end - start + 1
        if b3 = = 2:
            if arr[start] > arr[end]:
                arr[start], arr[end] = arr[end], arr[start]
        elif b3 > 2:
            b4 = b3
            fonk3(arr, start, end - b4)
            fonk3(arr, start + b4, end)
            fonk3(arr, start, end - b4)
    fonk3(array, 0, len(array) - 1)
def fonk4(b1, b5):
    with open(b5, "w") as file:
        for array in b1:
            file.write(" ".join(map(str, array)) + "\n")
def fonk5():
    b5 = "data.txt"
    b1 = fonk1(b5)
    print("Stooge Sort")
    print("The unsorted b1 are:")
    for array in b1:
        print(array)
    for array in b1:
        fonk2(array)
    print("The sorted b1 are:")
    for array in b1:
        print(array)
    fonk4(b1, "stooge.out")
if b6 = = "__main__":
    fonk5()