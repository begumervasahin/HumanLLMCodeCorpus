
__author__ = 's'
with open("distance_matrix_1698.csv", "r+") as file:
    lines = []
    line_count = 0
    for line in file:
        lines.append(line.strip())
        line_count += 1
        if line_count == 5:
            break
    if line_count == 5:
        values = lines[-1].split(",")
print(len(values) + 1698)
print(values[2])