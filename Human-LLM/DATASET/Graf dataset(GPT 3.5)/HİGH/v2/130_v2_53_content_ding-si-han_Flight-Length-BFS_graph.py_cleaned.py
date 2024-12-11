import random
from itertools import chain
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
        return
    def fonk6(self, max_cities, connectivity_percentage):
        for i in range(max_cities):
            b10 = chain(range(0, i), range(i + 1, max_cities))
            b11 = random.sample(list(b10), round(max_cities * connectivity_percentage))
            for neighbour in b11:
                self.fonk2(str(i + 1), str(neighbour + 1))
                self.fonk2(str(neighbour + 1), str(i + 1))
if b12 = = "__main__":
    b13 = class1()
    b13.fonk6(10, 0.3)
    b14 = '1'
    b15 = '10'
    print("Finding optimal route from", b14, "to", b15)
    b13.fonk4(b14, b15)