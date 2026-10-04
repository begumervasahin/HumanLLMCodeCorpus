from Util.Algorithms import Algorithm
from Map.map import Map
def fonk1(b7, b8):
    print("Solution:")
    print(f"  DFS: {b7}")
    print(f"  BFS: {b8}")
def fonk2():
    print("== Pacman b1 = =")
    print("Select a map:")
    print(" 1. Simple 3x4 Map")
    print(" 2. Hard 6x6 Map")
    b2 = input("Enter your b2 (1 or 2): ").strip()
    if b2 = = '1':
        print("== Simple 3x4 Map b3 = =")
        print(" - Start position: (1, 1)")
        print(" - Dot objective: (2, 3)")
        b4 = (1, 1)
        b5 = (2, 3)
        b6 = Map.graph1
    elif b2 = = '2':
        print("== Hard 6x6 Map b3 = =")
        print(" - Start position: (1, 1)")
        print(" - Dot objective: (6, 6)")
        b4 = (1, 1)
        b5 = (6, 6)
        b6 = Map.b6
    else:
        print("Invalid input. Please select either '1' or '2'.")
        return
    b7 = Algorithm.dfs(b6, b4, b5)
    b8 = Algorithm.bfs(b6, b4, b5)
    fonk1(b7, b8)
if b9 = = '__main__':
    fonk2()