class BFS:
    def bfs(self, graph, source, terminal, parent):
        visited = [False] * len(graph)
        queue = []
        queue.append(source)
        visited[source] = True
        while queue:
            current_vertex = queue.pop(0)
            for idx, capacity in enumerate(graph[current_vertex]):
                if capacity > 0 and not visited[idx]:
                    queue.append(idx)
                    visited[idx] = True
                    parent[idx] = current_vertex
        return visited[terminal]
if __name__ == "__main__":
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    source = 0
    terminal = 5
    parent = [-1] * len(graph)
    bfs_instance = BFS()
    if bfs_instance.bfs(graph, source, terminal, parent):
        print("There is a path from source to terminal")
    else:
        print("No path from source to terminal")