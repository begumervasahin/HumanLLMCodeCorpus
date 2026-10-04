edges2 = {
    "v_start": {"1_start": 0, "2_start": 0},
    "1_start": {"1_finish": 40},
    "2_start": {"2_finish": 36},
    "1_finish": {"v_finish": 0},
    "2_finish": {"v_finish": 0, "1_start": 0}
}
def connections(v_start):
    return edges2.get(v_start, {})
def weight(start, finish):
    return edges2.get(start, {}).get(finish, None)
def LongestPath(edges2, Ppaths):
    for i in range(len(Ppaths)):
        current_path = Ppaths[i]
        for j in connections(current_path[-1]):
            new_path = current_path + [j]
            Ppaths.append(new_path)
    print(Ppaths)
def ShortestPath(edges2):
    Ppaths = []
    Pweights = []
    for key, value in edges2['v_start'].items():
        Ppaths.append(['v_start', key])
        Pweights.append(value)
    i = 0
    while i < len(Ppaths):
        path = Ppaths[i]
        path_end = path[-1]
        connections_dict = connections(path_end)
        if len(connections_dict) == 1:
            next_node = next(iter(connections_dict))
            path.append(next_node)
            Pweights.append(connections_dict[next_node])
        elif len(connections_dict) > 1:
            for key in connections_dict:
                new_path = path + [key]
                Ppaths.append(new_path)
        i += 1
    return Ppaths, Pweights
if __name__ == '__main__':
    initial_paths = [['v_start']]
    LongestPath(edges2, initial_paths)
    paths, weights = ShortestPath(edges2)
    print("Paths:", paths)
    print("Weights:", weights)