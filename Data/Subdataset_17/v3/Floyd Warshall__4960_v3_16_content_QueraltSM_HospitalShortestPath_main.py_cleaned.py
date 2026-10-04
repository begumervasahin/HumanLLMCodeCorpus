def print_result(src, dest, path, distances):
    print(f"{src} -> {dest}")
    final_path = " -> ".join(path[::-1])
    print("\nShortest path:\n", final_path)
    print(f"Minimum cost = {distances[dest]} km")
def dijkstra(graph, src, dest):
    visited = []
    distances = {}
    predecessors = {}
    if src not in graph:
        raise ValueError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise ValueError('The target of the shortest path cannot be found')
    distances[src] = 0
    while src:
        for neighbor, distance in graph[src].items():
            if neighbor not in visited:
                new_distance = distances[src] + distance
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        visited.append(src)
        unvisited = {node: distances.get(node, float('inf')) for node in graph if node not in visited}
        src = min(unvisited, key=unvisited.get, default=None)
    if dest in distances:
        path = []
        while dest is not None:
            path.append(dest)
            dest = predecessors.get(dest)
        print_result(path[-1], path[0], path, distances)
    else:
        print(f"No path found from {path[-1]} to {path[0]}")
graph = {
    'Hospital Universitario de Gran Canaria Doctor Negrin': {
        'Clinica Centro - Las Palmas': 2.5,
        'Clinica del Carmen': 3.1,
        'Hospital Pediatrico Dr. Agustin Zubillaga': 1.3
    },
    'Clinica Centro - Las Palmas': {
        'Hospital Universitario de Gran Canaria Doctor Negrin': 2.5,
        'Hospital San Jose': 2,
        'Hospitales San Roque': 0.8,
        'Hospitales La Paloma': 3.7
    },
    'Hospital Pediatrico Dr. Agustin Zubillaga': {
        'Hospital Universitario de Gran Canaria Doctor Negrin': 1.3,
        'Hospitales La Paloma': 3.3
    },
    'Clinica del Carmen': {
        'Hospital Universitario de Gran Canaria Doctor Negrin': 3.1,
        'Hospital Vithas Santa Catalina': 1.2
    },
    'Hospital Vithas Santa Catalina': {
        'Clinica del Carmen': 1.2,
        'Hospital La Paloma': 0.25,
        'HPS - Hospital Perpetuo Socorro': 4.1
    },
    'Hospital La Paloma': {
        'Hospital Pediatrico Dr. Agustin Zubillaga': 3.3,
        'Clinica Centro - Las Palmas': 3.7,
        'Hospital Vithas Santa Catalina': 0.25
    },
    'Hospitales San Roque': {
        'HPS - Hospital Perpetuo Socorro': 1.7,
        'Clinica Centro - Las Palmas': 0.8
    },
    'HPS - Hospital Perpetuo Socorro': {
        'Hospital San Jose': 0.85,
        'Hospitales San Roque': 1.7,
        'Hospital Vithas Santa Catalina': 4.1
    },
    'Hospital San Jose': {
        'Clinica Centro - Las Palmas': 2,
        'HPS - Hospital Perpetuo Socorro': 0.85
    }
}
dijkstra(graph, 'Hospital San Jose', 'Hospital Universitario de Gran Canaria Doctor Negrin')