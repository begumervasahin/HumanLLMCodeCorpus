import sys
import romania
class RouteFinder:
    def __init__(self):
        self.graph = {}
    def find_route(self):
        file_input = sys.argv[1]
        source_city = sys.argv[2]
        destination_city = sys.argv[3]
        total_distance = 0
        stack = []
        bi_dir_graph = romania.romania(0).get_data_romania(file_input)
        graph = bi_dir_graph[0]
        vertices = bi_dir_graph[1]
        visited = [False] * vertices
        for i in range(vertices):
            if not visited[i]:
                self.sort(graph, source_city, visited, stack)
        dist = [float("Inf")] * vertices
        dist[graph.keys().index(source_city)] = 0.0
        from_city = [0] * vertices
        to_city = [0] * vertices
        to_fro_dist = [0] * vertices
        while stack:
            pos = stack.pop()
            for destination, distance in graph[pos]:
                cumulative_distance = float(dist[graph.keys().index(pos)]) + float(distance)
                if float(dist[graph.keys().index(destination)]) > cumulative_distance:
                    dist[graph.keys().index(destination)] = cumulative_distance
                    from_city[graph.keys().index(destination)] = pos
                    to_city[graph.keys().index(destination)] = destination
                    to_fro_dist[graph.keys().index(destination)] = float(distance)
                    if destination == destination_city:
                        total_distance = cumulative_distance
            pos = 0
            return_str = []
            final_dist = total_distance
        while total_distance != 0:
            if to_city[pos] == destination_city:
                    return_str.append(from_city[pos])
                    return_str.append(to_city[pos])
                    return_str.append(str(to_fro_dist[pos]))
                    total_distance = dist[pos] - to_fro_dist[pos]
                    destination_city = from_city[pos]
                    pos = 0
            else:
                pos += 1
        return_str.reverse()
        if final_dist == 0:
            path_str = "distance: infinity\nroute:\nnone\n"
        else:
            path_str = f"distance: {final_dist} km\nroute:\n"
            pos = 0
            while pos < len(return_str):
                path_str += f"{return_str[pos + 2]} to {return_str[pos + 1]}, {return_str[pos]} km\n"
                pos += 3
        print(path_str)
    def sort(self, graph, source_city, visited, stack):
        visited[graph.keys().index(source_city)] = True
        if source_city in graph.keys():
            for dest, distance in graph[source_city]:
                if not visited[graph.keys().index(dest)]:
                    self.sort(graph, dest, visited, stack)
        stack.append(source_city)
def main():
    route_finder = RouteFinder()
    route_finder.find_route()
if __name__ == "__main__":
    main()