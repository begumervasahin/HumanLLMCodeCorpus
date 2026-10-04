from graph import Graph
from shortest_paths import shortest_path_lengths, shortest_path_tree
def fonk1(b8):
    b1 = Graph()
    b2 = {}
    b3 = set()
    with open(b8, 'r') as file:
        for line in file:
            b9, end_city, b4 = line.strip().split(',')
            b5 = fonk2(b4)
            b3.add((b9, end_city, b5))
            b2.setdefault(b9, None)
            b2.setdefault(end_city, None)
    for city in b2:
        b2[city] = b1.insert_vertex(city)
    for b9, end_city, b5 in b3:
        b1.insert_edge(b2[b9], b2[end_city], b5)
    return b1, b2
def fonk2(b4):
    hours, b6 = map(int, b4.split(':'))
    return hours * 60 + b6
def fonk3(b1, b2):
    for source in b2:
        for destination in b2:
            if source != destination:
                b7 = b1.get_edge(b2[source], b2[destination])
                if b7:
                    print(f"Edge from {source} to {destination}: {b7}")
def fonk4():
    b8 = 'eurail.txt'
    b1, b2 = fonk1(b8)
    fonk3(b1, b2)
    b9 = 'London'
    if b9 in b2:
        b10 = b2[b9]
        b11 = shortest_path_lengths(b1, b10)
        b12 = shortest_path_tree(b1, b10, b11)
        print(f"Shortest b12 from {b9}:")
        print(b12)
    else:
        print(f"City '{b9}' not found in the rail system.")
if b13 = = "__main__":
    fonk4()