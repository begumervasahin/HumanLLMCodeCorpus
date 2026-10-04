from dijkstra import *
def addFunction():
    n1 = input("Enter node 1 ")
    n2 = input("Enter node 2 ")
    n3 = input("Enter cost")
    graph.add_edge("a", "b", int(n3))
def removeFunction():
    n1 = input("Enter node 1 ")
    n2 = input("Enter node 2 ")
    graph.remove_edge(n1, n2)
def dijkFunction():
    n1 = input("Enter node 1 ")
    n2 = input("Enter node 2 ")
    graph.dijkstra(n1, n2)
def viewGraph():
    neighbors = graph.neighbours()
    print(neighbors)
def switch_demo(argument):
    switcher = {
        "add": addFunction,
        "remove": removeFunction,
        "dijkstra": dijkFunction,
        "view": viewGraph,
    }
    print(switcher.get(argument, "Invalid argument"))
options = {
    "add": addFunction,
    "remove": removeFunction,
    "dijkstra": dijkFunction,
    "view": viewGraph
}
arg = input("Enter one of the following: add,remove.dijkstra,view")
switch_demo(arg)
print(graph.dijkstra("a", "e"))