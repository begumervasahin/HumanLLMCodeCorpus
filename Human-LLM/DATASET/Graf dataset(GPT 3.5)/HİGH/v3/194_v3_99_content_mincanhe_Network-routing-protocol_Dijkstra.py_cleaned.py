import collections
class class1:
    def fonk1(self):
        self.b1 = set()
        self.b2 = collections.defaultdict(list)
        self.b3 = {}
    def fonk2(self, node):
        self.b1.add(node)
    def fonk3(self, from_node, to_node, distance):
        self.b2[from_node].append(to_node)
        self.b2[to_node].append(from_node)
        self.b3[(from_node, to_node)] = distance
        self.b3[(to_node, from_node)] = distance
def fonk4(b10, start_node):
    b4 = {start_node: 0}
    b5 = {}
    b6 = set(b10.b1)
    while b6:
        b7 = max(b6, key=lambda node: b4.get(node, float('-inf')))
        if b7 is None:
            break
        b6.remove(b7)
        b8 = b4[b7]
        for neighbor in b10.b2[b7]:
            b9 = b8 + b10.b3[(b7, neighbor)]
            if neighbor not in b4 or b9 > b4[neighbor]:
                b4[neighbor] = b9
                b5[neighbor] = b7
    return b4, b5
b10 = class1()
for i in range(5):
    b10.fonk2(i)
b10.fonk3(0, 1, 6)
b10.fonk3(0, 2, 1)
b10.fonk3(0, 3, 4)
b10.fonk3(1, 4, 3)
b10.fonk3(2, 1, -3)
b10.fonk3(2, 3, 2)
b10.fonk3(3, 4, -1)
b10.fonk3(4, 2, 5)
shortest_distances, b11 = fonk4(b10, 0)
print("Shortest b3 from start node 0 to all other b1:")
for node, distance in shortest_distances.items():
    print(f"{node} = {distance}")
print("Predecessors of b1 in the shortest paths:")
for node, predecessor in b11.items():
    print(f"{node} = {predecessor}")