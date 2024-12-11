import heapq
class class1:
    def fonk1(self, node):
        self.b1 = node
        self.b2 = {}
        self.b3 = float("inf")
        self.b4 = False
        self.b5 = None
    def fonk2(self, neighbor, b6 = 0):
        self.b2[neighbor] = b6
    def fonk3(self):
        return self.b2.keys()
    def fonk4(self):
        return self.b1
    def fonk5(self, neighbor):
        return self.b2[neighbor]
    def fonk6(self, dist):
        self.b3 = dist
    def fonk7(self):
        return self.b3
    def fonk8(self, prev):
        self.b5 = prev
    def fonk9(self):
        self.b4 = True
class class2:
    def fonk10(self):
        self.b7 = {}
    def fonk11(self, node):
        self.b7[node] = class1(node)
    def fonk12(self, node):
        return self.b7.get(node)
    def fonk13(self, frm, to, b8 = 0):
        self.b7[frm].fonk2(self.b7[to], b8)
        self.b7[to].fonk2(self.b7[frm], b8)
def fonk14(vertex, path):
    if vertex.b5:
        path.append(vertex.b5.fonk4())
        fonk14(vertex.b5, path)
def fonk15(b13, start_vertex):
    start_vertex.fonk6(0)
    b9 = [(vertex.fonk7(), vertex) for vertex in b13.b7.values()]
    heapq.heapify(b9)
    while b9:
        current_distance, b10 = heapq.heappop(b9)
        if not b10.b4:
            b10.fonk9()
            for next_vertex in b10.fonk3():
                if not next_vertex.b4:
                    b11 = b10.fonk7() + b10.fonk5(next_vertex)
                    if b11 < next_vertex.fonk7():
                        next_vertex.fonk6(b11)
                        next_vertex.fonk8(b10)
        b9 = [(vertex.fonk7(), vertex) for vertex in b13.b7.values() if not vertex.b4]
        heapq.heapify(b9)
if b12 = = "__main__":
    b13 = class2()
    b13.fonk11('A')
    b13.fonk11('B')
    b13.fonk11('C')
    b13.fonk11('D')
    b13.fonk11('E')
    b13.fonk13('A', 'B', 1)
    b13.fonk13('A', 'C', 3)
    b13.fonk13('B', 'D', 2)
    b13.fonk13('C', 'D', 2)
    b13.fonk13('B', 'E', 4)
    b13.fonk13('D', 'E', 1)
    fonk15(b13, b13.fonk12('A'))
    b14 = b13.fonk12('E')
    b15 = [b14.fonk4()]
    fonk14(b14, b15)
    print(b15[::-1])
