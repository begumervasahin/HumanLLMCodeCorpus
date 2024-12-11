
import math
import matplotlib.pyplot as plt
from sympy import *
from Node import Node
def fonk1(b2, b1 = 100):
    return [(0, 0)] + [(cos(2 * pi / b1 * b6) * b2, sin(2 * pi / b1 * b6) * b2) for b6 in range(b1 + 1)]
def fonk2(node1, node2):
    return math.sqrt((node1.b6 - node2.b6) ** 2 + (node1.b7 - node2.b7) ** 2)
def fonk3(b2 = 1.0, a2=8):
    b3 = fonk1(b2, a2)
    b4 = [Node(b3[i][0], b3[i][1], i) for i in range(len(b3))]
    b5 = [[fonk2(b4[i], b4[j]) if i != j else 0 for j in range(len(b4))] for i in range(len(b4))]
    return b3, b4, b5
def fonk4(b3, b5, b2 = 1.0):
    b6 = [p[0] for p in b3]
    b7 = [p[1] for p in b3]
    plt.plot(b6, b7, 'ro')
    for edge in b5:
        print(edge[0].idx, edge[1].idx)
        plt.plot([edge[0].b6, edge[1].b6], [edge[0].b7, edge[1].b7], 'b-', b8 = 1)
    b9 = b2 * 2
    plt.axis([-b9, b9, -b9, b9])
    plt.grid(True)
    plt.gca().set_aspect('equal', b10 = 'box')
    plt.show()
def fonk5():
    a1 = 1.0
    a2 = 8
    b3, b4, b5 = fonk3(a1, a2)
    fonk4(b3, b5, a1)
if b11 = = "__main__":
    fonk5()