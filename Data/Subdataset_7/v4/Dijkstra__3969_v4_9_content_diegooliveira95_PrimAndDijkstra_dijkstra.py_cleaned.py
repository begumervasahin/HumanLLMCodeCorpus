import heapq
from b5 import Vertex, Graph
def fonk1(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        fonk1(v.previous, path)
def fonk2(b5, start):
    start.set_distance(0)
    b1 = [(vertex.get_distance(), vertex) for vertex in b5]
    heapq.heapify(b1)
    while b1:
        current_distance, b2 = heapq.heappop(b1)
        b2.set_visited()
        for next_vertex in b2.adjacent:
            if next_vertex.visited:
                continue
            b3 = b2.get_distance() + b2.get_weight(next_vertex)
            if b3 < next_vertex.get_distance():
                next_vertex.set_distance(b3)
                next_vertex.set_previous(b2)
        while b1:
            heapq.heappop(b1)
        b1 = [(vertex.get_distance(), vertex) for vertex in b5 if not vertex.visited]
        heapq.heapify(b1)
if b4 = = "__main__":
    b5 = Graph()
    b5.add_vertex('A')
    b5.add_vertex('B')
    b5.add_vertex('C')
    b5.add_vertex('D')
    b5.add_vertex('E')
    b5.add_edge('A', 'B', 1)
    b5.add_edge('A', 'C', 3)
    b5.add_edge('B', 'D', 2)
    b5.add_edge('C', 'D', 2)
    b5.add_edge('B', 'E', 4)
    b5.add_edge('D', 'E', 1)
    fonk2(b5, b5.get_vertex('A'))
    b6 = b5.get_vertex('E')
    b7 = [b6.get_id()]
    fonk1(b6, b7)
    print(b7[::-1])
