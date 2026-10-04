def partition(arr, low, high):
    i = low - 1
    pivot = arr[high][1]
    for j in range(low, high):
        if arr[j][1] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
def main():
    with open("db2.txt", encoding="utf-8") as file:
        lines = []
        for line in file:
            data = line.strip().split(",")
            if data[3] == "LOS OLIVOS":
                latitude = float(data[5])
                longitude = float(data[6])
                lines.append((latitude, longitude))
    quicksort(lines, 0, len(lines) - 1)
    for coord in lines:
        print(coord)
    with open("testSET4.txt", "w") as output_file:
        for coord in lines:
            output_file.write(f"{coord[0]},{coord[1]}\n")
    print(f"Total coordinates: {len(lines)}")
if __name__ == "__main__":
    print("Sorting coordinates for LOS OLIVOS...")
    main()