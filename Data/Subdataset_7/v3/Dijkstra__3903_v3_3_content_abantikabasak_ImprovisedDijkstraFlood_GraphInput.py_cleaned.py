import csv
import math
def fonk1(b7, b8):
    x1, b1 = b7
    x2, b2 = b8
    b3 = math.sqrt((x2 - x1) ** 2 + (b2 - b1) ** 2)
    return b3
def fonk2(b10, b9, b11):
    b4 = []
    b5 = {}
    a1 = 1
    for line in b10:
        b6 = line[0].split()
        b7 = (float(b6[1]), float(b6[2]))
        b8 = (float(b6[4]), float(b6[5]))
        for node in [b7, b8]:
            if node not in b4:
                b4.append(node)
                b9.writerow([a1, node[0], node[1]])
                b5[node] = a1
                a1 += 1
        b11.writerow([b5[b7], b5[b8], int(b6[8]), fonk1(b7, b8)])
        b11.writerow([b5[b8], b5[b7], int(b6[8]), fonk1(b7, b8)])
def fonk3():
    with open("bnk_node.csv", 'w') as node_file, \
         open("q_result.csv", 'r') as edge_input, \
         open("bnk_edge.csv", 'w') as edge_file:
        b9 = csv.writer(node_file)
        b10 = csv.reader(edge_input)
        b11 = csv.writer(edge_file)
        fonk2(b10, b9, b11)
if b12 = = "__main__":
    fonk3()