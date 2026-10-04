import romania
import sys
class FindRoute:
    def find_route(self):
        file_input = sys.argv[1]
        dest1 = sys.argv[2]
        dest2 = sys.argv[3]
        total_distance = 0
        stack = []
        bi_dir_graph = romania.Romania().get_data(file_input)
        graph = bi_dir_graph[0]
        vertices = bi_dir_graph[1]
        visited = [False] * vertices
        for i in range(vertices):
            if not visited[i]:
                self.sort(graph, dest1, visited, stack)
        dist = [float("Inf")] * vertices
        dist[list(graph.keys()).index(dest1)] = 0.0
        from_city = [0] * vertices
        to_city = [0] * vertices
        to_fro_dist = [0] * vertices
        while stack:
            pos = stack.pop()
            for destination, distance in graph[pos]:
                cumulative_distance = float(dist[list(graph.keys()).index(pos)]) + float(distance)
                if float(dist[list(graph.keys()).index(destination)]) > cumulative_distance:
                    dist[list(graph.keys()).index(destination)] = cumulative_distance
                    from_city[list(graph.keys()).index(destination)] = pos
                    to_city[list(graph.keys()).index(destination)] = destination
                    to_fro_dist[list(graph.keys()).index(destination)] = float(distance)
                    if destination == dest2:
                        total_distance = cumulative_distance
        pos = 0
        result_path = []
        final_distance = total_distance
        while total_distance != 0:
            if to_city[pos] == dest2:
                result_path.append(from_city[pos])
                result_path.append(to_city[pos])
                result_path.append(str(to_fro_dist[pos]))
                total_distance = dist[pos] - to_fro_dist[pos]
                dest2 = from_city[pos]
                pos = 0
            else:
                pos += 1
        result_path.reverse()
        if final_distance == 0:
            path_str = "distance: infinity\nroute:\nnone\n"
        else:
            path_str = f"distance: {final_distance} km\nroute:\n"
            pos = 0
            while pos < len(result_path):
                path_str += f"{result_path[pos]} to {result_path[pos + 1]}, {result_path[pos + 2]} km\n"
                pos += 3
        print(path_str)
    def sort(self, graph, dest1, visited, stack):
        visited[list(graph.keys()).index(dest1)] = True
        if dest1 in graph:
            for d, distance in graph[dest1]:
                if not visited[list(graph.keys()).index(d)]:
                    self.sort(graph, d, visited, stack)
        stack.append(dest1)
def main():
    route_finder = FindRoute()
    route_finder.find_route()
if __name__ == "__main__":
    main()