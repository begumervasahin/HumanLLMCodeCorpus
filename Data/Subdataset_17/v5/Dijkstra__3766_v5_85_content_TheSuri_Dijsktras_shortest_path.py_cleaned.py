import heapq
def shortest_path(graph, source, target):
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))
    visited = set()
    path = {source: None}
    distances = {source: 0}
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)
        if curr_node in visited:
            continue
        if curr_node == target:
            return get_path(source, target, path), curr_distance
        visited.add(curr_node)
        for neighbor, edge_weight in graph.get_neighbors(curr_node):
            if neighbor not in visited:
                new_distance = curr_distance + edge_weight
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    path[neighbor] = curr_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    return None, float('inf')
def get_path(source, target, path_dict):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = path_dict.get(node)
    path.reverse()
    return path