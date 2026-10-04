from Util.Algorithms import Algorithm
from Map.map import Map
def fonk1(dfs, bfs):
    print("Solution: ")
    print(f"\tDFS: {dfs}")
    print(f"\tBFS: {bfs}")
def fonk2():
    print("== Pacman b1 = =")
    print("Select a map: ")
    print(" 1. Simple 3x4 Map")
    print(" 2. Hard 6x6 Map")
    b2 = input("Enter your b2: ")
    if b2 = = '1':
        print("== Simple 3x4 Map b3 = =")
        print(" - Start b4 = (1, 1)")
        print(" - Dot b5 = (2, 3)")
        b6 = Algorithm.dfs(Map.graph1, (1, 1), (2, 3))
        b7 = Algorithm.bfs(Map.graph1, (1, 1), (2, 3))
        fonk1(b6, b7)
    elif b2 = = '2':
        print("== Hard 6x6 Map b3 = =")
        print(" - Start b4 = (1, 1)")
        print(" - Dot b5 = (6, 6)")
        b6 = Algorithm.dfs(Map.graph, (1, 1), (6, 6))
        b7 = Algorithm.bfs(Map.graph, (1, 1), (6, 6))
        fonk1(b6, b7)
    else:
        print("Invalid input. Please select either '1' or '2'.")
if b8 = = '__main__':
    fonk2()