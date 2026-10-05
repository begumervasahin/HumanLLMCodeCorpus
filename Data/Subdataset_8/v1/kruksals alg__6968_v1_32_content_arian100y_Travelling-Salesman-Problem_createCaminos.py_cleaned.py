from operator import itemgetter
import statistics
import time as ti
def dbToList(filename):
    arr = []
    with open(filename, "r") as file:
        for line in file:
            x, y = map(float, line.split(","))
            arr.append((x, y))
    return arr
def CrearCaminosGraf(quadrant, filename2):
    with open(filename2, "w") as file2:
        n = len(quadrant)
        for u in quadrant:
            s2 = f"{u[0]},{u[1]} "
            cercanos = []
            for j in range(1, int(len(quadrant) / 2) + 1):
                v1 = (c + j) % len(quadrant)
                v2 = (c - j) % len(quadrant)
                xv1, yv1 = quadrant[v1][0], quadrant[v1][1]
                d1 = ((xv1 - u[0]) ** 2 + (yv1 - u[1]) ** 2) ** 0.5
                xv2, yv2 = quadrant[v2][0], quadrant[v2][1]
                d2 = ((xv2 - u[0]) ** 2 + (yv2 - u[1]) ** 2) ** 0.5
                if [v1, xv1, yv1, d1] not in cercanos:
                    cercanos.append([v1, xv1, yv1, d1])
                if [v2, xv2, yv2, d2] not in cercanos:
                    cercanos.append([v2, xv2, yv2, d2])
            cercanos.sort(key=itemgetter(3))
            for j in cercanos[:10]:
                s2 += f"{j[1]},{j[2]} "
            file2.write(s2[:-1] + "\n")
            p = n
            c += 1
def separateLists(auxArr):
    yArr = [i[1] for i in auxArr]
    aux = auxArr[:]
    aux.sort(key=itemgetter(0))
    xArr = [i[0] for i in aux]
    return xArr, yArr
def CreateQuadrants(arr):
    xArr, yArr = separateLists(arr)
    yMedian = statistics.median(yArr)
    xMedian = statistics.median(xArr)
    q1, q2, q3, q4 = [], [], [], []
    for i in arr:
        if i[0] <= xMedian and i[1] >= yMedian:
            q1.append(i)
        if i[0] > xMedian and i[1] >= yMedian:
            q2.append(i)
        if i[0] <= xMedian and i[1] < yMedian:
            q3.append(i)
        if i[0] > xMedian and i[1] < yMedian:
            q4.append(i)
    return q1, q2, q3, q4, xMedian, yMedian
if __name__ == "__main__":
    timer = ti.clock()
    filename = "your_input_file.txt"
    filename2 = "your_output_file.txt"
    arr = dbToList(filename)
    q1, q2, q3, q4, xMedian, yMedian = CreateQuadrants(arr)
    print("Quadrant 1:", q1)
    print("Quadrant 2:", q2)
    print("Quadrant 3:", q3)
    print("Quadrant 4:", q4)
    CrearCaminosGraf(q1, filename2)
    elapsed_time = ti.clock() - timer
    print(f"Execution time: {elapsed_time} seconds")