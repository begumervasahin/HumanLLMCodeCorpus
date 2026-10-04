from graph import Graph
from shortest_paths import shortest_path_lengths, shortest_path_tree
from linked_stack import LinkedStack
def load_rail_system(file_path):
    rail_system = Graph()
    cities = {}
    routes = set()
    with open(file_path, 'r') as eurail:
        for line in eurail:
            s, d, w = line.strip().split(',')
            hours, minutes = map(int, w.split(':'))
            routes.add((s, d, hours * 60 + minutes))
            cities.setdefault(s)
            cities.setdefault(d)
    for city in cities:
        cities[city] = rail_system.insert_vertex(city)
    for route in routes:
        s, d, duration = route
        rail_system.insert_edge(cities[s], cities[d], duration)
    return rail_system, cities
def display_shortest_paths(rail_system, cities, start_city):
    start_vertex = cities[start_city]
    durations = shortest_path_lengths(rail_system, start_vertex)
    paths = shortest_path_tree(rail_system, start_vertex, durations)
    print(paths)
def main():
    file_path = 'eurail.txt'
    rail_system, cities = load_rail_system(file_path)
    display_shortest_paths(rail_system, cities, 'London')
if __name__ == "__main__":
    main()