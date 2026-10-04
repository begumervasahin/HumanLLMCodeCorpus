import networkx as nx
import csv
import math
def fonk1(Node1, Node2):
    x1, b1 = Node1
    x2, b2 = Node2
    b3 = math.sqrt((x2 - x1)**2 + (b2 - b1)**2)
    return b3
def fonk2():
    with open("bnk_node.csv", 'w', b4 = '') as node_file, \
         open("q_result.csv", 'r') as edge_input, \
         open("bnk_edge.csv", 'w', b4 = '') as edge_file:
        b5 = csv.writer(node_file)
        b6 = csv.writer(edge_file)
        b7 = csv.reader(edge_input)
        b8 = []
        b9 = {}
        a1 = 1
        for line in b7:
            print(line)
            b10 = str(line[0]).split()
            b11 = (float(b10[1]), float(b10[2]))
            b12 = (float(b10[4]), float(b10[5]))
            if b11 not in b8:
                b8.append(b11)
                b5.writerow([a1, b11[0], b11[1]])
                b9[b11] = a1
                a1 += 1
            if b12 not in b8:
                b8.append(b12)
                b5.writerow([a1, b12[0], b12[1]])
                b9[b12] = a1
                a1 += 1
            b3 = fonk1(b11, b12)
            b13 = int(b10[8])
            b6.writerow([b9[b11], b9[b12], b13, b3])
            b6.writerow([b9[b12], b9[b11], b13, b3])
if b14 = = "__main__":
    fonk2()