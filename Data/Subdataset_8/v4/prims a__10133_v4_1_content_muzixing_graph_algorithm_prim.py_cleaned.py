def prim(graph, root):
    assert isinstance(graph, dict), "The graph must be a dictionary."
    nodes = set(graph.keys()) - {root}
    visited = {root}
    path = []
    while nodes:
        distance = float('inf')
        next_node = None
        for current_node in visited:
            for neighbor, weight in graph[current_node].items():
                if neighbor in visited or current_node == neighbor:
                    continue
                if weight < distance:
                    distance = weight
                    previous = current_node
                    next_node = neighbor
        path.append((previous, next_node))
        visited.add(next_node)
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