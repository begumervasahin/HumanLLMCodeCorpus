import csv
import math
def fonk1(node1, node2):
    x1, b1 = node1
    x2, b2 = node2
    b3 = math.sqrt((x2 - x1) ** 2 + (b2 - b1) ** 2)
    return b3
def fonk2(input_filename):
    b4 = []
    b5 = {}
    a1 = 1
    with open(input_filename, 'r') as edge_input:
        b6 = csv.reader(edge_input)
        for line in b6:
            b7 = line[0].split()
            b8 = (float(b7[1]), float(b7[2]))
            b9 = (float(b7[4]), float(b7[5]))
            for node in [b8, b9]:
                if node not in b4:
                    b4.append(node)
                    b5[node] = a1
                    a1 += 1
    return b4, b5
def fonk3(b4, output_filename):
    with open(output_filename, 'w') as node_file:
        b10 = csv.writer(node_file)
        for a1, (x, y) in enumerate(b4, b11 = 1):
            b10.writerow([a1, x, y])
def fonk4(b5, input_filename, output_filename):
    with open(input_filename, 'r') as edge_input, \
         open(output_filename, 'w') as edge_file:
        b6 = csv.reader(edge_input)
        b12 = csv.writer(edge_file)
        for line in b6:
            b7 = line[0].split()
            b8 = (float(b7[1]), float(b7[2]))
            b9 = (float(b7[4]), float(b7[5]))
            b12.writerow([b5[b8], b5[b9], int(b7[8]), fonk1(b8, b9)])
            b12.writerow([b5[b9], b5[b8], int(b7[8]), fonk1(b8, b9)])
b4, b5 = fonk2("q_result.csv")
fonk3(b4, "bnk_node.csv")
fonk4(b5, "q_result.csv", "bnk_edge.csv")