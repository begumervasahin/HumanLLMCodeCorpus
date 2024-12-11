import csv
import math
def fonk1(b13, b14):
    x1, b1 = b13
    x2, b2 = b14
    b3 = math.sqrt((x2 - x1) ** 2 + (b2 - b1) ** 2)
    return b3
b4 = open("bnk_node.csv", 'w')
b5 = csv.writer(b4)
b6 = open("q_result.csv", 'r')
b7 = csv.reader(b6)
b8 = open("bnk_edge.csv", 'w')
b9 = csv.writer(b8)
b10 = []
b11 = {}
a1 = 1
for line in b7:
    b12 = line[0].split()
    b13 = (float(b12[1]), float(b12[2]))
    b14 = (float(b12[4]), float(b12[5]))
    if b13 not in b10:
        b10.append(b13)
        b5.writerow([a1, b13[0], b13[1]])
        b11[b13] = a1
        a1 += 1
    if b14 not in b10:
        b10.append(b14)
        b5.writerow([a1, b14[0], b14[1]])
        b11[b14] = a1
        a1 += 1
    b9.writerow([b11[b13], b11[b14], int(b12[8]), fonk1(b13, b14)])
    b9.writerow([b11[b14], b11[b13], int(b12[8]), fonk1(b13, b14)])
b4.close()
b8.close()
b6.close()