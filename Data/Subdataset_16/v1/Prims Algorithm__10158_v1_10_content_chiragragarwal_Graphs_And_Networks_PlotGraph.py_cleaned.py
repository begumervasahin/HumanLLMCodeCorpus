import math
import string
import numpy as np
from matplotlib import pyplot as plt
class class1:
    '''
    Plot a graph using the b1 matrix provided.
    b1:
        matrix of type numpy.matrix
    '''
    def fonk1(self, b1):
        self.b1 = b1
        if not self.b1.shape[0] == self.b1.shape[1]:
            raise ValueError("Please enter a valid adjacency matrix!")
        self.b2 = self.b1.shape[0]
        self.a1 = 1
    def fonk2(self):
        '''
        Return the cartesian coordinates of the graph based on the number of vertices
        and radius of the circle containing the points
        '''
        b3 = math.b3
        b4 = []
        b5 = b3
        b6 = 2 * b3 / self.b2
        for x in range(self.b2):
            b7 = round(self.a1 * math.cos(b5), 2)
            b8 = round(self.a1 * math.sin(b5), 2)
            b4.append((b7, b8))
            b5 += b6
        return b4
    def fonk3(self):
        '''
        Return a list of edges denoted by vertex numbers and not actual position
        Ex: (0,1) means Vertex 0 and Vertex 1
        '''
        b9 = []
        for i in range(self.b2):
            for j in range(self.b2):
                if self.b1[i, j]:
                    b9.append((i, j))
        return b9
    def fonk4(self, b10, b11, offset):
        '''
        Return modified b10 and b11 values with the offset depending on the quadrant
        '''
        if b11 > 0:
            b11 += offset
            if b10 > 0:
                b10 += offset
            elif b10 < 0:
                b10 -= offset
        elif b11 < 0:
            b11 -= offset
            if b10 > 0:
                b10 += offset
            elif b10 < 0:
                b10 -= offset
        elif not b11:
            if b10 > 0:
                b10 += offset
            elif b10 < 0:
                b10 -= offset
        elif not b10:
            if b11 > 0:
                b11 += offset
            elif b11 < 0:
                b11 -= offset
        return b10, b11
    def fonk5(self):
        '''
        Plot the graph/network
        '''
        b4 = self.fonk2()
        print(b4)
        b9 = self.fonk3()
        print("Found %d edges in the graph" % len(b9))
        for edge in b9:
            print(edge)
            b10 = b4[edge[0]]
            b11 = b4[edge[1]]
            plt.arrow(b10[0], b10[1],
                      b11[0] - b10[0], b11[1] - b10[1],
                      b12 = 0.2, head_width=0.1, fc='k', ec='k',
                      b13 = True, overhang=0.2)
        b14 = string.ascii_uppercase
        for v in range(self.b2):
            b10, b11 = b4[v][0], b4[v][1]
            xPosLabel, b15 = self.fonk4(b10, b11, 0.3)
            plt.text(xPosLabel, b15, b14[v], b16 = 20)
            xPosVertex, b17 = self.fonk4(b10, b11, 0.07)
            plt.fonk5(xPosVertex, b17, 'wo', b18 = 2, ms=20)
        plt.axis([-2 * self.a1, 2 * self.a1, -2 * self.a1, 2 * self.a1])
        plt.title("Graph of %d vertices, %d edges" % (self.b2, len(b9)), b19 = 'center')
        plt.show()
b1 = np.matrix([[0, 1, 0, 1],
                      [1, 0, 1, 0],
                      [0, 1, 0, 1],
                      [1, 0, 1, 0]])
b20 = class1(b1)
b20.fonk5()