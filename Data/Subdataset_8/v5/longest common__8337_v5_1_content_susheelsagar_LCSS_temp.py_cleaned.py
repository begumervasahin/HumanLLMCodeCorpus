
with open("distance_matrix_1698.csv", "r+") as file:
    data = []
    line_count = 0
    for line in file:
        if line_count == 5:
            break
        line_count += 1
        row_data = line.split(",")
        data = row_data
total_length = len(data) + 1698
print("Total length:", total_length)
print("Value at index 2:", data[2])