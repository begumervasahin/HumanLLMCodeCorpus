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
def fonk4(b11, start):
    b3 = {node: float('inf') for node in b11.b1}
    b4 = {}
    b3[start] = 0
    b5 = set(b11.b1)
    while b5:
        b6 = min(b5, key=lambda node: b3[node])
        if b3[b6] == float('inf'):
            break
        b5.remove(b6)
        b7 = b3[b6]
        for neighbor in b11.b2[b6]:
            b8 = b11.b3[(b6, neighbor)]
            b9 = b7 + b8
            if b9 < b3[neighbor]:
                b3[neighbor] = b9
                b4[neighbor] = b6
    return b3, b4
if b10 = = '__main__':
    b11 = class1()
    b1 = [0, 1, 2, 3, 4]
    b2 = [
        (0, 1, 6),
        (0, 2, 1),
        (0, 3, 4),
        (1, 4, 3),
        (2, 1, -3),
        (2, 3, 2),
        (3, 4, -1),
        (4, 2, 5)
    ]
    for node in b1:
        b11.fonk2(node)
    for from_node, to_node, distance in b2:
        b11.fonk3(from_node, to_node, distance)
    b3, b4 = fonk4(b11, 0)
    print("Shortest b3 from start node 0 to all other b1:")
    for node, distance in b3.items():
        print(f"Node {node}: b12 = {distance}")
    print("\nPredecessors in the shortest paths from start node 0:")
    for node, predecessor in b4.items():
        print(f"Node {node}: b13 = {predecessor}")