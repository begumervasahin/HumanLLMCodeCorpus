__author__ = 's'
with open("distance_matrix_1698.csv", "r+") as f:
    a = []
    k = 0
    for line in f:
        if k == 5:
            break
        k += 1
        a = line.split(",")
    print(len(a) + 1698)
    print(a[2])