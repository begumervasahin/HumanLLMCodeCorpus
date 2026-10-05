
file = open("distance_matrix_1698.csv", "r+")
data = []
line_count = 0
for line in iter(file):
    if line_count == 5:
        break
    line_count += 1
    row_data = line.split(",")
    data = row_data
total_length = len(data) + 1698
print(total_length)
print(data[2])
file.close()