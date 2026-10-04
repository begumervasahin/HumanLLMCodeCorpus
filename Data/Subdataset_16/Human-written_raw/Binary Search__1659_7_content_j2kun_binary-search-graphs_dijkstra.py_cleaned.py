import math
import heapq
'''
Dijkstra's algorithm with associated metadata to compute
all shortest paths
'''
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {b10: math.inf for b10 in b2.vertices}
        self.b3[b1] = 0
        self.b4 = {b10: [] for b10 in b2.vertices}
    def fonk2(self, vertex, edge, new_distance):
        self.b3[vertex] = new_distance
        if new_distance < self.b3[vertex]:
            self.b4[vertex] = [edge]
        else:
            self.b4[vertex].append(edge)
    def fonk3(self, destination, edge):
        b5 = self.b4[destination]
        if edge in b5:
            return True
        return any(self.fonk3(e.source, edge)
                   for e in b5)
    def fonk4(self, b6 = None):
        b6 = b6 or self.b2.vertices
        return sum(self.b3[x] for x in b6)
def fonk5(b2, b1):
    '''
    Compute the shortest paths and distances from the b1 vertex to all
    possible destination vertices. Return an instance of class1.
    '''
    b7 = class1(b2, b1)
    b8 = [(0, b1)]
    while len(b8) > 0:
        priority, b9 = heapq.heappop(b8)
        for incident_edge in b2.incident_edges[b9]:
            b10 = incident_edge.target
            b11 = incident_edge.b11
            b12 = b7.b3[b9] + b11
            if b12 <= b7.b3[b10]:
                b7.fonk2(b10, incident_edge, b12)
                heapq.heappush(b8, (b12, b10))
    return b7