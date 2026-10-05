import heapq
def fonk1(graph, source, target):
    b1 = []
    heapq.heappush(b1, (0, source))
    b2 = set()
    b3 = {source: None}
    b4 = {}
    while b1:
        curr_path_weight, b5 = heapq.heappop(b1)
        if b5 in b2:
            continue
        elif b5 = = target:
            return fonk2(source, b5, b3), curr_path_weight
        for neighbor, edge_weight in graph.get_neighbors(b5):
            if neighbor not in b2 and (neighbor not in b4 or b4[neighbor] > curr_path_weight + edge_weight):
                b4[neighbor] = curr_path_weight + edge_weight
                b3[neighbor] = b5
                heapq.heappush(b1, (b4[neighbor], neighbor))
        b2.add(b5)
    return None
def fonk2(source, target, path_dict):
    b6 = []
    b7 = target
    while b7 is not None:
        b6.append(b7)
        b7 = path_dict[b7]
    return b6