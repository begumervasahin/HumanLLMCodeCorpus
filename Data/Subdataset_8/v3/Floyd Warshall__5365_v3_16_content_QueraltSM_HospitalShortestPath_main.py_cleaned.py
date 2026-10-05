def print_shortest_path(source, destination, path, distances):
    print(f"{source} -> {destination}")
    final_path = " -> ".join(path)
    print("\nShortest path:\n", final_path)
    print(f"Minimum cost = {distances[destination]} km")
def dijkstra(graph, source, destination, visited=[], distances={}, predecessors={}):
    if source not in graph:
        raise ValueError('The source node is not in the graph')
    if destination not in graph:
        raise ValueError('The destination node is not in the graph')
    if source == destination:
        path = []
        pred = destination
        while pred is not None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        print_shortest_path(source, destination, reversed(path), distances)
    else:
        if not visited:
            distances[source] = 0
        for neighbor, weight in graph[source].items():
            if neighbor not in visited:
                new_distance = distances[source] + weight
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = source
        visited.append(source)
        unvisited = {k: distances.get(k, float('inf')) for k in graph if k not in visited}
        next_node = min(unvisited, key=unvisited.get)
        dijkstra(graph, next_node, destination, visited, distances, predecessors)
if __name__ == "__main__":
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