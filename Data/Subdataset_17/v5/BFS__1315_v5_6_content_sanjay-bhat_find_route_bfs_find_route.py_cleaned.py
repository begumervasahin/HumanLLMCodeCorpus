import romania
import sys
class FindRoute:
    def find_route(self):
        file_input = sys.argv[1]
        start_city = sys.argv[2]
        destination_city = sys.argv[3]
        graph, vertices_count = romania.Romania().get_data(file_input)
        visited = [False] * vertices_count
        stack = []
        for i in range(vertices_count):
            if not visited[i]:
                self.topological_sort(graph, start_city, visited, stack)
        distances = [float("Inf")] * vertices_count
        distances[list(graph.keys()).index(start_city)] = 0.0
        from_city = [None] * vertices_count
        to_city = [None] * vertices_count
        edge_distances = [0] * vertices_count
        total_distance = 0
        while stack:
            current_city = stack.pop()
            for neighbor, distance in graph[current_city]:
                neighbor_index = list(graph.keys()).index(neighbor)
                new_distance = distances[list(graph.keys()).index(current_city)] + float(distance)
                if distances[neighbor_index] > new_distance:
                    distances[neighbor_index] = new_distance
                    from_city[neighbor_index] = current_city
                    to_city[neighbor_index] = neighbor
                    edge_distances[neighbor_index] = float(distance)
                    if neighbor == destination_city:
                        total_distance = new_distance
        result_path = self.build_path(from_city, to_city, edge_distances, start_city, destination_city, total_distance)
        self.print_result(result_path, total_distance)
    def topological_sort(self, graph, start_city, visited, stack):
        city_index = list(graph.keys()).index(start_city)
        visited[city_index] = True
        for neighbor, _ in graph[start_city]:
            neighbor_index = list(graph.keys()).index(neighbor)
            if not visited[neighbor_index]:
                self.topological_sort(graph, neighbor, visited, stack)
        stack.append(start_city)
    def build_path(self, from_city, to_city, edge_distances, start_city, destination_city, total_distance):
        result_path = []
        current_distance = total_distance
        pos = list(to_city).index(destination_city)
        while current_distance != 0:
            result_path.append(from_city[pos])
            result_path.append(to_city[pos])
            result_path.append(str(edge_distances[pos]))
            current_distance = distances[pos] - edge_distances[pos]
            destination_city = from_city[pos]
            pos = list(to_city).index(destination_city)
        result_path.reverse()
        return result_path
    def print_result(self, result_path, total_distance):
        if total_distance == 0:
            print("distance: infinity\nroute:\nnone\n")
        else:
            print(f"distance: {total_distance} km\nroute:")
            for i in range(0, len(result_path), 3):
                print(f"{result_path[i]} to {result_path[i + 1]}, {result_path[i + 2]} km")
def main():
    route_finder = FindRoute()
    route_finder.find_route()
if __name__ == "__main__":
    main()