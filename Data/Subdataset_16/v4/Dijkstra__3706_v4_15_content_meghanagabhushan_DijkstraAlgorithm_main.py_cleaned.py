from dijkstra import Graph
b1 = Graph()
def fonk1():
    b2 = input("Enter the start node: ")
    b3 = input("Enter the end node: ")
    b4 = input("Enter the b4: ")
    b1.add_edge(b2, b3, int(b4))
    print(f"Edge added: {b2} -> {b3} with b4 {b4}")
def fonk2():
    b2 = input("Enter the start node: ")
    b3 = input("Enter the end node: ")
    b1.remove_edge(b2, b3)
    print(f"Edge removed: {b2} -> {b3}")
def fonk3():
    b5 = input("Enter the start node: ")
    b6 = input("Enter the end node: ")
    path, b4 = b1.dijkstra(b5, b6)
    print(f"Shortest path from {b5} to {b6}: {path} with b4 {b4}")
def fonk4():
    b7 = b1.neighbours()
    print("Graph b7:")
    for node, neighbors_list in b7.items():
        print(f"{node}: {neighbors_list}")
def fonk5(b10):
    b8 = {
        "add": add_function,
        "remove": remove_function,
        "dijkstra": run_dijkstra,
        "view": view_graph,
    }
    b9 = b8.get(b10)
    if b9:
        b9()
    else:
        print("Invalid b10")
def fonk6():
    while True:
        b10 = input("Enter a b10 (add, remove, dijkstra, view) or 'exit' to quit: ").strip().lower()
        if b10 = = 'exit':
            break
        fonk5(b10)
if b11 = = "__main__":
    fonk6()