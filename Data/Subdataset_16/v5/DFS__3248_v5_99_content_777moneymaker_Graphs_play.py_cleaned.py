b1 = 'Milosz Chodkowski PUT'
from b2 import Graph
def fonk1(b2):
    print("Adjacency List:")
    for vertex, neighbors in b2.adj_list.items():
        print(f"Vertex {vertex}: {neighbors}")
    b2.dfs()
    print("DFS Path:", b2.path)
def fonk2():
    b2 = Graph(10)
    fonk1(b2)
if b3 = = "__main__":
    fonk2()