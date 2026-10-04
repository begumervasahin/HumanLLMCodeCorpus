import math
import string
import matplotlib.pyplot as plt
from pathlib import Path
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        if self.b1.shape[0] != self.b1.shape[1]:
            raise ValueError("The adjacency matrix must be square.")
        self.b2 = self.b1.shape[0]
        self.a1 = 1
    def fonk2(self):
        b3 = []
        b4 = math.pi
        b5 = 2 * math.pi / self.b2
        for _ in range(self.b2):
            b6 = round(self.a1 * math.cos(b4), 2)
            b7 = round(self.a1 * math.sin(b4), 2)
            b3.append((b6, b7))
            b4 += b5
        return b3
    def fonk3(self):
        b8 = []
        for i in range(self.b2):
            for j in range(self.b2):
                if self.b1[i, j]:
                    b8.append((i, j))
        return b8
    def fonk4(self, b9, b15, offset):
        if b15 > 0:
            b15 += offset
            b9 += offset if b9 > 0 else b9 - offset
        elif b15 < 0:
            b15 -= offset
            b9 += offset if b9 > 0 else b9 - offset
        else:
            b9 += offset if b9 > 0 else b9 - offset
        if b9 = = 0:
            b15 += offset if b15 > 0 else b15 - offset
        return b9, b15
    def fonk5(self):
        b3 = self.fonk2()
        b8 = self.fonk3()
        print("Vertex coordinates:", b3)
        print(f"Found {len(b8)} edges in the graph.")
        for edge in b8:
            x_pos_start, b10 = b3[edge[0]]
            x_pos_end, b11 = b3[edge[1]]
            plt.arrow(
                x_pos_start, b10,
                x_pos_end - x_pos_start, b11 - b10,
                b12 = 0.2, head_width=0.1, fc='k', ec='k',
                b13 = True, overhang=0.2
            )
        b14 = string.ascii_uppercase
        for v in range(self.b2):
            b9, b15 = b3[v]
            x_pos_label, b16 = self.fonk4(b9, b15, 0.3)
            plt.text(x_pos_label, b16, b14[v], b17 = 20)
            x_pos_vertex, b18 = self.fonk4(b9, b15, 0.07)
            plt.fonk5(x_pos_vertex, b18, 'wo', b19 = 2, ms=20)
        plt.axis([-2 * self.a1, 2 * self.a1, -2 * self.a1, 2 * self.a1])
        plt.title(f"Graph with {self.b2} vertices and {len(b8)} edges", b20 = 'center')
        plt.show()
if b21 = = '__main__':
    b22 = np.matrix([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ])
    b23 = class1(b22)
    b23.fonk5()