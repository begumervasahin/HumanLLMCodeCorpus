import math
import string
import numpy as np
from matplotlib import pyplot as plt
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        if self.b1.shape[0] != self.b1.shape[1]:
            raise ValueError("Please enter a valid square adjacency matrix!")
        self.b2 = self.b1.shape[0]
        self.a1 = 1
    def fonk2(self):
        b3 = math.b3
        b4 = b3
        b5 = 2 * b3 / self.b2
        b6 = []
        for _ in range(self.b2):
            b7 = round(self.a1 * math.cos(b4), 2)
            b8 = round(self.a1 * math.sin(b4), 2)
            b6.append((b7, b8))
            b4 += b5
        return b6
    def fonk3(self):
        b9 = []
        for i in range(self.b2):
            for j in range(self.b2):
                if self.b1[i, j]:
                    b9.append((i, j))
        return b9
    def fonk4(self, b7, b8, offset):
        if b8 > 0:
            b8 += offset
            b7 += offset if b7 > 0 else -offset
        elif b8 < 0:
            b8 -= offset
            b7 += offset if b7 > 0 else -offset
        elif b8 = = 0:
            b7 += offset if b7 > 0 else -offset
        elif b7 = = 0:
            b8 += offset if b8 > 0 else -offset
        return b7, b8
    def fonk5(self):
        b6 = self.fonk2()
        b9 = self.fonk3()
        print(b6)
        print(f"Found {len(b9)} edges in the graph")
        for edge in b9:
            print(edge)
            b10 = b6[edge[0]]
            b11 = b6[edge[1]]
            plt.arrow(b10[0], b10[1], b11[0] - b10[0], b11[1] - b10[1],
                      b12 = 0.2, head_width=0.1, fc='k', ec='k',
                      b13 = True, overhang=0.2)
        for i in range(self.b2):
            b7, b8 = b6[i]
            label_x, b14 = self.fonk4(b7, b8, 0.3)
            plt.text(label_x, b14, string.ascii_uppercase[i], b15 = 20)
            vertex_x, b16 = self.fonk4(b7, b8, 0.07)
            plt.fonk5(vertex_x, b16, 'wo', b17 = 2, ms=20)
        plt.axis([-2 * self.a1, 2 * self.a1, -2 * self.a1, 2 * self.a1])
        plt.title(f"Graph of {self.b2} vertices, {len(b9)} edges", b18 = 'center')
        plt.show()
if b19 = = "__main__":
    b1 = np.matrix([[0, 1, 0, 1],
                          [1, 0, 1, 0],
                          [0, 1, 0, 1],
                          [1, 0, 1, 0]])
    b20 = class1(b1)
    b20.fonk5()