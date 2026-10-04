from graph import Graph
from shortest_paths import shortest_path_lengths, shortest_path_tree
from linked_stack import LinkedStack
def fonk1(b10):
    b1 = Graph()
    b2 = {}
    b3 = set()
    with open(b10, 'r') as eurail:
        for line in eurail:
            s, d, b4 = line.strip().split(',')
            hours, b5 = map(int, b4.split(':'))
            b3.add((s, d, hours * 60 + b5))
            b2.setdefault(s)
            b2.setdefault(d)
    for city in b2:
        b2[city] = b1.insert_vertex(city)
    for route in b3:
        s, d, b6 = route
        b1.insert_edge(b2[s], b2[d], b6)
    return b1, b2
def fonk2(b1, b2, start_city):
    b7 = b2[start_city]
    b8 = shortest_path_lengths(b1, b7)
    b9 = shortest_path_tree(b1, b7, b8)
    print(b9)
def fonk3():
    b10 = 'eurail.txt'
    b1, b2 = fonk1(b10)
    fonk2(b1, b2, 'London')
if b11 = = "__main__":
    fonk3()