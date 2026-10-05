from graph import Graph
from shortest_paths import shortest_path_lengths, shortest_path_tree
from linked_stack import LinkedStack
rail_system = Graph()
with open('eurail.txt', 'r') as eurail:
    cities = {}
    routes = set()
    for line in eurail.readlines():
        source, destination, duration = line.split(',')
        hours, minutes = map(int, duration.split(':'))
        duration_minutes = hours * 60 + minutes
        routes.add((source, destination, duration_minutes))
        cities.setdefault(source)
        cities.setdefault(destination)
    for city in cities:
        cities[city] = rail_system.insert_vertex(city)
    for route in routes:
        source, destination, duration = route
        rail_system.insert_edge(cities[source], cities[destination], duration)
counts = 0
flag = False
durations = shortest_path_lengths(rail_system, cities['London'])
paths = shortest_path_tree(rail_system, cities['London'], durations)
print(paths)