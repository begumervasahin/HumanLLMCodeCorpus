class class1:
    def fonk1(self, edges, node_count):
        edges.sort(b1 = lambda edge: edge.weight)
        b2 = set()
        b3 = set()
        b4 = edges[0]
        b2.add(b4)
        b3.update({b4.vertex1, b4.vertex2})
        while len(b2) < node_count - 1:
            for edge in edges:
                if (edge.vertex1 in b3) != (edge.vertex2 in b3):
                    b2.add(edge)
                    b3.update({edge.vertex1, edge.vertex2})
                    break
        return b2
    @staticmethod
    def fonk2(edge):
        return edge.weight