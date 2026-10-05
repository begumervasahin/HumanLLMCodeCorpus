class BFS:
    def bfs(self, graph, source, terminal, family):
        seen = [False] * len(graph)
        fifo = []
        fifo.append(source)
        seen[source] = True
        while fifo:
            vertex = fifo.pop(0)
            for idx, value in enumerate(graph[vertex]):
                if value > 0 and not seen[idx]:
                    fifo.append(idx)
                    seen[idx] = True
                    family[idx] = vertex
        return seen[terminal]
class EdmondsKarp:
    def __init__(self, graph):
        self.graph = graph
    def max_flow(self, source, terminal):
        flow = 0
        family = [-1] * len(self.graph)
        bfs = BFS()
        while bfs.bfs(self.graph, source, terminal, family):
            path_flow = float("inf")
            s = terminal
            while s != source:
                path_flow = min(path_flow, self.graph[family[s]][s])
                s = family[s]
            flow += path_flow
            v = terminal
            while v != source:
                u = family[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = family[v]
        return flow
def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_vertices, num_edges = map(int, lines[0].split())
        graph = [[0] * num_vertices for _ in range(num_vertices)]
        for line in lines[1:]:
            u, v, weight = map(int, line.split())
            graph[u][v] = weight
            graph[v][u] = weight
        return graph
def write_output(output_file, cut_size, cut_set, max_flow):
    with open(output_file, 'w') as file:
        file.write(str(cut_size) + '\n')
        file.write(' '.join(map(str, cut_set)) + '\n')
        file.write(str(max_flow) + '\n')
def main(input_file, output_file):
    graph = parse_input(input_file)
    source = 0
    terminal = len(graph) - 1
    edmonds_karp = EdmondsKarp(graph)
    max_flow = edmonds_karp.max_flow(source, terminal)
    cut_size = sum(1 for flow in graph[source] if flow > 0)
    cut_set = [i for i, flow in enumerate(graph[source]) if flow > 0]
    write_output(output_file, cut_size, cut_set, max_flow)
if __name__ == "__main__":
    input_file = "mincut_input/XXXX.in"
    output_file = "output_file.txt"
    main(input_file, output_file)