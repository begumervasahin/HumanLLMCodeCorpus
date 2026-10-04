import math
import matplotlib.pyplot as plt
from sympy import cos, sin, pi
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
def fonk2(b5, b4 = 100):
    return [
        (cos(2 * pi / b4 * b9) * b5,
         sin(2 * pi / b4 * b9) * b5)
        for b9 in range(b4)
    ]
def fonk3(node1, node2):
    return math.sqrt((node1.b1 - node2.b1) ** 2 + (node1.b2 - node2.b2) ** 2)
def fonk4(b5 = 1.0, b4=8):
    b6 = fonk2(b5, b4)
    b7 = [class1(b1, b2, b9) for b9, (b1, b2) in enumerate(b6)]
    b8 = [
        [0 if b9 = = j else fonk3(b7[b9], b7[j])
         for j in range(b4)]
        for b9 in range(b4)
    ]
    return b6, b7, b8
def fonk5(b6, edges, b5 = 1.0):
    x_coords, b10 = zip(*b6)
    plt.plot(x_coords, b10, 'ro', b11 = 'Nodes')
    for edge in edges:
        plt.plot(
            [edge[0].b1, edge[1].b1],
            [edge[0].b2, edge[1].b2],
            'b-', a1 = 1
        )
    plt.axis([-b5 * 1.5, b5 * 1.5, -b5 * 1.5, b5 * 1.5])
    plt.grid(True)
    plt.gca().set_aspect('equal', 'datalim')
    plt.legend()
    plt.show()
if b12 = = "__main__":
    b6, b7, b13 = fonk4(b5=1.0, b4=8)
    b14 = [
        (b7[b9], b7[j])
        for b9 in range(len(b7))
        for j in range(b9 + 1, len(b7))
    ]
    fonk5(b6, b14, b5 = 1.0)