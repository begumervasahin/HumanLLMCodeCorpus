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
def fonk4(b10, start_node):
    b4 = {start_node: 0}
    b5 = {}
    b1 = set(b10.b1)
    while b1:
        b6 = None
        for node in b1:
            if node in b4:
                if b6 is None or b4[node] < b4[b6]:
                    b6 = node
        if b6 is None:
            break
        b1.remove(b6)
        b7 = b4[b6]
        for neighbor in b10.b2[b6]:
            b8 = b7 + b10.b3[(b6, neighbor)]
            if neighbor not in b4 or b8 < b4[neighbor]:
                b4[neighbor] = b8
                b5[neighbor] = b6
    return b4, b5
if b9 = = '__main__':
    b10 = class1()
    for node in ['A', 'B', 'C', 'D', 'E']:
        b10.fonk2(node)
    b2 = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 6),
        ('C', 'D', 4),
        ('C', 'E', 2),
        ('D', 'E', 1)
    ]
    for edge in b2:
        b10.fonk3(*edge)
    b4, b5 = fonk4(b10, 'A')
    print("Visited Nodes and Distances:", b4)
    print("Paths:", b5)