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
def filter_data(filename, location):
    filtered_data = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            columns = line.split(",")
            if columns[3].strip() == location:
                filtered_data.append((float(columns[5]), float(columns[6])))
    return filtered_data
def write_data_to_file(data, output_filename):
    with open(output_filename, "w") as output_file:
        for item in data:
            output_file.write(f"{item[0]},{item[1]}\n")
def main():
    input_filename = "db2.txt"
    output_filename = "testSET4.txt"
    location = "LOS OLIVOS"
    filtered_data = filter_data(input_filename, location)
    quick_sort(filtered_data, 0, len(filtered_data) - 1)
    for item in filtered_data:
        print(item)
    write_data_to_file(filtered_data, output_filename)
    print(f"Number of filtered and sorted lines: {len(filtered_data)}")
if __name__ == "__main__":
    main()