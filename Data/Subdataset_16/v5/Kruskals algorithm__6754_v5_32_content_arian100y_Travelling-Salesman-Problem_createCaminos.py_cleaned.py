import statistics
from operator import itemgetter
def fonk1(filename):
    b1 = []
    with open(filename, "r") as file:
        for line in file:
            x, b2 = map(float, line.strip().split(","))
            b1.append((x, b2))
    return b1
def fonk2(quadrant, output_filename, b3 = 10):
    with open(output_filename, "w") as file:
        b4 = len(quadrant)
        for index, (x, b2) in enumerate(quadrant):
            b5 = []
            for j in range(1, (b4
                b6 = [
                    (index + j) % b4,
                    (index - j) % b4
                ]
                for neighbor in b6:
                    nx, b7 = quadrant[neighbor]
                    b8 = ((nx - x) ** 2 + (b7 - b2) ** 2) ** 0.5
                    b5.append((nx, b7, b8))
            b9 = sorted(b5, key=itemgetter(2))[:b3]
            b10 = f"{x},{b2} " + " ".join(f"{cx},{cy}" for cx, cy, _ in b9)
            file.write(b10 + "\n")
def fonk3(b1):
    b11 = [x for x, _ in b1]
    b12 = [b2 for _, b2 in b1]
    return b11, b12
def fonk4(b1):
    b11, b12 = fonk3(b1)
    b13 = statistics.median(b11)
    b14 = statistics.median(b12)
    q1, q2, q3, b15 = [], [], [], []
    for x, b2 in b1:
        if x <= b13 and b2 >= b14:
            q1.append((x, b2))
        elif x > b13 and b2 >= b14:
            q2.append((x, b2))
        elif x <= b13 and b2 < b14:
            q3.append((x, b2))
        else:
            b15.append((x, b2))
    return q1, q2, q3, b15, b13, b14
