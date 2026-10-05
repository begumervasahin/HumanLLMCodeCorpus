def prim(graph, root):
    assert isinstance(graph, dict)
    nodes = list(graph.keys())
    nodes.remove(root)
    visited = [root]
    path = []
    next_node = None
    while nodes:
        distance = float('inf')
        for source in visited:
            for destination in graph[source]:
                if destination in visited or source == destination:
                    continue
                if graph[source][destination] < distance:
                    distance = graph[source][destination]
                    pre = source
                    next_node = destination
        path.append((pre, next_node))
        visited.append(next_node)
        nodes.remove(next_node)
    return path
if __name__ == '__main__':
    graph_dict = {
        "s1": {"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5": 3},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5": 2},
        "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
        "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
        "s5": {"s1": 3, "s2": 5, "s10": 2, "s12": 4, "s5": 0},
    }
    path = prim(graph_dict, 's12')
    print(path)