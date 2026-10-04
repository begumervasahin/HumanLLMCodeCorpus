import collections
class class1:
    def fonk1(self):
        self.b1 = set()
        self.b2 = collections.defaultdict(list)
        self.b3 = {}
    def fonk2(self, value):
        self.b1.add(value)
    def fonk3(self, from_node, to_node, distance):
        self.b2[from_node].append(to_node)
        self.b2[to_node].append(from_node)
        self.b3[(from_node, to_node)] = distance
        self.b3[(to_node, from_node)] = distance
def fonk4(graph, start):
    b3 = {node: float('inf') for node in graph.b1}
    b4 = {}
    b3[start] = 0
    b5 = set(graph.b1)
    while b5:
        b6 = min(b5, key=lambda node: b3.get(node, float('inf')))
        if b3[b6] == float('inf'):
            break
        b5.remove(b6)
        b7 = b3[b6]
        for neighbor in graph.b2[b6]:
            b8 = graph.b3[(b6, neighbor)]
            b9 = b7 + b8
            if b9 < b3[neighbor]:
                b3[neighbor] = b9
                b4[neighbor] = b6
    return b3, b4
if b10 = = '__main__':
    b11 = class1()
    b11.fonk2(0)
    b11.fonk2(1)
    b11.fonk2(2)
    b11.fonk2(3)
    b11.fonk2(4)
    b11.fonk3(0, 1, 6)
    b11.fonk3(0, 2, 1)
    b11.fonk3(0, 3, 4)
    b11.fonk3(1, 4, 3)
    b11.fonk3(2, 1, -3)
    b11.fonk3(2, 3, 2)
    b11.fonk3(3, 4, -1)
    b11.fonk3(4, 2, 5)
    b3, b4 = fonk4(b11, 0)
    print("Shortest b3 from start node 0 to all other b1:")
    for node, distance in b3.items():
        print(f"Node {node}: b12 = {distance}")
    print("\nPredecessors in the shortest paths from start node 0:")
    for node, predecessor in b4.items():
        print(f"Node {node}: b13 = {predecessor}")