from dijkstra import Graph
b1 = Graph()
def fonk1():
    b2 = input("Enter the start node: ")
    b3 = input("Enter the end node: ")
    b4 = input("Enter the b4: ")
    b1.fonk1(b2, b3, int(b4))
    print(f"Edge added: {b2} -> {b3} with b4 {b4}")
def fonk2():
    b2 = input("Enter the start node: ")
    b3 = input("Enter the end node: ")
    b1.fonk2(b2, b3)
    print(f"Edge removed: {b2} -> {b3}")
def fonk3():
    b2 = input("Enter the start node: ")
    b3 = input("Enter the end node: ")
    path, b4 = b1.dijkstra(b2, b3)
    print(f"Shortest path from {b2} to {b3}: {path} with b4 {b4}")
def fonk4():
    b5 = b1.neighbours()
    print("Graph b5:")
    for node, neighbors_list in b5.items():
        print(f"{node}: {neighbors_list}")
def fonk5(b8):
    b6 = {
        "add": add_edge,
        "remove": remove_edge,
        "dijkstra": run_dijkstra,
        "view": view_graph,
    }
    b7 = b6.get(b8)
    if b7:
        b7()
    else:
        print("Invalid b8")
def fonk6():
    while True:
        b8 = input("Enter a b8 (add, remove, dijkstra, view) or 'exit' to quit: ").strip().lower()
        if b8 = = 'exit':
            break
        fonk5(b8)
if b9 = = "__main__":
    fonk6()