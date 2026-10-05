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
def fonk1(b14):
    b1 = nx.Graph()
    for i in range(len(b14)):
        b1.add_edge(
            b24[b14[i][0]],
            b24[b14[i][1]],
            b2 = int(b14[i][2]))
    b3 = [(b18, b17) for (b18, b17, d) in b1.edges(data=True)]
    b4 = nx.spring_layout(b1, a4=20, b4=None, fixed=None, iterations=150, b2='b2', scale=1.0)
    b2 = dict(map(lambda x: ((x[0], x[1]), str(x[2]['b2'])), b1.edges(data=True)))
    nx.draw_networkx_edge_labels(b1, b4, b5 = b2)
    a1 = 0
    for i in range(b25):
        if len(b24[i]) > a1:
            a1 = len(b24)
    nx.draw_networkx_nodes(b1, b4, b6 = a1 * 180, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(b1, b4, b7 = b3, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b4, b8 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk2(b26):
    b9 = []
    b9.append(b26[0])
    b10 = b26[0]
    for i in range(1, len(b26)):
        b11 = b26[i][2]
        a2 = 0
        while b11 > b9[a2][2] and a2 < len(b9) - 1:
            a2 += 1
        b9.insert(a2, b26[i])
    b12 = b9[len(b9) - 1]
    b9.remove(b9[len(b9) - 1])
    a2 = 0
    while b12[2] > b9[a2][2] and a2 < len(b9) - 1:
        a2 += 1
    b9.insert(a2, b12)
    return b9
def fonk3(b13, b15):
    while b13 != b15[b13]:
        b13 = b15[b13]
    return b13
def fonk4(b15, b20, b19, b16):
    if b16[b20] > b16[b19]:
        b15[b19] = b20
    elif b16[b20] < b16[b19]:
        b15[b20] = b19
    else:
        b15[b19] = b20
        b16[b20] += 1
def fonk5(b26):
    b14 = []
    b9 = fonk2(b26)
    b15 = []
    b16 = []
    for e in range(b25):
        b15.append(e)
        b16.append(0)
    a3 = 0
    a4 = 0
    while a3 < (b25 - 1):
        b17 = b9[a4][0]
        b18 = b9[a4][1]
        a4 += 1
        b19 = fonk3(b17, b15)
        b20 = fonk3(b18, b15)
        if b20 != b19:
            a3 += 1
            b14.append([b17, b18, b9[a4][2]])
            fonk4(b15, b20, b19, b16)
    return b14
b21 = sys.argv[1]
b22 = set()
with open(b21) as f:
    for i in f:
        b23 = i.strip().split(' ')
        b22.add(b23[0])
        b22.add(b23[1])
b24 = list(b22)
b25 = (len(b22))
b26 = []
with open(b21) as f:
    for i in f:
        b23 = i.strip().split(' ')
        b26.append([
            int(b24.index(b23[0])),
            int(b24.index(b23[1])),
            int(b23[2])])
b14 = fonk5(b26)
a5 = 0
print("The minimum spanning tree is as follows:")
for i in range(len(b14)):
    print(b24[b14[i][0]], " to ", b24[b14[i][1]], " = ", b14[i][2], "miles")
    a5 += b14[i][2]
print("a5 b2: ", a5, " miles.")
fonk1(b14)