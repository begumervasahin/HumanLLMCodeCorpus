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
def fonk4(graph, initial):
    b4 = {initial: 0}
    b5 = {}
    b1 = set(graph.b1)
    while b1:
        b6 = None
        for node in b1:
            if node in b4:
                if b6 is None:
                    b6 = node
                elif b4[node] < b4[b6]:
                    b6 = node
        if b6 is None:
            break
        b1.remove(b6)
        b7 = b4[b6]
        for neighbor in graph.b2[b6]:
            b8 = b7 + graph.b3[(b6, neighbor)]
            if neighbor not in b4 or b8 < b4[neighbor]:
                b4[neighbor] = b8
                b5[neighbor] = b6
    return b4, b5
if b9 = = '__main__':
    b10 = class1()
    b10.fonk2(0)
    b10.fonk2(1)
    b10.fonk2(2)
    b10.fonk2(3)
    b10.fonk2(4)
    b10.fonk3(0, 1, 6)
    b10.fonk3(0, 2, 1)
    b10.fonk3(0, 3, 4)
    b10.fonk3(1, 4, 3)
    b10.fonk3(2, 1, -3)
    b10.fonk3(2, 3, 2)
    b10.fonk3(3, 4, -1)
    b10.fonk3(4, 2, 5)
    b3, b11 = fonk4(b10, 0)
    print("Shortest b3 from start node 0 to all other b1:")
    for node, distance in b3.items():
        print(f"Node {node}: b12 = {distance}")
    print("\nPredecessors in the shortest paths from start node 0:")
    for node, predecessor in b11.items():
        print(f"Node {node}: b13 = {predecessor}")