from Util.Algorithms import Algorithm
from Map.map import Map
def fonk1(b4, b5):
    print("Solution:")
    print(f"  DFS: {b4}")
    print(f"  BFS: {b5}")
def fonk2(b1):
    if b1 = = '1':
        return (1, 1), (2, 3), Map.graph1
    elif b1 = = '2':
        return (1, 1), (6, 6), Map.b3
    else:
        return None, None, None
def fonk3():
    print("== Pacman b2 = =")
    print("Select a map:")
    print(" 1. Simple 3x4 Map")
    print(" 2. Hard 6x6 Map")
    b1 = input("Enter your b1 (1 or 2): ").strip()
    start, goal, b3 = fonk2(b1)
    if b3 is None:
        print("Invalid input. Please select either '1' or '2'.")
        return
    b4 = Algorithm.dfs(b3, start, goal)
    b5 = Algorithm.bfs(b3, start, goal)
    fonk1(b4, b5)
if b6 = = '__main__':
    fonk3()