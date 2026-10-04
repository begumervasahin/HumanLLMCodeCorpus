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
def fonk5(graph, start, b9):
    b3 = fonk4(graph, start)
    b7 = []
    while b9:
        b7.append(b9)
        b8 = b3[b9][0]
        b9 = b8
    b7 = b7[::-1]
    return b7
def fonk6():
    b10 = class1()
    b10.fonk2('a', 'b', 4)
    b10.fonk2('a', 'h', 8)
    b10.fonk2('b', 'c', 8)
    b10.fonk2('c', 'd', 7)
    b10.fonk2('b', 'h', 11)
    b10.fonk2('h', 'i', 7)
    b10.fonk2('i', 'c', 2)
    b10.fonk2('i', 'g', 6)
    b10.fonk2('h', 'g', 1)
    b10.fonk2('g', 'f', 2)
    b10.fonk2('c', 'f', 4)
    b10.fonk2('d', 'f', 14)
    b10.fonk2('d', 'e', 9)
    b10.fonk2('f', 'e', 10)
    b11 = class1()
    b11.fonk3('s', 't', 10)
    b11.fonk3('s', 'y', 5)
    b11.fonk3('t', 'x', 1)
    b11.fonk3('y', 'z', 2)
    b11.fonk3('t', 'y', 2)
    b11.fonk3('y', 't', 3)
    b11.fonk3('x', 'z', 4)
    b11.fonk3('z', 'x', 6)
    b11.fonk3('y', 'x', 9)
    b11.fonk3('z', 's', 7)
    b7 = fonk5(b11, 't', 's')
    print(f"The shortest b7 from 't' to 's' is: {b7}")
if b12 = = "__main__":
    fonk6()