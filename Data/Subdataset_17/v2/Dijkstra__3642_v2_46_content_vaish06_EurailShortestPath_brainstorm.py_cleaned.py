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
            cities.setdefault(start_city)
            cities.setdefault(end_city)
    for city in cities:
        cities[city] = rail_system.insert_vertex(city)
    for start_city, end_city, duration in routes:
        rail_system.insert_edge(cities[start_city], cities[end_city], duration)
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