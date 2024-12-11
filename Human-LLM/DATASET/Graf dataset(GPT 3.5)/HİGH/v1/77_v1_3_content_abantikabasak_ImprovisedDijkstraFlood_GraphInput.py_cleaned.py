import networkx as nx
import csv
import math
def fonk1(b13, b14):
    x1, b1 = b13
    x2, b2 = b14
    b3 = float(math.pow(math.pow((x2 - x1), 2) + math.pow((b2 - b1), 2), 0.5))
    return b3
b4 = open("bnk_node.csv", 'w')
b5 = csv.writer(b4)
b6 = []
b7 = {}
b8 = open("q_result.csv", 'r')
b9 = csv.reader(b8)
b10 = open("bnk_edge.csv", 'w')
b11 = csv.writer(b10)
a1 = 1
for l in b9:
    b12 = str(l[0]).split()
    b13 = (float(b12[1]), float(b12[2]))
    b14 = (float(b12[4]), float(b12[5]))
    if b13 not in b6:
        b6.append(b13)
        b5.writerow([a1, b13[0], b13[1]])
        b7[b13] = a1
        a1 += 1
    if b14 not in b6:
        b6.append(b14)
        b5.writerow([a1, b14[0], b14[1]])
        b7[b14] = a1
        a1 += 1
    b11.writerow([b7[b13], b7[b14], int(b12[8]), fonk1(b13, b14)])
    b11.writerow([b7[b14], b7[b13], int(b12[8]), fonk1(b13, b14)])
b4.close()
b10.close()
b8.close()