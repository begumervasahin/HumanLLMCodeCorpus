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
        return self.b7.get(key)
    def fonk13(self, f, t, b9 = 0):
        if f not in self.b7:
            self.fonk11(f)
        if t not in self.b7:
            self.fonk11(t)
        self.b7[f].fonk2(self.b7[t], b9)
def fonk14(vertex, b16):
    if vertex.b4:
        b16.append(vertex.b4.fonk3())
        fonk14(vertex.b4, b16)
    return
def fonk15(b14, start):
    start.fonk6(0)
    b10 = [(vertex.fonk5(), vertex) for vertex in b14.b7.values()]
    heapq.heapify(b10)
    while b10:
        current_distance, b11 = heapq.heappop(b10)
        b11.fonk9()
        for next_vertex, b6 in b11.b2.items():
            if not next_vertex.b5:
                b12 = current_distance + b6
                if b12 < next_vertex.fonk5():
                    next_vertex.fonk6(b12)
                    next_vertex.fonk8(b11)
        b10 = [(vertex.fonk5(), vertex) for vertex in b14.b7.values() if not vertex.b5]
        heapq.heapify(b10)
if b13 = = "__main__":
    b14 = class2()
    b14.fonk13('A', 'B', 4)
    b14.fonk13('A', 'C', 2)
    b14.fonk13('B', 'C', 5)
    b14.fonk13('B', 'D', 10)
    b14.fonk13('C', 'D', 3)
    b14.fonk13('D', 'E', 7)
    b14.fonk13('E', 'F', 2)
    b14.fonk13('F', 'A', 6)
    b15 = b14.fonk12('A')
    fonk15(b14, b15)
    for vertex in b14.b7.values():
        b16 = []
        fonk14(vertex, b16)
        print("Shortest b16 to vertex", vertex.fonk3(), ":", b16[::-1] + [vertex.fonk3()], "with b3", vertex.fonk5())