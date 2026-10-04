import heapq
class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
    def fonk2(self, from_node, to_node, b6):
        self.b1.setdefault(from_node, []).append(to_node)
        self.b2[(from_node, to_node)] = b6
    def fonk3(self, node1, node2, b6):
        self.fonk2(node1, node2, b6)
        self.fonk2(node2, node1, b6)
def fonk4(graph, start):
    b3 = {start: (None, 0)}
    b4 = [(0, start)]
    while b4:
        current_weight, b5 = heapq.heappop(b4)
        for neighbor in graph.b1.get(b5, []):
            b6 = current_weight + graph.b2[(b5, neighbor)]
            if neighbor not in b3 or b6 < b3[neighbor][1]:
                b3[neighbor] = (b5, b6)
                heapq.heappush(b4, (b6, neighbor))
    return b3
def fonk5(graph, start, b8):
    b3 = fonk4(graph, start)
    b7 = []
    while b8:
        b7.append(b8)
        b8 = b3[b8][0]
    b7.reverse()
    return b7
def fonk6():
    b9 = class1()
    b9.fonk2('a', 'b', 4)
    b9.fonk2('a', 'h', 8)
    b9.fonk2('b', 'c', 8)
    b9.fonk2('c', 'd', 7)
    b9.fonk2('b', 'h', 11)
    b9.fonk2('h', 'i', 7)
    b9.fonk2('i', 'c', 2)
    b9.fonk2('i', 'g', 6)
    b9.fonk2('h', 'g', 1)
    b9.fonk2('g', 'f', 2)
    b9.fonk2('c', 'f', 4)
    b9.fonk2('d', 'f', 14)
    b9.fonk2('d', 'e', 9)
    b9.fonk2('f', 'e', 10)
    b10 = class1()
    b10.fonk3('s', 't', 10)
    b10.fonk3('s', 'y', 5)
    b10.fonk3('t', 'x', 1)
    b10.fonk3('y', 'z', 2)
    b10.fonk3('t', 'y', 2)
    b10.fonk3('y', 't', 3)
    b10.fonk3('x', 'z', 4)
    b10.fonk3('z', 'x', 6)
    b10.fonk3('y', 'x', 9)
    b10.fonk3('z', 's', 7)
    b7 = fonk5(b10, 't', 's')
    print(f"The shortest b7 from 't' to 's' is: {b7}")
if b11 = = "__main__":
    fonk6()