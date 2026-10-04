import math
import string
import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        if self.b1.shape[0] != self.b1.shape[1]:
            raise ValueError("The adjacency matrix must be square.")
        self.b2 = self.b1.shape[0]
        self.a1 = 1
    def fonk2(self):
        b3 = []
        b4 = 2 * math.pi / self.b2
        b5 = math.pi
        for _ in range(self.b2):
            b6 = round(self.a1 * math.cos(b5), 2)
            b7 = round(self.a1 * math.sin(b5), 2)
            b3.append((b6, b7))
            b5 += b4
        return b3
    def fonk3(self):
        b8 = []
        for i in range(self.b2):
            for j in range(self.b2):
                if self.b1[i, j]:
                    b8.append((i, j))
        return b8
    def fonk4(self, b6, b7, offset):
        if b7 > 0:
            b7 += offset
            b6 += offset if b6 > 0 else b6 - offset
        elif b7 < 0:
            b7 -= offset
            b6 += offset if b6 > 0 else b6 - offset
        else:
            b6 += offset if b6 > 0 else b6 - offset
        if b6 = = 0:
            b7 += offset if b7 > 0 else b7 - offset
        return b6, b7
    def fonk5(self):
        b3 = self.fonk2()
        b8 = self.fonk3()
        print("Vertex coordinates:", b3)
        print(f"Found {len(b8)} b8 in the graph.")
        for edge in b8:
            x_start, b9 = b3[edge[0]]
            x_end, b10 = b3[edge[1]]
            plt.arrow(
                x_start, b9,
                x_end - x_start, b10 - b9,
                b11 = 0.2, head_width=0.1, fc='k', ec='k',
                b12 = True, overhang=0.2
            )
        b13 = string.ascii_uppercase
        for v in range(self.b2):
            b6, b7 = b3[v]
            x_label, b14 = self.fonk4(b6, b7, 0.3)
            plt.text(x_label, b14, b13[v], b15 = 20)
            x_vertex, b16 = self.fonk4(b6, b7, 0.07)
            plt.fonk5(x_vertex, b16, 'wo', b17 = 2, ms=20)
        plt.axis([-2 * self.a1, 2 * self.a1, -2 * self.a1, 2 * self.a1])
        plt.title(f"Graph with {self.b2} vertices and {len(b8)} b8", b18 = 'center')
        plt.show()
if b19 = = '__main__':
    b20 = np.matrix([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ])
    b21 = class1(b20)
    b21.fonk5()