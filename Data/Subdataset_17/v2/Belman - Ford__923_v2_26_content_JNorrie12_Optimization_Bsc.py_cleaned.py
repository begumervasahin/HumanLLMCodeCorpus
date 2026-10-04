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
    for i in Ppaths:
        for j in connections(i):
            Ppaths.append([i])
    print(Ppaths)
def ShortestPath(edges2):
    Ppaths = []
    Pweights = []
    for key, value in edges2['v_start'].items():
        Ppaths.append([key])
        Pweights.append(value)
    for path in Ppaths:
        path_end = path[-1]
        if len(edges2[path_end].keys()) == 1:
            path.extend(edges2[path_end].keys())
            Pweights.append(edges2[path_end][list(edges2[path_end].keys())[0]])
        elif len(edges2[path_end].keys()) > 1:
            for key in edges2[path_end].keys():
                new_path = path.copy()
                new_path.append(key)
                Ppaths.append(new_path)
    return Ppaths, Pweights
if __name__ == '__main__':
    initial_paths = ['v_start']
    LongestPath(edges2, initial_paths)
    paths, weights = ShortestPath(edges2)
    print("Paths:", paths)
    print("Weights:", weights)