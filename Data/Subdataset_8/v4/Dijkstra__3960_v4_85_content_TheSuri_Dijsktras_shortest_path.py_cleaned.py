import heapq
def shortest_path(graph, source, target):
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))
    visited = set()
    path = {source: None}
    remaining = {}
    while priority_queue:
        curr_path_weight, curr_node = heapq.heappop(priority_queue)
        if curr_node in visited:
            continue
        elif curr_node == target:
            return _get_path(source, curr_node, path), curr_path_weight
        for neighbor, edge_weight in graph.get_neighbors(curr_node):
            if neighbor not in visited and (neighbor not in remaining or remaining[neighbor] > curr_path_weight + edge_weight):
                remaining[neighbor] = curr_path_weight + edge_weight
                path[neighbor] = curr_node
                heapq.heappush(priority_queue, (remaining[neighbor], neighbor))
        visited.add(curr_node)
    return None
def _get_path(source, target, path_dict):
    result = []
    node = target
    while node is not None:
        result.append(node)
        node = path_dict[node]
    return result