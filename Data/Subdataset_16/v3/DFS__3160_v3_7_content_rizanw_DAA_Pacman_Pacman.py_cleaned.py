from Util.Algorithms import Algorithm
from Map.map import Map
def fonk1(b3, b4):
    print("Solution:")
    print(f"  DFS: {b3}")
    print(f"  BFS: {b4}")
def fonk2(b1, start, goal):
    if b1 = = '1':
        b2 = Map.graph1
    elif b1 = = '2':
        b2 = Map.b2
    else:
        raise ValueError("Invalid map b6")
    b3 = Algorithm.dfs(b2, start, goal)
    b4 = Algorithm.bfs(b2, start, goal)
    return b3, b4
def fonk3():
    print("== Pacman b5 = =")
    print("Select a map:")
    print(" 1. Simple 3x4 Map")
    print(" 2. Hard 6x6 Map")
    b6 = input("Enter your b6 (1 or 2): ").strip()
    if b6 = = '1':
        print("== Simple 3x4 Map b7 = =")
        b8 = (1, 1)
        b9 = (2, 3)
    elif b6 = = '2':
        print("== Hard 6x6 Map b7 = =")
        b8 = (1, 1)
        b9 = (6, 6)
    else:
        print("Invalid b6. Please select either '1' or '2'.")
        return
    print(f" - Start position: {b8}")
    print(f" - Dot objective: {b9}")
    b3, b4 = fonk2(b6, b8, b9)
    fonk1(b3, b4)
if b10 = = '__main__':
    fonk3()