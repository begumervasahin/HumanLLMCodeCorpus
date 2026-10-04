from dijkstra import *
def fonk1():
    b1 = input("Enter node 1 ")
    b2 = input("Enter node 2 ")
    b3 = input("Enter cost")
    graph.add_edge("a", "b", int(b3))
def fonk2():
    b1 = input("Enter node 1 ")
    b2 = input("Enter node 2 ")
    graph.remove_edge(b1, b2)
def fonk3():
    b1 = input("Enter node 1 ")
    b2 = input("Enter node 2 ")
    graph.dijkstra(b1, b2)
def fonk4():
    b4 = graph.neighbours()
    print(b4)
def fonk5(argument):
    b5 = {
        "add": addFunction,
        "remove": removeFunction,
        "dijkstra": dijkFunction,
        "view": viewGraph,
    }
    print(b5.get(argument, "Invalid argument"))
b6 = {
    "add": addFunction,
    "remove": removeFunction,
    "dijkstra": dijkFunction,
    "view": viewGraph
}
b7 = input("Enter one of the following: add,remove.dijkstra,view")
fonk5(b7)
print(graph.dijkstra("a", "e"))