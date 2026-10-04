import networkx as nx
import csv
import math
def fonk1(b10, b11):
    x1, b1 = b10
    x2, b2 = b11
    return math.sqrt((x2 - x1)**2 + (b2 - b1)**2)
def fonk2(b14, b15, b16):
    with open(b15, 'w', b3 = '') as node_file, \
         open(b14, 'r') as edge_input, \
         open(b16, 'w', b3 = '') as edge_file:
        b4 = csv.writer(node_file)
        b5 = csv.writer(edge_file)
        b6 = csv.reader(edge_input)
        b7 = []
        b8 = {}
        a1 = 1
        for line in b6:
            print(line)
            b9 = str(line[0]).split()
            b10 = (float(b9[1]), float(b9[2]))
            b11 = (float(b9[4]), float(b9[5]))
            if b10 not in b7:
                b7.append(b10)
                b4.writerow([a1, b10[0], b10[1]])
                b8[b10] = a1
                a1 += 1
            if b11 not in b7:
                b7.append(b11)
                b4.writerow([a1, b11[0], b11[1]])
                b8[b11] = a1
                a1 += 1
            b12 = fonk1(b10, b11)
            b13 = int(b9[8])
            b5.writerow([b8[b10], b8[b11], b13, b12])
            b5.writerow([b8[b11], b8[b10], b13, b12])
def fonk3():
    b14 = "q_result.csv"
    b15 = "bnk_node.csv"
    b16 = "bnk_edge.csv"
    fonk2(b14, b15, b16)
if b17 = = "__main__":
    fonk3()