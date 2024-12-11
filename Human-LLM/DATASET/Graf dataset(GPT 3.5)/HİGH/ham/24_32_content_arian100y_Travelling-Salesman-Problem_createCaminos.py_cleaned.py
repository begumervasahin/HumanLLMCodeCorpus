from operator import itemgetter
import statistics
import time as ti
b1 = ti.clock()
def fonk1(filename):
    b2 = []
    b3 = open(filename,"r")
    for i in b3:
        b4 = i.split(",")
        b2.append((float(b4[0]),float(b4[1])))
    return b2
def fonk2(quadrant, filename2):
    b5 = open(filename2, "w")
    b6 = len(quadrant)
    a1 = 0
    for u in quadrant:
        b7 = ""
        b7 += str(u[0]) + "," + str(u[1]) + " "
        b8 = []
        for j in range(1, int(len(quadrant)/2)+1):
            b9 = (a1 + j) % len(quadrant)
            b10 = (a1 - j) % len(quadrant)
            xv1, b11 = quadrant[b9][0], quadrant[b9][1]
            b12 = ((xv1 - u[0]) ** 2 + (b11 - u[1]) ** 2) ** 0.5
            xv2, b13 = quadrant[b10][0], quadrant[b10][1]
            b14 = ((xv2 - u[0]) ** 2 + (b13 - u[1]) ** 2) ** 0.5
            if [b9, xv1, b11, b12] not in b8 :
                b8.append([b9, xv1, b11, b12])
            if [b10, xv2, b13, b14] not in b8:
                b8.append([b10, xv2, b13, b14])
        b8.sort(b15 = itemgetter(3))
        for j in b8[:10]:
            b7 += str(j[1]) + "," + str(j[2]) + " "
        b5.write(b7[:-1] + "\b6")
        b16 = b6
        a1 += 1
def fonk3(auxArr):
    b17 = []
    for i in auxArr:
        b17 += [i[1]]
    b18 = []
    b19 = auxArr[:]
    b19.sort(b15 = itemgetter(0))
    for i in b19:
        b18 += [i[0]]
    return b18,b17
def fonk4(b2):
    b18,b17 = fonk3(b2)
    b20 = statistics.median(b17)
    b21 = statistics.median(b18)
    print(b21,b20)
    q1,q2,q3,b22 = [],[],[],[]
    for i in b2:
        if i[0]<= b21 and i[1] >= b20:
            q1 += [i]
        if i[0]> b21 and i[1] >= b20:
            q2 += [i]
        if i[0]<= b21 and i[1] < b20:
            q3 += [i]
        if i[0]> b21 and i[1] < b20:
            b22 += [i]
    return q1,q2,q3,b22,b21,b20