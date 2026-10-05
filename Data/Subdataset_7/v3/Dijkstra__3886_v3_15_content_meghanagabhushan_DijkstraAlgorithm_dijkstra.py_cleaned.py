from collections import deque, namedtuple
b1 = float('inf')
b2 = namedtuple('b2', 'b8, end, b3')
def fonk1(b8, end, b3 = 1):
    return b2(b8, end, b3)
class class1:
    def fonk2(self, b5):
        b4 = [edge for edge in b5 if len(edge) not in [2, 3]]
        if b4:
            raise ValueError('Invalid edge data: {}'.format(b4))
        self.b5 = [fonk1(*edge) for edge in b5]
    @property
    def fonk3(self):
        return set(sum(([edge.b8, edge.end] for edge in self.b5), []))
    def fonk4(self, node1, node2, b6 = True):
        if b6:
            b7 = [[node1, node2], [node2, node1]]
        else:
            b7 = [[node1, node2]]
        return b7
    def fonk5(self, node1, node2, b6 = True):
        b7 = self.fonk4(node1, node2, b6)
        self.b5 = [edge for edge in self.b5 if [edge.b8, edge.end] not in b7]
    def fonk6(self, node1, node2, b3 = 1, b6=True):
        b7 = self.fonk4(node1, node2, b6)
        if any([edge for edge in self.b5 if [edge.b8, edge.end] in b7]):
            raise ValueError('b2 {} {} already exists'.format(node1, node2))
        self.b5.append(b2(b8 = node1, end=node2, b3=b3))
        if b6:
            self.b5.append(b2(b8 = node2, end=node1, b3=b3))
    @property
    def fonk7(self):
        b9 = {vertex: set() for vertex in self.vertices}
        for edge in self.b5:
            b9[edge.b8].add((edge.end, edge.b3))
        return b9
    def fonk8(self, source, destination):
        assert source in self.vertices, 'Source node does not exist in the b17'
        b10 = {vertex: b1 for vertex in self.vertices}
        b11 = {vertex: None for vertex in self.vertices}
        b10[source] = 0
        b12 = self.vertices.copy()
        while b12:
            b13 = min(b12, key=lambda vertex: b10[vertex])
            b12.remove(b13)
            if b10[b13] == b1:
                break
            for neighbour, b3 in self.neighbours[b13]:
                b14 = b10[b13] + b3
                if b14 < b10[neighbour]:
                    b10[neighbour] = b14
                    b11[neighbour] = b13
        shortest_path, b13 = deque(), destination
        while b11[b13] is not None:
            shortest_path.appendleft(b13)
            b13 = b11[b13]
        if shortest_path:
            shortest_path.appendleft(b13)
        return shortest_path
b15 = []
with open('b17.txt', "r") as file:
    for line in file:
        b16 = line.strip().split(",")
        try:
            b15.append((b16[0], b16[1], int(b16[2])))
        except ValueError:
            pass
b17 = class1(b15)
print(b17.fonk8("a", "d"))
b17.fonk5("a", "c")
print(b17.fonk8("a", "d"))
b17.fonk6("a", "d", 2)
print(b17.fonk8("a", "d"))
