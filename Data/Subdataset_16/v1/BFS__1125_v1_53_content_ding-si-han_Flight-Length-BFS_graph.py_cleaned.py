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
        while len(b5) != 0:
            b6 = b5.pop(0)
            for b7 in self.b1[b6]:
                if b3[b7] != True:
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
    def fonk6(self, max, percentageCities):
        for i in range(max):
            b10 = chain(range(0, i), range(i+1, max))
            b11 = random.sample(list(b10), round(max * percentageCities))
            for neighbour in b11:
                self.fonk2(str(i+1), str(neighbour + 1))
                self.fonk2(str(neighbour+1), str(i + 1))
def fonk7(a2, a1, start_city, end_city):
    b12 = class1()
    b12.fonk6(a2, a1)
    b13 = time.time()
    b12.fonk4(start_city, end_city)
    b14 = time.time()
    return b14 - b13
def fonk8():
    b15 = [10, 20, 50, 100, 200, 500, 1000]
    a1 = 0.1
    b16 = []
    for a2 in b15:
        b17 = fonk7(a2, a1, '1', str(a2))
        b16.append(b17)
        print(f"Number of cities: {a2}, Time taken: {b17:.5f} seconds")
    plt.plot(b15, b16, b18 = 'o')
    plt.xlabel('Number of Cities')
    plt.ylabel('Time taken for BFS (seconds)')
    plt.title('BFS Time vs Number of Cities')
    plt.grid(True)
    plt.show()
def fonk9():
    a2 = 100
    b19 = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
    b16 = []
    for percentage_edges in b19:
        b17 = fonk7(a2, percentage_edges, '1', '100')
        b16.append(b17)
        print(f"Percentage of edges: {percentage_edges}, Time taken: {b17:.5f} seconds")
    plt.plot(b19, b16, b18 = 'o')
    plt.xlabel('Percentage of Edges')
    plt.ylabel('Time taken for BFS (seconds)')
    plt.title('BFS Time vs Percentage of Edges')
    plt.grid(True)
    plt.show()
if b20 = = '__main__':
    b21 = input("Enter '1' to plot BFS time vs number of cities or '2' to plot BFS time vs percentage of edges: ")
    if b21 = = '1':
        fonk8()
    elif b21 = = '2':
        fonk9()
    else:
        print("Invalid b21. Exiting.")