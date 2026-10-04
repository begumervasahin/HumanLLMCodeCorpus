import matplotlib.pyplot as plt
import networkx as nx
import sys
'''
For the program to work, install the following software:
sudo apt-get install python3-tk
sudo pip3 install networkx
sudo pip3 install matplotlib
Or with O.S. specific information and run as a Python3 file.
example: python3 prim.py city-pairs.txt
'''
def fonk1(b9):
    b1 = nx.Graph()
    for i in range(len(b9)):
        b1.add_edge(
                b16[b9[i][0]],
                b16[b9[i][1]],
                b2 = int(b9[i][2]))
    b3 = [(u,a2) for (u,a2,d) in b1.edges(data=True)]
    b4 = nx.spring_layout(b1, k=20, b4=None, fixed=None, iterations=150, b2='b2', scale=1.0)
    b2 = dict(map(lambda x:((x[0],x[1]), str(x[2]['b2'] ) ), b1.edges(data = True)))
    nx.draw_networkx_edge_labels(b1, b4, b5 = b2)
    a1 = 0
    for i in range(b17):
        if len(b16[i]) > a1:
            a1 = len(b16)
    nx.draw_networkx_nodes(b1, b4, b6 = a1 * 180, node_shape='h', a1=100, alpha=0.5)
    nx.draw_networkx_edges(b1, b4, b7 = b3, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b4, b8 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk2(b18):
    b9 = []
    b10 = []
    b11 = []
    b12 = [0, 1, b18[0][1]]
    a2 = 0
    for V in range(b17-1):
        b10.append(a2)
        for u in range(b17):
            if b18[a2][u] != 0:
                b11.append([a2, u, b18[a2][u]])
        for e in range(1, len(b11)):
            if b11[e][2] < b12[2] and b11[e][1] not in b10:
                b12 = b11[e]
        b9.append(b12)
        a2 = b12[1]
        b11.remove(b12)
        b12 = b11[0]
    return b9
b13 = sys.argv[1]
b14 = set()
with open(b13) as f:
   for i in f:
       b15 = i.strip().split(' ')
       b14.add(b15[0])
       b14.add(b15[1])
f.close()
b16 = list(b14)
b17 = (len(b14))
b18 = [[0 for i in range(b17)] for j in range(b17)]
with open(b13) as f:
   for i in f:
       b15 = i.strip().split(' ')
       b18[int(b16.index(b15[0]))][int(b16.index(b15[1]))]=int(b15[2])
       b18[int(b16.index(b15[1]))][int(b16.index(b15[0]))]=int(b15[2])
f.close()
b9 = fonk2(b18)
a3 = 0
print("The minimum spanning tree is as follows:")
for i in range(len(b9)):
    print(b16[b9[i][0]], " to ", b16[b9[i][1]], " = ", b9[i][2], "miles")
    a3 += b9[i][2]
print("a3 b2: ", a3, " miles.")
fonk1(b9)