from typing import List
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
'''
For the program to work, install the following software:
sudo apt-get install python3-tk
sudo pip3 install networkx
sudo pip3 install matplotlib
Or with O.S. specific information and run as a Python3 file.
example: python3 prim.py city-pairs.txt
'''
def display_graph(matrix):
    G = nx.Graph()
    for rows in matrix:
        G.add_edge(nod_list[rows[0]], nod_list[rows[1]], weight=int(rows[2]))
    edge = [(u, v) for (u, v, d) in G.edges(data=True)]
    pos = nx.spring_layout(G, k=40)
    weight = dict(map(lambda x: ((x[0], x[1]), str(x[2]['weight'])), G.edges(data=True)))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weight, font_size=7, alpha=0.7)
    node_len = 0
    for i in range(nod_cout):
        if len(nod_list[i]) > node_len:
            node_len = len(nod_list)
    nx.draw_networkx_nodes(G, pos, node_size=node_len * 110, node_shape='h', node_len=100, alpha=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=edge, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')
    plt.axis('off')
    plt.subplots_adjust(left=0.00, bottom=0.00, right=1.00, top=1.00, wspace=0.2, hspace=0.2)
    plt.figure(1, figsize=(1000, 1000))
    plt.show()
def getPrim(g_matrix):
    set_to_return = []
    my_set = g_matrix
    set_length = 0
    my_set[0][0] = 1
    for z in range(nod_cout):
        min_val: int = pow(2, 61)
        pos_x = 0
        pos_y = 0
        for i in range(nod_cout):
            if my_set[i][i] == 1:
                for j in range(nod_cout):
                    if my_set[j][j] == 0:
                        if int(min_val) > int(my_set[i][j]):
                            pos_y = j
                            pos_x = i
                            min_val = my_set[i][j]
        set_length += 1
        my_set[pos_y][pos_y] = 1
        set_to_return.append([pos_x, pos_y, int(my_set[pos_x][pos_y])])
    set_to_return[set_length - 1][2] = 0
    return set_to_return
file_name = "city-pairs.txt"
nod_set = set()
with open(file_name) as f:
    for l in f:
        column = l.strip().split(' ')
        nod_set.add(column[0])
        nod_set.add(column[1])
f.close()
nod_list = list(nod_set)
nod_cout = (len(nod_set))
gMatrix = [[0 for i in range(nod_cout)]
           for j in range(nod_cout)]
with open(file_name) as f:
    for l in f:
        column = l.strip().split(' ')
        gMatrix[int(nod_list.index(column[0]))][int(nod_list.index(column[1]))] = int(column[2])
        gMatrix[int(nod_list.index(column[1]))][int(nod_list.index(column[0]))] = int(column[2])
f.close()
for row in gMatrix:
    for val in row:
        print("{:4}".format(val), end=' ')
    print("\n")
miles = 0
primSet = getPrim(gMatrix)
for row in primSet:
    miles += row[2]
    print("From", nod_list[row[0]], "to", nod_list[row[1]], "=", row[2], "miles")
print("Total number of miles:", miles)
display_graph(primSet)