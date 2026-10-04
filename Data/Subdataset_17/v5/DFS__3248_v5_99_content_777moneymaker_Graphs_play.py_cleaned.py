__author__ = 'Milosz Chodkowski PUT'
from graph import Graph
def display_graph_info(graph):
    print("Adjacency List:")
    for vertex, neighbors in graph.adj_list.items():
        print(f"Vertex {vertex}: {neighbors}")
    graph.dfs()
    print("DFS Path:", graph.path)
def main():
    graph = Graph(10)
    display_graph_info(graph)
if __name__ == "__main__":
    main()