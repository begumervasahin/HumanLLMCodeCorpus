
def fonk1(arr):
    for i in range(1, len(arr)):
        b1 = arr[i]
        b2 = i - 1
        while b2 >= 0 and arr[b2] > b1:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1
def fonk2(filename):
    b3 = []
    with open(filename, "r") as file:
        for line in file:
            b4 = [int(num) for num in line.split()[1:]]
            b3.append(b4)
    return b3
def fonk3(filename, data):
    with open(filename, "w") as file:
        for number_list in data:
            file.write(" ".join(map(str, number_list)) + "\n")
def fonk4():
    b5 = fonk2("data.txt")
    for b4 in b5:
        fonk1(b4)
    fonk3("insertionsort.txt", b5)
if b6 = = "__main__":
    fonk4()