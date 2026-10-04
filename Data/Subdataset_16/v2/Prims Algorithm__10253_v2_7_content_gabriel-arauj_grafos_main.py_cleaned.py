import networkx as nx
class class1:
    def fonk1(self):
        pass
    def fonk2(self, b10):
        b1 = nx.Graph()
        b2 = sorted(b10.edges(data=True), key=lambda x: x[2]['b5'])
        b3 = class2()
        for node in b10.nodes():
            b3.fonk5(node)
        for edge in b2:
            b5, u, b4 = edge[2]['b5'], edge[0], edge[1]
            if b3.fonk6(u) != b3.fonk6(b4):
                b3.fonk7(u, b4)
                b1.add_edge(u, b4, b5 = b5)
        return b1
    def fonk3(self, b1):
        return sum(b5 for _, _, b5 in b1.edges.data('b5'))
class class2:
    def fonk4(self):
        self.b6 = {}
        self.b7 = {}
    def fonk5(self, x):
        self.b6[x] = x
        self.b7[x] = 0
    def fonk6(self, x):
        if self.b6[x] != x:
            self.b6[x] = self.fonk6(self.b6[x])
        return self.b6[x]
    def fonk7(self, x, y):
        b8 = self.fonk6(x)
        b9 = self.fonk6(y)
        if b8 != b9:
            if self.b7[b8] > self.b7[b9]:
                self.b6[b9] = b8
            else:
                self.b6[b8] = b9
                if self.b7[b8] == self.b7[b9]:
                    self.b7[b9] += 1
b10 = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': set([
        (1, 'A', 'B'),
        (5, 'A', 'C'),
        (3, 'A', 'D'),
        (4, 'B', 'C'),
        (2, 'B', 'D'),
        (1, 'C', 'D'),
    ])
}
b11 = set([
    (1, 'A', 'B'),
    (2, 'B', 'D'),
    (1, 'C', 'D'),
])
b12 = nx.Graph()
b12.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
b12.add_edges_from([
    ('A', 'B', {'b5': 1}),
    ('A', 'C', {'b5': 5}),
    ('A', 'D', {'b5': 3}),
    ('B', 'C', {'b5': 4}),
    ('B', 'D', {'b5': 2}),
    ('C', 'D', {'b5': 1}),
])
b13 = nx.Graph()
b13.add_nodes_from(['A', 'B', 'C', 'D'])
b13.add_edges_from([
    ('A', 'B', {'b5': 1}),
    ('B', 'D', {'b5': 2}),
    ('C', 'D', {'b5': 1}),
])
b14 = nx.Graph()
b14.add_weighted_edges_from([
    (1, 2, 4),
    (1, 3, 8),
    (2, 3, 11),
    (2, 4, 8),
    (3, 6, 7),
    (3, 7, 1),
    (6, 4, 2),
    (6, 7, 20),
    (7, 8, 2),
    (4, 8, 4),
    (5, 8, 14),
    (5, 9, 9),
    (8, 9, 10),
    (4, 5, 7)
])
b15 = class1()
b1 = b15.fonk2(b14)
print(b1.edges)
print(b15.fonk3(b1))