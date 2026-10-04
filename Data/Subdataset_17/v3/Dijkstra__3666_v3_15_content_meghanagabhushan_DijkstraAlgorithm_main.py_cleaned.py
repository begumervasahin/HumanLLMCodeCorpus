from dijkstra import Graph
graph = Graph()
def add_edge():
    start_node = input("Enter the start node: ")
    end_node = input("Enter the end node: ")
    cost = input("Enter the cost: ")
    graph.add_edge(start_node, end_node, int(cost))
    print(f"Edge added: {start_node} -> {end_node} with cost {cost}")
def remove_edge():
    start_node = input("Enter the start node: ")
    end_node = input("Enter the end node: ")
    graph.remove_edge(start_node, end_node)
    print(f"Edge removed: {start_node} -> {end_node}")
def run_dijkstra():
    start_node = input("Enter the start node: ")
    end_node = input("Enter the end node: ")
    path, cost = graph.dijkstra(start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {path} with cost {cost}")
def view_graph():
    neighbors = graph.neighbours()
    print("Graph neighbors:")
    for node, neighbors_list in neighbors.items():
        print(f"{node}: {neighbors_list}")
def execute_command(command):
    commands = {
        "add": add_edge,
        "remove": remove_edge,
        "dijkstra": run_dijkstra,
        "view": view_graph,
    }
    func = commands.get(command)
    if func:
        func()
    else:
        print("Invalid command")
def main():
    while True:
        command = input("Enter a command (add, remove, dijkstra, view) or 'exit' to quit: ").strip().lower()
        if command == 'exit':
            break
        execute_command(command)
if __name__ == "__main__":
    main()