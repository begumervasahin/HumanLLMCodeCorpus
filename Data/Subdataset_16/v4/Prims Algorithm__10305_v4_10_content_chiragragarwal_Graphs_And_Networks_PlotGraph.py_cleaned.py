import math
import string
import numpy as np
from matplotlib import pyplot as plt
class class1:
    '''
    Plot a graph using the b1 matrix provided.
    b1: matrix of type numpy.matrix
    '''
    def fonk1(self, b1):
        self.b1 = b1
        if not self.b1.shape[0] == self.b1.shape[1]:
            raise ValueError("Please enter a valid adjacency matrix!")
        self.b2 = self.b1.shape[0]
        self.a1 = 1
    def fonk2(self):
        '''
        Return the Cartesian coordinates of the graph based on the number of vertices
        and radius of the circle containing the points
        '''
        b3 = math.b3
        b4 = []
        b5 = b3
        b6 = 2 * b3 / self.b2
        for i in range(self.b2):
            b7 = round(self.a1 * math.cos(b5), 2)
            b8 = round(self.a1 * math.sin(b5), 2)
            b4.append((b7, b8))
            b5 += b6
        return b4
    def fonk3(self):
        '''
        Return a list of edges denoted by vertex numbers and not actual position.
        Ex: (0, 1) means Vertex 0 and Vertex 1
        '''
        b9 = []
        for i in range(self.b2):
            for j in range(self.b2):
                if self.b1[i, j]:
                    b9.append((i, j))
        return b9
    def fonk4(self, b11, b10, offset):
        '''
        Return modified b11 and b10 values with the offset depending on the quadrant
        '''
        if b10 > 0:
            b10 += offset
            b11 += offset if b11 > 0 else -offset
        elif b10 < 0:
            b10 -= offset
            b11 += offset if b11 > 0 else -offset
        elif b10 = = 0:
            b11 += offset if b11 > 0 else -offset
        elif b11 = = 0:
            b10 += offset if b10 > 0 else -offset
        return b11, b10
    def fonk5(self):
        '''
        Plot the graph/network
        '''
        b4 = self.fonk2()
        print(b4)
        b9 = self.fonk3()
        print(f"Found {len(b9)} edges in the graph")
        for edge in b9:
            print(edge)
            xStart, b12 = b4[edge[0]]
            xEnd, b13 = b4[edge[1]]
            plt.arrow(xStart, b12,
                      xEnd - xStart, b13 - b12,
                      b14 = 0.2, head_width=0.1, fc='k', ec='k',
                      b15 = True, overhang=0.2)
        b16 = string.ascii_uppercase
        for v in range(self.b2):
            b11, b10 = b4[v]
            xPosLabel, b17 = self.fonk4(b11, b10, 0.3)
            plt.text(xPosLabel, b17, b16[v], b18 = 20)
            xPosVertex, b19 = self.fonk4(b11, b10, 0.07)
            plt.fonk5(xPosVertex, b19, 'wo', b20 = 2, ms=20)
        plt.axis([-2 * self.a1, 2 * self.a1, -2 * self.a1, 2 * self.a1])
        plt.title(f"Graph of {self.b2} vertices, {len(b9)} edges", b21 = 'center')
        plt.show()
if b22 = = "__main__":
    b1 = np.matrix([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ])
    b23 = class1(b1)
    b23.fonk5()