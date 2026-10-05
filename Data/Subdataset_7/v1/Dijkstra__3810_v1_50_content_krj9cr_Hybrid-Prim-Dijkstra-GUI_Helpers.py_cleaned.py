import math
import matplotlib.pyplot as plt
from sympy import *
from Node import Node
def fonk1(r, b1 = 100):
    return [(0, 0)] + [(cos(2 * pi / b1 * b6) * r, sin(2 * pi / b1 * b6) * r) for b6 in range(0, b1 + 1)]
def fonk2(node1, node2):
    return math.sqrt((node1.b6 - node2.b6) ** 2 + (node1.b7 - node2.b7) ** 2)
def fonk3(b2 = 1.0, b1=8):
    b3 = fonk1(b2, b1)
    b4 = [Node(b3[i][0], b3[i][1], i) for i in range(len(b3))]
    b5 = [[fonk2(b4[i], b4[j]) if i != j else 0 for j in range(len(b4))] for i in range(len(b4))]
    return b3, b4, b5
def fonk4(b3, lines, b2 = 1.0):
    b6 = [p[0] for p in b3]
    b7 = [p[1] for p in b3]
    plt.plot(b6, b7, 'ro')
    for line in lines:
        print(line[0].idx, line[1].idx)
        plt.plot([line[0].b6, line[1].b6], [line[0].b7, line[1].b7], 'b-', b8 = 1)
    b9 = b2 * 2
    plt.axis([-b9, b9, -b9, b9])
    plt.grid(True)
    plt.gca().set_aspect('equal', b10 = 'box')
    plt.show()
def fonk5():
    b2 = 1.0
    b1 = 8
    b3, b4, b5 = fonk3(b2, b1)
    fonk4(b3, b5, b2)
if b11 = = "__main__":
    fonk5()