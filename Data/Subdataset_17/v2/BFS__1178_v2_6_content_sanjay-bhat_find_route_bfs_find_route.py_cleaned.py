import romania
import sys
class FindRoute:
    def find_route(self):
        file_input = sys.argv[1]
        start_city = sys.argv[2]
        end_city = sys.argv[3]
        total_distance = 0
        stack = []
        bi_dir_graph = romania.romania(0).getDataRomania(file_input)
        graph = bi_dir_graph[0]
        vertices = bi_dir_graph[1]
        visited = [False] * vertices
        for i in range(vertices):
            if not visited[i]:
                self.topological_sort(graph, start_city, visited, stack)
        dist = [float("Inf")] * vertices
        dist[list(graph.keys()).index(start_city)] = 0.0
        from_city = [0] * vertices
        to_city = [0] * vertices
        to_fro_dist = [0] * vertices
        while stack:
            current = stack.pop()
            for neighbor, distance in graph[current]:
                cumulative_distance = dist[list(graph.keys()).index(current)] + float(distance)
                neighbor_index = list(graph.keys()).index(neighbor)
                if dist[neighbor_index] > cumulative_distance:
                    dist[neighbor_index] = cumulative_distance
                    from_city[neighbor_index] = current
                    to_city[neighbor_index] = neighbor
                    to_fro_dist[neighbor_index] = float(distance)
                    if neighbor == end_city:
                        total_distance = cumulative_distance
        path = self.construct_path(from_city, to_city, to_fro_dist, dist, start_city, end_city, total_distance)
        print(self.format_path(path, total_distance))
    def topological_sort(self, graph, start_city, visited, stack):
        visited[list(graph.keys()).index(start_city)] = True
        if start_city in graph:
            for neighbor, _ in graph[start_city]:
                if not visited[list(graph.keys()).index(neighbor)]:
                    self.topological_sort(graph, neighbor, visited, stack)
        stack.append(start_city)
    def construct_path(self, from_city, to_city, to_fro_dist, dist, start_city, end_city, total_distance):
        pos = 0
        path = []
        final_distance = total_distance
        while total_distance != 0:
            if to_city[pos] == end_city:
                path.append((from_city[pos], to_city[pos], to_fro_dist[pos]))
                total_distance = dist[pos] - to_fro_dist[pos]
                end_city = from_city[pos]
                pos = 0
            else:
                pos += 1
        path.reverse()
        return path
    def format_path(self, path, total_distance):
        if total_distance == 0:
            return "distance: infinity\nroute:\nnone\n"
        else:
            path_str = f"distance: {total_distance} km\nroute:\n"
            for from_city, to_city, distance in path:
                path_str += f"{from_city} to {to_city}, {distance} km\n"
            return path_str
def main():
    obj = FindRoute()
    obj.find_route()
if __name__ == "__main__":
    main()