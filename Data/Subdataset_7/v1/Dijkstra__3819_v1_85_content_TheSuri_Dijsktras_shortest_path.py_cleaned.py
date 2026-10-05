import heapq
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, u, v, weight):
        if u not in self.b1:
            self.b1[u] = []
        self.b1[u].append((v, weight))
    def fonk3(self, b9):
        return self.b1.get(b9, [])
class class2:
    def fonk4(self, b2):
        self.b2 = b2
    def fonk5(self, b11, b12):
        b3 = []
        heapq.heappush(b3, (0, b11))
        b4 = set()
        b5 = {b11: None}
        b6 = {}
        while b3:
            curr_path_weight, b7 = heapq.heappop(b3)
            if b7 in b4:
                continue
            elif b7 = = b12:
                return self.fonk6(b11, b7, b5), curr_path_weight
            for neighbor, edge_weight in self.b2.fonk3(b7):
                if neighbor not in b4 and (neighbor not in b6 or b6[neighbor] > curr_path_weight + edge_weight):
                    b6[neighbor] = curr_path_weight + edge_weight
                    b5[neighbor] = b7
                    heapq.heappush(b3, (b6[neighbor], neighbor))
            b4.add(b7)
        return None
    def fonk6(self, b11, b12, path_dict):
        b8 = []
        b9 = b12
        while b9 is not None:
            b8.append(b9)
            b9 = path_dict[b9]
        return b8
def fonk7():
    b2 = class1()
    b2.fonk2('A', 'B', 5)
    b2.fonk2('A', 'C', 3)
    b2.fonk2('B', 'D', 2)
    b2.fonk2('C', 'D', 4)
    b2.fonk2('D', 'E', 6)
    b10 = class2(b2)
    b11 = 'A'
    b12 = 'E'
    shortest_path, b13 = b10.fonk5(b11, b12)
    if shortest_path:
        print(f"Shortest b5 from {b11} to {b12}: {' -> '.join(shortest_path)}")
        print(f"Shortest distance: {b13}")
    else:
        print(f"No b5 found from {b11} to {b12}")
if b14 = = "__main__":
    fonk7()