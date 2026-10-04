from graph import Graph
from shortest_paths import shortest_path_lengths, shortest_path_tree
def fonk1(b10):
    b1 = Graph()
    b2 = {}
    b3 = set()
    with open(b10, 'r') as file:
        for line in file:
            start_city, end_city, b4 = line.strip().split(',')
            hours, b5 = map(int, b4.split(':'))
            b6 = hours * 60 + b5
            b3.add((start_city, end_city, b6))
            b2.setdefault(start_city, None)
            b2.setdefault(end_city, None)
    for city in b2:
        b2[city] = b1.insert_vertex(city)
    for start_city, end_city, b6 in b3:
        b1.insert_edge(b2[start_city], b2[end_city], b6)
    return b1, b2
def fonk2(b1, b2, start_city):
    b7 = b2[start_city]
    b8 = shortest_path_lengths(b1, b7)
    b9 = shortest_path_tree(b1, b7, b8)
    print("Shortest b9 from", start_city)
    print(b9)
def fonk3():
    b10 = 'eurail.txt'
    b1, b2 = fonk1(b10)
    fonk2(b1, b2, 'London')
if b11 = = "__main__":
    fonk3()