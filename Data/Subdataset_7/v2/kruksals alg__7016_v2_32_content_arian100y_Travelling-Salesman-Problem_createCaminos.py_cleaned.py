from operator import itemgetter
import statistics
import time as ti
def fonk1(filename):
    b1 = []
    with open(filename, "r") as file:
        for line in file:
            x, b2 = map(float, line.split(","))
            b1.append((x, b2))
    return b1
def fonk2(quadrant, b22):
    with open(b22, "w") as file:
        for u in quadrant:
            b3 = []
            for j in range(1, int(len(quadrant) / 2) + 1):
                b4 = (c + j) % len(quadrant)
                b5 = (c - j) % len(quadrant)
                xv1, b6 = quadrant[b4][0], quadrant[b4][1]
                b7 = ((xv1 - u[0]) ** 2 + (b6 - u[1]) ** 2) ** 0.5
                xv2, b8 = quadrant[b5][0], quadrant[b5][1]
                b9 = ((xv2 - u[0]) ** 2 + (b8 - u[1]) ** 2) ** 0.5
                if [b4, xv1, b6, b7] not in b3:
                    b3.append([b4, xv1, b6, b7])
                if [b5, xv2, b8, b9] not in b3:
                    b3.append([b5, xv2, b8, b9])
            b3.sort(b10 = itemgetter(3))
            b11 = f"{u[0]},{u[1]} " + " ".join([f"{j[1]},{j[2]}" for j in b3[:10]])
            file.write(b11 + "\n")
            b12 = len(quadrant)
            c += 1
def fonk3(b1):
    b13 = [i[1] for i in b1]
    b14 = b1[:]
    b14.sort(b10 = itemgetter(0))
    b15 = [i[0] for i in b14]
    return b15, b13
def fonk4(b1):
    b15, b13 = fonk3(b1)
    b16 = statistics.median(b13)
    b17 = statistics.median(b15)
    q1, q2, q3, b18 = [], [], [], []
    for i in b1:
        if i[0] <= b17 and i[1] >= b16:
            q1.append(i)
        if i[0] > b17 and i[1] >= b16:
            q2.append(i)
        if i[0] <= b17 and i[1] < b16:
            q3.append(i)
        if i[0] > b17 and i[1] < b16:
            b18.append(i)
    return q1, q2, q3, b18, b17, b16
if b19 = = "__main__":
    b20 = ti.clock()
    b21 = "your_input_file.txt"
    b22 = "your_output_file.txt"
    b1 = fonk1(b21)
    q1, q2, q3, b18, b17, b16 = fonk4(b1)
    print("Quadrant 1:", q1)
    print("Quadrant 2:", q2)
    print("Quadrant 3:", q3)
    print("Quadrant 4:", b18)
    fonk2(q1, b22)
    b23 = ti.clock() - b20
    print(f"Execution time: {b23} seconds")