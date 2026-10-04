import random
from itertools import chain
import time
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
                print(f"({b7}, {neighbour})")
    def fonk4(self, b6, destination):
        b2 = b6
        b3 = {i: False for i in self.b1}
        b4 = {}
        b5 = [b6]
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
        b9 = destination
        b10 = []
        while b9 != b6:
            b10.append(b9)
            b9 = b4[b9]
        b10.append(b6)
        b10.reverse()
        print(" - ".join(b10))
    def fonk6(self, max_nodes, a1):
        for i in range(max_nodes):
            b11 = chain(range(0, i), range(i + 1, max_nodes))
            b12 = random.sample(list(b11), round(max_nodes * a1))
            for neighbour in b12:
                self.fonk2(str(i + 1), str(neighbour + 1))
                self.fonk2(str(neighbour + 1), str(i + 1))
def fonk7(a2, a1, start_city, end_city):
    b13 = class1()
    b13.fonk6(a2, a1)
    b14 = time.time()
    b13.fonk4(start_city, end_city)
    b15 = time.time()
    return b15 - b14
def fonk8():
    b16 = [10, 20, 50, 100, 200, 500, 1000]
    a1 = 0.1
    b17 = []
    for a2 in b16:
        b18 = fonk7(a2, a1, '1', str(a2))
        b17.append(b18)
        print(f"Number of cities: {a2}, Time taken: {b18:.5f} seconds")
    plt.plot(b16, b17, b19 = 'o')
    plt.xlabel('Number of Cities')
    plt.ylabel('Time taken for BFS (seconds)')
    plt.title('BFS Time vs Number of Cities')
    plt.grid(True)
    plt.show()
def fonk9():
    a2 = 100
    b20 = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
    b17 = []
    for percentage_edges in b20:
        b18 = fonk7(a2, percentage_edges, '1', '100')
        b17.append(b18)
        print(f"Percentage of edges: {percentage_edges}, Time taken: {b18:.5f} seconds")
    plt.plot(b20, b17, b19 = 'o')
    plt.xlabel('Percentage of Edges')
    plt.ylabel('Time taken for BFS (seconds)')
    plt.title('BFS Time vs Percentage of Edges')
    plt.grid(True)
    plt.show()
if b21 = = '__main__':
    b22 = input("Enter '1' to plot BFS time vs number of cities or '2' to plot BFS time vs percentage of edges: ")
    if b22 = = '1':
        fonk8()
    elif b22 = = '2':
        fonk9()
    else:
        print("Invalid b22. Exiting.")