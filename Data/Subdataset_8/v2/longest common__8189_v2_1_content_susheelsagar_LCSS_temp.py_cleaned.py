
with open("distance_matrix_1698.csv", "r+") as file:
    data = []
    line_counter = 0
    for line in file:
        if line_counter == 5:
            break
        line_counter += 1
        data = line.split(",")
    print("Total elements in the fifth line plus 1698:", len(data) + 1698)
    print("Third element of the fifth line:", data[2])