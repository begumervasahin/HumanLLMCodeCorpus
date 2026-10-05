class BFS:
    def breadth_first_search(self, graph, source, terminal, family):
        visited = [False] * len(graph)
        queue = []
        queue.append(source)
        visited[source] = True
        while queue:
            current_vertex = queue.pop(0)
            for neighbor_idx, edge_weight in enumerate(graph[current_vertex]):
                if edge_weight > 0 and not visited[neighbor_idx]:
                    queue.append(neighbor_idx)
                    visited[neighbor_idx] = True
                    family[neighbor_idx] = current_vertex
        if visited[terminal]:
            return True
        else:
            return False