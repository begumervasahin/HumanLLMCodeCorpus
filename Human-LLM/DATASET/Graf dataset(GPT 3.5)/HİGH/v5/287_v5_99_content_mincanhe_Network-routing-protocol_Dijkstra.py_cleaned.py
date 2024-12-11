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
def fonk4(graph, start_node):
    b4 = {start_node: 0}
    b5 = {}
    b6 = set(graph.b1)
    while b6:
        b7 = None
        for node in b6:
            if node in b4:
                if b7 is None or b4[node] > b4[b7]:
                    b7 = node
        if b7 is None:
            break
        b6.remove(b7)
        b8 = b4[b7]
        for neighbor in graph.b2[b7]:
            b9 = b8 + graph.b3[(b7, neighbor)]
            if neighbor not in b4 or b9 > b4[neighbor]:
                b4[neighbor] = b9
                b5[neighbor] = b7
    return b4, b5