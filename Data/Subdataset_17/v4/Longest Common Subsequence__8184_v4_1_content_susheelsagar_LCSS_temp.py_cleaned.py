
__author__ = 's'
with open("distance_matrix_1698.csv", "r+") as f:
    lines = []
    for i, line in enumerate(f):
        if i == 5:
            break
        lines.append(line.strip())
    if lines:
        last_line = lines[-1]
        elements = last_line.split(",")
        print(len(elements) + 1698)
        if len(elements) > 2:
            print(elements[2])
        else:
            print("The third element does not exist.")
    else:
        print("The file contains less than 5 lines.")