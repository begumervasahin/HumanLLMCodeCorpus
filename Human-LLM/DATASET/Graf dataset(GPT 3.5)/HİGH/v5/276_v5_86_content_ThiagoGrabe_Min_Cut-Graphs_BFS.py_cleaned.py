class class1:
    def fonk1(self, graph, source, terminal, family):
        b1 = [False] * len(graph)
        b2 = []
        b2.append(source)
        b1[source] = True
        while b2:
            b3 = b2.pop(0)
            for neighbor_idx, edge_weight in enumerate(graph[b3]):
                if edge_weight > 0 and not b1[neighbor_idx]:
                    b2.append(neighbor_idx)
                    b1[neighbor_idx] = True
                    family[neighbor_idx] = b3
        if b1[terminal]:
            return True
        else:
            return False