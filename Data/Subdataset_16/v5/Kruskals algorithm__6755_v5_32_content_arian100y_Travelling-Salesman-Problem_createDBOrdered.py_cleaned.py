def fonk1(arr, low, high):
    b1 = low - 1
    b2 = arr[high][0]
    for j in range(low, high):
        if arr[j][0] <= b2:
            b1 += 1
            arr[b1], arr[j] = arr[j], arr[b1]
    arr[b1 + 1], arr[high] = arr[high], arr[b1 + 1]
    return b1 + 1
def fonk2(arr, low, high):
    if low < high:
        b3 = fonk1(arr, low, high)
        fonk2(arr, low, b3 - 1)
        fonk2(arr, b3 + 1, high)
def fonk3(filename, b11):
    b4 = []
    with open(filename, b5 = "utf-8") as file:
        for line in file:
            b6 = line.strip().split(",")
            if b6[3] == b11:
                b7 = float(b6[5])
                b8 = float(b6[6])
                b4.append((b7, b8))
    fonk2(b4, 0, len(b4) - 1)
    return b4
def fonk4(b4, b10):
    with open(b10, "w") as output_file:
        for b7, b8 in b4:
            output_file.write(f"{b7},{b8}\n")
def fonk5():
    b9 = "db2.txt"
    b10 = "testSET4.txt"
    b11 = "LOS OLIVOS"
    b12 = fonk3(b9, b11)
    for coord in b12:
        print(coord)
    fonk4(b12, b10)
    print(f"Total b4: {len(b12)}")
if b13 = = "__main__":
    print("Sorting b4 for LOS OLIVOS...")
    fonk5()