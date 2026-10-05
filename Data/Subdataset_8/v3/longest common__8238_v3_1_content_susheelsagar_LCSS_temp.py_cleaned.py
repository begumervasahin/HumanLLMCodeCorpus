
with open("distance_matrix_1698.csv", "r+") as file:
    line_counter = 0
    fifth_line_elements = []
    for line in file:
        line_counter += 1
        if line_counter == 5:
            fifth_line_elements = line.split(",")
            break
    total_elements = len(fifth_line_elements) + 1698
    print("Total elements in the fifth line plus 1698:", total_elements)
    third_element = fifth_line_elements[2]
    print("Third element of the fifth line:", third_element)