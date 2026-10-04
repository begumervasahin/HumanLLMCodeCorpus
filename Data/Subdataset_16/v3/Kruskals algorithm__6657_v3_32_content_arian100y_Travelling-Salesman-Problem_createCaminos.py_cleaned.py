import statistics
def fonk1(b12):
    with open(b12, "r") as file:
        return [(float(x), float(y)) for line in file for x, y in [line.strip().split(",")]]
def fonk2(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
def fonk3(point, quadrant, b1 = 10):
    b2 = [(neighbor, fonk2(point, neighbor)) for neighbor in quadrant if neighbor != point]
    b2.sort(b3 = lambda x: x[1])
    return [x[0] for x in b2[:b1]]
def fonk4(quadrant, b12):
    with open(b12, "w") as file:
        for point in quadrant:
            b4 = fonk3(point, quadrant)
            b5 = " ".join(f"{x},{y}" for x, y in b4)
            file.write(f"{point[0]},{point[1]} {b5}\n")
def fonk5(b13):
    b6 = sorted(b13, b3=lambda p: p[0])
    b7 = [p[0] for p in b6]
    b8 = [p[1] for p in b13]
    return b7, b8
def fonk6(b13):
    b7, b8 = fonk5(b13)
    b9 = statistics.median(b7)
    b10 = statistics.median(b8)
    q1, q2, q3, b11 = [], [], [], []
    for x, y in b13:
        if x <= b9 and y >= b10:
            q1.append((x, y))
        elif x > b9 and y >= b10:
            q2.append((x, y))
        elif x <= b9 and y < b10:
            q3.append((x, y))
        else:
            b11.append((x, y))
    return q1, q2, q3, b11, b9, b10
b12 = "data.csv"
b13 = fonk1(b12)
b14 = fonk6(b13)[:4]
for idx, quadrant in enumerate(b14, 1):
    b15 = f"quadrant_{idx}_paths.txt"
    fonk4(quadrant, b15)