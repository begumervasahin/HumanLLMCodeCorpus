
b1 = 's'
with open("distance_matrix_1698.csv", "r+") as f:
    b2 = []
    for b3, line in enumerate(f):
        if b3 = = 5:
            break
        b2.append(line.strip())
    if b2:
        b4 = b2[-1]
        b5 = b4.split(",")
        print(len(b5) + 1698)
        if len(b5) > 2:
            print(b5[2])
        else:
            print("The third element does not exist.")
    else:
        print("The file contains less than 5 b2.")