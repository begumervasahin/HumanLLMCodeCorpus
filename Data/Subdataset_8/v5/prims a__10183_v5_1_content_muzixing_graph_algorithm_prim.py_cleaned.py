def prim(graph, root):
    assert isinstance(graph, dict), "The graph must be represented as a dictionary."
    remaining_nodes = set(graph.keys()) - {root}
    visited_nodes = {root}
    minimum_spanning_tree = []
    while remaining_nodes:
        min_distance = float('inf')
        next_node = None
        for current_node in visited_nodes:
            for neighbor, weight in graph[current_node].items():
                if neighbor in visited_nodes or current_node == neighbor:
                    continue
                if weight < min_distance:
                    min_distance = weight
                    previous_node = current_node
                    next_node = neighbor
        minimum_spanning_tree.append((previous_node, next_node))
        visited_nodes.add(next_node)
        remaining_nodes.remove(next_node)
    return minimum_spanning_tree
if __name__ == '__main__':
    graph = {
        "s1": {"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5": 3},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5": 2},
        "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
        "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
        "s5": {"s1": 3, "s2": 5, "s10": 2, "s12": 4, "s5": 0},
    }
    minimum_spanning_tree = prim(graph, 's12')
    print(minimum_spanning_tree)