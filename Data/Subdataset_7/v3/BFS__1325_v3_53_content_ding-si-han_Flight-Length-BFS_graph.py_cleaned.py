import random
from collections import deque
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, node, b6):
        if node not in self.b1:
            self.b1[node] = [b6]
        else:
            if b6 not in self.b1[node] and b6 != node:
                self.b1[node].append(b6)
    def fonk3(self):
        for node in self.b1:
            for b6 in self.b1[node]:
                print("(", node, ", ", b6, ")")
    def fonk4(self, start, destination):
        b2 = set()
        b3 = {}
        b4 = deque([start])
        b2.add(start)
        while b4:
            b5 = b4.popleft()
            for b6 in self.b1.get(b5, []):
                if b6 not in b2:
                    b3[b6] = b5
                    if b6 = = destination:
                        self.fonk5(b3, start, destination)
                        return
                    b2.add(b6)
                    b4.append(b6)
        print("NO FLIGHT PATH AVAILABLE")
    def fonk5(self, b3, start, destination):
        print("OPTIMAL ROUTE:", b7 = " ")
        b8 = b3[destination]
        print(destination, b7 = " ")
        while start != b8:
            print("-", b8, b7 = " ")
            b8 = b3[b8]
        print('-', start)
    def fonk6(self, max_cities, connectivity_percentage):
        for i in range(max_cities):
            b9 = range(0, i) + range(i + 1, max_cities)
            b10 = random.sample(b9, round(max_cities * connectivity_percentage))
            for b6 in b10:
                self.fonk2(str(i + 1), str(b6 + 1))
                self.fonk2(str(b6 + 1), str(i + 1))
if b11 = = "__main__":
    b12 = class1()
    b12.fonk6(10, 0.3)
    b13 = '1'
    b14 = '10'
    print("Finding optimal route from", b13, "to", b14)
    b12.fonk4(b13, b14)