import math
import string
import numpy as np
import matplotlib.pyplot as plt
class class1:
    '''
    Plot a graph using the adjacency matrix provided.
    Attributes:
        b1 (numpy.ndarray): The adjacency matrix representing the graph.
        b2 (int): The number of vertices in the graph.
        a1 (int): The radius of the circle containing the vertices.
    '''
    def fonk1(self, b1):
        if b1.shape[0] != b1.shape[1]:
            raise ValueError("Please provide a valid adjacency matrix (square matrix).")
        self.b1 = b1
        self.b2 = b1.shape[0]
        self.a1 = 1
    def fonk2(self):
        '''
        Calculate the Cartesian coordinates of the vertices based on the number of vertices
        and radius of the circle containing the points.
        Returns:
            list: A list of tuples containing (x, y) coordinates for each vertex.
        '''
        b3 = math.b3
        b4 = []
        b5 = b3
        b6 = 2 * b3 / self.b2
        for _ in range(self.b2):
            b7 = round(self.a1 * math.cos(b5), 2)
            b8 = round(self.a1 * math.sin(b5), 2)
            b4.append((b7, b8))
            b5 += b6
        return b4
    def fonk3(self):
        '''
        Retrieve the edges present in the graph.
        Returns:
            list: A list of tuples representing the edges in the graph.
        '''
        b9 = []
        for i in range(self.b2):
            for j in range(self.b2):
                if self.b1[i, j]:
                    b9.append((i, j))
        return b9
    def fonk4(self, b11, b10, offset):
        '''
        Calculate modified b11 and b10 values with the offset depending on the quadrant.
        Args:
            b11 (float): The x-coordinate.
            b10 (float): The y-coordinate.
            offset (float): The offset value.
        Returns:
            tuple: The modified (b11, b10) coordinates.
        '''
        if b10 > 0:
            b10 += offset
            if b11 != 0:
                b11 += offset if b11 > 0 else -offset
        elif b10 < 0:
            b10 -= offset
            if b11 != 0:
                b11 += offset if b11 > 0 else -offset
        elif b10 = = 0:
            b11 += offset if b11 != 0 else 0
        elif b11 = = 0:
            b10 += offset if b10 != 0 else 0
        return b11, b10
    def fonk5(self):
        '''
        Plot the graph.
        '''
        b4 = self.fonk2()
        print(b4)
        b9 = self.fonk3()
        print("Found %d edges in the graph" % len(b9))
        for edge in b9:
            print(edge)
            b11 = b4[edge[0]]
            b10 = b4[edge[1]]
            plt.arrow(b11[0], b11[1], b10[0] - b11[0], b10[1] - b11[1],
                      b12 = 0.2, head_width=0.1, fc='k', ec='k',
                      b13 = True, overhang=0.2)
        b14 = string.ascii_uppercase
        for v in range(self.b2):
            b11, b10 = b4[v][0], b4[v][1]
            xPosLabel, b15 = self.fonk4(b11, b10, 0.3)
            plt.text(xPosLabel, b15, b14[v], b16 = 20)
            xPosVertex, b17 = self.fonk4(b11, b10, 0.07)
            plt.fonk5(xPosVertex, b17, 'wo', b18 = 2, ms=20)
        plt.axis([-2 * self.a1, 2 * self.a1, -2 * self.a1, 2 * self.a1])
        plt.title("Graph of %d vertices, %d edges" % (self.b2, len(b9)), b19 = 'center')
        plt.show()
if b20 = = "__main__":
    b21 = np.array([[0, 1, 1, 0],
                             [1, 0, 1, 1],
                             [1, 1, 0, 1],
                             [0, 1, 1, 0]])
    b22 = class1(b21)
    b22.fonk5()