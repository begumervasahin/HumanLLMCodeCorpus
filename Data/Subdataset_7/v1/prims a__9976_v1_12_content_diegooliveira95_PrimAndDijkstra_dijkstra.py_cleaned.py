import heapq
class class1:
    def fonk1(self, key):
        self.b1 = key
        self.b2 = {}
        self.b3 = float('inf')
        self.b4 = None
        self.b5 = False
    def fonk2(self, neighbor, b6 = 0):
        self.b2[neighbor] = b6
    def fonk3(self):
        return self.b1
    def fonk4(self, neighbor):
        return self.b2[neighbor]
    def fonk5(self):
        return self.b3
    def fonk6(self, dist):
        self.b3 = dist
    def fonk7(self):
        return self.b4
    def fonk8(self, prev):
        self.b4 = prev
    def fonk9(self):
        self.b5 = True
class class2:
    def fonk10(self):
        self.b7 = {}
        self.a1 = 0
    def fonk11(self, key):
        self.a1 += 1
        b8 = class1(key)
        self.b7[key] = b8
        return b8
    def fonk12(self, key):
        if key in self.b7:
            return self.b7[key]
        else:
            return None
    def fonk13(self, key):
        return key in self.b7
    def fonk14(self, f, t, b9 = 0):
        if f not in self.b7:
            self.fonk11(f)
        if t not in self.b7:
            self.fonk11(t)
        self.b7[f].fonk2(self.b7[t], b9)
def fonk15(v, b17):
    if v.b4:
        b17.append(v.b4.fonk3())
        fonk15(v.b4, b17)
    return
def fonk16(aGraph, start):
    start.fonk6(0)
    b10 = [(vertex.fonk5(), vertex) for vertex in aGraph.b7.values()]
    heapq.heapify(b10)
    while len(b10):
        b11 = heapq.heappop(b10)
        b12 = b11[1]
        b12.fonk9()
        for nextVertex, b6 in b12.b2.items():
            if not nextVertex.b5:
                b13 = b12.fonk5() + b6
                if b13 < nextVertex.fonk5():
                    nextVertex.fonk6(b13)
                    nextVertex.fonk8(b12)
        b10 = [(vertex.fonk5(), vertex) for vertex in aGraph.b7.values() if not vertex.b5]
        heapq.heapify(b10)
if b14 = = "__main__":
    b15 = class2()
    b15.fonk14('A', 'B', 4)
    b15.fonk14('A', 'C', 2)
    b15.fonk14('B', 'C', 5)
    b15.fonk14('B', 'D', 10)
    b15.fonk14('C', 'D', 3)
    b15.fonk14('D', 'E', 7)
    b15.fonk14('E', 'F', 2)
    b15.fonk14('F', 'A', 6)
    b16 = b15.fonk12('A')
    fonk16(b15, b16)
    for v in b15.b7.values():
        b17 = []
        fonk15(v, b17)
        print("Shortest b17 to vertex", v.fonk3(), ":", b17[::-1] + [v.fonk3()], "with b3", v.fonk5())