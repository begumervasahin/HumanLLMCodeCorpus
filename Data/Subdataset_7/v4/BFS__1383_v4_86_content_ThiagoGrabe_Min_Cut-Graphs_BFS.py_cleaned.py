class class1:
    def fonk1(self, graph, source, terminal, family):
        b1 = [False] * len(graph)
        b2 = []
        b2.append(source)
        b1[source] = True
        while b2:
            b3 = b2.pop(0)
            for idx, value in enumerate(graph[b3]):
                if value > 0 and not b1[idx]:
                    b2.append(idx)
                    b1[idx] = True
                    family[idx] = b3
        if b1[terminal]:
            return True
        else:
            return False