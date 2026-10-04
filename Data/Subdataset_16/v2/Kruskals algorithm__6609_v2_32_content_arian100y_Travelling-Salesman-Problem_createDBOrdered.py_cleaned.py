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
b4 = []
with open("db2.txt", b5 = "utf-8") as file:
    for line in file:
        b6 = line.split(",")
        if b6[3].strip() == "LOS OLIVOS":
            b4.append((float(b6[5]), float(b6[6])))
fonk2(b4, 0, len(b4) - 1)
for item in b4:
    print(item)
with open("testSET4.txt", "w") as output_file:
    for item in b4:
        output_file.write(f"{item[0]},{item[1]}\n")
print(f"Number of filtered and sorted lines: {len(b4)}")