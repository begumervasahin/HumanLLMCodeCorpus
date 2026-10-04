from collections import defaultdict
import socket
import time
def initialize(graph, source):
    distances = defaultdict(dict)
    for node in graph:
        for target in graph:
            distances[node][target] = float('Inf') if node != target else 0
    return distances
def relax():
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
            relax()
            port = 60000
            with socket.socket() as s:
                host = "127.0.0.1"
                s.bind((host, port))
                s.listen(5)
                print('Server listening...')
                time.sleep(1)
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    to_send = ""
                    for v in graph:
                        to_send += f"{v} {distances[u][v]}\n"
                    forward_table_u = f"{u} {to_send}"
                    conn.sendall(forward_table_u.encode('utf-8'))
    for u in graph:
        for v in graph[u]:
            assert distances[v] <= distances[u] + graph[u][v]
    return distances
def test(graph):
    source = 0
    distances = bellman_ford(graph, source)
    print("Distances from source:")
    for node in distances:
        print(f"Node {node}: {distances[node]}")
if __name__ == '__main__':
    graph = defaultdict(dict)
    with open('test') as f:
        lines = f.readlines()
        for i in range(1, int(lines[0]) + 1):
            gf = lines[i].split()
            for k in range(1, len(gf), 2):
                graph[i][int(gf[k])] = int(gf[k + 1])
    test(graph)