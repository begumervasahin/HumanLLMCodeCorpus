def kruskal(graph):
    assert isinstance(graph, dict), "Input graph must be a dictionary"
    nodes = list(graph.keys())
    visited = set()
    minimum_spanning_tree = []
    while len(visited) < len(nodes):
        min_distance = float('inf')
        current_source = None
        current_destination = None
        for source in nodes:
            for destination in nodes:
                if source in visited and destination in visited or source == destination:
                    continue
                if graph[source][destination] < min_distance:
                    min_distance = graph[source][destination]
                    current_source = source
                    current_destination = destination
        minimum_spanning_tree.append((current_source, current_destination))
        visited.add(current_source)
        visited.add(current_destination)
    return minimum_spanning_tree
if __name__ == '__main__':
    graph_dict = {
        "s1": {"s1": 0, "s2": 6, "s10": 3, "s12": 4, "s5": 3},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 3, "s5": 4},
        "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
        "s12": {"s1": 1, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
        "s5": {"s1": 3, "s2": 5, "s10": 7, "s12": 4, "s5": 0},
    }
    minimum_spanning_tree = kruskal(graph_dict)
    print(minimum_spanning_tree)