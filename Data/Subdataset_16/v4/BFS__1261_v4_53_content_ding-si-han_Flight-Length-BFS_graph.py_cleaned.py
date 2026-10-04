import random
from itertools import chain
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, node, b7):
        if node not in self.b1:
            self.b1[node] = [b7]
        else:
            if b7 not in self.b1[node] and b7 != node:
                self.b1[node].append(b7)
    def fonk3(self):
        for node in self.b1:
            for b7 in self.b1[node]:
                print(f"({node}, {b7})")
    def fonk4(self, start, destination):
        b2 = start
        b3 = {node: False for node in self.b1}
        b4 = {}
        b5 = [start]
        b3[start] = True
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
    def fonk5(self, b4, start, destination):
        print("OPTIMAL ROUTE:", b8 = " ")
        b9 = destination
        b10 = []
        while b9 != start:
            b10.append(b9)
            b9 = b4.get(b9, start)
        b10.append(start)
        print(" - ".join(reversed(b10)))
    def fonk6(self, max_nodes, percentage_cities):
        for i in range(max_nodes):
            b11 = chain(range(0, i), range(i + 1, max_nodes))
            b12 = random.sample(list(b11), round(max_nodes * percentage_cities))
            for b7 in b12:
                self.fonk2(str(i + 1), str(b7 + 1))
                self.fonk2(str(b7 + 1), str(i + 1))
if b13 = = "__main__":
    b14 = class1()
    b14.fonk6(10, 0.3)
    b14.fonk3()
    b14.fonk4('1', '7')
This project measures the time taken for the BFS algorithm for:
1. Different numbers of cities in graphs (vertices).
2. Different numbers of non-stop flights (edges).
To plot the shortest b10 for an airline, enabling a passenger to fly from city A (Singapore) to city B (Florida).
1. To find how the number of cities in the network affects the time taken for the BFS algorithm:
   ```sh
   $ python numCities.py