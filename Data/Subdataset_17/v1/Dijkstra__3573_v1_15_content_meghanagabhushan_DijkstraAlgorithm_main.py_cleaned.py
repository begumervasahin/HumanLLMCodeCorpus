from dijkstra import Graph
graph = Graph()
def add_function():
    node1 = input("Enter node 1: ")
    node2 = input("Enter node 2: ")
    cost = input("Enter cost: ")
    graph.add_edge(node1, node2, int(cost))
    print(f"Edge added: {node1} -> {node2} with cost {cost}")
def remove_function():
    node1 = input("Enter node 1: ")
    node2 = input("Enter node 2: ")
    graph.remove_edge(node1, node2)
    print(f"Edge removed: {node1} -> {node2}")
def dijkstra_function():
    node1 = input("Enter start node: ")
    node2 = input("Enter end node: ")
    path, cost = graph.dijkstra(node1, node2)
    print(f"Shortest path from {node1} to {node2}: {path} with cost {cost}")
def view_graph():
    neighbors = graph.neighbours()
    print("Graph neighbors:")
    for node, neighbors_list in neighbors.items():
        print(f"{node}: {neighbors_list}")
def switch_demo(argument):
    switcher = {
        "add": add_function,
        "remove": remove_function,
        "dijkstra": dijkstra_function,
        "view": view_graph,
    }
    func = switcher.get(argument, None)
    if func:
        func()
    else:
        print("Invalid argument")
if __name__ == "__main__":
    while True:
        arg = input("Enter one of the following commands: add, remove, dijkstra, view, or 'exit' to quit: ").strip().lower()
        if arg == 'exit':
            break
        switch_demo(arg)