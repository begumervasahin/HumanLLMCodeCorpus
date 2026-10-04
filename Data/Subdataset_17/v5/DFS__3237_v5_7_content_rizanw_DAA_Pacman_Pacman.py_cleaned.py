from Util.Algorithms import Algorithm
from Map.map import Map
def print_solution(dfs_result, bfs_result):
    print("Solution:")
    print(f"  DFS: {dfs_result}")
    print(f"  BFS: {bfs_result}")
def get_map_details(choice):
    if choice == '1':
        return (1, 1), (2, 3), Map.graph1
    elif choice == '2':
        return (1, 1), (6, 6), Map.graph
    else:
        return None, None, None
def main():
    print("== Pacman Solver ==")
    print("Select a map:")
    print(" 1. Simple 3x4 Map")
    print(" 2. Hard 6x6 Map")
    choice = input("Enter your choice (1 or 2): ").strip()
    start, goal, graph = get_map_details(choice)
    if graph is None:
        print("Invalid input. Please select either '1' or '2'.")
        return
    dfs_result = Algorithm.dfs(graph, start, goal)
    bfs_result = Algorithm.bfs(graph, start, goal)
    print_solution(dfs_result, bfs_result)
if __name__ == '__main__':
    main()