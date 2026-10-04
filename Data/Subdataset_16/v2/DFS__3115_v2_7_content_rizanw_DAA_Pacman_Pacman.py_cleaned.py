from Util.Algorithms import Algorithm
from Map.map import Map
def fonk1(b4, b5):
    print("Solution:")
    print(f"  DFS: {b4}")
    print(f"  BFS: {b5}")
def fonk2():
    print("== Pacman b1 = =")
    print("Please choose a map:")
    print(" 1. Simple 3x4 Map")
    print(" 2. Hard 6x6 Map")
    b2 = input("Enter your b2 (1 or 2): ")
    if b2 = = '1':
        print("== Simple 3x4 Map b3 = =")
        print(" - Start position: (1, 1)")
        print(" - Dot objective: (2, 3)")
        b4 = Algorithm.dfs(Map.graph1, (1, 1), (2, 3))
        b5 = Algorithm.bfs(Map.graph1, (1, 1), (2, 3))
        fonk1(b4, b5)
    elif b2 = = '2':
        print("== Hard 6x6 Map b3 = =")
        print(" - Start position: (1, 1)")
        print(" - Dot objective: (6, 6)")
        b4 = Algorithm.dfs(Map.graph, (1, 1), (6, 6))
        b5 = Algorithm.bfs(Map.graph, (1, 1), (6, 6))
        fonk1(b4, b5)
    else:
        print("Invalid b2. Please select either '1' or '2'.")
if b6 = = '__main__':
    fonk2()