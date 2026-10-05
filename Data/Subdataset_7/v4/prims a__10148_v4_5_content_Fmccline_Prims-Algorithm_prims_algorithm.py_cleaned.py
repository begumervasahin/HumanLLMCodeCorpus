from prims_queue import PrimsQueue
class class1:
    a1 = 0
    a2 = 1
    a3 = 2
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        b1 = self.b1
        b2 = b1.b3(data='name')
        b3 = [b8[0] for b8 in b2]
        b4 = {b3[0]: True}
        b5 = []
        b6 = PrimsQueue()
        b7 = {}
        b8 = b3[0]
        for counter in range(0, len(b3)-1):
            for neighbor in b1.neighbors(b8):
                if neighbor in b4:
                    continue
                b9 = b1.get_edge_data(b8, neighbor)['b9']
                if neighbor in b7:
                    b6.update(b8, neighbor, b9)
                else:
                    b6.push(b8, neighbor, b9)
                    b7[neighbor] = True
            from_node, to_node, b10 = b6.front()
            b6.pop()
            b4[to_node] = True
            b5.append((from_node, to_node, b10))
            b8 = to_node
            yield b5