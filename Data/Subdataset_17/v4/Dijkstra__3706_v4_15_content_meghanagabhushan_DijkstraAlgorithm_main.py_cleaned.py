from dijkstra import Graph
graph = Graph()
def add_function():
    node1 = input("Enter the start node: ")
    node2 = input("Enter the end node: ")
    cost = input("Enter the cost: ")
    graph.add_edge(node1, node2, int(cost))
    print(f"Edge added: {node1} -> {node2} with cost {cost}")
def remove_function():
    node1 = input("Enter the start node: ")
    node2 = input("Enter the end node: ")
    graph.remove_edge(node1, node2)
    print(f"Edge removed: {node1} -> {node2}")
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
        "add": add_function,
        "remove": remove_function,
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