import heapq
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = float('inf')
        self.b3 = None
        self.b4 = []
        self.b5 = False
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, b2):
        self.b2 = b2
    def fonk5(self):
        return self.b3
    def fonk6(self, b3):
        self.b3 = b3
    def fonk7(self, neighbor, weight):
        self.b4.append((neighbor, weight))
    def fonk8(self, neighbor):
        for b6, weight in self.b4:
            if b6 = = neighbor:
                return weight
        return float('inf')
    def fonk9(self):
        self.b5 = True
class class2:
    def fonk10(self):
        self.b7 = {}
    def fonk11(self, b17):
        self.b7[b17.fonk2()] = b17
    def fonk12(self, b1):
        return self.b7.get(b1)
    def fonk13(self, from_id, to_id, weight):
        b8 = self.fonk12(from_id)
        b9 = self.fonk12(to_id)
        if b8 and b9:
            b8.fonk7(b9, weight)
            b9.fonk7(b8, weight)
def fonk14(graph, start_id):
    b10 = graph.fonk12(start_id)
    b10.fonk4(0)
    b11 = [(b17.fonk3(), b17) for b17 in graph.b7.values()]
    heapq.heapify(b11)
    while b11:
        current_distance, b12 = heapq.heappop(b11)
        if b12.b5:
            continue
        b12.fonk9()
        for neighbor, weight in b12.b4:
            if neighbor.b5:
                continue
            b13 = b12.fonk3() + weight
            if b13 < neighbor.fonk3():
                neighbor.fonk4(b13)
                neighbor.fonk6(b12)
        b11 = [(b17.fonk3(), b17) for b17 in graph.b7.values() if not b17.b5]
        heapq.heapify(b11)
    b14 = {b17.fonk2(): b17.fonk3() for b17 in graph.b7.values()}
    b15 = {b17.fonk2(): b17.fonk5().fonk2() if b17.fonk5() else None for b17 in graph.b7.values()}
    return b14, b15
def fonk15(b17, b15, graph):
    b16 = []
    while b17:
        b16.append(b17.fonk2())
        b17 = graph.fonk12(b15.get(b17.fonk2()))
    b16.reverse()
    print(" -> ".join(map(str, b16)))