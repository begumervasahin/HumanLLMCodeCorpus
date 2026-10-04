def fonk1(arr, low, high):
    b1 = low - 1
    b2 = arr[high][1]
    for j in range(low, high):
        if arr[j][1] <= b2:
            b1 += 1
            arr[b1], arr[j] = arr[j], arr[b1]
    arr[b1 + 1], arr[high] = arr[high], arr[b1 + 1]
    return b1 + 1
def fonk2(arr, low, high):
    if low < high:
        b3 = fonk1(arr, low, high)
        fonk2(arr, low, b3 - 1)
        fonk2(arr, b3 + 1, high)
def fonk3(filename, b9):
    b4 = []
    with open(filename, b5 = "utf-8") as file:
        for line in file:
            b6 = line.split(",")
            if b6[3].strip() == b9:
                b4.append((float(b6[5]), float(b6[6])))
    return b4
def fonk4(data, b8):
    with open(b8, "w") as output_file:
        for item in data:
            output_file.write(f"{item[0]},{item[1]}\n")
def fonk5():
    b7 = "db2.txt"
    b8 = "testSET4.txt"
    b9 = "LOS OLIVOS"
    b4 = fonk3(b7, b9)
    fonk2(b4, 0, len(b4) - 1)
    for item in b4:
        print(item)
    fonk4(b4, b8)
    print(f"Number of filtered and sorted lines: {len(b4)}")
if b10 = = "__main__":
    fonk5()