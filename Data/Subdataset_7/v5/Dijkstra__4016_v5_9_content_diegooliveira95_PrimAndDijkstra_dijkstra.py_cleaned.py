import heapq
from b5 import Vertex, Graph
def fonk1(vertex, path):
    if vertex.previous:
        path.append(vertex.previous.get_id())
        fonk1(vertex.previous, path)
def fonk2(b5, start_vertex):
    start_vertex.set_distance(0)
    b1 = [(v.get_distance(), v) for v in b5]
    heapq.heapify(b1)
    while b1:
        current_distance, b2 = heapq.heappop(b1)
        b2.set_visited()
        for neighbor_vertex in b2.adjacent:
            if neighbor_vertex.visited:
                continue
            b3 = b2.get_distance() + b2.get_weight(neighbor_vertex)
            if b3 < neighbor_vertex.get_distance():
                neighbor_vertex.set_distance(b3)
                neighbor_vertex.set_previous(b2)
        while b1:
            heapq.heappop(b1)
        b1 = [(v.get_distance(), v) for v in b5 if not v.visited]
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
