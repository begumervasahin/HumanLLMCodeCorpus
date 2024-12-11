from graph import Graph
from shortest_paths import shortest_path_lengths, shortest_path_tree
from linked_stack import LinkedStack
b1 = Graph()
with open('eurail.txt', 'r') as eurail:
    b2 = {}
    b3 = set()
    for line in eurail.readlines():
        source, destination, b4 = line.split(',')
        hours, b5 = map(int, b4.split(':'))
        b6 = hours * 60 + b5
        b3.add((source, destination, b6))
        b2.setdefault(source)
        b2.setdefault(destination)
    for city in b2:
        b2[city] = b1.insert_vertex(city)
    for route in b3:
        source, destination, b4 = route
        b1.insert_edge(b2[source], b2[destination], b4)
a1 = 0
b7 = False
b8 = shortest_path_lengths(b1, b2['London'])
b9 = shortest_path_tree(b1, b2['London'], b8)
print(b9)