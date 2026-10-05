
with open("db2.txt", b1 = "utf-8") as text_file:
    b2 = []
    for line in text_file:
        b3 = line.split(",")
        if b3[3] == "LOS OLIVOS":
            b2.append((float(b3[5]), float(b3[6])))
def fonk1(arr, low, high):
    b4 = low - 1
    b5 = arr[high][1]
    for j in range(low, high):
        if arr[j][1] <= b5:
            b4 += 1
            arr[b4], arr[j] = arr[j], arr[b4]
    arr[b4 + 1], arr[high] = arr[high], arr[b4 + 1]
    return b4 + 1
def fonk2(arr, low, high):
    if low < high:
        b6 = fonk1(arr, low, high)
        fonk2(arr, low, b6 - 1)
        fonk2(arr, b6 + 1, high)
fonk2(b2, 0, len(b2) - 1)
for line in b2:
    print(line)
with open("testSET4.txt", "w") as write_file:
    for line in b2:
        write_file.write(f"{line[0]},{line[1]}\n")
print("Number of b2:", len(b2))