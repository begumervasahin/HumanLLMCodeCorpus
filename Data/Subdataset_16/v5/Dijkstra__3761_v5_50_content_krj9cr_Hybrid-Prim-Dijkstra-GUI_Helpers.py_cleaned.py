import math
import matplotlib.pyplot as plt
from sympy import cos, sin, pi
from Node import Node
def fonk1(b5, b1 = 100):
    b2 = 2 * pi / b1
    return [
        (cos(b2 * x) * b5, sin(b2 * x) * b5)
        for x in range(b1)
    ]
def fonk2(node1, node2):
    b3 = node1.x - node2.x
    b4 = node1.y - node2.y
    return math.sqrt(b3 ** 2 + b4 ** 2)
def fonk3(b5 = 1.0, b1=8):
    b6 = fonk1(b5, b1)
    b7 = [Node(x, y, i) for i, (x, y) in enumerate(b6)]
    b8 = [
        [fonk2(b7[i], b7[j]) if i != j else 0
         for j in range(b1)]
        for i in range(b1)
    ]
    return b6, b7, b8
def fonk4(b6, edges, b5 = 1.0):
    x_coords, b9 = zip(*b6)
    plt.figure(b10 = (8, 8))
    plt.plot(x_coords, b9, 'ro', b11 = 'Nodes')
    for node1, node2 in edges:
        plt.plot(
            [node1.x, node2.x],
            [node1.y, node2.y],
            'b-',
            a1 = 1
        )
    plt.axis([-b5 * 1.5, b5 * 1.5, -b5 * 1.5, b5 * 1.5])
    plt.grid(True)
    plt.gca().set_aspect('equal', 'datalim')
    plt.legend()
    plt.show()
if b12 = = "__main__":
    b6, b7, b13 = fonk3(b5=1.0, b1=8)
    b14 = [
        (b7[i], b7[j])
        for i in range(len(b7))
        for j in range(i + 1, len(b7))
    ]
    fonk4(b6, b14, b5 = 1.0)