def partition(arr, low, high):
    i = low - 1
    pivot = arr[high][0]
    for j in range(low, high):
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
def filter_and_sort_coordinates(filename, location):
    coordinates = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(",")
            if data[3] == location:
                latitude = float(data[5])
                longitude = float(data[6])
                coordinates.append((latitude, longitude))
    quicksort(coordinates, 0, len(coordinates) - 1)
    return coordinates
def write_coordinates_to_file(coordinates, output_filename):
    with open(output_filename, "w") as output_file:
        for latitude, longitude in coordinates:
            output_file.write(f"{latitude},{longitude}\n")
def main():
    input_filename = "db2.txt"
    output_filename = "testSET4.txt"
    location = "LOS OLIVOS"
    sorted_coordinates = filter_and_sort_coordinates(input_filename, location)
    for coord in sorted_coordinates:
        print(coord)
    write_coordinates_to_file(sorted_coordinates, output_filename)
    print(f"Total coordinates: {len(sorted_coordinates)}")
if __name__ == "__main__":
    print("Sorting coordinates for LOS OLIVOS...")
    main()