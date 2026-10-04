from graph import Graph
from shortest_paths import shortest_path_lengths, shortest_path_tree
def load_rail_system(file_path):
    rail_system = Graph()
    cities = {}
    routes = set()
    with open(file_path, 'r') as file:
        for line in file:
            start_city, end_city, time_str = line.strip().split(',')
            hours, minutes = map(int, time_str.split(':'))
            duration = hours * 60 + minutes
            routes.add((start_city, end_city, duration))
            cities.setdefault(start_city, None)
            cities.setdefault(end_city, None)
    for city in cities:
        cities[city] = rail_system.insert_vertex(city)
    for start_city, end_city, duration in routes:
        rail_system.insert_edge(cities[start_city], cities[end_city], duration)
    return rail_system, cities
def display_edge_details(rail_system, cities):
    for source in cities:
        for destination in cities:
            if source != destination:
                edge = rail_system.get_edge(cities[source], cities[destination])
                if edge:
                    print(f"Edge from {source} to {destination}: {edge}")
def main():
    file_path = 'eurail.txt'
    rail_system, cities = load_rail_system(file_path)
    display_edge_details(rail_system, cities)
    start_city = 'London'
    start_vertex = cities[start_city]
    durations = shortest_path_lengths(rail_system, start_vertex)
    paths = shortest_path_tree(rail_system, start_vertex, durations)
    print(f"Shortest paths from {start_city}:")
    print(paths)
if __name__ == "__main__":
    main()