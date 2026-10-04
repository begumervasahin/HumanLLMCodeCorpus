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
with open("db2.txt", b4 = "utf-8") as text:
    b5 = []
    for line in text:
        b6 = line.split(",")
        if b6[3].strip() == "LOS OLIVOS":
            b5.append((float(b6[5]), float(b6[6])))
fonk2(b5, 0, len(b5) - 1)
for line in b5:
    print(line)
with open("testSET4.txt", "w") as write:
    for line in b5:
        write.write(f"{line[0]},{line[1]}\n")
print(len(b5))