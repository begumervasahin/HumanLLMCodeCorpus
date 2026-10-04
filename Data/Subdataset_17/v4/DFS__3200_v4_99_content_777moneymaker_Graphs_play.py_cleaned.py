__author__ = 'Milosz Chodkowski PUT'
from graph import Graph
def main():
    graph = Graph(10)
    print("Adjacency List:", graph.adj_list)
    graph.dfs()
    print("DFS Path:", graph.path)
if __name__ == "__main__":
    main()