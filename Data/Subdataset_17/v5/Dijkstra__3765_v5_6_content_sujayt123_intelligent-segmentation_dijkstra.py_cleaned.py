from DijkstraPriorityQueue import DijkstraPriorityQueue as DPQ
def is_within_bounding_box(start, end, point):
    if end is None:
        return True
    min_x, max_x = min(start[0], end[0]), max(start[0], end[0])
    min_y, max_y = min(start[1], end[1]), max(start[1], end[1])
    x, y = point
    return min_x <= x <= max_x and min_y <= y <= max_y
def shortest_path(adj_list, source, end=None):
    dist = {node: float('inf') for node in adj_list if is_within_bounding_box(source, end, node)}
    predecessors = {node: None for node in adj_list if is_within_bounding_box(source, end, node)}
    dist[source] = 0
    priority_queue = DPQ()
    priority_queue.build_heap([[dist[node], node] for node in dist])
    while priority_queue:
        current_distance, current_node = priority_queue.deleteMin()
        if current_node == end:
            return dist, predecessors
        for neighbor, weight in adj_list.get(current_node, []):
            if is_within_bounding_box(source, end, neighbor):
                new_distance = current_distance + weight
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    predecessors[neighbor] = current_node
                    priority_queue.update_priority(neighbor, new_distance)
    return dist, predecessors
def main():
    adj_list = {
        1: [(2, 15), (3, 71)],
        2: [(3, 7), (4, 1)],
        3: [(4, 19)],
        4: [(3, 1)]
    }
    source = 1
    distances, predecessors = shortest_path(adj_list, source)
    print("Distances from source:", distances)
    print("Predecessors in path:", predecessors)
if __name__ == "__main__":
    main()