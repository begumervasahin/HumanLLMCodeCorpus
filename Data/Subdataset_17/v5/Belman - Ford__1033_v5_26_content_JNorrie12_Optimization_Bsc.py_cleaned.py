edges2 = {
    "v_start": {"1_start": 0, "2_start": 0},
    "1_start": {"1_finish": 40},
    "2_start": {"2_finish": 36},
    "1_finish": {"v_finish": 0},
    "2_finish": {"v_finish": 0, "1_start": 0}
}
def connections(node):
    return edges2.get(node, {})
def weight(start, finish):
    return edges2.get(start, {}).get(finish, None)
def longest_path(edges2, initial_paths):
    for path in initial_paths:
        for connection in connections(path):
            initial_paths.append([path])
    print(initial_paths)
def shortest_path(edges2):
    paths = []
    weights = []
    for key, value in edges2['v_start'].items():
        paths.append([key])
        weights.append(value)
    for path in paths:
        path_end = path[-1]
        connections = edges2[path_end]
        if len(connections) == 1:
            next_node = list(connections.keys())[0]
            path.append(next_node)
            weights.append(connections[next_node])
        elif len(connections) > 1:
            for key in connections.keys():
                new_path = path.copy()
                new_path.append(key)
                paths.append(new_path)
    return paths, weights
if __name__ == '__main__':
    initial_paths = ['v_start']
    longest_path(edges2, initial_paths)
    paths, weights = shortest_path(edges2)
    print("Paths:", paths)
    print("Weights:", weights)