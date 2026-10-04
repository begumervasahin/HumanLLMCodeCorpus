import math
import matplotlib.pyplot as plt
from sympy import cos, sin, pi
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
def fonk2(b5, b4 = 100):
    return [(cos(2 * pi / b4 * i) * b5,
             sin(2 * pi / b4 * i) * b5)
            for i in range(b4)]
def fonk3(node1, node2):
    return math.sqrt((node1.b1 - node2.b1) ** 2 + (node1.b2 - node2.b2) ** 2)
def fonk4(b5 = 1.0, b4=8):
    b6 = fonk2(b5, b4)
    b7 = [class1(b1, b2, i) for i, (b1, b2) in enumerate(b6)]
    b8 = [[0 if i == j else fonk3(b7[i], b7[j])
                  for j in range(b4)] for i in range(b4)]
    return b6, b7, b8
def fonk5(b6, edges, b5 = 1.0):
    x_coords, b9 = zip(*b6)
    plt.plot(x_coords, b9, 'ro')
    for edge in edges:
        plt.plot([edge[0].b1, edge[1].b1], [edge[0].b2, edge[1].b2], 'b-', b10 = 1)
    plt.axis([-b5*2, b5*2, -b5*2, b5*2])
    plt.grid(True)
    plt.gca().set_aspect('equal', 'datalim')
    plt.show()
if b11 = = "__main__":
    b6, b7, b12 = fonk4(b5=1.0, b4=8)
    b13 = [(b7[i], b7[j]) for i in range(len(b7)) for j in range(i + 1, len(b7))]
    fonk5(b6, b13, b5 = 1.0)