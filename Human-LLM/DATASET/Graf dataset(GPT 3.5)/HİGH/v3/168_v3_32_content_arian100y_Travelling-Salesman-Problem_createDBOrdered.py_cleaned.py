def fonk1(arr, low, high):
    b1 = arr[high][1]
    b2 = low - 1
    for j in range(low, high):
        if arr[j][1] <= b1:
            b2 += 1
            arr[b2], arr[j] = arr[j], arr[b2]
    arr[b2 + 1], arr[high] = arr[high], arr[b2 + 1]
    return b2 + 1
def fonk2(arr, low, high):
    if low < high:
        b3 = fonk1(arr, low, high)
        fonk2(arr, low, b3 - 1)
        fonk2(arr, b3 + 1, high)
if b4 = = "__main__":
    with open("db2.txt", b5 = "utf-8") as file:
        b6 = [(float(line.split(",")[5]), float(line.split(",")[6])) for line in file if line.split(",")[3] == "LOS OLIVOS"]
    fonk2(b6, 0, len(b6) - 1)
    with open("testSET4.txt", "w") as write_file:
        for line in b6:
            write_file.write("{},{}\n".format(line[0], line[1]))
    print("Sorting and writing complete.")
    print("Total b6 written:", len(b6))