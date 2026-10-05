def kruskal(graph):
    assert isinstance(graph, dict)
    nodes = list(graph.keys())
    visited = set()
    path = []
    while len(visited) < len(nodes):
        shortest_distance = float('inf')
        source_node = None
        destination_node = None
        for source in nodes:
            for destination in nodes:
                if source in visited and destination in visited or source == destination:
                    continue
                if graph[source][destination] < shortest_distance:
                    shortest_distance = graph[source][destination]
                    source_node = source
                    destination_node = destination
        path.append((source_node, destination_node))
        visited.add(source_node)
        visited.add(destination_node)
    return path
if __name__ == '__main__':
    graph_dict = {
        "s1": {"s1": 0, "s2": 6, "s10": 3, "s12": 4, "s5": 3},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 3, "s5": 4},
        "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
        "s12": {"s1": 1, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
        "s5": {"s1": 3, "s2": 5, "s10": 7, "s12": 4, "s5": 0},
    }
    min_spanning_tree = kruskal(graph_dict)
    print(min_spanning_tree)