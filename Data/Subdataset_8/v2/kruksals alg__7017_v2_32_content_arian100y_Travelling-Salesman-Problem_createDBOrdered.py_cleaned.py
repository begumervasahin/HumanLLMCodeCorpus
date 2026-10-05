def partition(arr, low, high):
    i = low - 1
    pivot = arr[high][1]
    for j in range(low, high):
        if arr[j][1] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
if __name__ == "__main__":
    with open("db2.txt", encoding="utf-8") as file:
        lines = [(float(line.split(",")[5]), float(line.split(",")[6])) for line in file if line.split(",")[3] == "LOS OLIVOS"]
    quick_sort(lines, 0, len(lines) - 1)
    with open("testSET4.txt", "w") as write_file:
        for line in lines:
            write_file.write("{},{}\n".format(line[0], line[1]))
    print("Sorting and writing complete.")
    print("Total lines written:", len(lines))