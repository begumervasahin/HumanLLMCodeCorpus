
text_file = open("db2.txt", encoding="utf-8")
lines = []
for line in text_file:
    fields = line.split(",")
    if fields[3] == "LOS OLIVOS":
        lines.append((float(fields[5]), float(fields[6])))
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high][1]
    for j in range(low, high):
        if arr[j][1] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
quickSort(lines, 0, len(lines) - 1)
for line in lines:
    print(line)
write_file = open("testSET4.txt", "w")
for line in lines:
    write_file.write(str(line[0]) + "," + str(line[1]) + "\n")
write_file.close()
print("Number of lines:", len(lines))