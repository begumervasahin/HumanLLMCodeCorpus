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
with open("db2.txt", encoding="utf-8") as text:
    lines = []
    for line in text:
        test = line.split(",")
        if test[3].strip() == "LOS OLIVOS":
            lines.append((float(test[5]), float(test[6])))
quickSort(lines, 0, len(lines) - 1)
for line in lines:
    print(line)
with open("testSET4.txt", "w") as write:
    for line in lines:
        write.write(f"{line[0]},{line[1]}\n")
print(len(lines))