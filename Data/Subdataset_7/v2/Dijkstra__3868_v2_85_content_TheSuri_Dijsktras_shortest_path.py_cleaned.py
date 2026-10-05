import heapq
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, u, v, weight):
        if u not in self.b1:
            self.b1[u] = []
        self.b1[u].append((v, weight))
    def fonk3(self, b10):
        return self.b1.get(b10, [])
class class2:
    def fonk4(self, b2):
        self.b2 = b2
    def fonk5(self, b12, b13):
        b3 = []
        heapq.heappush(b3, (0, b12))
        b4 = set()
        b5 = {b12: None}
        b6 = {b12: 0}
        while b3:
            current_path_weight, b7 = heapq.heappop(b3)
            if b7 in b4:
                continue
            elif b7 = = b13:
                return self.fonk6(b12, b7, b5), b6[b7]
            for neighbor, edge_weight in self.b2.fonk3(b7):
                if neighbor not in b4:
                    b8 = current_path_weight + edge_weight
                    if neighbor not in b6 or b8 < b6[neighbor]:
                        b6[neighbor] = b8
                        b5[neighbor] = b7
                        heapq.heappush(b3, (b8, neighbor))
            b4.add(b7)
        return None
    def fonk6(self, b12, b13, b5):
        b9 = []
        b10 = b13
        while b10 is not None:
            b9.append(b10)
            b10 = b5[b10]
        return b9
def fonk7():
    b2 = class1()
    b2.fonk2('A', 'B', 5)
    b2.fonk2('A', 'C', 3)
    b2.fonk2('B', 'D', 2)
    b2.fonk2('C', 'D', 4)
    b2.fonk2('D', 'E', 6)
    b11 = class2(b2)
    b12 = 'A'
    b13 = 'E'
    shortest_path, b14 = b11.fonk5(b12, b13)
    if shortest_path:
        print(f"Shortest path from {b12} to {b13}: {' -> '.join(shortest_path)}")
        print(f"Shortest distance: {b14}")
    else:
        print(f"No path found from {b12} to {b13}")
if b15 = = "__main__":
    fonk7()