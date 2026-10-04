from Util.Algorithms import Algorithm
from Map.map import Map
def print_solution(dfs_result, bfs_result):
    print("Solution:")
    print(f"  DFS: {dfs_result}")
    print(f"  BFS: {bfs_result}")
def main():
    print("== Pacman Solver ==")
    print("Please choose a map:")
    print(" 1. Simple 3x4 Map")
    print(" 2. Hard 6x6 Map")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("== Simple 3x4 Map selected ==")
        print(" - Start position: (1, 1)")
        print(" - Dot objective: (2, 3)")
        dfs_result = Algorithm.dfs(Map.graph1, (1, 1), (2, 3))
        bfs_result = Algorithm.bfs(Map.graph1, (1, 1), (2, 3))
        print_solution(dfs_result, bfs_result)
    elif choice == '2':
        print("== Hard 6x6 Map selected ==")
        print(" - Start position: (1, 1)")
        print(" - Dot objective: (6, 6)")
        dfs_result = Algorithm.dfs(Map.graph, (1, 1), (6, 6))
        bfs_result = Algorithm.bfs(Map.graph, (1, 1), (6, 6))
        print_solution(dfs_result, bfs_result)
    else:
        print("Invalid choice. Please select either '1' or '2'.")
if __name__ == '__main__':
    main()