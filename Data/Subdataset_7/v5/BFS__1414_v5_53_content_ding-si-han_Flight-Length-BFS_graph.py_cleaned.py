import random
from itertools import chain
import time
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, b7, neighbour):
        if b7 not in self.b1:
            self.b1[b7] = [neighbour]
        else:
            if neighbour not in self.b1[b7] and neighbour != b7:
                self.b1[b7].append(neighbour)
    def fonk3(self):
        for b7 in self.b1:
            for neighbour in self.b1[b7]:
                print("(", b7, ", ", neighbour, ")")
    def fonk4(self, b6, destination):
        b2 = b6
        b3 = {}
        b4 = {}
        for i in self.b1:
            b3[i] = False
        b5 = []
        b5.append(b6)
        b3[b6] = True
        while b5:
            b6 = b5.pop(0)
            for b7 in self.b1[b6]:
                if not b3[b7]:
                    b4[b7] = b6
                    if b7 = = destination:
                        self.fonk5(b4, b2, destination)
                        return
                    b3[b7] = True
                    b5.append(b7)
        print("NO FLIGHT PATH AVAILABLE")
    def fonk5(self, b4, b6, destination):
        print("OPTIMAL ROUTE:", b8 = " ")
        b9 = b4[destination]
        print(destination, b8 = " ")
        while b6 != b9:
            print("-", b9, b8 = " ")
            b9 = b4[b9]
        print('-', b6)
    def fonk6(self, max_cities, percentage_cities):
        for i in range(max_cities):
            b10 = chain(range(0, i), range(i + 1, max_cities))
            b11 = random.sample(list(b10), round(max_cities * percentage_cities))
            for neighbour in b11:
                self.fonk2(str(i + 1), str(neighbour + 1))
                self.fonk2(str(neighbour + 1), str(i + 1))
"""
Measuring the time taken for BFS Algorithm for:
1. Different number of cities in graphs (Vertices)
2. Different number of non-stop flights (Edges)
Plotting the shortest path for an airline to enable a passenger to fly from city A (Singapore) to city B (Florida).
1. Finding how the number of cities in the network affect the time taken for BFS Algorithm.