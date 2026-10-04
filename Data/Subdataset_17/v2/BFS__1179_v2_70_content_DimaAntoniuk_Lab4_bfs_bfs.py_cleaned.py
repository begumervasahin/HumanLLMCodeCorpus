import queue
def max_value(a, b):
    return a if a >= b else b
def write_output(distance, farthest_node, parents):
    with open('output.txt', 'w') as output:
        output.write(f"{distance}\n")
        path = []
        node = farthest_node
        while node != -1:
            path.append(node + 1)
            node = parents[node]
        output.write(' '.join(map(str, path[::-1])))
def bfs(graph, start, total_nodes):
    q = queue.Queue()
    q.put(start)
    distances = [-1] * total_nodes
    visited = [False] * total_nodes
    parents = [None] * total_nodes
    distances[start] = 0
    visited[start] = True
    parents[start] = -1
    while not q.empty():
        current_node = q.get()
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[current_node] + 1
                parents[neighbor] = current_node
                q.put(neighbor)
    farthest_node = start
    for node in range(total_nodes):
        if distances[node] > distances[farthest_node]:
            farthest_node = node
    write_output(distances[farthest_node], farthest_node, parents)
def main():
    with open('input.txt', 'r') as input_file:
        edges, start_node = map(int, input_file.readline().split())
        start_node -= 1
        total_nodes = 0
        edge_list = []
        for _ in range(edges):
            from_node, to_node = map(int, input_file.readline().split())
            edge_list.append((from_node - 1, to_node - 1))
            total_nodes = max_value(total_nodes, max_value(from_node, to_node))
        total_nodes += 1
        graph = [[] for _ in range(total_nodes)]
        for from_node, to_node in edge_list:
            graph[from_node].append(to_node)
    bfs(graph, start_node, total_nodes)
if __name__ == "__main__":
    main()