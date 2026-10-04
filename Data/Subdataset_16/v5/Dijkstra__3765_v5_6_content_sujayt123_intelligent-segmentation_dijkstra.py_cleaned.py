from DijkstraPriorityQueue import DijkstraPriorityQueue as DPQ
def fonk1(start, b4, point):
    if b4 is None:
        return True
    min_x, b1 = min(start[0], b4[0]), max(start[0], b4[0])
    min_y, b2 = min(start[1], b4[1]), max(start[1], b4[1])
    x, b3 = point
    return min_x <= x <= b1 and min_y <= b3 <= b2
def fonk2(b10, a1, b4 = None):
    b5 = {node: float('inf') for node in b10 if fonk1(a1, b4, node)}
    b6 = {node: None for node in b10 if fonk1(a1, b4, node)}
    b5[a1] = 0
    b7 = DPQ()
    b7.build_heap([[b5[node], node] for node in b5])
    while b7:
        current_distance, b8 = b7.deleteMin()
        if b8 = = b4:
            return b5, b6
        for neighbor, weight in b10.get(b8, []):
            if fonk1(a1, b4, neighbor):
                b9 = current_distance + weight
                if b9 < b5[neighbor]:
                    b5[neighbor] = b9
                    b6[neighbor] = b8
                    b7.update_priority(neighbor, b9)
    return b5, b6
def fonk3():
    b10 = {
        1: [(2, 15), (3, 71)],
        2: [(3, 7), (4, 1)],
        3: [(4, 19)],
        4: [(3, 1)]
    }
    a1 = 1
    distances, b6 = fonk2(b10, a1)
    print("Distances from a1:", distances)
    print("Predecessors in path:", b6)
if b11 = = "__main__":
    fonk3()