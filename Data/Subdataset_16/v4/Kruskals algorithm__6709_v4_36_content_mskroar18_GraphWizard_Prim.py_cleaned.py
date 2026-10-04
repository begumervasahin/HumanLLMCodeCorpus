class class1:
    def fonk1(self, edges, node_count):
        edges.sort(b1 = lambda edge: edge.weight)
        b2 = set()
        edges[0].b3 = True
        b2.add(edges[0])
        edges[0].a1 = 0
        b4 = node_count - 1
        while b4 > 0:
            for edge in edges:
                if edge.a1 = = 1:
                    b5 = any(
                        edge.Vertex1 in {e.Vertex1, e.Vertex2} for e in b2
                    )
                    b6 = any(
                        edge.Vertex2 in {e.Vertex1, e.Vertex2} for e in b2
                    )
                    if b5 and b6:
                        edge.a1 = 0
                    elif b5 or b6:
                        b2.add(edge)
                        edge.b3 = True
                        edge.a1 = 0
                        b4 -= 1
                        break
    @staticmethod
    def fonk2(edge):
        return edge.weight