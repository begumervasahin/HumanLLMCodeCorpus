import math
import matplotlib.pyplot as plt
from sympy import cos, sin, pi
from Node import Node
def fonk1(b2, b1 = 100):
    return [
        (cos(2 * pi / b1 * x) * b2,
         sin(2 * pi / b1 * x) * b2)
        for x in range(b1)
    ]
def fonk2(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
def fonk3(b2 = 1.0, b1=8):
    b3 = fonk1(b2, b1)
    b4 = [Node(x, y, b6) for b6, (x, y) in enumerate(b3)]
    b5 = [
        [0 if b6 = = j else fonk2(b4[b6], b4[j])
         for j in range(b1)]
        for b6 in range(b1)
    ]
    return b3, b4, b5
def fonk4(b3, edges, b2 = 1.0):
    x_coords, b7 = zip(*b3)
    plt.plot(x_coords, b7, 'ro', b8 = 'Nodes')
    for edge in edges:
        plt.plot(
            [edge[0].x, edge[1].x],
            [edge[0].y, edge[1].y],
            'b-', a1 = 1
        )
    plt.axis([-b2 * 1.5, b2 * 1.5, -b2 * 1.5, b2 * 1.5])
    plt.grid(True)
    plt.gca().set_aspect('equal', 'datalim')
    plt.legend()
    plt.show()
if b9 = = "__main__":
    b3, b4, b10 = fonk3(b2=1.0, b1=8)
    b11 = [
        (b4[b6], b4[j])
        for b6 in range(len(b4))
        for j in range(b6 + 1, len(b4))
    ]
    fonk4(b3, b11, b2 = 1.0)