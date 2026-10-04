class class1:
    def fonk1(self, edgelist, nodecount):
        edgelist.sort(b1 = lambda edge: edge.weight)
        b2 = []
        b3 = []
        def fonk2(vertex):
            for index, subset in enumerate(b3):
                if vertex in subset:
                    return index
            return -1
        for edge in edgelist:
            b4 = fonk2(edge.Vertex1)
            b5 = fonk2(edge.Vertex2)
            if b4 = = b5 and b4 != -1:
                continue
            elif b4 = = -1 and b5 == -1:
                b3.append({edge.Vertex1, edge.Vertex2})
            elif b4 != -1 and b5 = = -1:
                b3 = b4.add(edge.Vertex2)
            elif b4 = = -1 and b5 != -1:
                b3[b5].add(edge.Vertex1)
            else:
                b3[b4].update(b3[b5])
                b3.pop(b5)
            edge.b6 = True
            b2.append(edge)
        return b2