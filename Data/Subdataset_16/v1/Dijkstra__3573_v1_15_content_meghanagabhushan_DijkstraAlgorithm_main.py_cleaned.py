from dijkstra import Graph
b1 = Graph()
def fonk1():
    b2 = input("Enter node 1: ")
    b3 = input("Enter node 2: ")
    b4 = input("Enter b4: ")
    b1.add_edge(b2, b3, int(b4))
    print(f"Edge added: {b2} -> {b3} with b4 {b4}")
def fonk2():
    b2 = input("Enter node 1: ")
    b3 = input("Enter node 2: ")
    b1.remove_edge(b2, b3)
    print(f"Edge removed: {b2} -> {b3}")
def fonk3():
    b2 = input("Enter start node: ")
    b3 = input("Enter end node: ")
    path, b4 = b1.dijkstra(b2, b3)
    print(f"Shortest path from {b2} to {b3}: {path} with b4 {b4}")
def fonk4():
    b5 = b1.neighbours()
    print("Graph b5:")
    for node, neighbors_list in b5.items():
        print(f"{node}: {neighbors_list}")
def fonk5(argument):
    b6 = {
        "add": add_function,
        "remove": remove_function,
        "dijkstra": dijkstra_function,
        "view": view_graph,
    }
    b7 = b6.get(argument, None)
    if b7:
        b7()
    else:
        print("Invalid argument")
if b8 = = "__main__":
    while True:
        b9 = input("Enter one of the following commands: add, remove, dijkstra, view, or 'exit' to quit: ").strip().lower()
        if b9 = = 'exit':
            break
        fonk5(b9)