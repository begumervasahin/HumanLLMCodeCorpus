class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, node_id):
        return self.b1.fonk7(node_id, [])
    def fonk3(self):
        for node, neighbors in self.b1.items():
            print(f"{node}: {neighbors}")
if b2 = = "__main__":
    b3 = class1()
    b3.b1 = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['A'],
        'D': ['E', 'A'],
        'E': ['B']
    }
    import collections
    class class2:
        def fonk4(self):
            self.b4 = collections.deque()
        def fonk5(self):
            return len(self.b4) == 0
        def fonk6(self, item):
            self.b4.append(item)
        def fonk7(self):
            return self.b4.popleft()
    def fonk8(graph, start_node):
        b5 = class2()
        b5.fonk6(start_node)
        b6 = {start_node: True}
        while not b5.fonk5():
            b7 = b5.fonk7()
            print("Visiting", b7)
            for neighbor_node in graph.fonk2(b7):
                if neighbor_node not in b6:
                    b5.fonk6(neighbor_node)
                    b6[neighbor_node] = True
    fonk8(b3, 'A')