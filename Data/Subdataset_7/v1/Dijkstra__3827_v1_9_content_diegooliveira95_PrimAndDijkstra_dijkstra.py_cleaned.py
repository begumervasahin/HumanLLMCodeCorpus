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
        self.a1 = 0
    def fonk11(self):
        return iter(self.b7.values())
    def fonk12(self, node):
        self.a1 += 1
        b8 = class1(node)
        self.b7[node] = b8
        return b8
    def fonk13(self, n):
        if n in self.b7:
            return self.b7[n]
        else:
            return None
    def fonk14(self, frm, to, b9 = 0):
        if frm not in self.b7:
            self.fonk12(frm)
        if to not in self.b7:
            self.fonk12(to)
        self.b7[frm].fonk2(self.b7[to], b9)
        self.b7[to].fonk2(self.b7[frm], b9)
def fonk15(v, b17):
    if v.b5:
        b17.append(v.b5.fonk4())
        fonk15(v.b5, b17)
    return
def fonk16(aGraph, start):
    start.fonk6(0)
    b10 = [(vertex.fonk7(), vertex) for vertex in aGraph]
    heapq.heapify(b10)
    while len(b10):
        b11 = heapq.heappop(b10)
        b12 = b11[1]
        b12.fonk9()
        for next_vertex in b12.fonk3():
            if next_vertex.b4:
                continue
            b13 = b12.fonk7() + b12.fonk5(next_vertex)
            if b13 < next_vertex.fonk7():
                next_vertex.fonk6(b13)
                next_vertex.fonk8(b12)
        while len(b10):
            heapq.heappop(b10)
        b10 = [(vertex.fonk7(), vertex) for vertex in aGraph if not vertex.b4]
        heapq.heapify(b10)
if b14 = = "__main__":
    b15 = class2()
    b15.fonk12('A')
    b15.fonk12('B')
    b15.fonk12('C')
    b15.fonk12('D')
    b15.fonk12('E')
    b15.fonk14('A', 'B', 1)
    b15.fonk14('A', 'C', 3)
    b15.fonk14('B', 'D', 2)
    b15.fonk14('C', 'D', 2)
    b15.fonk14('B', 'E', 4)
    b15.fonk14('D', 'E', 1)
    fonk16(b15, b15.fonk13('A'))
    b16 = b15.fonk13('E')
    b17 = [b16.fonk4()]
    fonk15(b16, b17)
    print(b17[::-1])
