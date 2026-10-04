import heapq
def fonk1(graph, source, target):
    b1 = []
    heapq.heappush(b1, (0, source))
    b2 = set()
    b3 = {source: None}
    b4 = {source: 0}
    while b1:
        curr_distance, b5 = heapq.heappop(b1)
        if b5 in b2:
            continue
        if b5 = = target:
            return fonk2(source, target, b3), curr_distance
        b2.add(b5)
        for neighbor, edge_weight in graph.get_neighbors(b5):
            if neighbor not in b2:
                b6 = curr_distance + edge_weight
                if neighbor not in b4 or b6 < b4[neighbor]:
                    b4[neighbor] = b6
                    b3[neighbor] = b5
                    heapq.heappush(b1, (b6, neighbor))
    return None, float('inf')
def fonk2(source, target, path_dict):
    b3 = []
    b7 = target
    while b7 is not None:
        b3.append(b7)
        b7 = path_dict.get(b7)
    b3.reverse()
    return b3