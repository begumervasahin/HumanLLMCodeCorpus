import networkx as nx
class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b1):
        b2 = nx.Graph()
        b3 = sorted(b1.edges(data=True), key=lambda x: x[2]['b6'])
        b4 = class2()
        for node in b1.nodes():
            b4.fonk5(node)
        for edge in b3:
            b6, u, b5 = edge[2]['b6'], edge[0], edge[1]
            if b4.fonk6(u) != b4.fonk6(b5):
                b4.fonk7(u, b5)
                b2.add_edge(u, b5, b6 = b6)
        return b2
    def fonk3(self, b2):
        return sum(b6 for u, b5, b6 in b2.edges.data('b6'))
class class2:
    def fonk4(self):
        self.b7 = {}
        self.b8 = {}
    def fonk5(self, x):
        self.b7[x] = x
        self.b8[x] = 0
    def fonk6(self, x):
        if self.b7[x] != x:
            self.b7[x] = self.fonk6(self.b7[x])
        return self.b7[x]
    def fonk7(self, x, y):
        b9 = self.fonk6(x)
        b10 = self.fonk6(y)
        if b9 != b10:
            if self.b8[b9] > self.b8[b10]:
                self.b7[b10] = b9
            else:
                self.b7[b9] = b10
                if self.b8[b9] == self.b8[b10]:
                    self.b8[b10] += 1
b1 = {
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
    ('A', 'B', {'b6': 1}),
    ('A', 'C', {'b6': 5}),
    ('A', 'D', {'b6': 3}),
    ('B', 'C', {'b6': 4}),
    ('B', 'D', {'b6': 2}),
    ('C', 'D', {'b6': 1}),
])
b13 = nx.Graph()
b13.add_nodes_from((['A', 'B', 'C', 'D']))
b13.add_edges_from([
    ('A', 'B', {'b6': 1}),
    ('B', 'D', {'b6': 2}),
    ('C', 'D', {'b6': 1}),
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
b2 = b15.fonk2(b14)
print(b2.edges)
print(b15.fonk3(b2))