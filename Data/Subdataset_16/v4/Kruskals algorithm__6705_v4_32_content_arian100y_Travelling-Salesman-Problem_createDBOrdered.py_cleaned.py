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
def fonk3():
    with open("db2.txt", b4 = "utf-8") as file:
        b5 = []
        for line in file:
            b6 = line.strip().split(",")
            if b6[3] == "LOS OLIVOS":
                b7 = float(b6[5])
                b8 = float(b6[6])
                b5.append((b7, b8))
    fonk2(b5, 0, len(b5) - 1)
    for coord in b5:
        print(coord)
    with open("testSET4.txt", "w") as output_file:
        for coord in b5:
            output_file.write(f"{coord[0]},{coord[1]}\n")
    print(f"Total coordinates: {len(b5)}")
if b9 = = "__main__":
    print("Sorting coordinates for LOS OLIVOS...")
    fonk3()