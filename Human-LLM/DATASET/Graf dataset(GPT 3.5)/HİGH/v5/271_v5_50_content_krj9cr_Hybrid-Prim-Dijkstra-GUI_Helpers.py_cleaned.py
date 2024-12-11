import math
import matplotlib.pyplot as plt
from sympy import *
from Node import Node
def fonk1(b3, b1 = 100):
    b2 = [(cos(2 * pi / b1 * b6) * b3, sin(2 * pi / b1 * b6) * b3) for b6 in range(b1 + 1)]
    return [(0, 0)] + b2
def fonk2(node1, node2):
    return math.sqrt((node1.b6 - node2.b6) ** 2 + (node1.b7 - node2.b7) ** 2)
def fonk3(b3 = 1.0, a2=8):
    b2 = fonk1(b3, a2)
    b4 = [Node(b6, b7, i) for i, (b6, b7) in enumerate(b2)]
    b5 = [[0 if i == j else fonk2(b4[i], b4[j]) for j in range(len(b4))] for i in range(len(b4))]
    return b2, b4, b5
def fonk4(b2, b5, b3 = 1.0):
    b6 = [p[0] for p in b2]
    b7 = [p[1] for p in b2]
    plt.plot(b6, b7, 'ro')
    for i in range(len(b5)):
        for j in range(len(b5[i])):
            if i != j:
                plt.plot([b2[i][0], b2[j][0]], [b2[i][1], b2[j][1]], 'b-', b8 = 1)
    b9 = b3 * 2
    plt.axis([-b9, b9, -b9, b9])
    plt.grid(True)
    plt.gca().set_aspect('equal', b10 = 'box')
    plt.show()
def fonk5():
    a1 = 1.0
    a2 = 8
    b2, _, b5 = fonk3(a1, a2)
    fonk4(b2, b5, a1)
if b11 = = "__main__":
    fonk5()