
b1 = 's'
with open("distance_matrix_1698.csv", "r+") as file:
    b2 = []
    a1 = 0
    for line in file:
        b2.append(line.strip())
        a1 += 1
        if a1 = = 5:
            break
    if a1 = = 5:
        b3 = b2[-1].split(",")
print(len(b3) + 1698)
print(b3[2])