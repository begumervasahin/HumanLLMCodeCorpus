
b1 = 's'
with open("distance_matrix_1698.csv", "r+") as file:
    b2 = [next(file).strip() for _ in range(5)]
b3 = b2[-1].split(",")
b4 = len(b3) + 1698
print(b4)
b5 = b3[2]
print(b5)