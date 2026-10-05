from operator import itemgetter
import statistics
import time as ti
def fonk1(b22):
    b1 = []
    with open(b22, "r") as file:
        for line in file:
            x, b2 = map(float, line.split(","))
            b1.append((x, b2))
    return b1
def fonk2(quadrant, b23):
    with open(b23, "w") as file2:
        b3 = len(quadrant)
        for u in quadrant:
            b4 = f"{u[0]},{u[1]} "
            b5 = []
            for j in range(1, int(len(quadrant) / 2) + 1):
                b6 = (c + j) % len(quadrant)
                b7 = (c - j) % len(quadrant)
                xv1, b8 = quadrant[b6][0], quadrant[b6][1]
                b9 = ((xv1 - u[0]) ** 2 + (b8 - u[1]) ** 2) ** 0.5
                xv2, b10 = quadrant[b7][0], quadrant[b7][1]
                b11 = ((xv2 - u[0]) ** 2 + (b10 - u[1]) ** 2) ** 0.5
                if [b6, xv1, b8, b9] not in b5:
                    b5.append([b6, xv1, b8, b9])
                if [b7, xv2, b10, b11] not in b5:
                    b5.append([b7, xv2, b10, b11])
            b5.sort(b12 = itemgetter(3))
            for j in b5[:10]:
                b4 += f"{j[1]},{j[2]} "
            file2.write(b4[:-1] + "\b3")
            b13 = b3
            c += 1
def fonk3(auxArr):
    b14 = [i[1] for i in auxArr]
    b15 = auxArr[:]
    b15.sort(b12 = itemgetter(0))
    b16 = [i[0] for i in b15]
    return b16, b14
def fonk4(b1):
    b16, b14 = fonk3(b1)
    b17 = statistics.median(b14)
    b18 = statistics.median(b16)
    q1, q2, q3, b19 = [], [], [], []
    for i in b1:
        if i[0] <= b18 and i[1] >= b17:
            q1.append(i)
        if i[0] > b18 and i[1] >= b17:
            q2.append(i)
        if i[0] <= b18 and i[1] < b17:
            q3.append(i)
        if i[0] > b18 and i[1] < b17:
            b19.append(i)
    return q1, q2, q3, b19, b18, b17
if b20 = = "__main__":
    b21 = ti.clock()
    b22 = "your_input_file.txt"
    b23 = "your_output_file.txt"
    b1 = fonk1(b22)
    q1, q2, q3, b19, b18, b17 = fonk4(b1)
    print("Quadrant 1:", q1)
    print("Quadrant 2:", q2)
    print("Quadrant 3:", q3)
    print("Quadrant 4:", b19)
    fonk2(q1, b23)
    b24 = ti.clock() - b21
    print(f"Execution time: {b24} seconds")