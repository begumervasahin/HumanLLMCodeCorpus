import math
import matplotlib.pyplot as plt
from sympy import cos, sin, pi
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
def fonk2(b5, b4 = 100):
    return [(0, 0)] + [(cos(2 * pi / b4 * b1) * b5,
                        sin(2 * pi / b4 * b1) * b5)
                       for b1 in range(b4 + 1)]
def fonk3(node1, node2):
    return math.sqrt((node1.b1 - node2.b1) ** 2 + (node1.b2 - node2.b2) ** 2)
def fonk4(b5 = 1.0, b4=8):
    b6 = fonk2(b5, b4)
    b7 = [class1(b1, b2, b10) for b10, (b1, b2) in enumerate(b6)]
    b8 = []
    for b10 in range(len(b7)):
        b9 = []
        for j in range(len(b7)):
            if b10 = = j:
                b9.append(0)
            else:
                b9.append(fonk3(b7[b10], b7[j]))
        b8.append(b9)
    return b6, b7, b8
def fonk5(b6, b8, b5 = 1.0):
    b1 = [p[0] for p in b6]
    b2 = [p[1] for p in b6]
    plt.plot(b1, b2, 'ro')
    for edge in b8:
        plt.plot([edge[0].b1, edge[1].b1], [edge[0].b2, edge[1].b2], 'b-', b11 = 1)
    b12 = b5 * 2
    plt.axis([-b12, b12, -b12, b12])
    plt.grid(True)
    plt.gca().set_aspect('equal', 'datalim')
    plt.show()
if b13 = = "__main__":
    b6, b7, b8 = fonk4(b5=1.0, b4=8)
    b14 = [(b7[b10], b7[j]) for b10 in range(len(b7)) for j in range(len(b7)) if b10 != j]
    fonk5(b6, b14, b5 = 1.0)