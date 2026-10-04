def get_path(start, current_node, current_sum, path_sum, graph):
    if current_node in graph:
        for neighbor, weight in graph[current_node]:
            new_sum = current_sum + weight
            if path_sum[neighbor - 1] is None or new_sum < path_sum[neighbor - 1]:
                path_sum[neighbor - 1] = new_sum
                get_path(start, neighbor, new_sum, path_sum, graph)
    return path_sum
def main():
    times = [
        [3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85],
        [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75], [5, 1, 15],
        [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31],
        [1, 2, 0], [2, 5, 4], [4, 2, 51], [3, 1, 36], [2, 3, 59]
    ]
    N = 5
    K = 5
    graph = {}
    for u, v, w in times:
        if u in graph:
            graph[u].append((v, w))
        else:
            graph[u] = [(v, w)]
    path_sum = [None] * N
    path_sum[K - 1] = 0
    path_sum = get_path(K, K, 0, path_sum, graph)
    result = max(path_sum) if None not in path_sum else -1
    print(result)
if __name__ == "__main__":
    main()