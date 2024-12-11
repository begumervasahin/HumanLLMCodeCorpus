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
                elif b4[node] > b4[b6]:
                    b6 = node
        if b6 is None:
            break
        b1.remove(b6)
        b7 = b4[b6]
        for neighbor in graph.b2[b6]:
            b8 = b7 + graph.b3[(b6, neighbor)]
            if neighbor not in b4 or b8 > b4[neighbor]:
                b4[neighbor] = b8
                b5[neighbor] = b6
    return b4, b5