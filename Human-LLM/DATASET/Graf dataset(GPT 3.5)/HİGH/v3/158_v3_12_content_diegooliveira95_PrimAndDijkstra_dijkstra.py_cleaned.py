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
    def fonk6(self, b3):
        self.b3 = b3
    def fonk7(self):
        return self.b4
    def fonk8(self, b4):
        self.b4 = b4
    def fonk9(self):
        self.b5 = True
class class2:
    def fonk10(self):
        self.b7 = {}
    def fonk11(self, key):
        b8 = class1(key)
        self.b7[key] = b8
        return b8
    def fonk12(self, key):
        return self.b7.get(key)
    def fonk13(self, from_vertex, to_vertex, b6 = 0):
        if from_vertex not in self.b7:
            self.fonk11(from_vertex)
        if to_vertex not in self.b7:
            self.fonk11(to_vertex)
        self.b7[from_vertex].fonk2(self.b7[to_vertex], b6)
def fonk14(vertex, b15):
    if vertex.b4:
        b15.append(vertex.b4.fonk3())
        fonk14(vertex.b4, b15)
    return
def fonk15(b13, b14):
    b14.fonk6(0)
    b9 = [(vertex.fonk5(), vertex) for vertex in b13.b7.values()]
    heapq.heapify(b9)
    while b9:
        current_distance, b10 = heapq.heappop(b9)
        b10.fonk9()
        for next_vertex, b6 in b10.b2.items():
            if not next_vertex.b5:
                b11 = current_distance + b6
                if b11 < next_vertex.fonk5():
                    next_vertex.fonk6(b11)
                    next_vertex.fonk8(b10)
        b9 = [(vertex.fonk5(), vertex) for vertex in b13.b7.values() if not vertex.b5]
        heapq.heapify(b9)
if b12 = = "__main__":
    b13 = class2()
    b13.fonk13('A', 'B', 4)
    b13.fonk13('A', 'C', 2)
    b13.fonk13('B', 'C', 5)
    b13.fonk13('B', 'D', 10)
    b13.fonk13('C', 'D', 3)
    b13.fonk13('D', 'E', 7)
    b13.fonk13('E', 'F', 2)
    b13.fonk13('F', 'A', 6)
    b14 = b13.fonk12('A')
    fonk15(b13, b14)
    for vertex in b13.b7.values():
        b15 = []
        fonk14(vertex, b15)
        print(f"Shortest b15 to vertex {vertex.fonk3()}: {b15[::-1] + [vertex.fonk3()]} with b3 {vertex.fonk5()}")