import math
import heapq
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {v: math.inf for v in b2.vertices}
        self.b3[b1] = 0
        self.b4 = {v: [] for v in b2.vertices}
    def fonk2(self, vertex, edge, new_distance):
        self.b3[vertex] = new_distance
        if new_distance < self.b3[vertex]:
            self.b4[vertex] = [edge]
        else:
            self.b4[vertex].append(edge)
    def fonk3(self, destination, edge):
        if edge in self.b4[destination]:
            return True
        return any(self.fonk3(e.source, edge)
                   for e in self.b4[destination])
    def fonk4(self, b5 = None):
        b5 = b5 or self.b2.vertices
        return sum(self.b3[v] for v in b5)
def fonk5(b2, b1):
    b6 = class1(b2, b1)
    b7 = [(0, b1)]
    while b7:
        current_distance, b8 = heapq.heappop(b7)
        for edge in b2.incident_edges[b8]:
            b9 = edge.target
            b10 = current_distance + edge.weight
            if b10 < b6.b3[b9]:
                b6.fonk2(b9, edge, b10)
                heapq.heappush(b7, (b10, b9))
            elif b10 = = b6.b3[b9]:
                b6.fonk2(b9, edge, b10)
    return b6