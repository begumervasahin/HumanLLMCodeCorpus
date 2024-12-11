import csv
import math
def fonk1(node1, node2):
    x1, b1 = node1
    x2, b2 = node2
    b3 = math.sqrt((x2 - x1) ** 2 + (b2 - b1) ** 2)
    return b3
b4 = open("bnk_node.csv", 'w')
b5 = csv.writer(b4)
b6 = open("q_result.csv", 'r')
b7 = csv.reader(b6)
b8 = open("bnk_edge.csv", 'w')
b9 = csv.writer(b8)
a1 = 1
b10 = []
b11 = {}
for line in b7:
    b12 = line[0].split()
    b13 = (float(b12[1]), float(b12[2]))
    b14 = (float(b12[4]), float(b12[5]))
    for node in [b13, b14]:
        if node not in b10:
            b10.append(node)
            b5.writerow([a1, node[0], node[1]])
            b11[node] = a1
            a1 += 1
    b9.writerow([b11[b13], b11[b14], int(b12[8]), fonk1(b13, b14)])
    b9.writerow([b11[b14], b11[b13], int(b12[8]), fonk1(b13, b14)])
b4.close()
b8.close()
b6.close()