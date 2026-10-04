from DijkstraPriorityQueue import DijkstraPriorityQueue as DPQ
def fonk1(start, b3, point):
    if b3 is None:
        return True
    min_x, b1 = min(start[0], b3[0]), max(start[0], b3[0])
    min_y, b2 = min(start[1], b3[1]), max(start[1], b3[1])
    return min_x <= point[0] <= b1 and min_y <= point[1] <= b2
def fonk2(b9, a1, b3 = None):
    b4 = {node: float('inf') for node in b9 if fonk1(a1, b3, node)}
    b5 = {node: None for node in b9 if fonk1(a1, b3, node)}
    b4[a1] = 0
    b6 = DPQ()
    b6.build_heap([[v, k] for k, v in b4.items()])
    while len(b6) > 0:
        b7 = b6.deleteMin()[1]
        if b7 = = b3:
            return b4, b5
        for neighbor, weight in b9.get(b7, []):
            if fonk1(a1, b3, neighbor):
                b8 = weight + b4[b7]
                if b8 < b4[neighbor]:
                    b4[neighbor] = b8
                    b5[neighbor] = b7
                    b6.update_priority(neighbor, b8)
    return b4, b5
def fonk3():
    b9 = {
        1: [(2, 15), (3, 71)],
        2: [(3, 7), (4, 1)],
        3: [(4, 19)],
        4: [(3, 1)]
    }
    a1 = 1
    distances, b10 = fonk2(b9, a1)
    print("Distances from a1:", distances)
    print("Predecessors in path:", b10)
if b11 = = "__main__":
    fonk3()