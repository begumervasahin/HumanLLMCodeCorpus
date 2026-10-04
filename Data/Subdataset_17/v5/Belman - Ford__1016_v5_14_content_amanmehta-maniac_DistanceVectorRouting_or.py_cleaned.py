from collections import defaultdict
import socket
import time
def initialize(graph, source):
    distances = {node: float('Inf') for node in graph}
    distances[source] = 0
    return distances
def simulate_relax():
    print("Relax called")
    with socket.socket() as s:
        host = "127.0.0.1"
        port = 60000
        s.connect((host, port))
        data = s.recv(1024)
        print(data.decode('utf-8'))
def bellman_ford(graph, source):
    distances = initialize(graph, source)
    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                weight = graph[u][v]
                if distances[u] != float('Inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
            simulate_relax()
            with socket.socket() as s:
                host = "127.0.0.1"
                port = 60000
                s.bind((host, port))
                s.listen(5)
                print('Server listening...')
                time.sleep(1)
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    to_send = "".join(f"{v} {distances[v]}\n" for v in graph)
                    forward_table_u = f"{u} {to_send}"
                    conn.sendall(forward_table_u.encode('utf-8'))
    for u in graph:
        for v in graph[u]:
            weight = graph[u][v]
            if distances[u] != float('Inf') and distances[u] + weight < distances[v]:
                print("Graph contains a negative weight cycle")
                return
    return distances
def test(graph):
    source = 0
    distances = bellman_ford(graph, source)
    print("Distances from source:")
    for node in distances:
        print(f"Node {node}: {distances[node]}")
def load_graph(filename):
    graph = defaultdict(dict)
    with open(filename) as f:
        lines = f.readlines()
        num_nodes = int(lines[0])
        for i in range(1, num_nodes + 1):
            gf = lines[i].split()
            node = int(gf[0])
            for k in range(1, len(gf), 2):
                graph[node][int(gf[k])] = int(gf[k + 1])
    return graph
if __name__ == '__main__':
    graph = load_graph('test')
    test(graph)