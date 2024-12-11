
with open("distance_matrix_1698.csv", "r+") as file:
    a1 = 0
    b1 = []
    for line in file:
        a1 += 1
        if a1 = = 5:
            b1 = line.split(",")
            break
    b2 = len(b1) + 1698
    print("Total elements in the fifth line plus 1698:", b2)
    b3 = b1[2]
    print("Third element of the fifth line:", b3)