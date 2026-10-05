class BFS:
    def breadth_first_search(self, graph, source, terminal, family):
        seen = [False] * len(graph)
        queue = []
        queue.append(source)
        seen[source] = True
        while queue:
            vertex = queue.pop(0)
            for idx, value in enumerate(graph[vertex]):
                if value > 0 and not seen[idx]:
                    queue.append(idx)
                    seen[idx] = True
                    family[idx] = vertex
        if seen[terminal]:
            return True
        else:
            return False